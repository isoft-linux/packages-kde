%global         framework kwayland

%global         wayland_min_version 1.3

Name:           kf5-%{framework}
Version:        5.6.4
Release:        1
Summary:        KDE Frameworks 5 library that wraps Client and Server Wayland libraries

License:        GPLv2+
URL:            http://www.kde.org

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/kwayland-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  libwayland-client-devel >= %{wayland_min_version}
BuildRequires:  libwayland-cursor-devel >= %{wayland_min_version}
BuildRequires:  libwayland-server-devel >= %{wayland_min_version}
BuildRequires:  mesa-libwayland-egl-devel
BuildRequires:  wayland-devel >= %{wayland_min_version}

BuildRequires:  libwayland-client-devel >= %{wayland_min_version}

Requires:       kf5-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

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
%doc COPYING.LIB
%{_kf5_libdir}/libKF5WaylandClient.so.*
%{_kf5_libdir}/libKF5WaylandServer.so.*
%{_sysconfdir}/xdg/org_kde_kwayland.categories
%{_libdir}/qt5/mkspecs/modules/qt_KWaylandClient.pri
%{_libdir}/qt5/mkspecs/modules/qt_KWaylandServer.pri

%files devel
%{_kf5_includedir}/KWayland
%{_kf5_includedir}/kwayland_version.h
%{_kf5_libdir}/cmake/KF5Wayland
%{_kf5_libdir}/libKF5WaylandClient.so
%{_kf5_libdir}/libKF5WaylandServer.so


%changelog
* Thu May 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.4-1
- 5.6.4

* Wed Apr 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.3-1
- 5.6.3

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
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

