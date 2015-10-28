Name: kdepimlibs
Summary: KDE PIM Libraries
Version: 4.14.10
Release: 3

License: LGPLv2+
URL: http://www.kde.org/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/kdepimlibs-%{version}.tar.xz

Patch0: kdepimlibs-only-keep-qgpgme-and-kxmlrpclient.patch
Patch1: kdepimlibs-fix-cmake-err.patch

BuildRequires: boost-devel
BuildRequires: gpgme-devel
BuildRequires: kdelibs-devel >= 4.14
BuildRequires: libical-devel >= 0.33
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(xpm) pkgconfig(xtst)

%description
Personal Information Management (PIM) libraries for KDE 4.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:  kdepimlibs4-devel = %{version}-%{release}
Requires: boost-devel
Requires: gpgme-devel
Requires: kdelibs-devel
%description devel
Header files for developing applications using %{name}.




%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. 
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_kde4_libdir}/libkmime.so.*
%{_kde4_libdir}/libgpgme++-pth*.so.2*
%{_kde4_libdir}/libgpgme++.so.2*
%{_kde4_libdir}/libqgpgme.so.1*
%{_kde4_libdir}/libkxmlrpcclient.so.4*

%files devel
%{_kde4_appsdir}/cmake/modules/*
%{_kde4_includedir}/*
%{_kde4_libdir}/lib*.so
%{_kde4_libdir}/cmake/KdepimLibs*
%{_kde4_libdir}/gpgmepp/




%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 4.14.10-3
- Rebuild for new 4.0 release

