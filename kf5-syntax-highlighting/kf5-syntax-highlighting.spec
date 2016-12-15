%global framework syntax-highlighting

Name:           kf5-%{framework}
Version:        5.29.0
Release:        1
Summary:        Syntax highlighting engine and library
License:        LGPL-2.1+ and GPL-2.0 and GPL-2.0+ and GPL-3.0 and MIT and BSD-3-Clause

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

Url:            http://www.kde.org
BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-filesystem
BuildRequires:  qt5-qtbase-devel

%description
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%package devel
Summary:        Syntax highlighting engine and library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       extra-cmake-modules

%description devel
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%prep
%setup -q -n %{framework}-%{version}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%install
make %{?_smp_mflags} -C %{_target_platform}
cd %{_target_platform} && %make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING* README*
#%config %{_kf5_configdir}/org_kde_ksyntaxhighlighting.categories
%config /etc/xdg/org_kde_ksyntaxhighlighting.categories
%{_kf5_bindir}/kate-syntax-highlighter
%{_kf5_libdir}/libKF5SyntaxHighlighting.so.*

%files devel
%{_kf5_libdir}/libKF5SyntaxHighlighting.so
%{_kf5_libdir}/cmake/KF5SyntaxHighlighting/
%{_kf5_libdir}/qt5/mkspecs/modules/qt_KSyntaxHighlighting.pri
%{_kf5_includedir}/*

%changelog
* Wed Dec 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-1
- 5.29.0-1
