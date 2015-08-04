Summary:    Attica is a Qt library that implements the Open Collaboration Services API.
Name:	    attica	
Version:	0.4.2
Release:    2	
License:	GPL
Group:		Desktop/KDE4
Source0:	%{name}-%{version}.tar.bz2
Requires:   qt4
BuildRequires: qt4-devel

%description
Attica is a Qt library that implements the Open Collaboration Services API.

%package devel
Summary: Development files for attica 
Requires: %{name}
Requires: qt4-devel
Group: Development/Libraries

%description devel
Header files for developing applications using attica 

%prep
%setup -q
%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=Release -DQT4_BUILD:BOOL=ON ..
popd

make %{_smp_mflags} -C build

%install
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C build

rpmclean

%check
make test -C build

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%dir %{_includedir}/attica
%{_includedir}/attica/*
