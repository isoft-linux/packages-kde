%define webkit 1
# Require kscreen, omit kcontrol/randr bits
%define kscreen 1
%define systemd_login1 1

Summary: KDE Workspace
Name:    kde-workspace
Version: 4.11.22
Release: 1%{?dist}

License: GPLv2
URL:     https://projects.kde.org/projects/kde/kde-workspace
Source0: http://download.kde.org/stable/applications/15.08.0/src/kde-workspace-%{version}.tar.xz

BuildRequires: kde-filesystem
BuildRequires: desktop-file-utils
BuildRequires: kdelibs-devel >= 4.14.4
BuildRequires: kactivities-devel
BuildRequires: libjpeg-devel
BuildRequires: pam-devel
BuildRequires: pkgconfig(dbusmenu-qt)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libstreamanalyzer)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xres)

%description
The KDE Workspace consists of what is the desktop of the
KDE Desktop Environment.

%package -n ksystraycmd
Summary:  Allows any application to be kept in the system tray
%description -n ksystraycmd
%{summary}.

%prep
%setup -q -n kde-workspace-%{version}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  -DKDE4_ENABLE_FPIE:BOOL=ON \
  -DBUILD_kscreensaver:BOOL=OFF \
  -DBUILD_systemsettings:BOOL=OFF \
  -DBUILD_kcheckpass:BOOL=OFF \
  -DBUILD_kdm:BOOL=OFF \
  -DBUILD_kwin:BOOL=OFF \
  -DBUILD_ksmserver:BOOL=OFF \
  -DBUILD_ksplash:BOOL=OFF \
  -DBUILD_powerdevil:BOOL=OFF \
  -DBUILD_qguiplatformplugin_kde:BOOL=ON \
  -DBUILD_ksysguard:BOOL=OFF \
  -DBUILD_klipper:BOOL=OFF \
  -DBUILD_kmenuedit:BOOL=OFF \
  -DBUILD_krunner:BOOL=OFF \
  -DBUILD_solid-actions-kcm:BOOL=OFF \
  -DBUILD_kstartupconfig:BOOL=OFF \
  -DBUILD_freespacenotifier:BOOL=OFF \
  -DBUILD_kscreensaver:BOOL=OFF \
  -DBUILD_kinfocenter:BOOL=OFF \
  -DBUILD_ktouchpadenabler:BOOL=OFF \
  -DBUILD_kcminit:BOOL=OFF \
  -DBUILD_khotkeys:BOOL=OFF \
  -DBUILD_kwrited:BOOL=OFF \
  -DBUILD_appmenu:BOOL=OFF \
  -DBUILD_cursors:BOOL=OFF \
  -DBUILD_plasma:BOOL=OFF \
  -DBUILD_statusnotifierwatcher:BOOL=OFF \
  -DBUILD_kstyles:BOOL=OFF \
  -DBUILD_kcontrol:BOOL=OFF \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}/ksystraycmd


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/ksystraycmd

%files -n ksystraycmd
%{_kde4_bindir}/ksystraycmd

%changelog
