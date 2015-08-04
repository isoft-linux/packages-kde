Summary: Graphical effect and filter library
Name:    qimageblitz
Version: 0.0.6
Release: 10.svn20150702

Group:   System Environment/Libraries
License: BSD and ImageMagick
URL:     http://qimageblitz.sourceforge.net/
#svn://anonsvn.kde.org/home/kde/trunk/kdesupport/qimageblitz

#Source0: http://download.kde.org/stable/qimageblitz/qimageblitz-%{version}.tar.bz2
Source0: %{name}.tar.gz

BuildRequires: cmake
BuildRequires: qt5-qtbase-devel

%description
Blitz is a graphical effect and filter library for Qt5 that contains
improvements over KDE 3.x's kdefx library including bugfixes, memory and
speed improvements, and MMX/SSE support.

%package devel
Summary: Developer files for %{name}
Group:   Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n %{name}


%build
mkdir -p %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{cmake} %{?_cmake_skip_rpath} -DQT4_BUILD=OFF ..
popd

make %{?_smp_mflags} -C %{_target_platform}-qt5


%install
rm -rf $RPM_BUILD_ROOT
make install/fast  DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}-qt5


%check

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/blitztest
%{_libdir}/libqimageblitz.so.**

%files devel
%defattr(-,root,root,-)
%{_libdir}/libqimageblitz.so
%{_libdir}/pkgconfig/qimageblitz.pc
%{_includedir}/qimageblitz/


%changelog
