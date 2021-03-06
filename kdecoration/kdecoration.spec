%global kf5_version 5.29.0

Name:           kdecoration
Summary:        A plugin-based library to create window decorations
Version:        5.8.5
Release:        1

License:        LGPLv2
URL:            https://projects.kde.org/projects/kde/workspace/kdecoration

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-rpm-macros >= %{kf5_version}
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%setup -q -n %{name}-%{version}


%build
# Cleanup includes mess, install everything into %%{_kf5_includedir}/KDecoration2
sed -i "s/set(KDECORATION2_INCLUDEDIR \"\${CMAKE_INSTALL_INCLUDEDIR}\/KDecoration2\")/set(KDECORATION2_INCLUDEDIR \"\${KF5_INCLUDE_INSTALL_DIR}\/KDecoration2\")/" CMakeLists.txt

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
%{_kf5_libdir}/libkdecorations2.so.*
%{_kf5_libdir}/libkdecorations2private.so.*

%files devel
%{_kf5_libdir}/libkdecorations2.so
%{_kf5_libdir}/libkdecorations2private.so
%{_kf5_libdir}/cmake/KDecoration2
%{_kf5_includedir}/KDecoration2
%{_kf5_includedir}/kdecoration2_version.h

%changelog
* Thu Dec 29 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.5-1
- 5.8.5-1

* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.4-1
- 5.8.4-1

* Wed Nov 02 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Tue Nov 01 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.2-1
- 5.8.2

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

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

