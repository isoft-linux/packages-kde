Name:    libkdegames
Summary: Common code and data for many KDE games
Version: 15.12.0
Release: 2

# libKF5KDEGames is LGPLv2, libKF5KDEGamesPrivate is GPLv2+
License: LGPLv2 and GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegames/libkdegames
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/libkdegames-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdnssd-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-khtml-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kio-devel
BuildREquires: kf5-knewstuff-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: pkgconfig(Qt5Widgets) pkgconfig(Qt5Qml) pkgconfig(Qt5Quick) pkgconfig(Qt5QuickWidgets) pkgconfig(Qt5Svg) pkgconfig(Qt5Test)

BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(sndfile)

Provides: libkdegames-kf5 = %{version}-%{release}
Provides: libkdegames-kf5%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package devel
Summary:  Development files for %{name} 
Provides: libkdegames-kf5-devel = %{version}-%{release}
Provides: libkdegames-kf5-devel%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig(Qt5Network) pkgconfig(Qt5Widgets) pkgconfig(Qt5Qml) pkgconfig(Qt5QuickWidgets) pkgconfig(Qt5Xml)
Requires: kf5-kconfig-devel
Requires: kf5-kconfigwidgets-devel
Requires: kf5-kcompletion-devel
Requires: kf5-ki18n-devel
Requires: kf5-kdelibs4support-devel
Requires: kf5-kwidgetsaddons-devel
%description devel
%{summary}.


%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_kf5_libdir}/libKF5KDEGames.so.*
%{_kf5_libdir}/libKF5KDEGamesPrivate.so.*
%{_qt5_archdatadir}/qml/org/kde/games/
%{_kf5_datadir}/kconf_update/kgthemeprovider-migration.upd
# consider common/noarch subpkg
%{_kf5_datadir}/carddecks/

%files devel
%{_kf5_libdir}/libKF5KDEGames.so
%{_kf5_libdir}/libKF5KDEGamesPrivate.so
%{_kf5_includedir}/KF5KDEGames/
%{_kf5_libdir}/cmake/KF5KDEGames/


%changelog
* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-3
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

