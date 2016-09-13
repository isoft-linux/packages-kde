%global framework kactivities-stats

Name:           kf5-%{framework}
Summary:        A KDE Frameworks 5 Tier 3 library for accessing the usage data collected by the activities system
Version:        5.26.0
Release:        1%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
License:        LGPLv2 or LGPLv3 
URL:            https://quickgit.kde.org/?p=kactivities-stats.git

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-kactivities-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig

Requires: kf5-filesystem

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  -DBUILD_TESTING=ON
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


# Currently includes no tests
%check
make test -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc MAINTAINER README.developers TODO
%license COPYING*
%{_kf5_libdir}/libKF5ActivitiesStats.so.*

%files devel
%{_kf5_libdir}/libKF5ActivitiesStats.so
%{_kf5_includedir}/KActivitiesStats/
%{_kf5_includedir}/kactivitiesstats_version.h
%{_kf5_libdir}/cmake/KF5ActivitiesStats/
%{_kf5_libdir}/pkgconfig/libKActivitiesStats.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_KActivitiesStats.pri


%changelog
* Tue Sep 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.26.0-1
- 5.26.0

* Wed Aug 17 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Tue Apr 19 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

