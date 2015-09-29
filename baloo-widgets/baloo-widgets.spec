
Name:    baloo-widgets
Summary: Widgets for Baloo
Version: 15.08.1
Release: 3%{?dist}

# # KDE e.V. may determine that future LGPL versions are accepted
License: LGPLv2 or LGPLv3
URL:     https://projects.kde.org/projects/kde/kdelibs/baloo-widgets

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

Provides: kf5-baloo-widgets = %{version}-%{release}
Provides: kf5-baloo-widgets%{?_isa} = %{version}-%{release}

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kfilemetadata-devel
BuildRequires:  kf5-baloo-devel
BuildRequires:  kf5-kdelibs4support-devel

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Provides: kf5-baloo-widgets-devel = %{version}-%{release}
Provides: kf5-baloo-widgets-devel%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
Requires: kf5-kcoreaddons-devel
Requires: kf5-kio-devel
%description devel
%{summary}.


%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING.LIB
%{_kf5_libdir}/libKF5BalooWidgets.so.*
%{_kf5_bindir}/baloo_filemetadata_temp_extractor

%files devel
%{_kf5_libdir}/cmake/KF5BalooWidgets
%{_kf5_includedir}/BalooWidgets
%{_kf5_libdir}/libKF5BalooWidgets.so


%changelog
