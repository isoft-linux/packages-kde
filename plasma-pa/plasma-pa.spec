Name:    plasma-pa
Version: 5.8.3
Release: 1%{?dist}
Summary: Plasma applet for audio volume management using PulseAudio

License: LGPLv2+ and GPLv2+
URL:     https://quickgit.kde.org/?p=%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  glib2-devel
BuildRequires:  kde-filesystem
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

Requires:       kf5-filesystem

%description
%{summary}.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name

## unpackaged files
rm -rfv %{buildroot}%{_kde4_appsdir}/kconf_update/


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING COPYING.LIB
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.volume
%{_kf5_qmldir}/org/kde/plasma/private/volume/
%{_kf5_qtplugindir}/kcms/kcm_pulseaudio.so
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.volume.desktop
%{_kf5_datadir}/kconf_update/*
%{_kf5_libdir}/libQPulseAudioPrivate.so
%{_kf5_datadir}/kpackage/kcms/kcm_pulseaudio
%{_kf5_datadir}/kservices5/kcm_pulseaudio.desktop
#%lang(en) %{_kf5_docdir}/HTML/en/plasma-pa/
#%lang(uk) %{_kf5_docdir}/HTML/uk/plasma-pa/
#%lang(ca) %{_kf5_docdir}/HTML/ca/plasma-pa/
#%lang(pt_BR) %{_kf5_docdir}/HTML/pt_BR/plasma-pa/


%changelog
* Thu Nov 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Mon Jun 27 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-1
- 5.6.95

* Thu Apr 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
- 5.6.2
