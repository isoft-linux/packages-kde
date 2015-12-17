Name:           plasma-desktop
Version:        5.4.3
Release:        23
Summary:        Plasma Desktop shell

License:        GPLv2+ and (GPLv2 or GPLv3)
URL:            https://projects.kde.org/projects/kde/workspace/plasma-desktop

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

## downstream patches
# adjust default kickoff favorites: -preferred_browser(buggy) +konqueror +konsole +apper
Patch100: plasma-desktop-default_favorites.patch
# FIXME: make upstreamable, fix dup'd PREFIX KAUTH_HELPER_INSTALL_DIR when using absolute paths
#Patch101: plasma-desktop-fix-fontinst-service-path.patch
# Default to Folder containment (rather than Desktop)
Patch102: plasma-desktop-default-layout.patch

#patches from Leslie Zhai
Patch200: 0001-kickoff-accounts-service.patch  
Patch201: plasma-desktop-kickoff-face-click-open-user_account.patch
# Cancelable when disable fontinst
Patch202: 0002-cancel-fontinst.patch
# Replace trolltech for fontinst
Patch203: 0003-kfontinst-replace-trolltech.patch
# Port kauth for fontinst and use asynchronous interface of KJob
Patch204: 0004-kfontinst-port-kauth.patch
# Add faceIcon for kicker
# TEMP disabled by Cjacker, please do not enable it until reviewed.
Patch205: 0005-kicker-add-faceicon.patch

#add showdesktop to panel
Patch300: plasma-desktop-add-showdesktop-to-panel-by-default.patch

#By default, lock the panel.
Patch301: plasma-desktop-default-locked.patch

#increase the default panel height.
Patch302: plasma-desktop-increase-default-panel-height.patch

#tweak some default settings
Patch303: plasma-desktop-tweak.patch

#hide desktopath modules from systemsettings, but still can be used as "kcmshell5 desktoppath"
Patch304: plasma-desktop-hide-desktoppath-from-systemsettings.patch

#remove formats/translation setting module, it's crappy and buggy.
#we use our own 'kcmlocale' now.

Patch305: plasma-desktop-say-goodbye-to-crappy-and-buggy-locale-setting.patch

Patch306: plasma-desktop-disable-kcm-mouse-and-touchpad.patch

Patch307: plasma-desktop-kickoff-sync-url.patch

# Kickoff isoft-logo
Patch308: 0006-kickoff-isoft-logo.patch

# Kicker isoft-logo
Patch309: 0007-kicker-isoft-logo.patch

# uninstall kcm-kemail.desktop
Patch310: plasma-desktop-uninstall-component-kcm-kemail.patch

#https://git.reviewboard.kde.org/r/125908/
Patch311: plasmadesktop-scrollabletasktooltip.diff

# Open history documents with bash script
# But it needs to distinguish between *.desktop and general file
# Fix open systrayed application twice issue
Patch312: plasma-desktop-startup-history-documents.patch

# kcm_splashscreen use isoft logo
Patch313: 0008-preview-splash-isoft-logo.patch

# https://git.reviewboard.kde.org/r/126079/
Patch314: fix-kde-bug-355365.patch

# https://git.reviewboard.kde.org/r/124675/
Patch315: fix-kde-bug-311991.patch

# https://git.reviewboard.kde.org/r/126162/
Patch316: taskmanager-tooltipdelegate.diff

# Fix DnD file to Trash access denied issue
Patch317: 0009-dnd-file-to-trash.patch

# Add desktop folderview ctrl+c, ctrl+v, ctrl+x support
Patch318: 0010-desktop-folderview-shortcut.patch

# Remove leave unchaged kcm_keyboard, there is ONLY ON or OFF.
#Patch319: 0011-remove-numlock-unchanged.patch

# Remove icons advance setting KDEBUG-356712
Patch320: 0012-drop-icons-advance-setting.patch

# Remove suspend 
Patch321: 0013-remove-suspend.patch

# Fix recent document icon issue.
Patch322: 0014-kickoff-recentdoc-icon.patch

# kcmsmserver starts with default session.
Patch323: 0015-kcm-ksmserver-default-session.patch

BuildRequires:  libusb-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libX11-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libxkbcommon-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  phonon-qt5-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kdesu-devel
BuildRequires:  kf5-attica-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-krunner-devel
BuildRequires:  kf5-ksysguard-devel
BuildRequires:  kf5-baloo-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kpeople-devel
BuildRequires:  kf5-kded-devel
BuildRequires:  kf5-kinit-devel >= 5.10.0-3
# libkdeinit5_*
%{?kf5_kinit_requires}

BuildRequires:  plasma-workspace-devel
BuildRequires:  kwin-devel

