Summary:	Multi-purpose calculator library
Name:		libqalculate
Version:	0.9.7
Release:	15
License:	GPLv2+
URL:		http://qalculate.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:		libqalculate-0.9.7-pkgconfig_private.patch
Patch2:		libqalculate-htmldir.patch
# don't spam errors if euroref-daily.xml doesn't (yet) exist
Patch3:         libqalculate-0.9.7-euroref-daily.patch
BuildRequires:	glib2-devel, cln-devel
BuildRequires:	libxml2-devel
BuildRequires:	readline-devel, ncurses-devel
BuildRequires:	perl(XML::Parser), gettext

%description
This library underpins the Qalculate! multi-purpose desktop calculator for
GNU/Linux

%package	devel
Summary:	Development tools for the Qalculate calculator library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2-devel, libxml2-devel, cln-devel

%description	devel
The libqalculate-devel package contains the header files needed for development
with libqalculate.

%package -n	qalculate
Summary:	Multi-purpose calculator, text mode interface
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description -n	qalculate
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides the text-mode interface for Qalculate! The GTK and QT
frontends are provided by qalculate-gtk and qalculate-kde packages resp.

%prep
%setup -q
%patch1 -p1 -b .pkgconfig_private
%patch2 -p0 -b .htmldir-unversioned
%patch3 -p1 -b .euroref-daily

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{name}
rm -f %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{_libdir}/libqalculate.so.*
%{_datadir}/qalculate/

%files devel
%defattr(-,root,root,-)
%{_libdir}/libqalculate.so
%{_libdir}/pkgconfig/libqalculate.pc
%{_includedir}/libqalculate/
%{_docdir}/libqalculate

%files -n qalculate
%defattr(-,root,root,-)
%{_bindir}/qalc

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.9.7-15
- Rebuild for new 4.0 release

