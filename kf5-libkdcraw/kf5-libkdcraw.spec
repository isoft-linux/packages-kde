Name: kf5-libkdcraw
Summary: A C++ interface used to decode RAW picture. KF5 Frameworks branch. 
Version: 15.08.0
Release: 3.kf5.git%{?dist}

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/libs/libkcraw
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

#Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

#git clone git://anongit.kde.org/libkcraw
#git checkout frameworks
Source0: libkdcraw.tar.xz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: qt5-qtbase-devel
BuildRequires: LibRaw-devel

%description
%{summary}

%package devel
Summary:  Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n libkdcraw

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
%{_kf5_libdir}/libKF5KDcraw.so.*

%files devel
%{_kf5_libdir}/libKF5KDcraw.so
%{_kf5_includedir}/libkdcraw_version.h
%{_kf5_includedir}/KDCRAW
%{_libdir}/cmake/KF5KDcraw

%changelog
* Sun Oct 18 2015 Cjacker <cjacker@foxmail.com> 
- git version, initial build for kf5
