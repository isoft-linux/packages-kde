# Enable bootstrap when building plasma-workspace on a new repo
# or arch where there's no package that would provide plasmashell
#define bootstrap 1

Name:           plasma-workspace
Version:        5.7.4
Release:        2
Summary:        Plasma workspace, applications and applets
License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/plasma-workspace

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

# This goes to PAM
Source10:       kde

#Add isoft logo for splash
Patch30: 0003-splash-isoft-logo.patch

#Rebase kjieba Chinese word segmentation for 5.6.95
Patch34: 0007-query-for-cjk.patch

BuildRequires:  zlib-devel
BuildRequires:  dbusmenu-qt5-devel
BuildRequires:  libGL-devel
BuildRequires:  mesa-libGLES-devel
#BuildRequires:  wayland-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-devel
BuildRequires:  glib2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  python-devel
BuildRequires:  boost-devel
#BuildRequires:  akonadi-qt5-devel
#BuildRequires:  kdepimlibs-devel
BuildRequires:  libusb-devel
BuildRequires:  libbsd-devel
BuildRequires:  pam-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  pciutils-devel
%ifnarch s390 s390x
BuildRequires:  libraw1394-devel
%endif

#BuildRequires:  gpsd-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  phonon-qt5-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-krunner-devel
BuildRequires:  kf5-kjsembed-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kdesu-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-threadweaver-devel
BuildRequires:  kf5-ktexteditor-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-plasma-devel >= 5.23.0
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kdewebkit-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kglobalaccel-devel >= 5.23.0
BuildRequires:  kf5-networkmanager-qt-devel
BuildRequires:  kf5-kxmlrpcclient-devel
BuildRequires:  kf5-kinit-devel >= 5.23.0
BuildRequires:  kscreenlocker-devel >= %{version}
BuildRequires:  kf5-kemoticons-devel

#git codes
BuildRequires:  kf5-prison-devel

BuildRequires:  kf5-ksysguard-devel >= %{version}
BuildRequires:  kf5-kscreen-devel >= %{version}
BuildRequires:  kf5-baloo-devel

BuildRequires:  kf5-kwayland-devel >= 5.23.0
BuildRequires:  libwayland-client-devel >= 1.3.0
BuildRequires:  libwayland-server-devel >= 1.3.0

BuildRequires:  kwin-devel >= %{version}

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

# Optional
BuildRequires:  kf5-kactivities-devel

BuildRequires:  libqalculate-devel

BuildRequires: qt5-qtaccountsservice-devel >= 0.6.0
Requires: qt5-qtaccountsservice >= 0.6.0

BuildRequires: kjieba-devel
Requires: kjieba

# for libkdeinit5_*
%{?kf5_kinit_requires}
#Requires:       kf5-kactivities
Requires:       kf5-kded
Requires:       kf5-kdoctools
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtgraphicaleffects
Requires:       kf5-filesystem
Requires:       kf5-baloo
Requires:       kf5-kglobalaccel >= 5.7
# for translations mostly, can drop for plasma-5.3 (#1208947) -- rex
Requires:       kf5-kxmlrpcclient >= 5.8
Requires:       khotkeys

# Without the platformtheme plugins we get broken fonts
Requires:       kf5-frameworkintegration

# For krunner
Requires:       plasma-milou

# Power management
Requires:       powerdevil

# startkde
Requires:       coreutils
Requires:       dbus-x11
Requires:       socat
Requires:       xmessage
Requires:       qt5-qttools

Requires:       xorg-x11-utils
Requires:       xorg-x11-server-utils

Requires:       systemd

# SysTray support for Qt 4 apps
Requires:       sni-qt

# Oxygen
Requires:       oxygen-icon-theme
Requires:       oxygen-sound-theme
Requires:       oxygen-fonts

#our patch on kio_desktop need xdg-user-dirs.
Requires: xdg-user-dirs

# PolicyKit authentication agent
Requires:        polkit-kde

# Require any plasmashell (plasma-desktop provides plasmashell(desktop))
%if 0%{?bootstrap}
Provides:       plasmashell
%else
Requires:       plasmashell
%endif

%description
Plasma 5 libraries and runtime components


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation and user manuals for %{name}
# switch to noarch
Obsoletes: plasma-workspace-doc < 5.3.1-2
BuildArch: noarch
%description    doc
Documentation and user manuals for %{name}.


%prep
%setup -q

%patch30 -p1
%patch34 -p1

