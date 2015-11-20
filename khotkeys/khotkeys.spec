Name:           khotkeys
Version:        5.4.3
Release:        3%{?dist}
Summary:        Application to configure hotkeys in KDE

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/khotkeys

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

Patch0: khotkeys-5.4.2-qdbusviewer-qt5.patch

#backport patches and fixes from plasma-5.5
#https://git.reviewboard.kde.org/r/125630/
Patch1: 0001-do-not-write-back-dated-settings-from-daemon.patch
#https://git.reviewboard.kde.org/r/125680/
Patch2: 0001-unselect-current-item-on-clicking-into-empty-space.patch
#https://quickgit.kde.org/?p=khotkeys.git&a=commit&h=4747599badf67389530483ea62b6f54bc36ac9c3
Patch3: schedule-saving-to-next-event-cycle.patch
#https://git.reviewboard.kde.org/r/125769/
Patch4: use-dbus-mutex-to-prevent-write-back-outdated-configs.patch
 
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros

BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  libX11-devel
BuildRequires:  plasma-workspace-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel


Requires:       kf5-filesystem

# when khotkeys was split out of kde-workspace-4.11.x
Conflicts:      kde-workspace < 4.11.15-3

# upgrade path from khotkeys-libs-4.11.x (skip Provides for now, it was only ever a private library)
Obsoletes:      khotkeys-libs < 5.0.0
#Provides:       khotkeys-libs = %{version}-%{release}

%description
An advanced editor component which is used in numerous KDE applications
requiring a text editing component.

%package        devel
Summary:        Development files for %{name}
# strictly speaking, not required in this case, but still often expected to pull in subpkg -- rex
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang khotkeys


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f khotkeys.lang
%doc COPYING
%{_kf5_libdir}/libkhotkeysprivate.so.*
%{_kf5_qtplugindir}/kcm_hotkeys.so
%{_kf5_qtplugindir}/kded_khotkeys.so
%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservices5/khotkeys.desktop
%{_datadir}/khotkeys/
%{_datadir}/doc/HTML/en/kcontrol/khotkeys/

%files devel
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
%{_libdir}/cmake/KHotKeysDBusInterface/


%changelog
* Fri Nov 20 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-3
- Backport some fixes from plasma-5.5

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-4
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

