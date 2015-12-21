Name:    kamera
Summary: Digital camera support for KDE 
Version: 15.12.0
Release: 3%{?dist}

License: GPLv2
URL:     https://projects.kde.org/projects/kde/kdegraphics/kamera
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0: kamera-fix-i18n.patch

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kdoctools-devel

BuildRequires: pkgconfig(libgphoto2)

%description
%{summary}.


%prep
%setup -q
%patch0 -p1

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
%doc AUTHORS README
%{_kf5_qtplugindir}/kio_kamera.so
%{_kf5_qtplugindir}/kcm_kamera.so
%{_kf5_datadir}/solid/actions/solid_camera.desktop
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_docdir}/HTML/en/kcontrol/%{name}/


%changelog
* Sat Dec 19 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-3
- Fix i18n

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.07.90-3
- Rebuild for new 4.0 release

