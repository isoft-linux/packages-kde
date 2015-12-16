Name: kjieba
Version: 0.3.0
Release: 2%{?dist}
Summary: DBus interface of libcppjieba for KDE5

License: GPLv2 or GPLv3
URL: http://github.com/xiangzhai/kjieba
Source0: %{name}-%{version}.tar.bz2

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: qt5-qtbase-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kdbusaddons-devel

Requires: kf5-filesystem


%description
DBus interface of libcppjieba for KDE5.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for 
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%{_datadir}/dbus-1/services/org.isoftlinux.kjieba.service
# own this dir.
%dir %{_datadir}/libcppjieba/
%{_datadir}/libcppjieba/*
%{_kf5_bindir}/kjieba
%{_kf5_bindir}/kjieba-query
%{_datadir}/dbus-1/interfaces/org.isoftlinux.kjieba.App.xml
%{_sysconfdir}/xdg/autostart/kjieba.desktop
%{_libdir}/libKJieba.so.*

%files devel
%{_libdir}/cmake/KJiebaAppDBusInterface
%{_includedir}/KJieba
%{_libdir}/cmake/KJieba
%{_libdir}/libKJieba.so

%changelog
* Wed Dec 16 2015 Cjacker <cjacker@foxmail.com> - 0.3.0-2
- Own libcppjieba dir and add missing pinyin dict

* Wed Dec 16 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add Chinese2Pinyin support.

* Tue Nov 24 2015 Cjacker <cjacker@foxmail.com> - 0.2.0-2
- Add missing kjieba-query to filelist

* Mon Nov 23 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Autostart kjieba dbus service when qdbus call.
- Add query sync API with CutMethod parameter and install example.
- Release kjieba 0.2.0
- Release kjieba 0.1.0
