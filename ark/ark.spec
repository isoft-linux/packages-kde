%global p7zip 1

Name:    ark
Summary: Archive manager
Version: 15.12.0
Release: 2 

License: GPLv2+
URL:     http://utils.kde.org/projects/ark 
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0: del-rar.patch
Patch1: servicesmenus-localization.patch

#git clone git://anongit.kde.org/ark
#git checkout frameworks
#Source0: ark.tar.gz

## upstream patches

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
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-khtml-devel
BuildRequires: kf5-kjs-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kpty-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-karchive-devel
BuildRequires: qt5-qtbase-devel

BuildRequires: libarchive-devel
BuildRequires: bzip2-devel
BuildRequires: appstream-glib
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(liblzma) 
BuildRequires: zlib-devel

Provides: ark-part = %{version}-%{release}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Requires: bzip2
Requires: gzip

%if 0%{?p7zip}
Requires: p7zip-plugins
%endif

#Requires: unar
Requires: unzip

%description
Ark is a program for managing various archive formats.

Archives can be viewed, extracted, created and modified from within Ark.
The program can handle various formats such as tar, gzip, bzip2, zip,
rar and lha (if appropriate command-line programs are installed).

%package libs
Summary: Runtime libraries for %{name} 
# libkerfuffle is BSD, plugins are mix of BSD and GPLv2+
License: BSD and GPLv2+
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1 

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

rm -rf %{buildroot}%{_libdir}/libkerfuffle.so

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_datadir}/appdata/*.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.ark.desktop


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:
fi

%files 
%{_kf5_mandir}/man1/ark.1*
%{_sysconfdir}/xdg/ark.categories
%{_kf5_bindir}/ark
%{_kf5_qtplugindir}/kf5/kio_dnd/extracthere.so
%{_kf5_qtplugindir}/arkpart.so
%{_kf5_datadir}/kxmlgui5/ark/ark_part.rc
%{_kf5_datadir}/kxmlgui5/ark/arkui.rc

%{_kf5_datadir}/config.kcfg/ark.kcfg
%{_kf5_datadir}/appdata/*.appdata.xml
%{_kf5_datadir}/applications/org.kde.ark.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/ark.*
%{_kf5_datadir}/kservices5/ServiceMenus/ark_addtoservicemenu.desktop
%{_kf5_datadir}/kservices5/ServiceMenus/ark_servicemenu.desktop
%{_kf5_datadir}/kservices5/ark_part.desktop

%{_kf5_docdir}/HTML/*/ark
%{_mandir}/man1/ark.1*

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{_kf5_libdir}/libkerfuffle.so.*
%{_kf5_qtplugindir}/kerfuffle_*.so
%{_kf5_datadir}/kservices5/kerfuffle_*.desktop
%{_kf5_datadir}/kservicetypes5/kerfufflePlugin.desktop


%changelog
* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update to stable release

* Thu Dec 03 2015 kun.li@i-soft.com.cn - 15.11.80-8
- add servicesmenus-localization.patch 

* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-7
- Update

* Mon Nov 16 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-6
- Only disable rar support in popup menu

* Mon Nov 16 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-5
- DO NOT disable rar support, Otherwise dolphin can not unrar archives, 
- we already provide the opensource unrar in framework.
- to solve the problem, we should provide rar command in app.

* Fri Nov 13 2015 kun.li@i-soft.com.cn - 15.08.3-5
- Add del-rar.patch 

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-3
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2
