Name:    kde-baseapps
Summary: KDE Core Applications 
Version: 5.11.0
Release: 5.git

License: GPLv2 and GFDL
URL:     https://projects.kde.org/projects/kde/kde-baseapps 

#git clone git://anongit.kde.org/kde-baseapps
#git checkout frameworks
Source0: %{name}.tar.gz

Requires: accountsservice

# kdepasswd uses chfn
Requires: util-linux

BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(zlib)

BuildRequires: cmake 
BuildRequires: kf5-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gettext

BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-kdesu-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kpty-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: libX11-devel
BuildRequires: qt5-qtbase-devel

%description
Core applications of KF5, including:
kdepasswd : Changes a UNIX password
kdialog : Nice dialog boxes from shell scripts
libkonq : Filemanager ment popup menu service.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n kde-baseapps

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/lib
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/kdepasswd
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/kdialog

#%find_lang kdepasswd --with-kde --without-mo

#remove unneeded "New" templates.
rm -rf %{buildroot}%{_datadir}/templates/linkCAMERA.desktop
rm -rf %{buildroot}%{_datadir}/templates/linkCDROM.desktop
rm -rf %{buildroot}%{_datadir}/templates/linkCDWRITER.desktop
rm -rf %{buildroot}%{_datadir}/templates/linkDVDROM.desktop
rm -rf %{buildroot}%{_datadir}/templates/linkFloppy.desktop
rm -rf %{buildroot}%{_datadir}/templates/linkHD.desktop
rm -rf %{buildroot}%{_datadir}/templates/linkMO.desktop
rm -rf %{buildroot}%{_datadir}/templates/linkNFS.desktop
rm -rf %{buildroot}%{_datadir}/templates/linkZIP.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/CAMERA-Device.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/CDROM-Device.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/CDWRITER-Device.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/DVDROM-Device.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/Floppy.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/HD.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/HTMLFile.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/MO-Device.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/NFS.desktop
rm -rf %{buildroot}%{_datadir}/templates/.source/ZIP-Device.desktop

#already in kio
rm -rf %{buildroot}%{_datadir}/kservicetypes5/konqpopupmenuplugin.desktop

%check
for f in %{buildroot}%{_kde4_datadir}/applications/*.desktop ; do
  desktop-file-validate $f
done


%post
/sbin/ldconfig ||:
#touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:
#touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null ||:

%posttrans
#gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
#gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null ||:
update-desktop-database -q &> /dev/null ||:

%postun
/sbin/ldconfig ||:
if [ $1 -eq 0 ] ; then
#  touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:
#  touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null ||:
#  gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
#  gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null ||:
  update-desktop-database -q &> /dev/null ||:
fi


%files
%{_kf5_bindir}/kdepasswd
%{_kf5_bindir}/kdialog
%{_kf5_libdir}/libKF5Konq.so.*
%{_kf5_qtplugindir}/kf5/kded/favicons.so
%{_kf5_datadir}/applications/org.kde.kdepasswd.desktop
%{_kf5_datadir}/dbus-1/interfaces/org.kde.FavIcon.xml
%{_kf5_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml
%{_kf5_datadir}/kf5/kbookmark
%{_kf5_datadir}/kf5/konqueror
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/templates/.source/*
%{_kf5_datadir}/templates/*.desktop
%{_docdir}/HTML/en/kdepasswd

%files devel
%{_kf5_includedir}/*
%{_kf5_libdir}/cmake/KF5Konq
%{_kf5_libdir}/libKF5Konq.so

%changelog
* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.11.0-5.git
- Update to latest git, remove confliction file with kio

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.11.0-4.git
- Rebuild for new 4.0 release

* Wed Oct 14 2015 Cjacker <cjacker@foxmail.com>
- remove unneeded "new" templates.
