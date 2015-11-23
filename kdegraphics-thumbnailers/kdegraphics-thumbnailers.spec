Name:    kdegraphics-thumbnailers
Summary: Thumbnailers for various graphic types 
Version: 15.11.80
Release: 2%{?dist}

# most sources GPLv2+, dscparse.* GPL, gscreator.* LGPLv2+, 
License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/kdegraphics-thumbnailers 
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kio-devel
BuildRequires: kf5-libkexiv2-devel 
BuildRequires: kf5-libkdcraw-devel

%description
%{summary}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%{_kf5_qtplugindir}/gsthumbnail.so
%{_kf5_qtplugindir}/rawthumbnail.so
%{_kf5_datadir}/kservices5/gsthumbnail.desktop
%{_kf5_datadir}/kservices5/rawthumbnail.desktop

%changelog
* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.0-3.kf5.git
- Rebuild for new 4.0 release

* Sun Oct 18 2015 Cjacker <cjacker@foxmail.com>
- git version, initial build for kf5.
