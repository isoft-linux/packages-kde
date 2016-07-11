%global framework kio

Name:           kf5-%{framework}
Version:        5.24.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution for filesystem abstraction

License:        GPLv2+ and MIT and BSD
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  zlib-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-knotifications-devel >= %{version}
BuildRequires:  kf5-kwallet-devel >= %{version}
BuildRequires:  qt5-qtscript-devel
BuildRequires:  kf5-kxmlgui-devel >= %{version}
BuildRequires:  kf5-ktextwidgets-devel >= %{version}

BuildRequires:  kf5-karchive-devel >= %{version}
BuildRequires:  kf5-kbookmarks-devel >= %{version}
BuildRequires:  kf5-kcompletion-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kconfigwidgets-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-kitemviews-devel >= %{version}
BuildRequires:  kf5-kjobwidgets-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}
BuildRequires:  kf5-solid-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}

Requires:       kf5-filesystem

Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets = %{version}-%{release}
Requires:       %{name}-widgets-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-ntlm%{?_isa} = %{version}-%{release}

%description
KDE Frameworks 5 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kbookmarks-devel
Requires:       kf5-kcompletion-devel
Requires:       kf5-kconfig-devel
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kitemviews-devel
Requires:       kf5-kjobwidgets-devel
Requires:       kf5-kservice-devel
Requires:       kf5-solid-devel
Requires:       kf5-kxmlgui-devel
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    doc
Documentation for %{name}.

%package        core
Summary:        Core components of the KIO Framework
Requires:       %{name}-core-libs%{?_isa} = %{version}-%{release}
# last version of the main package before the split
Conflicts:      %{name} < 5.3.0-2
%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
Requires:       %{name}-core = %{version}-%{release}
# last version of the main package before the split
Conflicts:      %{name} < 5.3.0-2
%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
# last version of the main package before the split
Conflicts:      %{name} < 5.3.0-2
%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-widgets = %{version}-%{release}
# last version of the main package before the split
Conflicts:      %{name} < 5.3.0-2
%description    widgets-libs
%{summary}.

%package        file-widgets
Summary:        Widgets for file-handling for KIO Framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
# last version of the main package before the split
Conflicts:      %{name} < 5.3.0-2
%description    file-widgets
The KIOFileWidgets library provides the file selection dialog and
its components.

%package        ntlm
Summary:        NTLM support for KIO Framework
# last version of the main package before the split
Conflicts:      %{name} < 5.3.0-2
%description    ntlm
KIONTLM provides support for NTLM authentication mechanism in KIO


%prep
%autosetup -n %{framework}-%{version} -p1


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kio5 --with-qt --all-name


%files
%doc COPYING.LIB README.md

%posttrans core
/usr/bin/update-desktop-database -q &> /dev/null ||:

%postun core
if [ $1 -eq 0 ] ; then
/usr/bin/update-desktop-database -q &> /dev/null ||:
fi

