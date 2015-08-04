#define snaptag .20080527svn811390
%define beta 0.9.88
%define beta_tag rc3

Name:           automoc
Version:        1.0
Release:        0.23.%{?beta_tag}%{?dist}
Summary:        Automatic moc for Qt 4
Group:          Development/Tools
License:        BSD
URL:            http://www.kde.org
Source0:        ftp://ftp.kde.org/pub/kde/stable/automoc4/%{beta}/automoc4-%{beta}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides: automoc4 = %{beta}

Requires:       cmake >= 2.4.5
BuildRequires:  cmake >= 2.4.5
BuildRequires:  qt4-devel

%description
This package contains the automoc4 binary which is used to run moc on the
right source files in a Qt 4 or KDE 4 application.
Moc is the meta object compiler which is a widely used tool with Qt and
creates standard C++ files to provide syntactic sugar of the signal/slots
mechanism.


%prep
%setup -q -n automoc4-%{beta}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/automoc4
%{_libdir}/automoc4/


%changelog
