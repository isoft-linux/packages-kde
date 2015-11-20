Name:           powerdevil
Version:        5.4.3
Release:        3
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

Patch0:         powerdevil-enable-upower.patch

#https://git.reviewboard.kde.org/r/125182/
Patch1:         do-not-ignore-brightness-key-during-animation.patch
#https://quickgit.kde.org/?p=powerdevil.git&a=commit&h=4c66646761834236f6b14789162fe71f6179f472
Patch2:         show-full-charged-msg-instead-of-not-charging-when-full.patch

 
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

BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kscreen-devel
BuildRequires:  kf5-kactivities-devel

BuildRequires:  plasma-workspace-devel

Requires:       kf5-filesystem

%description
Powerdevil is an utility for powermanagement. It consists
of a daemon (a KDED module) and a KCModule for its configuration.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .enable-upower
%patch1 -p1
%patch2 -p1

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
%{_kf5_libexecdir}/kauth/backlighthelper
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_kf5_datadir}/knotifications5/powerdevil.notifyrc
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_datadir}/doc/HTML/en/kcontrol/powerdevil


%changelog
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

