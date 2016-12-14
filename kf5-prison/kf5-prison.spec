Name:           kf5-prison
Version:        5.29.0
Release:        1
Summary:        A Qt-based barcode abstraction library

License:        MIT
URL:            https://projects.kde.org/projects/kdesupport/prison

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/prison-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  libdmtx-devel
BuildRequires:  qrencode-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}


%prep
%setup -q -n prison-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} -DQT5_BUILD=ON ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast -C %{_target_platform} DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_kf5_libdir}/libKF5Prison.so.*

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/prison_version.h
%{_kf5_includedir}/prison
%{_kf5_libdir}/libKF5Prison.so
%{_kf5_libdir}/cmake/KF5Prison/
%{_libdir}/qt5/mkspecs/modules/qt_Prison.pri

%changelog
* Wed Dec 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-1
- 5.29.0-1

* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-1.git
- 5.28.0-1.git

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 2.8.8-2.git
- Rebuild for new 4.0 release

* Thu Aug 13 2015 Cjacker <cjacker@foxmail.com>
- initial build.
