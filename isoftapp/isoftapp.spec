Name: isoftapp
Version: 2.1.1
Release: 1%{?dist}
Summary: iSOFT AppStore Skeleton

License: GPLv2 or GPLv3
URL: http://git.isoft.zhcn.cc/zhaixiang/isoftapp
Source0: %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: dbus-glib-devel
BuildRequires: librpm-devel
BuildRequires: popt-devel
BuildRequires: uriparser-devel
BuildRequires: libcurl-devel
BuildRequires: sqlite-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qtsingleapplication-qt5-devel

Requires: systemd

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
iSOFT AppStore Skeleton.


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

%find_lang org.isoftlinux.Isoftapp

%post
%systemd_post isoftapp-daemon.service

%preun
%systemd_preun isoftapp-daemon.service

%postun
%systemd_postun isoftapp-daemon.service


%files -f org.isoftlinux.Isoftapp.lang
%{_sysconfdir}/isoftapp/default.conf.example
%{_sysconfdir}/isoftapp/config.d/other.conf.example
%{_sysconfdir}/xdg/autostart/isoftapp_systray.desktop
%{_sysconfdir}/dbus-1/system.d/org.isoftlinux.Isoftapp.conf
%{_datadir}/isoftapp/pkgcache.db
%{_datadir}/dbus-1/interfaces/org.isoftlinux.Isoftapp.xml
%{_datadir}/dbus-1/system-services/org.isoftlinux.Isoftapp.service
%{_unitdir}/isoftapp-daemon.service
%{_bindir}/isoft-genpkglist
%{_bindir}/isoft-gensrclist
%{_bindir}/isoft-countpkglist
%{_bindir}/isoft-genbasedir
%{_bindir}/isoftapp
%{_bindir}/isoftapp-daemon
%{_bindir}/isoftapp_systray

%changelog
* Tue Dec 29 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- isoftapp system dbus service implementation by fujiang.
- Fix search hang issue by fujiang.
- Fix search duplicate issue by fujiang.

* Tue Dec 15 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix remove package not in cache issue.

* Mon Dec 14 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Cleanup command info. 

* Fri Dec 11 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Full features support by fujiang.
- Fix upgrade issue.

* Thu Dec 10 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add list-uninstalled and upgrade by fujiang.

* Wed Dec 09 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Rename gen* to isoft-gen* to avoid conflict with apt package.
- New configuration multi-repos support.
- Show detail error notice for configuration file.
- Add remove confirm.
- Add list-installed by fujiang.

* Tue Dec 08 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Release isoftapp v0.1.0 only support update, install, remove, check by fujiang.

