%define         framework baloo

Name:           kf5-%{framework}
Version:        5.16.0
Release:        7
Summary:        A Tier 3 KDE Frameworks 5 module that provides indexing and search functionality
License:        LGPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/baloo
# backup URL: https://community.kde.org/Baloo

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/frameworks/5.16/%{framework}-%{version}.tar.xz

Source1: 97-kde-baloo-filewatch-inotify.conf

#backport from git
Patch0: baloo-to-git.patch

#simple chinese support for baloo filename index/search.
Patch10: baloo-rude-chinese-support.patch
#extend to support all CJKV
Patch11: baloo-extend-to-support-all-CJKV.patch
#use kjieba to segment Chinese
Patch12: baloo-enable-kjieba.patch 

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kidletime-devel >= %{version}
BuildRequires:  kf5-solid-devel >= %{version}
BuildRequires:  kf5-kfilemetadata-devel >= %{version} 
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}

BuildRequires:  kjieba-devel

BuildRequires:  lmdb-devel 

Requires:       kf5-filesystem
Requires:       kjieba

Obsoletes:      kf5-baloo-tools < 5.5.95-1
Obsoletes:      baloo < 5
Provides:       baloo = %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-file%{?_isa} = %{version}-%{release}
Requires:       kf5-kfilemetadata-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        file
Summary:        File indexing and search for Baloo
Obsoletes:      %{name} < 5.0.1-2
Obsoletes:      baloo-file < 5.0.1-2
Provides:       baloo-file = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
%description    file
%{summary}.

%package        libs
Summary:        Runtime libraries for %{name}
%description    libs
%{summary}.


%prep
%setup -qn %{framework}-%{version}
%patch0 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

install -p -m644 -D %{SOURCE1} %{buildroot}%{_prefix}/lib/sysctl.d/97-kde-baloo-filewatch-inotify.conf

%find_lang baloomonitorplugin --with-qt
%find_lang balooctl --with-qt
%find_lang kio_baloosearch --with-qt
%find_lang baloo_file --with-qt
%find_lang kio_tags --with-qt
%find_lang baloosearch --with-qt
%find_lang kio_timeline --with-qt
%find_lang baloo_file_extractor --with-qt
%find_lang balooshow --with-qt

cat kio_tags.lang kio_baloosearch.lang kio_timeline.lang \
    > %{name}-libs.lang

cat baloo_file.lang baloo_file_extractor.lang \
    > %{name}-file.lang

cat baloomonitorplugin.lang baloosearch.lang balooshow.lang balooctl.lang \
    > %{name}.lang


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%{_kf5_bindir}/baloosearch
%{_kf5_bindir}/balooshow
%{_kf5_bindir}/balooctl
%{_kf5_plugindir}/kio/baloosearch.so
%{_kf5_plugindir}/kio/tags.so
%{_kf5_plugindir}/kio/timeline.so
%{_kf5_plugindir}/kded/baloosearchmodule.so
%{_kf5_qmldir}/org/kde/baloo
%{_kf5_datadir}/kservices5/baloosearch.protocol
%{_kf5_datadir}/kservices5/tags.protocol
%{_kf5_datadir}/kservices5/timeline.protocol
%{_kf5_datadir}/icons/hicolor/*/apps/baloo.png

%files file -f %{name}-file.lang
%{_prefix}/lib/sysctl.d/97-kde-baloo-filewatch-inotify.conf
%{_kf5_bindir}/baloo_file
%{_kf5_bindir}/baloo_file_extractor
%{_kf5_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_kf5_datadir}/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%{_kf5_datadir}/dbus-1/interfaces/org.kde.baloo.fileindexer.xml
%{_kf5_datadir}/dbus-1/interfaces/org.kde.baloo.main.xml
%{_kf5_datadir}/dbus-1/interfaces/org.kde.baloo.scheduler.xml


%files libs -f %{name}-libs.lang
%{_kf5_libdir}/libKF5Baloo.so.*
%{_kf5_libdir}/libKF5BalooEngine.so.*

%files devel
%{_kf5_libdir}/libKF5Baloo.so
%{_kf5_libdir}/cmake/KF5Baloo
%{_kf5_libdir}/pkgconfig/Baloo.pc
%{_kf5_includedir}/Baloo
%{_kf5_includedir}/baloo_version.h


%changelog
* Wed Nov 25 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-7
- Update to git master

* Tue Nov 24 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-6
- Use kjieba to segment Chinese

* Sun Nov 22 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-5
- Merge git patch back

* Fri Nov 20 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-4
- Extend to support all CJKV

* Fri Nov 20 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- simple Chinese support

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-2
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0

