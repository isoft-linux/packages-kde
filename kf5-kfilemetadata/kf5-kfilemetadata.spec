%global framework kfilemetadata

# Enable to build ffmpeg extractor
%global         ffmpeg 1 

Name:           kf5-%{framework}
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version:        5.16.0
Release:        2

# # KDE e.V. may determine that future LGPL versions are accepted
License:        LGPLv2 or LGPLv3
URL:            https://www.kde.org

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-karchive-devel >= %{version}
BuildRequires:  qt5-qtbase-devel

BuildRequires:  ebook-tools-devel
BuildRequires:  pkgconfig(exiv2) >= 0.20
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(taglib)
%if 0%{?ffmpeg}
BuildRequires:  ffmpeg-devel
%endif

BuildRequires:  libattr-devel
#runtime require.
BuildRequires:  catdoc

Requires: catdoc

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-ki18n-devel
Requires:       kf5-kservice-devel
Requires:       kf5-karchive-devel

%description devel
%{summary}.


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
%find_lang kfilemetadata5_qt --with-qt --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kfilemetadata5_qt.lang
%doc COPYING.LGPL*
%{_kf5_libdir}/libKF5FileMetaData.so.*
%{_kf5_plugindir}/kfilemetadata/kfilemetadata_*.so

%files devel
%{_kf5_libdir}/libKF5FileMetaData.so
%{_kf5_libdir}/cmake/KF5FileMetaData
%{_kf5_includedir}/KFileMetaData

%changelog
* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-2
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
