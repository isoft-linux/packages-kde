Name:           khotkeys
Version:        5.7.4
Release:        1%{?dist}
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

%description
An advanced editor component which is used in numerous KDE applications
requiring a text editing component.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

#NOT conflict with spectacle
rm -rf %{buildroot}%{_kf5_datadir}/khotkeys/printscreen.khotkeys
rm -rf %{buildroot}%{_kf5_datadir}/khotkeys/defaults.khotkeys
rm -rf %{buildroot}%{_kf5_datadir}/khotkeys/kde32b1.khotkeys
rm -rf %{buildroot}%{_kf5_datadir}/khotkeys/konqueror_gestures_kde321.khotkeys

%find_lang khotkeys

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f khotkeys.lang
%doc COPYING
%{_kf5_libdir}/libkhotkeysprivate.so.*
%{_kf5_qtplugindir}/kcm_hotkeys.so
%{_kf5_qtplugindir}/kf5/kded/khotkeys.so
#%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservices5/khotkeys.desktop
%dir %{_kf5_datadir}/khotkeys/
%{_docdir}/HTML/en/kcontrol/khotkeys/

%files devel
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
%{_libdir}/cmake/KHotKeysDBusInterface/


%changelog
* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Thu Jan 07 2016 Cjacker <cjacker@foxmail.com> - 5.4.3-6
- Backport git fix of QString QKeySequence compare

* Sat Dec 19 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-5
- Remove all preset non-used hotkeys

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-4
- Remove printscreen hotkeys

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