# Optional
BuildRequires:  kf5-kactivities-devel
BuildRequires:  libcanberra-devel
BuildRequires:  boost-devel
BuildRequires:  pulseaudio-libs-devel

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

# for kcm_touchpad
BuildRequires:  xorg-x11-drv-synaptics-devel
# for xserver-properties
BuildRequires:  xorg-x11-server-devel

BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
 
#for patch200/201
BuildRequires: qt5-qtaccountsservice-devel >= 0.6.0
Requires: qt5-qtaccountsservice >= 0.6.0

Requires:       kf5-kded

# for kcm_keyboard
Requires:       iso-codes

# for kcm_input
BuildRequires:  xorg-x11-drv-evdev-devel

# Desktop
Requires:       plasma-workspace
Requires:       kf5-filesystem

# Install breeze
Requires:       plasma-breeze
Requires:       breeze-icon-theme
Requires:       kde-style-breeze

# Install systemsettings, full set of KIO slaves and write() notifications
Requires:       plasma-systemsettings
Requires:       kio-extras
Requires:       kwrited

# Install KWin
Requires:       kwin

# kickoff -> edit applications (#1229393)
Requires: kmenuedit

# KCM touchpad has been merged to plasma-desktop in 5.3
Provides:       kcm_touchpad = %{version}-%{release}
Obsoletes:      kcm_touchpad < 5.3.0

# Virtual provides for plasma-workspace
Provides:       plasmashell(desktop) = %{version}-%{release}
Provides:       plasmashell = %{version}-%{release}

Obsoletes:      kde-workspace < 5.0.0-1

%description
%{summary}.

%package        doc
Summary:        Documentation and user manuals for %{name}
BuildArch: noarch

%description    doc
%{summary}.


%prep
%autosetup -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang plasmadesktop5 --with-qt --all-name

# No -devel
rm -fv %{buildroot}%{_libdir}/libkfontinst{,ui}.so

# KDM is dead
rm -rf %{buildroot}%{_datadir}/kdm

# Copy konqsidebartng to kde4/apps so that KDE Konqueror can find it
mkdir -p %{buildroot}%{_datadir}/kde4/apps/konqsidebartng/virtual_folders/services/
cp %{buildroot}%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop \
   %{buildroot}%{_datadir}/kde4/apps/konqsidebartng/virtual_folders/services

# create own `kf5-config --path data`/plasma/shells/org.kde.plasma.desktop/updates/
# per https://techbase.kde.org/KDE_System_Administration/PlasmaTwoDesktopScripting#Running_Scripts
mkdir -p %{buildroot}%{_datadir}/plasma/shells/org.kde.plasma.desktop/updates/

