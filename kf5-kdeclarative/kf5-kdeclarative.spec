%global framework kdeclarative

Name:           kf5-%{framework}
Version:        5.16.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 addon for Qt declarative

License:        GPLv2+ and MIT
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-kglobalaccel-devel >= %{version}
BuildRequires:  kf5-kguiaddons-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-kpackage-devel >= %{version}

BuildRequires:  libepoxy-devel

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 addon for Qt declarative

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel
Requires:       kf5-kpackage-devel
Requires:       qt5-qtdeclarative-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kdeclarative5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kdeclarative5_qt.lang
%doc COPYING COPYING.LIB README.md
%{_kf5_bindir}/kpackagelauncherqml
%{_kf5_libdir}/libKF5Declarative.so.*
%{_kf5_libdir}/libKF5QuickAddons.so.*
%{_kf5_qmldir}/org/kde/draganddrop
%{_kf5_qmldir}/org/kde/kcoreaddons
%{_kf5_qmldir}/org/kde/kquickcontrols
%{_kf5_qmldir}/org/kde/kquickcontrolsaddons
%{_kf5_qmldir}/org/kde/private/kquickcontrols
%{_kf5_qmldir}/org/kde/kio
%{_kf5_qmldir}/org/kde/kwindowsystem

%files devel
%{_kf5_includedir}/kdeclarative_version.h
%{_kf5_includedir}/KDeclarative
%{_kf5_libdir}/libKF5Declarative.so
%{_kf5_libdir}/libKF5QuickAddons.so
%{_kf5_libdir}/cmake/KF5Declarative
%{_kf5_archdatadir}/mkspecs/modules/qt_KDeclarative.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_QuickAddons.pri


%changelog
* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
