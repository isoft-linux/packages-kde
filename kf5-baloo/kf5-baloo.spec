%define         framework baloo

Name:           kf5-%{framework}
Version:        5.29.0
Release:        1
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

#simple chinese support for baloo filename index/search.
Patch10: baloo-rude-chinese-support.patch
#extend to support all CJKV
Patch11: baloo-extend-to-support-all-CJKV.patch
#use kjieba to segment Chinese
Patch12: baloo-enable-kjieba.patch 

#enable pinyin and pinyin initial letter support for Chinese.
Patch13: baloo-add-pinyin-support.patch

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}
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
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1


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
* Wed Dec 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-1
- 5.29.0-1

* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-2
- 5.28.0-2

* Thu Nov 17 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-1
- 5.28.0

* Tue Nov 01 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.27.0-1
- 5.27.0

* Wed Aug 17 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Tue Jun 28 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-2
- rebase CJK, Chinese word segmentation and pinyin support for 5.23.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Mon Apr 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Tue Dec 22 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-11
- Backport from 5.17.0

* Mon Dec 21 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-10
- backport from 5.17

* Mon Dec 21 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-9
- Disable max inofity watch settings

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-8
- Add pinyin support

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

