%global framework kwallet

Name:           kf5-%{framework}
Version:        5.15.0
Release:        4%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution for password management

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

#create a default wallet with empty password when kwalletd launched initially.
#By Cjacker.
Patch0: kwalletd-create-empty-password-wallet-first-time-run.patch

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel


BuildRequires:  libgcrypt-devel

BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-knotifications-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel

Obsoletes:      kf5-kwallet-runtime < 5.8.0-2
Provides:       kf5-kwallet-runtime = %{version}-%{release}
Provides:       kf5-kwallet-runtime%{?_isa} = %{version}-%{release}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
KWallet is a secure and unified container for user passwords.

%package        libs
Summary:        KWallet framework libraries
Requires:       kf5-filesystem
Requires:       %{name} = %{version}-%{release}
%description    libs
Provides API to access KWallet data from applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang %{name} --with-qt --all-name


%files -f %{name}.lang
%doc COPYING.LIB README.md
%{_kf5_datadir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf5_datadir}/dbus-1/services/org.kde.kwalletd.service
%{_kf5_bindir}/kwalletd5
%{_kf5_bindir}/kwallet-query

%{_kf5_datadir}/kservices5/kwalletd5.desktop
%{_kf5_datadir}/knotifications5/kwalletd.notifyrc
%{_mandir}/man1/kwallet-query.1.gz

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{_kf5_libdir}/libKF5Wallet.so.*
%{_kf5_libdir}/libkwalletbackend5.so.*

%files devel
%{_kf5_datadir}/dbus-1/interfaces/kf5_org.kde.KWallet.xml
%{_kf5_includedir}/kwallet_version.h
%{_kf5_includedir}/KWallet
%{_kf5_libdir}/cmake/KF5Wallet
%{_kf5_libdir}/libKF5Wallet.so
%{_kf5_libdir}/libkwalletbackend5.so
%{_kf5_archdatadir}/mkspecs/modules/qt_KWallet.pri


%changelog
* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-4
- Add patch0 to create a default wallet with empty password

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
- drop kwallet-pam patch, already upstream.
