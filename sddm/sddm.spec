Name:           sddm
Version:        0.12.0
Release:        9 
License:        GPLv2+
Summary:        QML based X11 desktop manager

Url:            https://github.com/sddm/sddm

#git@git.isoft.zhcn.cc:zhaixiang/sddm.git

Source0:        https://github.com/sddm/sddm/releases/download/v0.12.0/sddm-%{version}.tar.xz

# Shamelessly stolen from gdm
Source11:       sddm.pam
# Shamelessly stolen from gdm
Source12:       sddm-autologin.pam

# systemd tmpfiles support for /var/run/sddm
Source13:       tmpfiles-sddm.conf

# sample sddm.conf generated with sddm --example-config, and entries commented-out
Source14:   sddm.conf

#patch from leslie to enable accountservice face icon support.
Patch0: 0001-greeter-accounts-service.patch
#!!!!!!!This patch is very important, sddm drops a lot system environment settings such as PATH/JAVA_HOME ...
#it will cause a lot of problem in plasma, since plasma got envs from dm directly.
#Remember, when konsole or other terminal started, it will reload all env settings automatically.
#So, test in konsole works DO NOT means it will works from kickoff menu.
#The better way is respect sysenv and replace some of them use 'insert' as sddm does.
#By Cjacker.
Patch1:	sddm-please-respect-system-path-settings.patch

Provides: service(graphical-login) = sddm

BuildRequires:  cmake
BuildRequires:  systemd
BuildRequires:  pam-devel
BuildRequires:  libxcb-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  pkgconfig
BuildRequires:  python-docutils

BuildRequires: qt5-qtaccountsservice-devel >= 0.6.0
Requires: qt5-qtaccountsservice >= 0.6.0

Requires: qt5-qtbase
Requires: qt5-qtdeclarative
Requires: systemd
Requires: xorg-x11-xinit
Requires: xorg-x11-server-Xorg
%{?systemd_requires}

Requires(pre): shadow-utils

%description
SDDM is a modern display manager for X11 aiming to be fast, simple and
beautiful. It uses modern technologies like QtQuick, which in turn gives the
designer the ability to create smooth, animated user interfaces.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
	-DUSE_QT5=true \
	-DBUILD_MAN_PAGES=true \
	-DENABLE_JOURNALD=true \
	-DENABLE_PLYMOUTH=OFF ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -Dpm 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/sddm
install -Dpm 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/pam.d/sddm-autologin
install -Dpm 644 %{SOURCE13} %{buildroot}%{_tmpfilesdir}/sddm.conf
install -Dpm 644 %{SOURCE14} %{buildroot}%{_sysconfdir}/sddm.conf
mkdir -p %{buildroot}%{_localstatedir}/run/sddm
mkdir -p %{buildroot}%{_localstatedir}/lib/sddm


%pre
getent group sddm >/dev/null || groupadd -r sddm
getent passwd sddm >/dev/null || \
    useradd -r -g sddm -d %{_localstatedir}/lib/sddm -s /sbin/nologin \
    -c "Simple Desktop Display Manager" sddm
exit 0

%post
%systemd_post sddm.service

%preun
%systemd_preun sddm.service

%postun
%systemd_postun sddm.service

%files
%doc COPYING README.md CONTRIBUTORS
%config(noreplace)   %{_sysconfdir}/sddm.conf
%config(noreplace)   %{_sysconfdir}/pam.d/sddm
%config(noreplace)   %{_sysconfdir}/pam.d/sddm-autologin
%config(noreplace)   %{_sysconfdir}/pam.d/sddm-greeter
# it's under /etc, sure, but it's not a config file -- rex
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%{_bindir}/sddm
%{_bindir}/sddm-greeter
%{_libexecdir}/sddm-helper
%{_tmpfilesdir}/sddm.conf
%attr(0711, root, sddm) %dir %{_localstatedir}/run/sddm
%attr(1770, sddm, sddm) %dir %{_localstatedir}/lib/sddm
%{_unitdir}/sddm.service
#%{_unitdir}/sddm-plymouth.service
%{_qt5_archdatadir}/qml/SddmComponents/
%dir %{_datadir}/sddm
%{_datadir}/sddm/faces/
%{_datadir}/sddm/flags/
%{_datadir}/sddm/scripts/
%dir %{_datadir}/sddm/themes/
%{_datadir}/sddm/translations/
%{_mandir}/man*/sddm*

%{_datadir}/sddm/themes/circles/
%{_datadir}/sddm/themes/elarun/
%{_datadir}/sddm/themes/maldives/
%{_datadir}/sddm/themes/maui/

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.12.0-9
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- set default theme to breeze.

* Sun Sep 06 2015 Cjacker <cjacker@foxmail.com>
- update to 0.12

* Fri Aug 07 2015 Cjacker <cjacker@foxmail.com>
- take codes from Leslie Zhai with plymouth smooth transition and qtaccountservice support.
- ENABLE_PLYMOUTH=ON
- rebase patch1.

* Tue Aug 04 2015 Cjacker <cjacker@foxmail.com>
- add patch1, let sddm respect system path settings.