# omit conflicts with kf5-kxmlrpcclient-5.8
rm -fv po/*/libkxmlrpcclient5.po


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

chrpath --delete %{buildroot}/%{_kf5_qtplugindir}/phonon_platform/kde.so

# Make kcheckpass work
install -m455 -p -D %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/kde

#DO NOT display this menu item, already in plasma tray.
echo "NoDisplay=true" >> $RPM_BUILD_ROOT%{_datadir}/applications/org.kde.klipper.desktop

%find_lang plasmaworkspace5 --with-qt --with-kde --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/{plasma-windowed,org.kde.klipper}.desktop


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f plasmaworkspace5.lang
%{_kf5_bindir}/*
%{_kf5_libdir}/*.so.*
%{_kf5_libdir}/libkdeinit5_*.so
%{_kf5_qtplugindir}/plasma/applets/
%{_kf5_qtplugindir}/plasma/dataengine/*.so
%{_kf5_qtplugindir}/plasma/packagestructure/*.so
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/phonon_platform/kde.so
%{_kf5_qtplugindir}/kpackage/packagestructure/*.so
%{_kf5_qtplugindir}/kf5/kded/*.so
%{_kf5_qmldir}/org/kde/*
%{_libexecdir}/*
%{_kf5_datadir}/ksmserver
%{_kf5_datadir}/ksplash
%{_kf5_datadir}/plasma/plasmoids
%{_kf5_datadir}/plasma/services
%{_kf5_datadir}/plasma/shareprovider
%{_kf5_datadir}/plasma/wallpapers
%{_kf5_datadir}/plasma/look-and-feel
#%{_kf5_datadir}/plasma/kcms
%{_kf5_datadir}/solid
%{_kf5_datadir}/kstyle
%{_kf5_datadir}/drkonqi/debuggers/external/*
%{_kf5_datadir}/drkonqi/debuggers/internal/*
%{_kf5_datadir}/drkonqi/mappings
#%{_kf5_datadir}/drkonqi/pics/*.png
#%{_kf5_datadir}/kconf_update/*
%{_sysconfdir}/xdg/*.knsrc
%{_sysconfdir}/xdg/taskmanagerrulesrc
%{_sysconfdir}/xdg/legacytaskmanagerrulesrc
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
#%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/knotifications5/*.notifyrc
%{_kf5_datadir}/config.kcfg/*
%{_datadir}/applications/*.desktop
%{_datadir}/sddm/themes/breeze
%{_datadir}/xsessions/plasma.desktop
%{_datadir}/wayland-sessions/plasmawayland.desktop

%{_kf5_plugindir}/kio/desktop.so
%{_datadir}/kio_desktop/DesktopLinks/Home.desktop
%{_datadir}/kio_desktop/directory.desktop
%{_datadir}/kio_desktop/directory.trash

# PAM
%config %{_sysconfdir}/pam.d/kde

%files doc
%lang(en) %{_docdir}/HTML/en/klipper/
%lang(ca) %{_docdir}/HTML/ca/klipper/
%lang(en) %{_docdir}/HTML/en/kcontrol/
#%lang(cs) %{_docdir}/HTML/cs/kcontrol/

%files devel
%{_libdir}/libweather_ion.so
%{_libdir}/libtaskmanager.so
%{_libdir}/libplasma-geolocation-interface.so
%{_libdir}/libkworkspace5.so
%{_libdir}/liblegacytaskmanager.so
%{_includedir}/*
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
#%{_libdir}/cmake/ScreenSaverDBusInterface
%{_libdir}/cmake/LibLegacyTaskManager

# TODO split to subpackages
# - KCM (?)
# - plasmoids
# - icons
# - individual tools


%changelog
* Mon Aug 29 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-2
- backport to commit 565dedb84ac51bde96bc0586a260fd444a32cd43
- rebuild for KDEBUG-367828

* Wed Aug 24 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Wed Aug 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.3-1
- 5.7.3

* Wed Jul 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.2-1
- 5.7.2

* Thu Jul 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.1-2
- Rebuild.

* Wed Jul 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.1-1
- 5.7.1

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.0-3
- It does not need to use KServiceOffset.

* Fri Jul 08 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.0-2
- Rebuild for qt5-qtdeclarative.

* Wed Jul 06 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.0-1
- 5.7.0

* Mon Jun 27 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-5
- Rebase kjieba for 5.6.95

* Thu Jun 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-4
- ksplash with background.

* Wed Jun 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-2
- plasma-desktop broken dependence.

* Tue Jun 21 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-1
- 5.6.95
- add unpacking file.

* Thu May 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.4-1
- 5.6.4

* Wed Apr 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.3-1
- 5.6.3

* Fri Apr 15 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-4
- Add plasmawayland session.

* Thu Apr 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-3
- Add isoft logo for splash.

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-2
- Add missing files

* Tue Apr 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
- powerdevil, kf5-kactivities broken
- 5.6.2

* Mon Apr 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.1-1
- 5.6.1

* Thu Jan 21 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Disable drkonqi.

* Wed Jan 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix switch to oxygen theme NO background issue.

* Mon Jan 18 2016 <ming.wang@i-soft.com.cn> - 5.4.3-39
- Amend: set shortcut enable:edit contents, prev history, next history.

* Mon Jan 18 2016 <ming.wang@i-soft.com.cn> - 5.4.3-38
- set shortcut enable:edit contents, prev history, next history.

* Fri Jan 15 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add plasmoid blacklist for PM.

* Thu Jan 07 2016 Cjacker <cjacker@foxmail.com> - 5.4.3-36
- Fix rare empty tray and segfault

* Tue Jan 05 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Use iSOFT background by default for loginmanager.

* Mon Jan 04 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Use iSOFT logo by default for lockscreen.

* Thu Dec 31 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-33
- Fix xembed sni proxy always segfault

* Tue Dec 29 2015 <ming.wang@i-soft.com.cn> - 5.4.3-32
- Hide timezone widget of analogclock when width less than  text's width.

* Tue Dec 29 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-31
- Update xembed sni proxy backport codes to git master, drop some dirty patches

* Thu Dec 24 2015 <ming.wang@i-soft.com.cn> - 5.4.3-30
- Remove checkbox kcfg_PreventEmptyClipboard.

* Thu Dec 24 2015 <ming.wang@i-soft.com.cn> - 5.4.3-28
- Remove PartiallyChecked state of use24hFormat checkbox.

* Thu Dec 24 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-28
- Update trash patch, do not check trashdir, it's not enough.
- we now ensure trashrc update in kio trash.

* Thu Dec 24 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-27
- Update trash patch, also check trash dir to determine is empty or not

* Wed Dec 23 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-26
- Add kio_desktop po for zh_CN

* Wed Dec 23 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-25
- Drop trash.desktop, use virtual Trash UDSEntry

* Wed Dec 23 2015 fj <fujiang.zhu@i-soft.com.cn> - 5.4.3-24
- set default focus on button for breezeblock

* Mon Dec 21 2015 xiaotian.wu@i-soft.com.cn - 5.4.3-23
- remove two checkbox from clipboard configdialog: IgnoreImage and textonly

* Thu Dec 17 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add kservice exec() is empty check and query && topinyin GenericName.
- ksmserver starts with default empty session.

* Wed Dec 16 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Use queryForCJK for Application search.
- Remove kservice queryForCJK API.
- Integrate some code from KServiceTypeTrader.
- Add KJieba query and topinyin support.

* Fri Dec 11 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Changed the name of the enum to HiddenStatus.
- Fix showAllItems HiddenStatus empty area issue.

* Thu Dec 10 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add systemtray HideMyself status implementation for plasmoid.
- Fix systemtray's empty area issue for HideMyself status plasmoid.

* Thu Dec 03 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix systemtray applet show/hide items settings issue.

* Thu Dec 03 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-11
- https://git.reviewboard.kde.org/r/126216

* Tue Dec 01 2015 fujiang <fujiang.zhu@i-soft.com.cn> - 5.4.3-10
- Fix:spelling mistake:qdbus service name error

* Thu Nov 26 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-9
- Fix more xembed sni proxy bugs

* Tue Nov 24 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-8
- Fix KDE bug 354903

* Mon Nov 23 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-7
- Fix kde bug 355504

* Thu Nov 19 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Drop 0002-add-paste-for-desktopview.patch, CTRL+V also need to consider other
  items for example plasmoid.

* Mon Nov 16 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-5
- Fix xembedsniproxy always segfault issue, Dirty hack for isoft to not handle
  the cold bootup embed window

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-4
- Add some patches from kde reviewboard.

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-3
- Add more killall to startkde, bad, bad, bad

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Fri Nov 06 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add isoft logo for splash.

* Thu Oct 29 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add CTRL+V for plasmashell desktopview.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-5
- Rebuild for new 4.0 release

* Fri Oct 16 2015 Cjacker <cjacker@foxmail.com>
- modify startkde.cmake to generate plasma-locale-setting.sh at first login.

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95
- drop patch11

* Fri Aug 07 2015 Cjacker <cjacker@foxmail.com>
- add patch 13 to enable qtaccountservice face support.

* Wed Jul 15 2015 Cjacker <cjacker@foxmail.com>
- add patch11, fix logout crash.
