
Summary: Library for accessing MusicBrainz servers
Name: libmusicbrainz
Version: 2.1.5
Release: 20%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
URL: http://www.musicbrainz.org/
Source0: ftp://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1: libmusicbrainz-2.1.5-gcc43.patch

BuildRequires: expat-devel

# prepare for libmusicbrainz3
Provides: libmusicbrainz2 = %{version}-%{release}

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary: Headers for developing programs that will use %{name} 
Group: Development/Libraries
Provides: libmusicbrainz2-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}. 


%prep
%setup -q

%patch1 -p1 -b .gcc43

%{__cp} -a examples/README examples/README.examples

%build
%configure --disable-static
make %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc docs/mb_howto.txt examples/README.examples examples/*.c examples/*.cpp
%{_includedir}/musicbrainz/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc


%changelog
