Name:           qjson
Version:        0.8.1
Release:        10
Summary:        A qt-based library that maps JSON data to QVariant objects

License:        GPLv2+
URL:            http://sourceforge.net/projects/qjson/
Source0:        http://sourceforge.net/projects/%{name}/files/qjson/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  cmake >= 2.6
BuildRequires:  doxygen
BuildRequires:  pkgconfig(QtCore)

%description
JSON is a lightweight data-interchange format. It can represents integer, real
number, string, an ordered sequence of value, and a collection of
name/value pairs.QJson is a qt-based library that maps JSON data to
QVariant objects.

%package devel
Summary:  Development files for qjson
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains the libraries and header files required for
developing applications that use %{name}.

%prep
%setup -qn %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
  -DQJSON_BUILD_TESTS:BOOL=ON \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}

# build docs
pushd doc
doxygen
popd

%install
make install DESTDIR=%{buildroot} -C %{_target_platform}

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion QJson)" = "%{version}"
export CTEST_OUTPUT_ON_FAILURE=1
make test -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING.lib
%doc README.md README.license
%{_libdir}/libqjson.so.%{version}
%{_libdir}/libqjson.so.0*

%files devel
%doc doc/html
%{_includedir}/qjson/
%{_libdir}/libqjson.so
%{_libdir}/pkgconfig/QJson.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/qjson/

%changelog
