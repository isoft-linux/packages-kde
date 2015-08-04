%define nam             fcitx-libpinyin 
%define ver             0.3.1 
%define rel             1

Summary:        LibPinyin IM of FCITX input framework
Name:           %{nam}
Version:        %{ver}
Release:        %{rel}
License:        GPL
Group:          User Interface/Desktops 
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Source0:        %{name}-%{version}_dict.tar.xz
BuildRequires:  fcitx-devel 
BuildRequires:  libpinyin-devel
BuildRequires:  cmake

%description
LibPinyin IM of FCITX input framework

%prep
%setup -n %{name}-%{version}
%build
mkdir build
pushd build
cmake .. -DSYSCONFDIR=%{_sysconfdir} -DSYSCONF_INSTALL_DIR=%{_sysconfdir} -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_prefix}/%{_lib}
make
popd

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
pushd build
make DESTDIR=${RPM_BUILD_ROOT} install
popd

%find_lang fcitx-libpinyin
rpmclean
%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files -f fcitx-libpinyin.lang
%defattr(-, root, root)
%{_libdir}/fcitx/fcitx-libpinyin.so
%{_libdir}/fcitx/qt/libfcitx-libpinyin-dictmanager.so
%{_datadir}/fcitx/addon/fcitx-libpinyin.conf
%{_datadir}/fcitx/configdesc/fcitx-libpinyin.desc
%{_datadir}/fcitx/imicon/bopomofo.png
%{_datadir}/fcitx/imicon/pinyin-libpinyin.png
%{_datadir}/fcitx/imicon/shuangpin-libpinyin.png
%{_datadir}/fcitx/inputmethod/pinyin-libpinyin.conf
%{_datadir}/fcitx/inputmethod/shuangpin-libpinyin.conf
%{_datadir}/fcitx/inputmethod/zhuyin-libpinyin.conf
%{_datadir}/fcitx/libpinyin/
%{_datadir}/icons/hicolor/*/status/*
