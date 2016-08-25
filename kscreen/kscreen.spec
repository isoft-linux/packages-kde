Name:           kscreen
Epoch:			2
Version:        5.7.4
Release:        1
Summary:        KDE Display Management software

License:        GPLv2 or GPLv3
URL:            https://projects.kde.org/projects/playground/base/kscreen

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  libkscreen-devel >= %{version}

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kservice-devel

Requires:       kf5-filesystem
Requires:       qt5-qtgraphicaleffects

%description
KCM and KDED modules for managing displays in KDE.


%prep
%setup -q -n %{name}-%{version}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang %{name} --with-kde --with-qt --all-name

%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%files -f %{name}.lang
%doc COPYING
%{_bindir}/kscreen-console
#%{_bindir}/kscreen-osd
%{_kf5_qtplugindir}/kcm_kscreen.so
%{_kf5_qtplugindir}/kf5/kded/kscreen.so
%{_datadir}/kcm_kscreen/
%{_kf5_datadir}/kservices5/kcm_kscreen.desktop
#%{_kf5_datadir}/kservices5/kded/kscreen.desktop
%{_datadir}/icons/hicolor/*/actions/*


%changelog
* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Wed Jul 13 2016 sulit <sulitsrc@gmail.com> - 2:5.7.1-2
- readd Epoch to kscreen.spec. If it has Epoch flag, it will not be removed for
  the package life

* Wed Jul 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.1-1
- 5.7.1

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.95-1
- 5.6.95

* Wed Apr 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.3-1
- 5.6.3

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.2-1
- 5.6.2

* Tue Apr 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.6.1-1
- 5.6.1

* Tue Jan 19 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix i18n issue.

* Mon Dec 21 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- KDEBUG-356228 QScreen issue workaround patch.

* Mon Nov 23 2015 <kun.li@i-soft.com.cn> - 1:5.4.3-3
- add Patch2, additional translations

* Fri Nov 13 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add ToolTip for XF86Display shortcut setting. 

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 1:5.4.3-2
- Update, drop private git codes with kscreen-osd support
- Now we use patch and extra source to add osd support to original kscreen codes.
- Since it will not be merged upstream.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1:5.4.0-4
- Rebuild for new 4.0 release

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Fri Aug 07 2015 Cjacker <cjacker@foxmail.com>
- taken codes from Leslie Zhai.
- Kscreen-OSD should works.
