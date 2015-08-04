Name:    sni-qt
Summary: Plugin for Qt4 that turns QSystemTrayIcons into status notifiers
Version: 0.2.6
Release: 6

License: LGPLv3
URL:     https://launchpad.net/sni-qt
Source0: https://launchpad.net/sni-qt/trunk/%{version}/+download/sni-qt-%{version}.tar.bz2

# From Ubuntu packaging version 0.2.5-0ubuntu3
Source1: sni-qt.conf

BuildRequires: cmake
BuildRequires: pkgconfig(dbusmenu-qt)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtGui) pkgconfig(QtTest)
# %%check
BuildRequires: dbus-x11 xorg-x11-server-Xvfb

%description
This package contains a Qt4 plugin which turns all QSystemTrayIcon into
StatusNotifierItems (appindicators).


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -m644 -D -p %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/sni-qt.conf


%check
#xvfb-run -a dbus-launch --exit-with-session make check ARGS="--output-on-failure --timeout 300" -C %{_target_platform}


%files
%doc COPYING NEWS README
%config(noreplace) %{_sysconfdir}/xdg/sni-qt.conf
%{_qt4_plugindir}/systemtrayicon/


%changelog
