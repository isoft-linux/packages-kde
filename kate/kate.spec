Name:    kate
Summary: Advanced Text Editor
Version: 15.08.2
Release: 3 
License: LGPLv2 and LGPLv2+ and GPLv2+ 
URL:     https://projects.kde.org/projects/kde/applications/kate

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/kate-%{version}.tar.xz

#use /usr/src/rust/src instead of /usr/local/src/rust/src
Patch0: kate-rust-plugin-src-dir.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(x11)
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kinit-devel >= 5.10.0-3
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-threadweaver-devel
BuildRequires: kf5-kwallet-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel

# not sure if we want -plugins by default, let's play it safe
# and go with no initially -- rex
#Requires: %{name}-plugins%{?_isa} = %{version}-%{release}

%{?kf5_kinit_requires}

%description
%{summary}.

%package plugins
Summary: Kate plugins
License: LGPLv2
# upgrade path, when -plugins were split
Obsoletes: kate < 14.12.1
Requires: %{name} = %{version}-%{release}
%description plugins
%{summary}.

%package -n kwrite
Summary: Text Editor
License: LGPLv2+
%{?kf5_kinit_requires}
%description -n kwrite
%{summary}.


%prep
%setup -q -n kate-%{version}
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.kate.desktop
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.kwrite.desktop


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null || :
fi

%postun -n kwrite
if [ $1 -eq 0 ] ; then
update-desktop-database -q &> /dev/null || :
fi

%posttrans -n kwrite
update-desktop-database -q &> /dev/null || :


%files
%doc COPYING.LIB
%doc AUTHORS
%config(noreplace) %{_sysconfdir}/xdg/katerc
%{_kf5_bindir}/kate
%{_kf5_libdir}/libkdeinit5_kate.so
%{_kf5_datadir}/applications/org.kde.kate.desktop
%{_datadir}/appdata/org.kde.kate.appdata.xml
%{_kf5_datadir}/icons/hicolor/*/*
%{_mandir}/man1/kate.1*
%{_kf5_docdir}/HTML/en/kate/
%{_kf5_docdir}/HTML/en/katepart/
%{_kf5_datadir}/kxmlgui5/kate/
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.katesessions.desktop
%{_kf5_datadir}/kservices5/plasma-dataengine-katesessions.desktop
%{_kf5_datadir}/plasma/services/org.kde.plasma.katesessions.operations

%files plugins
%config(noreplace) %{_sysconfdir}/xdg/ktexteditor_codesnippets_core.knsrc
%{_kf5_qtplugindir}/ktexteditor/*.so
%{_kf5_qtplugindir}/plasma/dataengine/plasma_engine_katesessions.so
%{_kf5_datadir}/kateproject/
%{_kf5_datadir}/katexmltools/
%{_kf5_datadir}/kservices5/katesymbolviewerplugin.desktop
%{_kf5_datadir}/kxmlgui5/katebuild/
%{_kf5_datadir}/kxmlgui5/katecloseexceptplugin/
%{_kf5_datadir}/kxmlgui5/katectags/
%{_kf5_datadir}/kxmlgui5/katefiletree/
%{_kf5_datadir}/kxmlgui5/kategdb/
%{_kf5_datadir}/kxmlgui5/katekonsole/
%{_kf5_datadir}/kxmlgui5/kateopenheaderplugin/
%{_kf5_datadir}/kxmlgui5/kateproject/
%{_kf5_datadir}/kxmlgui5/katesearch/
%{_kf5_datadir}/kxmlgui5/katesnippets/
%{_kf5_datadir}/kxmlgui5/katesql/
%{_kf5_datadir}/kxmlgui5/katesymbolviewer/
%{_kf5_datadir}/kxmlgui5/katexmltools/
%{_kf5_datadir}/kxmlgui5/tabswitcher/
%{_kf5_datadir}/kxmlgui5/katereplicodeplugin
%{_kf5_datadir}/kxmlgui5/kterustcompletion


%files -n kwrite
%{_kf5_bindir}/kwrite
%{_kf5_libdir}/libkdeinit5_kwrite.so
%{_kf5_datadir}/applications/org.kde.kwrite.desktop
%{_datadir}/appdata/org.kde.kwrite.appdata.xml
%{_kf5_datadir}/kxmlgui5/kwrite/
%{_kf5_docdir}/HTML/en/kwrite/


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-3
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- rebuild with new libgit2
