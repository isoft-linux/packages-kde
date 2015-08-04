%global framework kconfig

Name:           kf5-%{framework}
Version:        5.12.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with advanced configuration system

License:        GPLv2+ and LGPLv2+ and MIT
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       kf5-filesystem
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

%description
KDE Frameworks 5 Tier 1 addon with advanced configuration system made of two
parts: KConfigCore and KConfigGui.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
## included for completeness and documentation, but part of qtbase-devel already -- rex
#Requires:       pkgconfig(Qt5Xml)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        core
Summary:        Non-GUI part of KConfig framework

%description    core
KConfigCore provides access to the configuration files themselves. It features
centralized definition and lock-down (kiosk) support.

%package        gui
Summary:        GUI part of KConfig framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    gui
KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kconfig5_qt --with-qt --all-name


%files
%doc COPYING.LIB DESIGN README.md TODO

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%files core -f kconfig5_qt.lang
%{_kf5_bindir}/kreadconfig5
%{_kf5_bindir}/kwriteconfig5
%{_kf5_libdir}/libKF5ConfigCore.so.*
%{_kf5_libexecdir}/kconfig_compiler_kf5
%{_kf5_libexecdir}/kconf_update

%post gui -p /sbin/ldconfig
%postun gui -p /sbin/ldconfig

%files gui
%{_kf5_libdir}/libKF5ConfigGui.so.*

%files devel
%{_kf5_includedir}/kconfig_version.h
%{_kf5_includedir}/KConfigCore
%{_kf5_includedir}/KConfigGui
%{_kf5_libdir}/libKF5ConfigCore.so
%{_kf5_libdir}/libKF5ConfigGui.so
%{_kf5_libdir}/cmake/KF5Config
%{_kf5_archdatadir}/mkspecs/modules/qt_KConfigCore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KConfigGui.pri


%changelog
