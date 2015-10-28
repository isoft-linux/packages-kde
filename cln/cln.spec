Name:           cln
Version:        1.3.4
Release:        4
Summary:        Class Library for Numbers
License:        GPLv2+
URL:            http://www.ginac.de/CLN/
Source0:        http://www.ginac.de/CLN/%{name}-%{version}.tar.bz2
BuildRequires:  gmp-devel

%description
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

%package        devel
Summary:        Development files for programs using the CLN library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    devel
A collection of C++ math classes and functions, which are designed for
memory and speed efficiency, and enable type safety and algebraic
syntax.

This package is necessary if you wish to develop software based on
the CLN library.

%ifarch %{arm}
%global XFLAGS %{optflags} -DNO_ASM
%else
%global XFLAGS %{optflags}
%endif

%prep
%setup -q

%build
%configure --disable-static CXXFLAGS="%{XFLAGS}" CFLAGS="%{XFLAGS}"
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/pi.*

%check
make %{_smp_mflags} check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/cln.pc
%{_includedir}/cln/

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1.3.4-4
- Rebuild for new 4.0 release

