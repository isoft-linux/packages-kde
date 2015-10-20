Name: zeroconf-ioslave
Summary: Network Monitor for DNS-SD services (Zeroconf)
Version: 15.08.0
Release: 3.kf5.git%{?dist}

License: GPLv2+
#URL:     https://projects.kde.org
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

#Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

#git clone git://anongit.kde.org/zeroconf-ioslave
#git checkout frameworks
Source0: zeroconf-ioslave.tar.xz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kdnssd-devel

%description
%{summary}

%prep
%autosetup -n %{name} 

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_kf5_qtplugindir}/kio_zeroconf.so
%{_kf5_qtplugindir}/kded_dnssdwatcher.so
%{_kf5_datadir}/kservices5/zeroconf.protocol
%{_kf5_datadir}/kservices5/kded/dnssdwatcher.desktop
%{_kf5_datadir}/remoteview/zeroconf.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml

%changelog
* Sun Oct 18 2015 Cjacker <cjacker@foxmail.com> 
- git version, initial build for kf5
