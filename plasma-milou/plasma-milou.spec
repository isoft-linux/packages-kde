%define         base_name milou

Name:           plasma-%{base_name}
Version:        5.3.2
Release:        1
Summary:        A dedicated KDE search application built on top of Baloo

License:        GPLv2+
URL:            https://projects.kde.org/kde/workspace/milou

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtscript-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-krunner-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-baloo-devel

Requires:       kf5-filesystem

Obsoletes:      kde-plasma-milou < 5.0.0
Provides:       kde-plasma-milou = %{version}-%{release}

%description
%{summary}.

%prep
%setup -q -n %{base_name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang milou --with-qt --all-name

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f milou.lang
%{_kf5_qtplugindir}/miloutextplugin.so
%{_kf5_datadir}/kservicetypes5/miloupreviewplugin.desktop
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.milou.desktop
%{_kf5_datadir}/kservices5/miloutextpreview.desktop
%{_libdir}/libmilou.so.*
%{_kf5_qmldir}/org/kde/milou
%{_datadir}/plasma/plasmoids/org.kde.milou


%changelog
