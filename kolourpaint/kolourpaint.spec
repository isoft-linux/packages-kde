Name:    kolourpaint
Summary: An easy-to-use paint program 
Version: 15.12.0 
Release: 2.git

License: BSD 
URL:     https://projects.kde.org/projects/kde/kdegraphics/kolourpaint
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

#git version
#git clone git://anongit.kde.org/kolourpaint
#git checkout frameworks
Source0: kolourpaint.tar.gz
Patch1: modify_include_head_file_for_scandialog.patch
#kxmlgui menubar item not localized, fix it
Patch2: kolourpaint-fix-menu-i18n.patch
Patch3: kolourpaint-bump-verion-to-match-kde-applications.patch

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
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: libksane5-devel
BuildRequires: qimageblitz-devel

BuildRequires: appstream-glib
#BuildRequires: pkgconfig(qimageblitz)

%description
%{summary}.

%prep
%setup -q -n %{name}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-kde --without-mo || :

## unpackaged files
rm -fv %{buildroot}%{_kf5_libdir}/libkolourpaint_lgpl.so


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_datadir}/appdata/%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/%{name}.desktop


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%files
%{_kf5_bindir}/kolourpaint
%{_kf5_libdir}/libkolourpaint_lgpl.so.*

%{_kf5_datadir}/kolourpaint
%{_kf5_datadir}/appdata/kolourpaint.appdata.xml
%{_kf5_datadir}/doc/HTML/*/kolourpaint
%{_kf5_datadir}/applications/kolourpaint.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/kolourpaint.*
%{_kf5_datadir}/kxmlgui5/kolourpaint/

%changelog
* Sat Dec 19 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2.git
- Bump version

* Sat Dec 19 2015 Cjacker <cjacker@foxmail.com> - 5.0.0-5.git
- Fix menu bar item i18n

* Thu Dec 17 2015 sulit <sulitsrc@gmail.com> - 5.0.0-4.git
- add libksane5-devel buildrequire for scan
- add qimageblitz-devel buildrequire for scan
- update to git codes
- add modify scandialog head file include patch, I get the help
- from Leslie Zhai

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.0.0-3.git
- Rebuild for new 4.0 release

