
%global rel 11
%global system_kde_theme_ver 20.90

Summary: Config files for kde
Name:    kde-settings
Version: 22
Release: %{rel}%{?dist}

License: MIT
Url:     http://fedorahosted.org/kde-settings
Source0: https://fedorahosted.org/releases/k/d/kde-settings/%{name}-%{version}-%{rel}.tar.xz

BuildArch: noarch

BuildRequires: kde-filesystem
BuildRequires: systemd

# when kdebugrc was moved here
Conflicts: kf5-kdelibs4support < 5.7.0-3

Requires: kde-filesystem
# /etc/pam.d/ ownership
Requires: pam
Requires: xdg-user-dirs
## add breeze deps here? probably, need more too -- rex
Requires: breeze-icon-theme

Requires(post): coreutils sed

%description
%{summary}.

## FIXME
%package minimal
Summary: Minimal configuration files for KDE
Requires: %{name} = %{version}-%{release}
Requires: xorg-x11-xinit
%description minimal
%{summary}.

%package plasma
Summary: Configuration files for plasma 
Requires: %{name} = %{version}-%{release}
%description plasma 
%{summary}.

%package -n qt-settings
Summary: Configuration files for Qt 
# qt-graphicssystem.* scripts use lspci
Requires: pciutils
%description -n qt-settings
%{summary}.


%prep
%setup -q -n %{name}-%{version}-%{rel}


%build
# Intentionally left blank.  Nothing to see here.


%install
mkdir -p %{buildroot}{%{_datadir}/config,%{_sysconfdir}/kde/kdm}

tar cpf - . | tar --directory %{buildroot} -xvpf -

rm -rf $RPM_BUILD_ROOT/etc/kde/env/fedora-bookmarks.sh
rm -rf $RPM_BUILD_ROOT/etc/kde/kdm/README
rm -rf $RPM_BUILD_ROOT/etc/kde/kdm/Xaccess
rm -rf $RPM_BUILD_ROOT/etc/kde/kdm/Xresources
rm -rf $RPM_BUILD_ROOT/etc/kde/kdm/Xsession
rm -rf $RPM_BUILD_ROOT/etc/kde/kdm/Xsetup
rm -rf $RPM_BUILD_ROOT/etc/kde/kdm/Xwilling
rm -rf $RPM_BUILD_ROOT/etc/kde/kdm/kdmrc
rm -rf $RPM_BUILD_ROOT/etc/logrotate.d/kdm
rm -rf $RPM_BUILD_ROOT/etc/pam.d/kdm
rm -rf $RPM_BUILD_ROOT/etc/pam.d/kdm-np
rm -rf $RPM_BUILD_ROOT/etc/xdg/kdebugrc
rm -rf $RPM_BUILD_ROOT/etc/xdg/plasmarc
rm -rf $RPM_BUILD_ROOT/usr/lib/rpm/fileattrs/plasma4.attr
rm -rf $RPM_BUILD_ROOT/usr/lib/rpm/plasma4.prov
rm -rf $RPM_BUILD_ROOT/usr/lib/rpm/plasma4.req
rm -rf $RPM_BUILD_ROOT/usr/lib/systemd/system/kdm.service
rm -rf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/kdm.conf
rm -rf $RPM_BUILD_ROOT/usr/share/plasma/shells/org.kde.plasma.desktop/updates/00-start-here-kde-fedora-2.js
rm -rf $RPM_BUILD_ROOT/usr/share/polkit-1/rules.d/11-fedora-kde-policy.rules
rm -rf $RPM_BUILD_ROOT/var/lib/kdm/backgroundrc

#rm -rf $RPM_BUILD_ROOT/usr/share/kde-settings/kde-profile/default/share/applications
rm -rf $RPM_BUILD_ROOT/usr/share/kde-settings/kde-profile/default/share/apps/konqueror
#rm -rf $RPM_BUILD_ROOT/usr/share/kde-settings/kde-profile/default/share/apps/plasma-desktop
#rm -rf $RPM_BUILD_ROOT/usr/share/kde-settings/kde-profile/minimal/share/apps/plasma-desktop
#rm -rf $RPM_BUILD_ROOT/usr/share/kde-settings/kde-profile/minimal/share/config


%files 
%config(noreplace) %{_sysconfdir}/profile.d/kde.*
%{_sysconfdir}/kde/env/env.sh
%{_sysconfdir}/kde/env/gpg-agent-startup.sh
%{_sysconfdir}/kde/shutdown/gpg-agent-shutdown.sh
%{_sysconfdir}/kde/env/gtk2_rc_files.sh
%config(noreplace) %{_sysconfdir}/xdg/kdeglobals
%config(noreplace) /etc/pam.d/kcheckpass
%config(noreplace) /etc/pam.d/kscreensaver

# drop noreplace, so we can be sure to get the new kiosk bits
%config %{_sysconfdir}/kderc
%config %{_sysconfdir}/kde4rc
%dir %{_datadir}/kde-settings/
%dir %{_datadir}/kde-settings/kde-profile/
%{_datadir}/kde-settings/kde-profile/default/

%files minimal
%{_datadir}/kde-settings/kde-profile/minimal/
%{_sysconfdir}/X11/xinit/xinitrc.d/20-kdedirs-minimal.sh

%files plasma
%config(noreplace) %{_sysconfdir}/xdg/kcminputrc
#%config(noreplace) %{_sysconfdir}/xdg/plasmarc
#%{_datadir}/plasma/shells/org.kde.plasma.desktop/updates/00-start-here-kde-fedora-2.js
%{_sysconfdir}/xdg/plasma-workspace/env/env.sh
%{_sysconfdir}/xdg/plasma-workspace/env/gtk2_rc_files.sh
%{_sysconfdir}/xdg/plasma-workspace/env/gtk3_scrolling.sh

%files -n qt-settings
%config(noreplace) %{_sysconfdir}/xdg/QtProject/qtlogging.ini
%config(noreplace) %{_sysconfdir}/Trolltech.conf
%config(noreplace) %{_sysconfdir}/profile.d/qt-graphicssystem.*


%changelog
