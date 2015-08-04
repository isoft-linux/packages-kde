Name:           libaccounts-qt5
Version:        1.13
Release:        5%{?dist}
Summary:        Accounts framework Qt 5 bindings
Group:          System Environment/Libraries
License:        LGPLv2
URL:            http://code.google.com/p/accounts-sso/

# Source available from https://drive.google.com/#folders/0B8fX9XOwH_g4alFsYV8tZTI4VjQ
# as per https://groups.google.com/forum/#!topic/accounts-sso-announce/cQd7M9stcCs
Source0:        accounts-qt-%{version}.tar.bz2

Patch1:         libaccounts-qt-64bitarchs.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  libaccounts-glib-devel
BuildRequires:  doxygen

%description
Framework to provide accounts for Qt 5.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}
%description    devel
Headers, development libraries and documentation for %{name}.

%package        doc
Summary:        User and developer documentation for %{name}
%description    doc
%{summary}.

%prep
%setup -q -n accounts-qt-%{version}

%patch1 -p1 -b .64bitarchs

%build
%{_qt5_qmake} QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    accounts-qt.pro

make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

rm -f %{buildroot}/%{_datadir}/doc/accounts-qt/html/installdox

#remove tests for now
rm -rf %{buildroot}%{_datadir}/libaccounts-qt-tests
rm -f %{buildroot}%{_bindir}/accountstest

# Make sure we don't conflict with Qt 5 version
mv %{buildroot}%{_docdir}/accounts-qt{,5}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libaccounts-qt5.so.*

%files devel
%{_libdir}/libaccounts-qt5.so
%{_includedir}/accounts-qt5/
%{_libdir}/pkgconfig/accounts-qt5.pc
%{_libdir}/cmake/AccountsQt5

%files doc
%{_docdir}/accounts-qt5

%changelog
