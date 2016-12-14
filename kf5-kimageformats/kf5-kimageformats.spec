%global framework kimageformats

Name:           kf5-%{framework}
Version:        5.29.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with additional image plugins for QtGui

License:        LGPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

#original psd support in kimageformats broken, use this one.
#https://github.com/Code-ReaQtor/libqpsd
Source1: libqpsd.tar.gz

BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.


%prep
%setup -q -n %{framework}-%{version} -a1

pushd libqpsd
popd

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

pushd libqpsd
qmake-qt5
make
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

#use psd plugin from libqpsd
install -m0755 libqpsd/libqpsd.so %{buildroot}%{_kf5_qtplugindir}/imageformats/
#drop kimg_psd provided by kimageformats.
rm -rf  %{buildroot}%{_kf5_qtplugindir}/imageformats/kimg_psd.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING.LIB README.md
%{_kf5_qtplugindir}/imageformats/*.so
%{_kf5_datadir}/kservices5/qimageioplugins/*.desktop


%changelog
* Wed Dec 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-1
- 5.29.0-1

* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-2
- 5.28.0-2

* Thu Nov 17 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-1
- 5.28.0

* Wed Aug 17 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Thu Nov 19 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- Use libqpsd instead of kimg_psd

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
