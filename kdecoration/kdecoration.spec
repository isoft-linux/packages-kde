Name:           kdecoration
Summary:        A plugin-based library to create window decorations
Version:        5.4.2
Release:        2

License:        LGPLv2
URL:            https://projects.kde.org/projects/kde/workspace/kdecoration

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
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

