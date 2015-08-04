%global framework kded

Name:           kf5-%{framework}
Version:        5.12.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 addon with extensible daemon for system-level services

License:        LGPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}
BuildRequires:  kf5-kinit-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}

Requires:       kf5-filesystem

# libkdeinit5_kded5
%{?kf5_kinit_requires}

%description
KDED stands for KDE Daemon which isn't very descriptive. KDED runs
in the background and performs a number of small tasks. Some of these
tasks are built in, others are started on demand.

Custom KDED modules can be provided by 3rd party frameworks and
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

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
%doc COPYING.LIB README.md
%{_kf5_bindir}/kded5
%{_kf5_libdir}/libkdeinit5_kded5.so
%{_kf5_datadir}/dbus-1/services/*.service
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_mandir}/man8/*
%{_kf5_mandir}/*/man8/*
%exclude %{_kf5_mandir}/man8

%files devel
%{_kf5_libdir}/cmake/KDED
%{_kf5_datadir}/dbus-1/interfaces/*.xml


%changelog
