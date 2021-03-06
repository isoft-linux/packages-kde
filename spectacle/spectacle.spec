%global kf5_version 5.28.0

Name: spectacle
Summary: A screen capture utility 
Version: 16.08.3
Release: 1

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/ksnapshot
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif 
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules >= %{kf5_version}
BuildRequires: gettext
BuildRequires: kf5-rpm-macros >= %{kf5_version}
BuildRequires: kf5-kcompletion-devel >= %{kf5_version}
BuildRequires: kf5-kconfig-devel >= %{kf5_version}
BuildRequires: kf5-kconfigwidgets-devel >= %{kf5_version}
BuildRequires: kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires: kf5-kdbusaddons-devel >= %{kf5_version}
BuildRequires: kf5-kdeclarative-devel >= %{kf5_version}
BuildRequires: kf5-kguiaddons-devel >= %{kf5_version}
BuildRequires: kf5-ki18n-devel >= %{kf5_version}
BuildRequires: kf5-kiconthemes-devel >= %{kf5_version}
BuildRequires: kf5-kitemviews-devel >= %{kf5_version}
BuildRequires: kf5-kio-devel >= %{kf5_version}
BuildRequires: kf5-kjobwidgets-devel >= %{kf5_version}
BuildRequires: kf5-knewstuff-devel >= %{kf5_version}
BuildRequires: kf5-knotifyconfig-devel >= %{kf5_version}
BuildRequires: kf5-knewstuff-devel >= %{kf5_version}
BuildRequires: kf5-kservice-devel >= %{kf5_version}
BuildRequires: kf5-kwindowsystem-devel >= %{kf5_version}
BuildRequires: kf5-kwidgetsaddons-devel >= %{kf5_version}
BuildRequires: kf5-kxmlgui-devel >= %{kf5_version}
BuildRequires: kf5-kdoctools-devel >= %{kf5_version}
BuildRequires: kf5-kparts-devel >= %{kf5_version}
BuildRequires: kf5-knotifications-devel >= %{kf5_version}
BuildRequires: kf5-libkipi-devel >= %{version}
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(xfixes) 

BuildRequires: libkscreen-devel

BuildRequires: qt5-qtx11extras-devel

%description
%{summary}.


%prep
%setup -q

%build
mkdir -p %{_target_platform}
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

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%files
%doc COPYING
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/knotifications5/spectacle.notifyrc
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/khotkeys/spectacle.khotkeys
%{_kf5_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_kf5_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_docdir}/HTML/en/spectacle



%changelog
* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 16.08.3-1
- 16.08.3-1

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 15.12.3-1
- 15.12.3

* Sat Dec 19 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-4
- Add zh_CN info for khotkeys

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-3
- Fix xcb dependency

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sun Nov 22 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Initial build

