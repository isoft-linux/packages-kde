Name:           libkscreen
Version:        5.8.3
Release:        1
Summary:        KDE display configuration library

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/libkscreen


%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXrandr-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kwayland-devel

Requires:       kf5-filesystem

Provides:       kf5-kscreen%{?_isa} = %{version}-%{release}
Provides:       kf5-kscreen = %{version}-%{release}
Obsoletes:      kf5-kscreen <= 1:5.2.0


%description
LibKScreen is a library that provides access to current configuration
of connected displays and ways to change the configuration.

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
%setup -q -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_kf5_bindir}/kscreen-doctor
%{_kf5_libexecdir}/kscreen_backend_launcher
%{_kf5_libdir}/libKF5Screen.so.*
%{_kf5_plugindir}/kscreen/
%{_datadir}/dbus-1/services/org.kde.kscreen.service

%files devel
%{_kf5_includedir}/KScreen/
%{_kf5_includedir}/kscreen_version.h
%{_kf5_libdir}/libKF5Screen.so
%{_kf5_libdir}/cmake/KF5Screen/
%{_libdir}/pkgconfig/kscreen2.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KScreen.pri


%changelog
* Wed Nov 02 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Tue Nov 01 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.2-1
- 5.8.2

* Wed Aug 24 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Wed Aug 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.3-2
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

* Tue Apr 19 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-3
- Verify rotation when updating screen size in XRandR backend

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-2
- Add missing file

* Tue Apr 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
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

