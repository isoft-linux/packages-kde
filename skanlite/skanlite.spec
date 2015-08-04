Name:           skanlite
Version:        1.1
Release:        6.git
Summary:        Lightweight scanning program
Group:          Applications/Productivity
# Actually: GPLv2 or GPLv3 or any later Version approved by KDE e.V.
License:        GPLv2 or GPLv3
URL:            http://kde-apps.org/content/show.php?content=109803
#Source0:        ftp://ftp.kde.org/pub/kde/stable/%{name}/1.1/src/%{name}-1.1.tar.xz

#git clone clone git://anongit.kde.org/skanlite
#git checkout frameworks
Source0: skanlite.tar.gz

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

BuildRequires: libpng-devel
BuildRequires: pkgconfig(libksane) 

%description
Skanlite is a light-weight scanning application based on libksane.

%prep
%setup -q -n skanlite

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.skanlite.desktop

%files
%{_kf5_bindir}/skanlite
%{_kf5_datadir}/applications/org.kde.skanlite.desktop
%{_docdir}/HTML/*/skanlite

%changelog
