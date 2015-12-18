Name:           plasma-nm
Version:        5.4.3
Release:        4
Summary:        Plasma Next applet written in QML for managing network connections
License:        LGPLv2+ and GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/plasma-nm

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

# Add plasma-nm to default systray if needed, for upgraders...
Source10:       01-plasma-nm.js

#add an entry to systemsettings.
Source11: connection-editor.desktop

#patch
Patch0001: hide-menu-item.patch

#https://git.reviewboard.kde.org/r/126035/
#Add --import-vpn argument to connection editor
Patch0002: importvpn.patch

Patch0003: hide-wired-autonegotiate-checkbox.patch
# Upstream patches

BuildRequires:  gettext

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kinit-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-networkmanager-qt-devel
# API changed in 5.9.0
BuildRequires:  kf5-modemmanager-qt-devel >= 5.9.0

BuildRequires:  pkgconfig(NetworkManager) >= 0.9.8
BuildRequires:  pkgconfig(ModemManager) >= 1.0.0
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(openconnect) >= 4.00

BuildRequires:  mobile-broadband-provider-info-devel

Requires:       NetworkManager >= 0.9.8

Requires:       kf5-filesystem

Provides:       kde-plasma-nm = %{version}-%{release}

%description
Plasma applet and editor for managing your network connections in KDE 4 using
the default NetworkManager service.

# Required for properly working GMS/CDMA connections
%package        mobile
Summary:        Mobile support for %{name}
Requires:       ModemManager
Requires:       mobile-broadband-provider-info
Requires:       kf5-modemmanager-qt >= 5.0.0-1
Obsoletes:      kde-plasma-networkmanagement-mobile < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-mobile < 5.0.0-1
Provides:       kde-plasma-nm-mobile = %{version}-%{release}
%description    mobile
%{summary}.

%package        openvpn
Summary:        OpenVPN support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openvpn
Obsoletes:      kde-plasma-networkmanagement-openvpn < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-openvpn < 5.0.0-1
Provides:       kde-plasma-nm-openvpn = %{version}-%{release}
%description    openvpn
%{summary}.

%package        vpnc
Summary:        Vpnc support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-vpnc
Obsoletes:      kde-plasma-networkmanagement-vpnc < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-vpnc < 5.0.0-1
Provides:       kde-plasma-nm-vpnc = %{version}-%{release}
%description    vpnc
%{summary}.

%package        openconnect
Summary:        OpenConnect support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openconnect
Obsoletes:      kde-plasma-networkmanagement-openconnect < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-openconnect < 5.0.0-1
Provides:       kde-plasma-nm-openconnect = %{version}-%{release}
%description    openconnect
%{summary}.

%package        openswan
Summary:        Openswan support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openswan
Obsoletes:      kde-plasma-nm-openswan < 5.0.0-1
Provides:       kde-plasma-nm-openswan = %{version}-%{release}
%description    openswan
%{summary}.

%package        strongswan
Summary:        Strongswan support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       strongswan
Obsoletes:      kde-plasma-nm-strongswan < 5.0.0-1
Provides:       kde-plasma-nm-strongswan = %{version}-%{release}
%description    strongswan
%{summary}.

%package        l2tp
Summary:        L2TP support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-l2tp
Obsoletes:      kde-plasma-nm-l2tp < 5.0.0-1
Provides:       kde-plasma-nm-l2tp = %{version}-%{release}
%description    l2tp
%{summary}.

%package        pptp
Summary:        PPTP support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-pptp
Obsoletes:      kde-plasma-networkmanagement-pptp < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-pptp < 5.0.0-1
Provides:       kde-plasma-nm-pptp = %{version}-%{release}
%description    pptp
%{summary}.

%package        ssh
Summary:        SSH suppor for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-ssh
%description    ssh
%{summary}.

