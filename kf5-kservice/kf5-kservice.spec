%global framework kservice

Name:           kf5-%{framework}
Version:        5.29.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution for advanced plugin and service introspection

License:        GPLv2+ and LGPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

# Workaround flex bug (https://bugzilla.redhat.com/show_bug.cgi?id=1364943)
Patch102:  kservice-5.25-fix-build-with-flex-2.6.0.patch

Patch110:  lex-flex-2.6.2.patch

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  flex
BuildRequires:  bison

BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 solution for advanced plugin and service
introspection.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel
Requires:       kf5-kcoreaddons-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}
%patch102 -p1
%patch110 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kservice5_qt --with-man --with-qt --all-name

mv %{buildroot}%{_kf5_sysconfdir}/xdg/menus/applications.menu %{buildroot}/%{_kf5_sysconfdir}/xdg/menus/kf5-applications.menu

mkdir -p %{buildroot}%{_kf5_datadir}/kservices5
mkdir -p %{buildroot}%{_kf5_datadir}/kservicetypes5


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kservice5_qt.lang
%doc COPYING COPYING.LIB README.md
# this is not a config file, despite rpmlint complaining otherwise -- rex
%{_kf5_sysconfdir}/xdg/menus/kf5-applications.menu
%{_kf5_bindir}/kbuildsycoca5
%{_kf5_libdir}/libKF5Service.so.*
%{_kf5_datadir}/kservicetypes5/
%{_kf5_datadir}/kservices5/
%{_kf5_mandir}/man8/*.8*

%files devel
%{_kf5_includedir}/kservice_version.h
%{_kf5_includedir}/KService/
%{_kf5_libdir}/libKF5Service.so
%{_kf5_libdir}/cmake/KF5Service/
%{_kf5_archdatadir}/mkspecs/modules/qt_KService.pri


%changelog
* Tue Dec 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-2
- flex-2.6.2 issue https://github.com/westes/flex/issues/134
- 5.29.0-2

* Tue Nov 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-2
- 5.28.0-2

* Tue Nov 15 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-1
- 5.28.0

* Mon Oct 31 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.27.0-1
- 5.27.0

* Tue Sep 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.26.0-1
- 5.26.0

* Tue Aug 16 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0.

* Mon Jun 27 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-3
- Rebase for 5.23.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Thu Apr 07 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Fri Dec 18 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-8
- Extend kautostart.cpp to support kde4 autostart desktop condition

* Wed Dec 16 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add queryForCJK with kjieba support.
- Remove kjieba support.
- Public KServiceOffer.

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-6
- Add some patches from reviewboard

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-5
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
