Name:    dolphin 
Summary: KDE File Manager
Version: 15.08.1
Release: 2 
License: LGPLv2 and LGPLv2+ and GPLv2+ 
URL:     https://projects.kde.org/projects/kde/applications/dolphin

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/applications/%{version}/%{name}-%{version}.tar.xz

#KFileItem.iconName() return iconName from mimedatabase, but the icon may not exist in theme at all.
Patch0:     dolphin-fix-no-icon.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(x11)
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kinit-devel >= 5.10.0-3
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-threadweaver-devel
BuildRequires: kf5-kwallet-devel
#for sidebar search
BuildRequires: baloo-widgets-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel

%{?kf5_kinit_requires}

%description
%{summary}.


%package devel
Summary: Development files for %{name}
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q 
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null || :
fi

%files
%{_sysconfdir}/xdg/servicemenu.knsrc
%{_kf5_bindir}/dolphin
%{_kf5_bindir}/servicemenudeinstallation
%{_kf5_bindir}/servicemenuinstallation

%{_kf5_libdir}/libdolphinprivate.so.*
%{_kf5_libdir}/libdolphinvcs.so.*
%{_kf5_libdir}/libkdeinit5_dolphin.so
%{_kf5_qtplugindir}/*.so
%{_datadir}/appdata/dolphin.appdata.xml
%{_datadir}/applications/org.kde.dolphin.desktop
%{_kf5_datadir}/config.kcfg/*
%{_datadir}/dbus-1/interfaces/org.freedesktop.FileManager1.xml
%{_datadir}/dbus-1/services/org.kde.dolphin.FileManager1.service
%{_kf5_docdir}/HTML/en/dolphin
%{_kf5_datadir}/kservices5/*
%{_kf5_datadir}/kservicetypes5/*
%{_kf5_datadir}/kxmlgui5/dolphin/
%{_kf5_datadir}/kxmlgui5/dolphinpart/

%files devel
%{_includedir}/Dolphin/
%{_includedir}/*.h
%{_kf5_libdir}/cmake/DolphinVcs/
%{_kf5_libdir}/libdolphinvcs.so

%changelog
* Wed Sep 16 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.1
- add baloo-widgets-devel build requires.
