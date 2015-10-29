Name:    ksnapshot 
Summary: A screen capture utility 
Version: 15.04.2
Release: 7.git 

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/ksnapshot
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif 
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}.tar.gz

# Fix file QUrl issue for example $HOME/snapshot1.png/snapshot1.png
Patch1: 0001-fix-file-url.patch

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kparts-devel

BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(xfixes) 

BuildRequires: qt5-qtx11extras-devel

%description
%{summary}.


%prep
%setup -q -n %{name}

%patch1 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-kde --without-mo


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%files -f %{name}.lang
%doc COPYING
%{_kf5_bindir}/%{name}
%{_kf5_bindir}/kbackgroundsnapshot
%{_datadir}/dbus-1/interfaces/org.kde.ksnapshot.xml
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/icons/hicolor/*/*/*


%changelog
* Thu Oct 29 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix file QUrl issue for example $HOME/snapshot1.png/snapshot1.png
- Add missing BuildRequires.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.04.2-6.git
- Rebuild for new 4.0 release

