%define active 0 
%define chm 1
%define ebook 1
%define mobi 0 

Name:    okular 
Summary: A document viewer
Version: 1.0.0 
Release: 8.git%{?dist}

License: GPLv2
URL:     https://projects.kde.org/projects/kde/kdegraphics/okular
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

#git clone git://anongit.kde.org/okular
#git checkout frameworks
Source0: okular.tar.gz

#below patches is created by Cjacker.
Patch0: okular-fix-accident-pdf-stretch.patch
Patch1: okular-kio-with-slash-not-work-fix.patch
Patch2: okular-fix-epub-fetch-file.patch

%if 0%{?chm}
BuildRequires: chmlib-devel
%endif
BuildRequires: desktop-file-utils
%if 0%{?ebook}
BuildRequires: ebook-tools-devel
%endif
%if 0%{?mobi}
BuildRequires: qmobipocket-devel
%endif
BuildRequires: kf5-libkexiv2-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig(ddjvuapi) 

BuildRequires: kscreen >= 5.3.2 

BuildRequires: pkgconfig(libspectre)
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: pkgconfig(qca2)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: pkgconfig(zlib)

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


%description
%{summary}.

%package active
Summary: Document viewer for plasma active
# todo: test/confirm this dep is sufficient (or too much) -- rex
Requires: %{name}-part%{?_isa} = %{version}-%{release}
%description active
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kdelibs-devel
%description devel
%{summary}.

%package  libs 
Summary:  Runtime files for %{name} 
%description libs 
%{summary}.

%package part
Summary: Okular kpart plugin
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description part
%{summary}.

%package -n kio_msits
Summary: A kioslave for displaying WinHelp files
%description -n kio_msits
%{summary}.



%prep
%setup -q -n okular
%patch0 -p1
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

%if ! 0%{?active}
rm -rf %{buildroot}%{_kf5_datadir}/kpackage/genericqml/org.kde.active.documentviewer
rm -rf %{buildroot}%{_kf5_datadir}/applications/active-documentviewer_*.desktop
rm -rf %{buildroot}%{_kf5_datadir}/applications/org.kde.active.documentviewer.desktop
rm -rf %{buildroot}%{_kf5_datadir}/applications/org.kde.mobile.*
rm -rf %{buildroot}%{_kf5_datadir}/kpackage/genericqml/org.kde.mobile.okular
%endif


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.okular.desktop

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
%{_kf5_bindir}/okular*
%{_kf5_datadir}/applications/okularApplication_*.desktop
%{_kf5_datadir}/applications/org.kde.okular.desktop

%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_docdir}/HTML/*/okular
%{_mandir}/man1/okular.1*

%if 0%{?active}
%files active
%{_kf5_datadir}/kpackage/genericqml/org.kde.active.documentviewer
%{_kf5_datadir}/applications/active-documentviewer_fb.desktop
%{_kf5_datadir}/applications/org.kde.active.documentviewer.desktop
%endif

%files devel
%{_kf5_libdir}/libOkular5Core.so
%dir %{_libdir}/cmake/Okular5
%{_libdir}/cmake/Okular5/*

%dir %{_includedir}/okular
%{_includedir}/okular/*

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig


%files libs
%{_kf5_libdir}/libOkular5Core.so.*
%{_kf5_datadir}/kconf_update/okular.upd


%files part
%{_kf5_qtplugindir}/okularGenerator_*.so
%{_kf5_qtplugindir}/okularpart.so

%dir %{_kf5_qmldir}/org/kde/okular
%{_kf5_qmldir}/org/kde/okular/*

%{_kf5_datadir}/kservicetypes5/okularGenerator.desktop
%{_kf5_datadir}/kservices5/libokularGenerator_*.desktop
%{_kf5_datadir}/kservices5/okular[A-Z]*.desktop
%{_kf5_datadir}/kservices5/okular_part.desktop

%dir %{_kf5_datadir}/okular
%{_kf5_datadir}/okular/*

%dir %{_kf5_datadir}/kxmlgui5/okular
%{_kf5_datadir}/kxmlgui5/okular/*

%{_kf5_datadir}/config.kcfg/*.kcfg

%if 0%{?chm}
%files -n kio_msits
%{_kf5_qtplugindir}/kio_msits.so
%{_kf5_datadir}/kservices5/msits.protocol
%endif


%changelog
* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 1.0.0-8.git
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1.0.0-7.git
- Rebuild for new 4.0 release

* Sat Oct 10 2015 Cjacker <cjacker@foxmail.com>
- add patch0 to fix pdf stretch issue.
- it's related to qt5, the dpi width should be equal to height.
- add patch1 to fix chm kio_msits issue.
- add patch2 to fix epub image fetch issue.






