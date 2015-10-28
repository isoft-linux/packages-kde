Name:           perl-Any-URI-Escape
Version:        0.01
Release:        9
Summary:        Load URI::Escape::XS preferentially over URI::Escape
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Any-URI-Escape/
Source0:        http://www.cpan.org/authors/id/P/PH/PHRED/Any-URI-Escape-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Escape)
Requires:       perl(URI::Escape)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
URI::Escape is great, but URI::Escape::XS is faster. This module loads
URI::Escape::XS and imports the two most common methods if XS is installed.

%prep
%setup -q -n Any-URI-Escape-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Any*
%{_mandir}/man3/*

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.01-9
- Rebuild for new 4.0 release

