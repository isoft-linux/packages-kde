Name: kwrite
Summary: Text Editor
Version: 15.11.90
Release: 2
License: LGPLv2 and LGPLv2+ and GPLv2+ 
URL:     https://projects.kde.org/projects/kde/applications/kate

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/kate-%{version}.tar.xz

#use /usr/src/rust/src instead of /usr/local/src/rust/src
Patch0: kate-rust-plugin-src-dir.patch

# https://git.reviewboard.kde.org/r/126197/
Patch1: prepend-dir-when-open-file-via-dbus.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(x11)
BuildRequires: kf5-rpm-macros
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
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel

%description
%{summary}.

%prep
%setup -q -n kate-%{version}
%patch0 -p1
%patch1 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}/kwrite
make %{?_smp_mflags} -C %{_target_platform}/doc/kwrite


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/kwrite
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/doc/kwrite


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.kwrite.desktop


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
%{_kf5_bindir}/kwrite
%{_kf5_datadir}/icons/hicolor/*/apps/kwrite.*
%{_kf5_datadir}/applications/org.kde.kwrite.desktop
%{_datadir}/appdata/org.kde.kwrite.appdata.xml
%{_kf5_docdir}/HTML/en/kwrite/


%changelog
* Wed Dec 16 2015 Cjacker <cjacker@foxmail.com> - 15.11.90-2
- Update

* Thu Dec 03 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-3
- https://git.reviewboard.kde.org/r/126197/

* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-3
- add toml highlight patch

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-3
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- rebuild with new libgit2
