# Enable bootstrap when building plasma-workspace on a new repo
# or arch where there's no package that would provide plasmashell
#define bootstrap 1

Name:           plasma-workspace
Version:        5.4.3
Release:        22
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
# upstream startkde.kde, minus stuff we don't want or need, plus a minor bit of customization --rex
Source11:       startkde.cmake
# Desktop file for Fedora Twenty Two look-and-feel package
Source12:       metadata.desktop

## downstream Patches
Patch10: plasma-workspace-5.3.0-konsole-in-contextmenu.patch

#always disable gpsd, most desktop had no need to run a gpsd service
Patch11: plasma-workspace-disable-gpsd.patch

#Patch from Leslie Zhai
Patch12: 0001-kscreenlocker-accounts-service.patch

#from Cjacker, protect ~/Desktop(localized by xdg-user-dirs)
#if it get deleted or Home.desktop/trash.desktop get deleted.
#when desktop started, all will be restored.
Patch13:  plasma-workspace-protect-home-Desktop-dir.patch

#backporting of xembedsniproxy
Patch20: 0000-backport-xembedsniproxy.patch
#all this patches already upstreamed.
Patch21: 0001-xembedsniproxy-fix-always-segfault.patch
Patch22: 0002-xembedsniproxy-workaround-for-java-systemtray.patch
Patch23: 0003-xembedsniproxy-crop-large-transparent-border.patch
Patch24: 0004-xembedsniproxy-workaround-for-totally-transparent-xcb-image.patch
Patch25: xembedsniproxy-dirty-fix-for-isoft-startup.patch

#Add isoft logo for splash
Patch30: 0003-splash-isoft-logo.patch

#https://git.reviewboard.kde.org/r/125898/
#fadeout text where buttons are. 
Patch40: klippergradient3.patch

#https://git.reviewboard.kde.org/r/124980/
#Click outside of logout dialog, cancel logout dialog.
Patch41: dismissonclickoutside3.patch 

#https://git.reviewboard.kde.org/r/126016/
#fix: properly recognise Plasma 5 KCM modules (wmClass=kcmshell5)
Patch42: kcmshell5-show-correct-icon-in-taskbar.patch

#https://git.reviewboard.kde.org/r/125997/
#Catch other openGL error gracefully
Patch43: catch-other-opengl-errors.patch 

#http://git.reviewboard.kde.org/r/126042/
Patch44: avoid-qmenu-exec-in-plasmoid-context-menu.patch

#fix: spelling mistake:kwin vs KWin
Patch45: plasma-workspace-taskwinjob-qdbus-kwin.patch

#https://git.reviewboard.kde.org/r/126216/
Patch46: do-not-produce-negative-struts-on-switching-screens.patch

#Fix systemtray applet show/hide items settings issue
Patch47: 0004-systemtray-applet-show-hide-items.patch

# Hidden status implementation for plasmoid
Patch48: 0005-systemtray-hidden-status.patch

# Integrate some kservice's code into plasma-workspace/runners/services
Patch49: 0007-query-for-cjk.patch

# ksmserver starts with default empty session
Patch50: 0008-ksmserver-default-session.patch

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
BuildRequires:  kf5-plasma-devel >= 5.13.0
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kdewebkit-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kglobalaccel-devel >= 5.7
BuildRequires:  kf5-networkmanager-qt-devel
BuildRequires:  kf5-kxmlrpcclient-devel
BuildRequires:  kf5-kinit-devel >= 5.10.0-3

#git codes
BuildRequires:  kf5-prison-devel

BuildRequires:  kf5-ksysguard-devel
BuildRequires:  kf5-kscreen-devel
BuildRequires:  kf5-baloo-devel

BuildRequires:  kf5-kwayland-devel
BuildRequires:  libwayland-client-devel >= 1.3.0
BuildRequires:  libwayland-server-devel >= 1.3.0

BuildRequires:  kwin-devel

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

# Optional
BuildRequires:  kf5-kactivities-devel

BuildRequires:  libqalculate-devel

#for patch13
BuildRequires: qt5-qtaccountsservice-devel >= 0.6.0
Requires: qt5-qtaccountsservice >= 0.6.0

BuildRequires: kjieba-devel
Requires: kjieba

# for libkdeinit5_*
%{?kf5_kinit_requires}
Requires:       kf5-kactivities
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
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1

%patch30 -p1

%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1

%patch46 -p1

%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1

mv startkde/startkde.cmake startkde/startkde.cmake.orig
install -m644 -p %{SOURCE11} startkde/startkde.cmake

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
%{_kf5_qtplugindir}/plasma/dataengine/*.so
%{_kf5_qtplugindir}/plasma/packagestructure/*.so
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/phonon_platform/kde.so
%{_kf5_qtplugindir}/kpackage/packagestructure/*.so
%{_kf5_qmldir}/org/kde/*
%{_libexecdir}/*
%{_kf5_datadir}/ksmserver
%{_kf5_datadir}/ksplash
%{_kf5_datadir}/plasma/plasmoids
%{_kf5_datadir}/plasma/services
%{_kf5_datadir}/plasma/shareprovider
%{_kf5_datadir}/plasma/wallpapers
%{_kf5_datadir}/plasma/look-and-feel
%{_kf5_datadir}/plasma/kcms
%{_kf5_datadir}/solid
%{_kf5_datadir}/kstyle
%{_kf5_datadir}/drkonqi/debuggers/external/*
%{_kf5_datadir}/drkonqi/debuggers/internal/*
%{_kf5_datadir}/drkonqi/mappings
%{_kf5_datadir}/drkonqi/pics/*.png
%{_kf5_datadir}/kconf_update/*
%{_sysconfdir}/xdg/*.knsrc
%{_sysconfdir}/xdg/taskmanagerrulesrc
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/knotifications5/*.notifyrc
%{_kf5_datadir}/config.kcfg/*
%{_datadir}/applications/*.desktop
%{_datadir}/sddm/themes/breeze
%{_datadir}/xsessions/plasma.desktop

%{_kf5_plugindir}/kio/desktop.so
%{_datadir}/kio_desktop/Home.desktop
%{_datadir}/kio_desktop/directory.desktop
%{_datadir}/kio_desktop/directory.trash

# PAM
%config %{_sysconfdir}/pam.d/kde

%files doc
%lang(en) %{_docdir}/HTML/en/klipper/
%lang(ca) %{_docdir}/HTML/ca/klipper/

%files devel
%{_libdir}/libweather_ion.so
%{_libdir}/libtaskmanager.so
%{_libdir}/libplasma-geolocation-interface.so
%{_libdir}/libkworkspace5.so
%{_includedir}/*
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/ScreenSaverDBusInterface

# TODO split to subpackages
# - KCM (?)
# - plasmoids
# - icons
# - individual tools


%changelog
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
