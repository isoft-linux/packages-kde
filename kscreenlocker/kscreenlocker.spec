Name:    kscreenlocker
Version: 5.7.4
Release: 1%{?dist}
Summary: Library and components for secure lock screen architecture

License: GPLv2+
URL:     https://quickgit.kde.org/?p=%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

# Accounts service face icon
Patch1: 0001-kscreenlocker-accounts-service.patch

# help upgrades, split from plasma-workspace since 5.5
Conflicts: plasma-workspace < 5.5

## upstream patches

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  libkscreen-devel >= %{version}
BuildRequires:  kf5-kwayland-devel

BuildRequires:  libX11-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel
BuildRequires:  pkgconfig(xi)

BuildRequires:  libXcursor-devel
BuildRequires:  pam-devel
BuildRequires:  qt5-qtaccountsservice-devel >= 0.6.0

Requires:       kf5-filesystem
Requires:       qt5-qtaccountsservice-devel >= 0.6.0

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf5-kscreen-devel = %{version}-%{release}
Provides:       kf5-kscreen-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf5-kscreen-devel <= 1:5.2.0
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%{_kf5_libdir}/libKScreenLocker.so.*
%{_kf5_datadir}/knotifications5/*.notifyrc
%{_kf5_datadir}/kconf_update/*
%{_libexecdir}/kcheckpass
%{_libexecdir}/kscreenlocker_greet
%dir %{_kf5_datadir}/ksmserver/
%{_kf5_datadir}/ksmserver/screenlocker/
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_qtplugindir}/screenlocker_kcm.so

%files devel
%{_kf5_libdir}/libKScreenLocker.so
%{_kf5_libdir}/cmake/ScreenSaverDBusInterface/
%{_kf5_libdir}/cmake/KScreenLocker/
%{_includedir}/KScreenLocker/
%{_datadir}/dbus-1/interfaces/*.xml


%changelog
* Wed Aug 24 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Wed Aug 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.3-1
- 5.7.3

* Wed Jul 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.2-1
- 5.7.2

* Wed Jul 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.1-1
- 5.7.1

* Wed Jul 06 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.0-1
- 5.7.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-1
- 5.6.95

* Thu May 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.4-1
- 5.6.4

* Wed Apr 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.3-1
- 5.6.3

* Thu Apr 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-2
- Accounts service face icon.

* Tue Apr 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
- Add libkscreen build require.
- 5.6.2

* Mon Apr 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.1-1
- 5.6.1
