Name:           qt5-prison
Version:        2.8.8
Release:        1.git
Summary:        A Qt-based barcode abstraction library

Group:          System Environment/Libraries
License:        MIT
URL:            https://projects.kde.org/projects/kdesupport/prison
Source0:        prison.tar.gz

BuildRequires:  cmake
BuildRequires:  libdmtx-devel
BuildRequires:  qrencode-devel
BuildRequires:  qt5-qtbase-devel

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}


%prep
%setup -q -n prison


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} -DQT5_BUILD=ON ..
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
%{_libdir}/libprison.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/prison/
%{_libdir}/libprison.so
%{_libdir}/cmake/Prison/


%changelog
