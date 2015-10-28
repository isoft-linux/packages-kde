Name:           kf5-prison
Version:        2.8.8
Release:        2.git
Summary:        A Qt-based barcode abstraction library

License:        MIT
URL:            https://projects.kde.org/projects/kdesupport/prison
#git clone git://anongit.kde.org/prison
#git checkout frameworks
Source0:        prison.tar.gz

BuildRequires:  cmake
BuildRequires:  libdmtx-devel
BuildRequires:  qrencode-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

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
%{cmake_kf5} -DQT5_BUILD=ON ..
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
%{_kf5_libdir}/libKF5Prison.so.*

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/prison_version.h
%{_kf5_includedir}/PRISON
%{_kf5_libdir}/libKF5Prison.so
%{_kf5_libdir}/cmake/KF5Prison/
%{_libdir}/qt5/mkspecs/modules/qt_Prison.pri

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 2.8.8-2.git
- Rebuild for new 4.0 release

* Thu Aug 13 2015 Cjacker <cjacker@foxmail.com>
- initial build.