%files core -f kio5.lang
%config %{_kf5_sysconfdir}/xdg/accept-languages.codes
%{_kf5_libexecdir}/kio_http_cache_cleaner
%{_kf5_libexecdir}/kpac_dhcp_helper
%{_kf5_libexecdir}/kioexec
%{_kf5_libexecdir}/kioslave
%{_kf5_libexecdir}/kiod5
%{_kf5_bindir}/ktelnetservice5
%{_kf5_bindir}/kcookiejar5
#%{_kf5_bindir}/kmailservice5
%{_kf5_bindir}/ktrash5
%{_kf5_plugindir}/kio/*.so
%{_kf5_plugindir}/kded/*.so
%{_kf5_qtplugindir}/kcm_kio.so
%{_kf5_qtplugindir}/kcm_trash.so
%dir %{_kf5_plugindir}/kiod/
%{_kf5_plugindir}/kiod/*.so
%{_kf5_datadir}/kservices5/cache.desktop
%{_kf5_datadir}/kservices5/cookies.desktop
%{_kf5_datadir}/kservices5/netpref.desktop
%{_kf5_datadir}/kservices5/proxy.desktop
%{_kf5_datadir}/kservices5/smb.desktop
%{_kf5_datadir}/kservices5/useragent.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/kservices5/http_cache_cleaner.desktop
%{_kf5_datadir}/kservices5/kcmtrash.desktop
%{_kf5_datadir}/kservices5/useragentstrings
%{_kf5_datadir}/knotifications5/proxyscout.*
%{_kf5_datadir}/kf5/kcookiejar/domain_info
%{_kf5_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.kde.kiod5.service

%post core-libs -p /sbin/ldconfig
%postun core-libs -p /sbin/ldconfig

%files core-libs
%{_kf5_libdir}/libKF5KIOCore.so.*

%posttrans widgets
/usr/bin/update-desktop-database -q &> /dev/null ||:

%postun widgets
if [ $1 -eq 0 ] ; then
/usr/bin/update-desktop-database -q &> /dev/null ||:
fi

%files widgets
%config %{_kf5_sysconfdir}/xdg/kshorturifilterrc
%{_kf5_qtplugindir}/kcm_webshortcuts.so
%{_kf5_plugindir}/urifilters/*.so
%{_kf5_datadir}/kservices5/fixhosturifilter.desktop
%{_kf5_datadir}/kservices5/kshorturifilter.desktop
%{_kf5_datadir}/kservices5/kuriikwsfilter.desktop
%{_kf5_datadir}/kservices5/kurisearchfilter.desktop
%{_kf5_datadir}/kservices5/localdomainurifilter.desktop
%{_kf5_datadir}/kservices5/webshortcuts.desktop
%{_kf5_datadir}/kservices5/searchproviders
%{_kf5_datadir}/kservicetypes5/*.desktop

%post widgets-libs -p /sbin/ldconfig
%postun widgets-libs -p /sbin/ldconfig

%files widgets-libs
%{_kf5_libdir}/libKF5KIOWidgets.so.*

%post file-widgets -p /sbin/ldconfig
%postun file-widgets -p /sbin/ldconfig

%files file-widgets
%{_kf5_libdir}/libKF5KIOFileWidgets.so.*

%post ntlm -p /sbin/ldconfig
%postun ntlm -p /sbin/ldconfig

%files ntlm
%{_kf5_libdir}/libKF5KIONTLM.so.*

%files devel
%{_kf5_bindir}/protocoltojson
%{_kf5_includedir}/*
%{_kf5_libdir}/*.so
%{_kf5_libdir}/*.so.*
%{_kf5_libdir}/cmake/KF5KIO/
%{_kf5_archdatadir}/mkspecs/modules/qt_KIOCore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KIOFileWidgets.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KNTLM.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KIOWidgets.pri
%{_datadir}/dbus-1/interfaces/*.xml

%files doc
%{_kf5_mandir}/man8/*
%{_kf5_mandir}/*/man8/*
%exclude %{_kf5_mandir}/man8
%{_kf5_docdir}/HTML/en/kioslave5/


%changelog
* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Fri Apr 08 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-2
- missing *KIOGui.so.*

* Thu Apr 07 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Wed Jan 06 2016 kun.li@i-soft.com.cn - 5.16.0-11
- add zh_CN translation for kio5.po  

* Thu Dec 24 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-10
- Ensure trashrc updated

* Thu Dec 24 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-9
- Drop trash.desktop specitial treatment codes

* Tue Dec 22 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-8
- Fix trash hang

* Mon Dec 21 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-7
- Backport from 5.17

* Mon Dec 21 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix cut and paste info myself issue.

* Mon Nov 30 2015 fujiang <fujiang.zhu@i-soft.com.cn> - 5.16.0-5
- Adjust trash_filepath(bug 12844)

* Thu Nov 26 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-4
- Merge patch from git reviewboard

* Tue Nov 24 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- Merge git reviewboard patch back

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-7
- Add Socks5 support for KTcpSocket

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-6
- Rebuild for new 4.0 release

* Wed Oct 14 2015 Cjacker <cjacker@foxmail.com>
- remove "Link to Device" submenu from "Create New" menu.

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0

* Mon Jul 20 2015 Cjacker <cjacker@foxmail.com>
- drop kfileitem icon patch

* Mon Jul 20 2015 Cjacker <cjacker@foxmail.com>
- add kfileitem icon patch.
