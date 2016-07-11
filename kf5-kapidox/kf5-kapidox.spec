%global framework kapidox

Name:           kf5-%{framework}
Version:        5.24.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 4 scripts and data for building API documentation
BuildArch:      noarch

License:        BSD
URL:            http://download.kde.org/

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel

BuildRequires:  python-devel

Requires:       kf5-filesystem

%description
Scripts and data for building API documentation (dox) in a standard format and
style.


%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc LICENSE
%{python_sitelib}/kapidox
%{python_sitelib}/kapidox-%{version}-py2.7.egg-info
%{_kf5_bindir}/kgenapidox
%{_kf5_bindir}/depdiagram-prepare
%{_kf5_bindir}/depdiagram-generate
%{_kf5_bindir}/kgenframeworksapidox
%{_kf5_bindir}/depdiagram-generate-all
%{_mandir}/man1/depdiagram-generate-all.1*
%{_mandir}/man1/depdiagram-generate.1*
%{_mandir}/man1/depdiagram-prepare.1*
%{_mandir}/man1/kgenapidox.1*
%{_mandir}/man1/kgenframeworksapidox.1*


%changelog
* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
