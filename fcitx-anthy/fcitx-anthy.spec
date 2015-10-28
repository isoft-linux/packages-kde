Name:			fcitx-anthy
Version:		0.2.2
Release:		7%{?dist}
Summary:		Anthy Engine for Fcitx
License:		GPLv2+
URL:			https://fcitx-im.org/wiki/Anthy
Source0:		http://download.fcitx-im.org/fcitx-anthy/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	fcitx-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	anthy-devel
Requires:		fcitx

%description
Fcitx-anthy is an Anthy engine wrapper for Fcitx. It provides a Japanese input
method. You can input hiragana and katakana by romaji or using a Japanese
keyboard. And fcitx-anthy also supports converting hiragana or katakana to
kanji.

%prep
%setup -q 


%build
mkdir -pv build
pushd build
%cmake ..
make %{?_smp_mflags} VERBOSE=1

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %{name}


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
%doc COPYING AUTHORS README
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/anthy/
%{_datadir}/fcitx/inputmethod/anthy.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/imicon/anthy.png
%{_datadir}/icons/hicolor/48x48/status/%{name}.png
%{_datadir}/icons/hicolor/22x22/status/%{name}-symbol.png
%{_datadir}/icons/hicolor/scalable/status/%{name}-*.svg

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.2.2-7
- Rebuild for new 4.0 release

