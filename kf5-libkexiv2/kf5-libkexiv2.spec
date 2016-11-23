%define realname libkexiv2
%global kf5_version 5.28.0

Name:    kf5-libkexiv2
Summary: An Exiv2 wrapper library
Version: 16.08.3
Release: 1%{?dist}

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/libs/libkexiv2
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{realname}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules >= %{kf5_version}
BuildRequires: gettext
BuildRequires: kf5-rpm-macros >= %{kf5_version}
BuildRequires: qt5-qtbase-devel qt5-qttools-devel
BuildRequires: pkgconfig(exiv2)

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata as EXIF/IPTC and XMP. 

%package devel
Summary:  Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%autosetup -n %{realname}-%{version} 

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_kf5_libdir}/libKF5KExiv2.so.*


%files devel
%{_kf5_libdir}/libKF5KExiv2.so
%{_kf5_includedir}/libkexiv2_version.h
%{_kf5_includedir}/KExiv2
%{_libdir}/cmake/KF5KExiv2


%changelog
* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 16.08.3-1
- 16.08.3-1

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.0.0-4.git
- Rebuild for new 4.0 release

