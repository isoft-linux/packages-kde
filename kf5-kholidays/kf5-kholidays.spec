%global framework kholidays

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 16.04.2
Release: 1%{?dist}
Summary: The KHolidays Library

License: LGPLv2+ and GPLv3+
URL:     https://quickgit.kde.org/?p=%{framework}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kdelibs4support-devel >= 5.15
BuildRequires:  kf5-kitemviews-devel >= 5.15
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel

%description
The KHolidays library provides a C++ API that determines holiday
and other special events for a geographical region.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kdelibs4support-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING.LIB
%{_kf5_libdir}/libKF5Holidays.so.*
%{_kf5_datadir}/kf5/libkholidays/
%{_kf5_qmldir}/org/kde/kholidays/

%files devel
%{_kf5_includedir}/kholidays_version.h
%{_kf5_includedir}/KHolidays/
%{_kf5_libdir}/libKF5Holidays.so
%{_kf5_libdir}/cmake/KF5Holidays/
%{_kf5_archdatadir}/mkspecs/modules/qt_KHolidays.pri


%changelog
* Mon Jun 27 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 16.04.2-1
- 16.04.2
