%define apidocs 0 
Name:    grantlee
Summary: Qt string template engine based on the Django template system
Version: 0.5.1
Release: 1 

License: LGPLv2+
Group:   System Environment/Libraries
URL:     http://www.gitorious.org/grantlee/pages/Home
Source0: http://downloads.grantlee.org/grantlee-%{version}%{?pre:-%{pre}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: cmake
BuildRequires: pkgconfig(QtGui) pkgconfig(QtScript) 
%if 0%{?apidocs}
BuildRequires: doxygen
BuildRequires: graphviz
%endif

%description
Grantlee is a plug-in based String Template system written 
using the Qt framework. The goals of the project are to make it easier for
application developers to separate the structure of documents from the 
data they contain, opening the door for theming.

The syntax is intended to follow the syntax of the Django template system, 
and the design of Django is reused in Grantlee. 
Django is covered by a BSD style license.

Part of the design of both is that application developers can extend 
the syntax by implementing their own tags and filters. For details of 
how to do that, see the API documentation.

For template authors, different applications using Grantlee will present 
the same interface and core syntax for creating new themes. For details of 
how to write templates, see the documentation.

%package devel
Summary: Development files for %{name}
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package apidocs
Group: Development/Documentation
Summary: Grantlee API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the Grantlee API documentation in HTML
format for easy browsing.


%prep
%setup -q -n grantlee-%{version}%{?pre:-%{pre}}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast -C %{_target_platform} DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%dir %{_libdir}/grantlee
%{_libdir}/grantlee/*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/cmake/*
%dir %{_includedir}/grantlee
%{_includedir}/grantlee/*
%{_includedir}/*
