%global kf5_version 5.27.0

Name:           powerdevil
Version:        5.8.3
Release:        1
Summary:        Manages the power consumption settings of a Plasma Shell

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/powerdevil

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
 
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  systemd-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-kauth-devel >= %{kf5_version}
BuildRequires:  kf5-kidletime-devel >= %{kf5_version}
BuildRequires:  kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  kf5-solid-devel >= %{kf5_version}
BuildRequires:  kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  kf5-kglobalaccel-devel >= %{kf5_version}
BuildRequires:  kf5-kio-devel >= %{kf5_version}
BuildRequires:  kf5-kwindowsystem-devel >= %{kf5_version}
BuildRequires:  kf5-plasma-devel >= %{kf5_version}
BuildRequires:  kf5-knotifyconfig-devel >= %{kf5_version}
BuildRequires:  kf5-kdelibs4support-devel >= %{kf5_version}
BuildRequires:  libkscreen-devel >= %{version}
BuildRequires:  kf5-kactivities-devel >= %{kf5_version}
BuildRequires:  kf5-kwayland-devel >= %{kf5_version}
BuildRequires:  plasma-workspace-devel >= %{version}
BuildRequires:  kf5-networkmanager-qt-devel >= %{kf5_version}
BuildRequires:  kf5-bluez-qt-devel >= %{kf5_version}

Requires:       kf5-filesystem
Requires:       libkscreen >= %{version}

%description
Powerdevil is an utility for powermanagement. It consists
of a daemon (a KDED module) and a KCModule for its configuration.

%prep
%setup -q -n %{name}-%{version}

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang powerdevil5 --with-qt --with-kde --all-name

# Don't bother with -devel
rm %{buildroot}/%{_libdir}/libpowerdevil{configcommonprivate,core,ui}.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f powerdevil5.lang
%doc COPYING
%config %{_sysconfdir}/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%{_libdir}/libpowerdevilconfigcommonprivate.so.*
%{_libdir}/libpowerdevilcore.so.*
%{_libdir}/libpowerdevilui.so.*
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/kf5/kded/powerdevil.so
%{_kf5_libexecdir}/kauth/backlighthelper
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_kf5_datadir}/knotifications5/powerdevil.notifyrc
%{_kf5_datadir}/kservices5/*.desktop
#%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_datadir}/doc/HTML/en/kcontrol/powerdevil


%changelog
* Thu Nov 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Thu Jun 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-1
- 5.6.95

* Wed Apr 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.3-1
- 5.6.3

* Thu Apr 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-2
- Add missing file

* Tue Apr 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
- 5.6.2

* Mon Apr 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.1-1
- 5.6.1

* Tue Jan 19 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Remove Hibernate for activityWidget.

* Thu Jan 14 2016 <ming.wang@i-soft.com.cn> - 5.4.3-7
- Amend 5.4.3-4, Fixed logical conflit on Activity Settings.

* Wed Jan 06 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Remove Hibernate but keep suspend.

* Fri Dec 25 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Remove suspend for QA.

* Wed Dec 16 2015 wangming <ming.wang@i-soft.com.cn> - 5.4.3-4
- Fixed logical conflit on Activity Settings.

* Fri Nov 20 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-3
- Backport patches from 5.5

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-3
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

