%global kf5_version 5.27.0

Name:           kdeplasma-addons
Version:        5.8.2
Release:        1
Summary:        Additional Plasmoids for Plasma 5.

License:        GPLv2+
URL:            http://www.kde.org

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

Obsoletes:      kdeplasma-addons-libs < 5.0.0
Provides:       kdeplasma-addons-libs = %{version}-%{release}
Provides:       kdeplasma-addons-libs%{?dist} = %{version}-%{release}


BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  ibus-devel
BuildRequires:  kf5-kcmutils-devel >= %{kf5_version}
BuildRequires:  kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  kf5-kconfigwidgets-devel >= %{kf5_version}
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kf5-kdelibs4support-devel >= %{kf5_version}
BuildRequires:  kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  kf5-kio-devel >= %{kf5_version}
BuildRequires:  kf5-knewstuff-devel >= %{kf5_version}
BuildRequires:  kf5-kross-devel >= %{kf5_version}
BuildRequires:  kf5-krunner-devel >= %{kf5_version}
BuildRequires:  kf5-kservice-devel >= %{kf5_version}
BuildRequires:  kf5-kunitconversion-devel >= %{kf5_version}
BuildRequires:  kf5-plasma-devel >= %{kf5_version}
BuildRequires:  kf5-kactivities-devel >= %{kf5_version}
BuildRequires:  plasma-workspace-devel >= %{version}
BuildRequires:  libksysguard-devel >= %{version}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel

Requires:       kf5-filesystem

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kdeplasmaaddons5_qt --with-qt --all-name

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f kdeplasmaaddons5_qt.lang
%doc COPYING COPYING.LIB
%{_kf5_datadir}/plasma/plasmoids/*
%{_kf5_datadir}/plasma/desktoptheme/default/widgets/*
%{_kf5_datadir}/plasma/desktoptheme/default/icons/*
%{_kf5_datadir}/plasma/desktoptheme/default/weather/*
%{_kf5_datadir}/plasma/wallpapers/*
%{_kf5_datadir}/plasma/services/*.operations
%{_kf5_qtplugindir}/plasma/dataengine/*.so
%{_kf5_qtplugindir}/plasma/applets/*.so
%{_kf5_qtplugindir}/*.so
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/kwin/*.desktop
%{_kf5_qmldir}/org/kde/plasma/*
%{_datadir}/kwin/desktoptabbox/
%{_datadir}/kwin/tabbox/
%{_datadir}/icons/hicolor/*/apps/fifteenpuzzle.*
%{_sysconfdir}/xdg/comic.knsrc
%{_kf5_libdir}/libplasmacomicprovidercore.so.*
%{_kf5_libdir}/libplasmaweather.so.*
%{_kf5_qtplugindir}/kpackage/packagestructure/plasma_packagestructure_comic.so
%{_kf5_datadir}/kservicetypes5/plasma_comicprovider.desktop

%changelog
* Tue Nov 01 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.2-1
- 5.8.2

* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Thu Jul 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.1-3
- Rebuild.
- Add missing files.

* Wed Jul 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.1-1
- 5.7.1

* Thu Jun 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-1
- 5.6.95

* Tue Apr 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.1-1
- 5.6.1

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-3
- Backport colorpicker plasmoid

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-2
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

