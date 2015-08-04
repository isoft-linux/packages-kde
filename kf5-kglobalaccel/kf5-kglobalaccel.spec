%global framework kglobalaccel

Name:           kf5-%{framework}
Version:        5.12.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 integration module for global shortcuts

License:        LGPLv2+
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

BuildRequires:  libX11-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}

BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}

BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel

Requires:       kf5-filesystem

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Conflicts: plasma-workspace < 5.2.0-8

%description
KDE Framework 5 Tier 1 integration module for global shortcuts.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{framework}-%{version}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%find_lang_kf5 kglobalaccel5_qt

%files -f kglobalaccel5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_bindir}/kglobalaccel5
%{_kf5_datadir}/kservices5/kglobalaccel5.desktop
%{_datadir}/dbus-1/services/org.kde.kglobalaccel.service
%{_kf5_qtplugindir}/org.kde.kglobalaccel5.platforms/KF5GlobalAccelPrivateXcb.so

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{_kf5_libdir}/libKF5GlobalAccel.so.*
%{_kf5_libdir}/libKF5GlobalAccelPrivate.so.*

%files devel
%{_kf5_includedir}/kglobalaccel_version.h
%{_kf5_includedir}/KGlobalAccel/
%{_kf5_libdir}/libKF5GlobalAccel.so
%{_kf5_libdir}/libKF5GlobalAccelPrivate.so
%{_kf5_datadir}/dbus-1/interfaces/*
%{_kf5_libdir}/cmake/KF5GlobalAccel
%{_kf5_archdatadir}/mkspecs/modules/qt_KGlobalAccel.pri


%changelog
