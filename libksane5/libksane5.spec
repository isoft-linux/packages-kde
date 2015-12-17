%define realname libksane
Name: libksane5
Summary: SANE Library interface for KDE5
Version: 15.12.0
Release: 2
License: LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/libs/libksane
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{realname}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-ktextwidgets-devel

BuildRequires: pkgconfig(sane-backends)

%description
%{summary}.

%package devel
Summary:  Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%setup -q -n %{realname}-%{version} 

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


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
%{_kf5_libdir}/cmake/KF5Sane/
%{_includedir}/KF5/KSane/
%{_includedir}/KF5/*.h


%changelog
* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.3.0-3
- Rebuild for new 4.0 release

