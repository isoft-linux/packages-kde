Name:    ffmpegthumbs 
Summary: Video thumbnailer for KDE5
Version: 5.11.0
Release: 3.git%{?dist}

License: GPLv2+ and GFDL
URL:     https://projects.kde.org/projects/kde/kdegames/%{name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

#git clone git://anongit.kde.org/ffmpegthumbs
#git checkout frameworks
Source0: ffmpegthumbs.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: ffmpeg-devel

BuildRequires: pkgconfig(Qt5Widgets)

%description
%{summary}

%prep
%setup -q -n %{name}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
#appstream-util validate-relax --nonet %{buildroot}%{_kf5_datadir}/appdata/%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf5_datadir}/kservices5/ffmpegthumbs.desktop ||:


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%files
%{_qt5_plugindir}/ffmpegthumbs.so
%{_kf5_datadir}/kservices5/ffmpegthumbs.desktop


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.11.0-3.git
- Rebuild for new 4.0 release

