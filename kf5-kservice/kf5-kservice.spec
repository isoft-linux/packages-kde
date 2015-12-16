%global framework kservice

Name:           kf5-%{framework}
Version:        5.16.0
Release:        4%{?dist}
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

# Add queryForCJK with kjieba support
Patch0: 0001-query-for-cjk-with-kjieba.patch

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}

BuildRequires:  kjieba-devel
Requires:       kjieba

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
%patch0 -p1

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
* Wed Dec 16 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add queryForCJK with kjieba support.

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
