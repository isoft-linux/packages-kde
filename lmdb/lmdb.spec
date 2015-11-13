# The files themselves are in several subdirectories and need to be prefixed wit this.
%global archive_path libraries/lib%{name}

Name:           lmdb
Version:        0.9.16
Release:        2%{?dist}
Summary:        Memory-mapped key-value database

License:        OpenLDAP
URL:            http://symas.com/mdb/
Source:         https://github.com/LMDB/lmdb/archive/LMDB_%{version}.tar.gz
# Patch description in the corresponding file
Patch0: lmdb-make.patch
Patch1: lmdb-s390-check.patch

#from ZhaiXiang, rebased and refined.
Patch2: 0001-fix-env-is-null.patch

BuildRequires: make
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

%description    doc
The %{name}-doc package contains automatically generated documentation for %{name}.


%prep
%setup -q -n %{name}-LMDB_%{version}
%patch0 -p1 -b .make
%patch1 -p1 -b .s390-check
%patch2 -p1

%build
pushd %{archive_path}
make XCFLAGS="%{optflags}" %{?_smp_mflags}
# Build doxygen documentation
doxygen
# remove unpackaged files
rm -f Doxyfile
rm -rf man # Doxygen generated manpages
popd

%install
pushd %{archive_path}
# make install expects existing directory tree
mkdir -m 0755 -p %{buildroot}%{_prefix}{/bin,/include}
mkdir -m 0755 -p %{buildroot}{%{_libdir},%{_mandir}/man1}
make DESTDIR=%{buildroot} prefix=%{_prefix} libprefix=%{_libdir} manprefix=%{_mandir} install
popd


%check
pushd %{archive_path}
rm -rf testdb
LD_LIBRARY_PATH=$PWD make test
popd

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%doc %{archive_path}/COPYRIGHT
%doc %{archive_path}/CHANGES
%license %{archive_path}/LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc %{archive_path}/html
%doc %{archive_path}/COPYRIGHT
%doc %{archive_path}/CHANGES
%license %{archive_path}/LICENSE


%changelog
* Thu Nov 12 2015 Cjacker <cjacker@foxmail.com> - 0.9.16-2
- Update

* Tue Nov 10 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix abort segfault issue.

* Wed Nov 04 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix env is NULL issue.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.9.14-3
- Rebuild for new 4.0 release

