Name:		fcitx-chewing
Version:	0.2.1
Release:	5%{?dist}
Summary:	Chewing Wrapper for Fcitx
License:	GPLv2+
URL:		https://fcitx-im.org/wiki/Chewing
Source0:	http://download.fcitx-im.org/fcitx-chewing/%{name}-%{version}.tar.xz

BuildRequires:	cmake, fcitx-devel, gettext, intltool, libchewing-devel
Requires:	fcitx

%description
Fcitx-chewing is a Chewing Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese 
Phonetic IME.


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
%doc AUTHORS README COPYING
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/chewing.conf
%{_datadir}/fcitx/imicon/*.png
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/skin/classic/chewing.png
%{_datadir}/fcitx/skin/dark/chewing.png
%{_datadir}/fcitx/skin/default/chewing.png
%{_datadir}/icons/hicolor/48x48/apps/fcitx-chewing.png

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.2.1-5
- Rebuild for new 4.0 release

