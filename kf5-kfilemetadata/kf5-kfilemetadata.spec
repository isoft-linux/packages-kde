%global framework kfilemetadata
%global plasma_version 5.2.95

# Enable to build ffmpeg extractor
%global         ffmpeg  0

Name:           kf5-%{framework}
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version:        5.9.2
Release:        1

# # KDE e.V. may determine that future LGPL versions are accepted
License:        LGPLv2 or LGPLv3
URL:            https://www.kde.org

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{plasma_version}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  qt5-qtbase-devel

BuildRequires:  ebook-tools-devel
BuildRequires:  pkgconfig(exiv2) >= 0.20
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(taglib)
%if 0%{?ffmpeg}
BuildRequires:  ffmpeg-devel
%endif

BuildRequires:  libattr-devel

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
