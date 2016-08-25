Name:           kde-gtk-config
Summary:        Configure the appearance of GTK apps in KDE
Version:        5.7.4
Release:        1

# KDE e.V. may determine that future GPL versions are accepted
# KDE e.V. may determine that future LGPL versions are accepted
License:        (GPLv2 or GPLv3) and (LGPLv2 or LGPLv3)
URL:            https://projects.kde.org/projects/kde/workspace/kde-gtk-config

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/kde-gtk-config-%{version}.tar.xz

#the condition to detect whether it's icontheme or not IS WRONG.
#for example, Adwaita icon theme folder also contains 'cursors' folder.

#here 'breeze' icon theme contains 'apps' folder.
#triditional icon theme always contains '32x32' folder 
Patch0:	kde-gtk-fix-wrong-icontheme-condition.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kcmutils-devel

BuildRequires:  gtk3-devel
BuildRequires:  gtk2-devel

# need kcmshell5 from kde-cli-tools
Requires:       kde-cli-tools

%description
This is a System Settings configuration module for configuring the
appearance of GTK apps in KDE.

%prep
%setup -q -n kde-gtk-config-%{version}
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kcmgtk5_qt --with-qt --all-name


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f kcmgtk5_qt.lang
%doc ChangeLog COPYING COPYING.LIB
%{_kf5_qtplugindir}/kcm_kdegtkconfig.so
%{_sysconfdir}/xdg/*.knsrc
%{_kf5_datadir}/kservices5/kde-gtk-config.desktop
%{_libexecdir}/reload_gtk_apps
%{_libexecdir}/gtk_preview
%{_libexecdir}/gtk3_preview
%{_datadir}/kcm-gtk-module/
%{_datadir}/icons/hicolor/*/apps/kde-gtk-config.*


%changelog
* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-2
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95
