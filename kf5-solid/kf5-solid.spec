%global framework solid

Name:           kf5-%{framework}
Version:        5.12.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 1 integration module that provides hardware information

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

BuildRequires:  libupnp-devel
BuildRequires:  systemd-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel

%if ! 0%{?bootstrap}
# Predicate parser deps
BuildRequires:  bison
BuildRequires:  flex
# really runtime-only dep, but doesn't hurt to check availability at buildtime
BuildRequires:  media-player-info
Requires:       media-player-info
%endif

Requires:       kf5-filesystem

Provides:       %{name}-runtime = %{version}-%{release}
Provides:       %{name}-runtime%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-runtime < 4.99.0.1

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Solid provides the following features for application developers:
 - Hardware Discovery
 - Power Management
 - Network Management

%package        libs
Summary:        Runtime libraries for Solid Framework
# When the split occured
Conflicts:      %{name} < 5.4.0-1
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}
%find_lang solid5_qt --with-qt --all-name


%files
%doc COPYING.LIB README.md TODO
%{_kf5_bindir}/solid-hardware5

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs -f solid5_qt.lang
%{_kf5_qmldir}/org/kde/solid
%{_kf5_libdir}/libKF5Solid.so.*

%files devel
%{_kf5_includedir}/solid_version.h
%{_kf5_includedir}/Solid
%{_kf5_libdir}/libKF5Solid.so
%{_kf5_libdir}/cmake/KF5Solid
%{_kf5_archdatadir}/mkspecs/modules/qt_Solid.pri


%changelog
