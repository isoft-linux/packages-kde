Name:           libksysguard
Version:        5.7.1
Release:        1
Summary:        Library for managing processes running on the system

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/libksysguard

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libXres-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  zlib-devel

Requires:       kf5-filesystem

Obsoletes:      kf5-ksysguard < 5.1.95
Provides:       kf5-ksysguard = %{version}-%{release}

Requires:       libksysguard-common = %{version}-%{release}

%description
KSysGuard library provides API to read and manage processes
running on the system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      kf5-ksysguard-devel < 5.1.95
Provides:       kf5-ksysguard-devel = %{version}-%{release}
Conflicts:      kde-workspace-devel < 1:4.11.16-11

%package        common
Summary:        Runtime data files shared by libksysguard and ksysguard-libs
Conflicts:      libksysguard < 5.2.1-2
Conflicts:      ksysguard < 5.2
%description    common
%{summary}.

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. -DINCLUDE_INSTALL_DIR=%{_kf5_includedir}
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang ksysguard_qt5 --with-qt --with-kde --all-name

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f ksysguard_qt5.lang
%doc COPYING.LIB
%{_kf5_libdir}/liblsofui.so.*
%{_kf5_libdir}/libprocessui.so.*
%{_kf5_libdir}/libprocesscore.so.*
%{_kf5_libdir}/libksignalplotter.so.*
%{_kf5_libdir}/libksgrd.so.*
%{_kf5_datadir}/ksysguard

%files common
%{_kf5_libexecdir}/kauth/ksysguardprocesslist_helper
%{_sysconfdir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

%files devel
%{_kf5_includedir}/ksysguard
%{_kf5_libdir}/liblsofui.so
%{_kf5_libdir}/libprocessui.so
%{_kf5_libdir}/libprocesscore.so
%{_kf5_libdir}/libksignalplotter.so
%{_kf5_libdir}/libksgrd.so
%{_kf5_libdir}/cmake/KF5SysGuard

%changelog
* Wed Jul 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.1-1
- 5.7.1

* Wed Jul 06 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.0-1
- 5.7.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-1
- 5.6.95

* Thu May 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.4-1
- 5.6.4

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
- 5.6.2

* Mon Apr 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.1-1
- Release 5.6.1

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-2
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95
