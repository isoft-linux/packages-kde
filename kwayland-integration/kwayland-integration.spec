Name:           kwayland-integration 
Version:        5.8.3
Release:        1
Summary:        KDE wayland integration

License:        GPLv2+
URL:            http://www.kde.org

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros

BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem

%description
%{summary}.

%prep
%setup -q

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%files
%doc COPYING.LIB
%{_kf5_plugindir}/org.kde.kidletime.platforms/KF5IdleTimeKWaylandPlugin.so
%{_kf5_plugindir}/org.kde.kwindowsystem.platforms/KF5WindowSystemKWaylandPlugin.so

%changelog
* Thu Nov 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

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

