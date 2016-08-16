Name:           extra-cmake-modules
Summary:        Additional modules for CMake build system
Version:        5.25.0
Release:        1

License:        BSD
URL:            http://community.kde.org/KDE_Core/Platform_11/Buildsystem/FindFilesSurvey

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  cmake >= 2.8.12
BuildRequires:  qt5-qtbase-devel qt5-qttools-devel
BuildRequires:  python-sphinx
Requires:       cmake >= 2.8.12

%description
Additional modules for CMake build system needed by KDE Frameworks.


%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%doc README.rst COPYING-CMAKE-SCRIPTS
%{_datadir}/ECM
%{_mandir}/man7/*
%{_docdir}/ECM/

%changelog
* Tue Aug 16 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Thu Apr 07 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Mon Dec 21 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-4
- Backport from 5.17.0

* Sun Nov 15 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- Add patch from reviewboard

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-2
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0