%package        sstp
Summary:        SSTP support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    sstp
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang plasma_applet_org.kde.plasma.networkmanagement
%find_lang plasmanetworkmanagement-kded
%find_lang kde5-nm-connection-editor
%find_lang plasmanetworkmanagement-libs
%find_lang plasmanetworkmanagement_vpncui
%find_lang plasmanetworkmanagement_openvpnui
%find_lang plasmanetworkmanagement_openconnectui
%find_lang plasmanetworkmanagement_openswanui
%find_lang plasmanetworkmanagement_strongswanui
%find_lang plasmanetworkmanagement_l2tpui
%find_lang plasmanetworkmanagement_pptpui
%find_lang plasmanetworkmanagement_sshui
%find_lang plasmanetworkmanagement_sstpui

# migrate to nm plasmoid
install -m644 -p -D %{SOURCE10} %{buildroot}%{_datadir}/plasma/updates/01-plasma-nm.js

# Add an systemsettings entry.
mkdir -p %{buildroot}%{_datadir}/kservices5/
install -m 0644 %{SOURCE11} %{buildroot}%{_datadir}/kservices5/


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f plasma_applet_org.kde.plasma.networkmanagement.lang -f plasmanetworkmanagement-kded.lang -f kde5-nm-connection-editor.lang -f plasmanetworkmanagement-libs.lang
%{_bindir}/kde5-nm-connection-editor
%{_libdir}/libplasmanm_internal.so
%{_libdir}/libplasmanm_editor.so
%{_kf5_datadir}/kxmlgui5/kde5-nm-connection-editor/kde5-nm-connection-editorui.rc
%{_datadir}/applications/kde5-nm-connection-editor.desktop
# plasma-nm applet
%{_qt5_prefix}/qml/org/kde/plasma/networkmanagement/libplasmanm_qmlplugins.so
%{_qt5_prefix}/qml/org/kde/plasma/networkmanagement/qmldir
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement/
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement/contents
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement/metadata.desktop
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.networkmanagement.desktop
%{_datadir}/plasma/updates/*.js
# plasma-nm notifications
%{_kf5_datadir}/knotifications5/networkmanagement.notifyrc
# plasma-nm kded
%{_kf5_qtplugindir}/kded_networkmanagement.so
%{_kf5_datadir}/kservices5/kded/networkmanagement.desktop
# plasma-nm other
%{_kf5_datadir}/kservicetypes5/plasma-networkmanagement-vpnuiplugin.desktop

#systemsettings entry
%{_datadir}/kservices5/connection-editor.desktop

%files mobile

%files openvpn -f plasmanetworkmanagement_openvpnui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_openvpnui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_openvpnui.desktop

%files vpnc -f plasmanetworkmanagement_vpncui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_vpncui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_vpncui.desktop

%files openconnect -f plasmanetworkmanagement_openconnectui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_openconnectui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_openconnectui.desktop

%files openswan -f plasmanetworkmanagement_openswanui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_openswanui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_openswanui.desktop

%files strongswan -f plasmanetworkmanagement_strongswanui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_strongswanui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_strongswanui.desktop

%files l2tp -f plasmanetworkmanagement_l2tpui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_l2tpui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_l2tpui.desktop

%files pptp -f plasmanetworkmanagement_pptpui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_pptpui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_pptpui.desktop

%files ssh -f plasmanetworkmanagement_sshui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_sshui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_sshui.desktop

%files sstp -f plasmanetworkmanagement_sstpui.lang
%{_kf5_qtplugindir}/libplasmanetworkmanagement_sstpui.so
%{_kf5_datadir}/kservices5/plasmanetworkmanagement_sstpui.desktop

%changelog
* Fri Dec 18 2015 fj <fujiang.zhu@i-soft.com.cn> - 5.4.3-4
- hide-wired-autonegotiate-checkbox

* Thu Nov 12 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-3
- Add importvpn arg to connection-editor

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Tue Nov 03 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-7
- Change patch, restore all VPN protocols

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-4
- Rebuild for new 4.0 release

* Mon Oct 19 2015 Cjacker <cjacker@foxmail.com>
- add an systemsettings entry for kde4-nm-connection-editor

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

