Name:		fcitx-hangul
Version:	0.3.0
Release:	5%{?dist}
Summary:	Hangul Engine for Fcitx
License:	GPLv2+
URL:		https://fcitx-im.org/wiki/Hangul
Source0:	http://download.fcitx-im.org/fcitx-hangul/%{name}-%{version}.tar.xz

BuildRequires:	cmake, fcitx-devel, gettext, intltool, libhangul-devel
Requires:	fcitx

%description
Fcitx-hangul is a Hangul engine wrapper for Fcitx. It
Provides Korean input method from libhangul.

%prep
%setup -q -n %{name}-%{version}


%build
mkdir -pv build
pushd build
%cmake ..
make %{?_smp_mflags} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/hangul.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/imicon/hangul.png
%dir %{_datadir}/fcitx/hangul/
%{_datadir}/fcitx/hangul/symbol.txt
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/*/status/fcitx-hanja-active.png
%{_datadir}/icons/hicolor/*/status/fcitx-hanja-inactive.png

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.3.0-5
- Rebuild for new 4.0 release