#Hide knetattach menu item
echo "NoDisplay=true" >> %{buildroot}/%{_datadir}/applications/org.kde.knetattach.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.{kfontview,knetattach}.desktop


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%files -f plasmadesktop5.lang
%{_bindir}/kapplymousetheme
%{_bindir}/kaccess
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/krdb
%{_bindir}/knetattach
%{_bindir}/solid-action-desktop-gen
%{_kf5_libexecdir}/kauth/kcmdatetimehelper
%{_kf5_libexecdir}/kauth/fontinst
%{_kf5_libexecdir}/kauth/fontinst_helper
%{_kf5_libexecdir}/kauth/fontinst_x11
%{_libexecdir}/kfontprint
%{_qt5_prefix}/qml/org/kde/plasma/private
%{_kf5_libdir}/libkdeinit5_kaccess.so
%{_kf5_libdir}/kconf_update_bin/*
# TODO: -libs subpkg -- rex
%{_kf5_libdir}/libkfontinst.so.*
%{_kf5_libdir}/libkfontinstui.so.*
%{_kf5_libdir}/libKF5ActivitiesExperimentalStats.so.*
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/kcms/*.so
%{_kf5_qmldir}/org/kde/plasma/activityswitcher
%{_kf5_qmldir}/org/kde/private/desktopcontainment/*
%{_kf5_datadir}/plasma/*
%{_kf5_datadir}/color-schemes
%{_kf5_datadir}/kconf_update/*
%{_kf5_datadir}/kdisplay
%{_kf5_datadir}/kcontrol
%{_kf5_datadir}/kcmkeys
%{_kf5_datadir}/kcm_componentchooser
%{_kf5_datadir}/kcm_phonon
%{_kf5_datadir}/kfontinst
%{_kf5_datadir}/kcminput
%{_kf5_datadir}/kcmkeyboard
%{_kf5_datadir}/ksmserver
%{_kf5_datadir}/kpackage/kcms/*
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/kde4/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{_kf5_datadir}/kcmsolidactions
%{_kf5_datadir}/solid/devices/*.desktop
%config %{_sysconfdir}/dbus-1/system.d/*.conf
%config %{_sysconfdir}/xdg/*.knsrc
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/ServiceMenus/installfont.desktop
%{_kf5_datadir}/kservices5/fonts.protocol
%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/kxmlgui5/kfontview
%{_kf5_datadir}/kxmlgui5/kfontinst
%{_kf5_datadir}/knotifications5/*.notifyrc
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
# kcm_touchpad
#%{_bindir}/kcm-touchpad-list-devices
#%{_kf5_qtplugindir}/plasma/dataengine/plasma_engine_touchpad.so
#%{_datadir}/config.kcfg/touchpad.kcfg
#%{_datadir}/config.kcfg/touchpaddaemon.kcfg
#%{_datadir}/dbus-1/interfaces/org.kde.touchpad.xml

%files doc
%lang(ca) %{_docdir}/HTML/ca/kcontrol/
%lang(ca) %{_docdir}/HTML/ca/kfontview/
%lang(ca) %{_docdir}/HTML/ca/knetattach/
%lang(ca) %{_docdir}/HTML/ca/plasma-desktop/
%lang(en) %{_docdir}/HTML/en/kcontrol/
%lang(en) %{_docdir}/HTML/en/kfontview/
%lang(en) %{_docdir}/HTML/en/knetattach/
%lang(en) %{_docdir}/HTML/en/plasma-desktop/
%lang(it) %{_docdir}/HTML/it/plasma-desktop/
%lang(nl) %{_docdir}/HTML/nl/plasma-desktop/
%lang(pt_BR) %{_docdir}/HTML/pt_BR/plasma-desktop/
%lang(ru) %{_docdir}/HTML/ru/plasma-desktop/
%lang(sv) %{_docdir}/HTML/sv/plasma-desktop/
%lang(uk) %{_docdir}/HTML/uk/plasma-desktop/


%changelog
* Thu Dec 17 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- kcmsmserver starts with default session.
- Restore kcmsmserver ui.
- Filter directory and html for kickoff recent document.

* Wed Dec 16 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-20
- patch319 cause kcm_keyboard segfault, remove temp

* Tue Dec 15 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Remove icons advance setting KDEBUG-356712
- Remove suspend.
- Fix recent document icon issue.

* Mon Dec 14 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Remove leave unchaged kcm_keyboard, there is ONLY ON or OFF.

* Tue Dec 08 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add shift+delete support for desktop folderview.

* Fri Dec 04 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add desktop folderview ctrl+c, ctrl+v, ctrl+x support.
- Fix open systrayed application twice issue.

* Thu Dec 03 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix DnD file to Trash access denied issue.

* Thu Nov 26 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix kicker plasmoid icon issue.

* Thu Nov 26 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-10
- merge patch back

* Tue Nov 24 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-9
- Fix KDE BUG 355365, 311991

* Thu Nov 19 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- kcm_splashscreen use isoft logo.

* Sun Nov 15 2015 wangming <ming.wang@i-soft.com.cn> - 5.4.3-7
- Patch for open desktop file with Type=Link.

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-6
- Add some patches from reviewboard

* Tue Nov 10 2015 Wang Ming <ming.wang@i-soft.com.cn> - 5.4.3-5
- Uninstall component kcm-kemail.

* Tue Nov 10 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Rebuild kicker.
- Port kauth for fontinst and use asynchronous interface of KJob.

* Mon Nov 09 2015 sulit <sulitsrc@gmail.com>
- do apt repo use 5.4.3-2.

* Mon Nov 09 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Kicker use isoft-logo. 

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Fri Nov 06 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add faceIcon for kicker.

* Thu Nov 05 2015 fujiang <fujiang.zhu@i-soft.com.cn> - 5.4.2-26
- sync favorites,add patch kickoff-sync-url.patch

* Wed Nov 04 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix disable fontinst can not cancelable issue.
- Port kauth for fontinst.

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-23
- add depend on gl/glu to fix build in koji

* Thu Oct 29 2015 sulit <sulitsrc@gmail.com> - 5.4.2-22
- add show desktop widget for pannel

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-21
- Rebuild for new 4.0 release

* Fri Oct 16 2015 Cjacker <cjacker@foxmail.com>
- remove 'formats'/'translation' setting tool.

* Wed Oct 14 2015 Cjacker <cjacker@foxmail.com>
- hide desktoppath.desktop from systemsettings.

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

* Fri Aug 07 2015 Cjacker <cjacker@foxmail.com>
- add patch 200/201 to enable qtaccountservice face support.
