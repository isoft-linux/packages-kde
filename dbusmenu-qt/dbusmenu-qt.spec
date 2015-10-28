%define cmake_pkg cmake

Summary: A Qt implementation of the DBusMenu protocol 
Name:    dbusmenu-qt
Version: 0.9.2
Release: 11

License: LGPLv2+
URL: https://launchpad.net/libdbusmenu-qt/
Source0  https://launchpad.net/libdbusmenu-qt/trunk/%{version}/+download/libdbusmenu-qt-%{version}.tar.bz2

## upstream patches

BuildRequires: %{cmake_pkg}
BuildRequires: doxygen
BuildRequires: pkgconfig
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtGui) 
# test-suite
BuildRequires: xorg-x11-server-Xvfb dbus-x11

Provides: libdbusmenu-qt = %{version}-%{release}

%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package devel
Summary: Development files for %{name}
Provides: libdbusmenu-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n libdbusmenu-qt-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# unpackaged files
rm -rfv %{buildroot}%{_docdir}/dbusmenu-qt


%check
# verify pkg-config version
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion dbusmenu-qt)" = "%{version}"
# test suite
#xvfb-run -a dbus-launch --exit-with-session make -C %{_target_platform} check ARGS="--output-on-failure" ||:


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING README
%{_libdir}/libdbusmenu-qt.so.2*

%files devel
%doc %{_target_platform}/html/
%{_includedir}/dbusmenu-qt/
%{_libdir}/libdbusmenu-qt.so
%{_libdir}/pkgconfig/dbusmenu-qt.pc


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.9.2-11
- Rebuild for new 4.0 release

