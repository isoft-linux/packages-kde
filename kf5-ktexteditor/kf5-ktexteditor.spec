%global framework ktexteditor

Name:           kf5-%{framework}
Version:        5.27.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 with advanced embeddable text editor

License:        LGPLv2+
URL:            https://projects.kde.org/projects/frameworks/ktexteditor

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  kf5-kiconthemes-devel >= %{version}

BuildRequires:  kf5-karchive-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kguiaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-kparts-devel >= %{version}
BuildRequires:  kf5-sonnet-devel >= %{version}

BuildRequires:  libgit2-devel >= 0.22.0

Requires:       kf5-filesystem

%description
KTextEditor provides a powerful text editor component that you can embed in your
application, either as a KPart or using the KF5::TextEditor library (if you need
more control).

The text editor component contains many useful features, from syntax
highlighting and automatic indentation to advanced scripting support, making it
suitable for everything from a simple embedded text-file editor to an advanced
IDE.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kparts-devel

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
%find_lang ktexteditor5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f ktexteditor5_qt.lang
%doc README.md
%license COPYING.LIB
%{_kf5_libdir}/libKF5TextEditor.so.*
%{_kf5_plugindir}/parts/katepart.so
%{_kf5_datadir}/kservices5/katepart.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/katepart5/

%files devel
%{_kf5_libdir}/libKF5TextEditor.so
%{_kf5_libdir}/cmake/KF5TextEditor/
%{_kf5_includedir}/ktexteditor_version.h
%{_kf5_includedir}/KTextEditor/
%{_kf5_archdatadir}/mkspecs/modules/qt_KTextEditor.pri


%changelog
* Mon Oct 31 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.27.0-1
- 5.27.0

* Thu Aug 18 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Wed Jul 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-2
- Rebuild.

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Mon Apr 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Tue Dec 22 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-5
- Backport from 5.17.0

* Fri Nov 27 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Use ~/.config/KDE/Sonnet.conf ignore setted by kcm_spellchecking.
- KF5::Sonnet handle ignore word is better ;-)

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-4
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- rebuild with new libgit2

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
