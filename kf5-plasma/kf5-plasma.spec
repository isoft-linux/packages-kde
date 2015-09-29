%global framework plasma

Name:           kf5-%{framework}
Version:        5.14.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 framework is foundation to build a primary user interface

License:        GPLv2+ and LGPLv2+ and BSD
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-framework-%{version}.tar.xz

## upstream patches

BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXext-devel
BuildRequires:  libSM-devel
BuildRequires:  openssl-devel
BuildRequires:  libGL-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtscript-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-kactivities-devel >= %{version}
BuildRequires:  kf5-karchive-devel >= %{version}
BuildRequires:  kf5-kconfigwidgets-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-kdeclarative-devel >= %{version}
BuildRequires:  kf5-kglobalaccel-devel >= %{version}
BuildRequires:  kf5-kguiaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-kxmlgui-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}
BuildRequires:  kf5-kpackage-devel >= %{version}
BuildRequires:  kf5-kdesu-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-knotifications-devel >= %{version}
BuildRequires:  kf5-solid-devel >= %{version}
BuildRequires:  kf5-kparts-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}

Requires:       kf5-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       extra-cmake-modules
Requires:       kf5-kpackage-devel
Requires:       kf5-kservice-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-framework-%{version} 


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang plasma5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f plasma5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_bindir}/plasmapkg2
%{_kf5_libdir}/libKF5Plasma.so.*
%{_kf5_libdir}/libKF5PlasmaQuick.so.*
%{_kf5_qmldir}/org/kde/*
%{_kf5_qmldir}/QtQuick/Controls/Styles/Plasma
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/plasma/
%{_kf5_qtplugindir}/plasma/scriptengines/
%{_kf5_datadir}/dbus-1/interfaces/*.xml
%{_kf5_datadir}/plasma/
%{_kf5_datadir}/kservices5/*.desktop
#%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_mandir}/man1/plasmapkg2.1.gz
%{_kf5_plugindir}/kded/platformstatus.so

%lang(lt) %{_datadir}/locale/lt/LC_SCRIPTS/libplasma5/*.js

%files devel
%{_kf5_libdir}/cmake/KF5Plasma
%{_kf5_libdir}/cmake/KF5PlasmaQuick
%{_kf5_libdir}/libKF5Plasma.so
%{_kf5_libdir}/libKF5PlasmaQuick.so
%{_kf5_includedir}/plasma_version.h
%{_kf5_includedir}/plasma/
%{_kf5_includedir}/Plasma/


%changelog
* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
