Name:           lmdb
Version:        0.9.14
Release:        2%{?dist}
Summary:        Memory-mapped key-value database

License:        OpenLDAP
URL:            http://symas.com/mdb/
# Source built from git. To get the tarball, execute following commands:
# $ export VERSION=%%{version}
# $ git clone git://gitorious.org/mdb/mdb.git lmdb && pushd lmdb
# $ git checkout tags/LMDB_$VERSION && popd
# $ tar cvzf lmdb-$VERSION.tar.gz -C lmdb/libraries/ liblmdb
Source:        %{name}-%{version}.tar.gz
# Patch description in the corresponding file
Patch0: lmdb-make.patch
Patch1: lmdb-s390-check.patch

BuildRequires: doxygen

%description
LMDB is an ultra-fast, ultra-compact key-value embedded data
store developed by for the OpenLDAP Project. By using memory-mapped files,
it provides the read performance of a pure in-memory database while still 
offering the persistence of standard disk-based databases, and is only limited
to the size of the virtual address space.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs
The %{name}-libs package contains shared libraries necessary for running
applications that use %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
Group:          Documentation

%description    doc
The %{name}-doc package contains automatically generated documentation for %{name}.


%prep
%setup -q -n lib%{name}
%patch0 -p1 -b .make
%patch1 -p1 -b .s390-check


%build
make XCFLAGS="%{optflags}" %{?_smp_mflags}
# Build doxygen documentation
doxygen
# remove unpackaged files
rm -f Doxyfile
rm -rf man # Doxygen generated manpages

%install
# make install expects existing directory tree
mkdir -m 0755 -p %{buildroot}%{_prefix}{/bin,/include}
mkdir -m 0755 -p %{buildroot}{%{_libdir},%{_mandir}/man1}
make DESTDIR=%{buildroot} prefix=%{_prefix} libprefix=%{_libdir} manprefix=%{_mandir} install


%check
rm -rf testdb
LD_LIBRARY_PATH=$PWD make test

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%doc COPYRIGHT CHANGES LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc html COPYRIGHT CHANGES LICENSE


%changelog
