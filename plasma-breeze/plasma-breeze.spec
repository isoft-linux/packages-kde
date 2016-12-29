%global kf5_version 5.29.0
%global         base_name   breeze

%global         build_kde4  1

Name:           plasma-breeze
Version:        5.8.5
Release:        1
Summary:        Artwork, styles and assets for the Breeze visual style for the Plasma Desktop

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/breeze

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros >= %{kf5_version}
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:	kf5-kservice-devel >= %{kf5_version}
BuildRequires:  kf5-kcmutils-devel >= %{kf5_version}
BuildRequires:  kf5-kpackage-devel >= %{kf5_version}

# kde4breeze
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  kf5-kguiaddons-devel >= %{kf5_version}

# kstyle
BuildRequires:  kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  kf5-kcompletion-devel >= %{kf5_version}
BuildRequires:  kf5-frameworkintegration-devel >= %{kf5_version}
BuildRequires:  kf5-kwindowsystem-devel >= %{kf5_version}
BuildRequires:  kdecoration-devel >= %{version}

BuildRequires:  libxcb-devel

BuildRequires:  gettext

#for kde4 macros
%if 0%{?build_kde4:1}
BuildRequires: kde-filesystem
%endif

Requires:       kf5-filesystem

Requires:       %{name}-common = %{version}-%{release}

# since we provide a cmake dev-like file
Provides:       %{name}-devel = %{version}-%{release}

%description
%{summary}.

%package        common
Summary:        Common files shared between KDE 4 and Plasma 5 versions of the Breeze style
BuildArch:      noarch
%description    common
%{summary}.

%package -n     breeze-cursor-theme
Summary:        Breeze cursor theme
BuildArch:      noarch
%description -n breeze-cursor-theme
%{summary}.

%if 0%{?build_kde4:1}
%package -n     kde-style-breeze
Summary:        KDE 4 version of Plasma 5 artwork, style and assets
BuildRequires:  kdelibs-devel
BuildRequires:  libxcb-devel
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      plasma-breeze-kde4 < 5.1.95
Provides:       plasma-breeze-kde4%{?_isa} = %{version}-%{release}
%description -n kde-style-breeze
%{summary}.
%endif


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%if 0%{?build_kde4:1}
mkdir -p %{_target_platform}_kde4
pushd %{_target_platform}_kde4
%{cmake_kde4} -DUSE_KDE4=TRUE ..
popd

make %{?_smp_mflags} -C %{_target_platform}_kde4
%endif


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang breeze --with-qt --all-name

%if 0%{?build_kde4:1}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}_kde4
%endif

#already provided by breeze-icons in framework.
rm -rf %{buildroot}%{_datadir}/icons/breeze
rm -rf %{buildroot}%{_datadir}/icons/breeze-dark

%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%files
%doc cursors/Breeze/README COPYING COPYING-ICONS
%{_kf5_qtplugindir}/org.kde.kdecoration2/breezedecoration.so
%{_kf5_qtplugindir}/styles/breeze.so
%{_kf5_datadir}/kstyle/themes/breeze.themerc
%{_kf5_qtplugindir}/kstyle_breeze_config.so
%{_kf5_datadir}/kconf_update/kde4breeze.upd
%{_kf5_libdir}/kconf_update_bin/kde4breeze
#%{_kf5_datadir}/kconf_update/gtkbreeze.upd
#%{_kf5_libdir}/kconf_update_bin/gtkbreeze
%{_kf5_qmldir}/QtQuick/Controls/Styles/Breeze
%{_bindir}/breeze-settings5
%{_datadir}/icons/hicolor/scalable/apps/breeze-settings.svgz
%{_kf5_datadir}/kservices5/breezedecorationconfig.desktop
%{_kf5_datadir}/kservices5/breezestyleconfig.desktop

%files common -f breeze.lang
%{_datadir}/color-schemes/*.colors
%{_datadir}/QtCurve/Breeze.qtcurve
%{_datadir}/wallpapers/Next

%files -n breeze-cursor-theme
%{_datadir}/icons/breeze_cursors
#%{_datadir}/icons/breeze
#%{_datadir}/icons/breeze-dark
%{_datadir}/icons/Breeze_Snow

%if 0%{?build_kde4:1}
%files -n kde-style-breeze
%{_kde4_libdir}/kde4/plugins/styles/breeze.so
%{_kde4_libdir}/kde4/kstyle_breeze_config.so
%{_kde4_appsdir}/kstyle/themes/breeze.themerc
%endif


%changelog
* Thu Dec 29 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.5-1
- 5.8.5-1

* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.4-1
- 5.8.4-1

* Wed Nov 02 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Tue Nov 01 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.2-1
- 5.8.2

* Wed Aug 24 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-2
- 5.7.4
- Provides: plasma-breeze-devel

* Wed Jul 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.1-1
- 5.7.1

* Thu Jun 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-1
- 5.6.95

* Fri Apr 15 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
- 5.6.2

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-3
- Update

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

