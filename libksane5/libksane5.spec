Name:    libksane5
Summary: SANE Library interface for KDE5
Version: 0.3.0
Release: 2

License: LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/libs/libksane
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

#git clone git://anongit.kde.org/libksane
#git checkout frameworks
Source0: libksane.tar.gz

BuildRequires: pkgconfig(sane-backends)

%description
%{summary}.

%package devel
Summary:  Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n libksane

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
pkg-config --modversion libksane


%post
/sbin/ldconfig
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%files
%{_kf5_libdir}/libKF5Sane.so.*

%files devel
%{_kf5_libdir}/libKF5Sane.so
%{_kf5_libdir}/pkgconfig/libksane.pc
%{_kf5_libdir}/cmake/KF5Sane/
%{_includedir}/KSane/
%{_includedir}/ksane*.h


%changelog
