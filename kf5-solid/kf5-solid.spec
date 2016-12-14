%global framework solid

Name:           kf5-%{framework}
Version:        5.29.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 integration module that provides hardware information

License:        LGPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

# Workaround https://bugzilla.redhat.com/show_bug.cgi?id=1364943
# Technically only affects rawhide/f26, but is harmless elsewhere too
Patch0:         solid-5.25-fix-build-with-flex-2.6.0.patch

BuildRequires:  systemd-devel

BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel

%if ! 0%{?bootstrap}
# Predicate parser deps
BuildRequires:  bison
BuildRequires:  flex
# really runtime-only dep, but doesn't hurt to check availability at buildtime
BuildRequires:  media-player-info
Requires:       media-player-info
%endif

Requires:       kf5-filesystem

Provides:       %{name}-runtime = %{version}-%{release}
Provides:       %{name}-runtime%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-runtime < 4.99.0.1

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Solid provides the following features for application developers:
 - Hardware Discovery
 - Power Management
 - Network Management

%package        libs
Summary:        Runtime libraries for Solid Framework
# When the split occured
Conflicts:      %{name} < 5.4.0-1
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}
%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}
%find_lang solid5_qt --with-qt --all-name


%files
%doc COPYING.LIB README.md TODO
%{_kf5_bindir}/solid-hardware5

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs -f solid5_qt.lang
%{_kf5_qmldir}/org/kde/solid
%{_kf5_libdir}/libKF5Solid.so.*

%files devel
%{_kf5_includedir}/solid_version.h
%{_kf5_includedir}/Solid
%{_kf5_libdir}/libKF5Solid.so
%{_kf5_libdir}/cmake/KF5Solid
%{_kf5_archdatadir}/mkspecs/modules/qt_Solid.pri


%changelog
* Wed Dec 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-1
- 5.29.0-1

* Tue Nov 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-2
- 5.28.0-2

* Wed Nov 16 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-1
- 5.28.0

* Mon Oct 31 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.27.0-1
- 5.27.0

* Tue Sep 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.26.0-1
- 5.26.0

* Tue Aug 16 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Thu Apr 07 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
