Summary: Config files for kde
Name:    kde-settings
Version: 40 
Release: 7%{?dist}

License: MIT
Source0: %{name}-%{version}.tar.xz

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
%setup -q -n %{name}-%{version}


%build
# Intentionally left blank.  Nothing to see here.


%install
mkdir -p %{buildroot}{%{_datadir}/config,%{_sysconfdir}/kde/kdm}

tar cpf - . | tar --directory %{buildroot} -xvpf -


#until our logo finished. use it to setup logo's of start menu
rm -rf %{buildroot}%{_datadir}/plasma/shells/org.kde.plasma.desktop/updates/00-start-here-kde-isoft-2.js

#this is for kde4
rm -rf %{buildroot}%{_datadir}/kde-settings/kde-profile/default/share/apps/plasma-desktop/updates/00-start-here-kde-isoft-2.js

%files 
%config(noreplace) %{_sysconfdir}/profile.d/kde.*
%{_sysconfdir}/kde/env/env.sh
%{_sysconfdir}/kde/env/gtk2_rc_files.sh
%config(noreplace) %{_sysconfdir}/xdg/kdeglobals
%config(noreplace) %{_sysconfdir}/xdg/kdebugrc
%{_datadir}/polkit-1/rules.d/11-isoft-policy.rules
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
%{_sysconfdir}/xdg/dolphinrc
#%{_datadir}/plasma/shells/org.kde.plasma.desktop/updates/00-start-here-kde-isoft-2.js
%{_sysconfdir}/xdg/plasma-workspace/env/env.sh
%{_sysconfdir}/xdg/plasma-workspace/env/gtk2_rc_files.sh
%{_sysconfdir}/xdg/plasma-workspace/env/gtk3_scrolling.sh

%files -n qt-settings
%config(noreplace) %{_sysconfdir}/xdg/QtProject/qtlogging.ini
%config(noreplace) %{_sysconfdir}/Trolltech.conf
%config(noreplace) %{_sysconfdir}/profile.d/qt-graphicssystem.*


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 40-7
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- change default browser to chromium in /etc/xdg/kdeglobals.

* Tue Oct 13 2015 Cjacker <cjacker@foxmail.com>
- set default icon size of dolphin IconMode to 64. /etc/xdg/dolphinrc
- set "SingleClick=false" in /etc/xdg/kdeglobals

* Mon Aug 17 2015 Cjacker <cjacker@foxmail.com>
- add more policy controls of wheel group to 11-isoft-policy.rules

* Fri Aug 14 2015 Cjacker <cjacker@foxmail.com>
- add default browser in /etc/xdg/kdeglobals
