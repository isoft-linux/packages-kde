%global framework plasma

Name:           kf5-%{framework}
Version:        5.16.0
Release:        12
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

#plasma-5.16.0 changed the theme, it change the look and feel of entire desktop
#we choose to use themes from 5.15.0
Source1:        desktoptheme-from-plasma-5.15.0.tar.gz

Patch0: plasma-framework-backport-from-5.17.patch
 
#By default, unlock widget and add widget can not appear at the same time in the menu.
Patch1: plasma-framework-plasma-reset-action.patch

# add lunar tip on calendar
Patch2: plasma-framework-add-lunar-tip.patch

# HiddenStatus implementation for plasmoid
Patch3: 0002-hidden-status.patch

# https://git.reviewboard.kde.org/r/126296/
# [Window Thumbnails] Don't crash if Composite is disabled
Patch10: windowthumbcomposite.patch

BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXext-devel
BuildRequires:  libSM-devel
BuildRequires:  openssl-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  lunar-date-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtscript-devel

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-kactivities-devel >= %{version}
BuildRequires:  kf5-karchive-devel >= %{version}
BuildRequires:  kf5-kconfigwidgets-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
#an import backport of calenderevent support
BuildRequires:  kf5-kdeclarative-devel >= %{version}-5
BuildRequires:  kf5-kglobalaccel-devel >= %{version}
BuildRequires:  kf5-kguiaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-kxmlgui-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}
#an import backport
BuildRequires:  kf5-kpackage-devel >= %{version}-3
BuildRequires:  kf5-kdesu-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-knotifications-devel >= %{version}
BuildRequires:  kf5-solid-devel >= %{version}
BuildRequires:  kf5-kparts-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}


Requires:       kf5-filesystem
Requires:       lunar-date

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
%autosetup -n %{framework}-framework-%{version}  -p1

#we remove all theme provided by plasma-5.16.0, 
#and use theme from 5.15.0
rm -rf src/desktoptheme
tar zxf %{SOURCE1} -C src

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
%{_kf5_datadir}/plasma/
%{_kf5_datadir}/kservices5/*.desktop
#%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_mandir}/man1/plasmapkg2.1.gz

%lang(lt) %{_datadir}/locale/lt/LC_SCRIPTS/libplasma5/*.js

%files devel
%{_kf5_libdir}/cmake/KF5Plasma
%{_kf5_libdir}/cmake/KF5PlasmaQuick
%{_kf5_libdir}/libKF5Plasma.so
%{_kf5_libdir}/libKF5PlasmaQuick.so
%{_kf5_includedir}/plasma_version.h
%{_kf5_includedir}/plasma/
%{_kf5_includedir}/Plasma/
%{_kf5_datadir}/kdevappwizard/templates/*


%changelog
* Tue Dec 22 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-12
- Rebase lunar calender patch

* Tue Dec 22 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-11
- Backport from 5.17

* Fri Dec 18 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-10
- Merge patch back

* Fri Dec 11 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Changed the name of the enum to HiddenStatus.

* Thu Dec 10 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- HideMyself implementation for plasmoid.

* Tue Dec 08 2015 WangMing <ming.wang@i-soft.com.cn> - 5.16.0-7
- Format lunar date.

* Thu Nov 26 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-6
- Merge patch from git reviewboard

* Mon Nov 23 2015 WangMing <ming.wang@i-soft.com.cn> - 5.16.0-5
- Modify patch, set tip alignment the gird cell. Set transparent.

* Fri Nov 20 2015 WangMing <ming.wang@i-soft.com.cn> - 5.16.0-4
- Modify patch, fixed high CPU utilization.

* Fri Nov 20 2015 WangMing <ming.wang@i-soft.com.cn> 5.16.0-3
- Add lunar tip on calendar.

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-9
- Import some patches from kde reviewboard

* Fri Nov 06 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Rebuild.

* Wed Nov 04 2015 fujiang <fujiang.zhu@i-soft.com.cn> - 5.15.0-6
- add patch file

* Wed Nov 04 2015 fujiang <fujiang.zhu@i-soft.com.cn> - 5.15.0-5
- update spec

* Wed Nov 04 2015 fujiang <fujiang.zhu@i-soft.com.cn> - 5.15.0-4
- update corona:unlock and add widget never appear at the same time.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
