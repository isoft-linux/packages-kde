%global framework kdoctools

Name:           kf5-%{framework}
Version:        5.20.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon for generating documentation

License:        GPLv2+ and MIT
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-ki18n-devel  >= %{version}
BuildRequires:  kf5-karchive-devel >= %{version}

BuildRequires:  perl-Any-URI-Escape

Requires:       docbook-dtds
Requires:       docbook-style-xsl
Requires:       kf5-filesystem

Obsoletes:      kf5-kdoctools-doc < 5.3.0-2
Provides:       kf5-kdoctools-doc = %{version}-%{release}

%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf5-kdoctools-static = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       perl-Any-URI-Escape

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kdoctools5_qt --with-qt --with-man --all-name


%files -f kdoctools5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_bindir}/checkXML5
%{_kf5_bindir}/meinproc5
%{_kf5_datadir}/man/man1/*
%{_kf5_datadir}/man/man7/*
%{_kf5_datadir}/man/man8/*
%{_kf5_datadir}/kf5/kdoctools/
# FIXME/TODO: %%lang'ify these -- rex
%{_kf5_docdir}/HTML/*/kdoctools5-common/

%files devel
%{_kf5_includedir}/XsltKde/
%{_kf5_libdir}/libKF5XsltKde.a
%{_kf5_libdir}/cmake/KF5DocTools/


%changelog
* Thu Apr 07 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

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
