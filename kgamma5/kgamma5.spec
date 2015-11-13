%global base_name kgamma5
Name:    kgamma5
Summary: A monitor calibration tool 
Version: 5.4.3
Release: 2%{?dist}

License: GPLv2
URL:     https://projects.kde.org/projects/kde/kdegraphics/kgamma
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif 
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: kf5-kinit-devel
# libkdeinit5_*
%{?kf5_kinit_requires}


%description
%{summary}.


%prep
%setup -q -n %{base_name}-%{version}


%build

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kcmkgamma

%files -f kcmkgamma.lang
%{_kf5_qtplugindir}/kcm_kgamma.so
%{_docdir}/HTML/en/kgamma5
%{_kf5_datadir}/kgamma
%{_kf5_datadir}/kservices5/kgamma.desktop


%changelog
* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-3
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

