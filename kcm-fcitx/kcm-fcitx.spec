Name:		kcm-fcitx
Version:	0.4.3
Release:	7
Summary:	KDE Config Module for Fcitx
License:	GPLv2+
URL:		https://fcitx-im.org/wiki/Fcitx
#git clone https://github.com/fcitx/kcm-fcitx.git
Source0:	http://download.fcitx-im.org/%{name}/%{name}.tar.gz

BuildRequires:	qt5-qtbase-devel, fcitx-devel, gettext 
BuildRequires:	desktop-file-utils
Requires:	fcitx

%description
Kcm-fcitx is a System Settings module to manage
Fcitx.
 
You can config fcitx through 
"Configue Desktop" - "Locale" - Fcitx now.

%prep
%setup -q -n %{name}

%build
mkdir -pv build
pushd build
%{cmake_kf5} ..
make %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C build

%find_lang %{name} --all-name --with-kde

#%check
#desktop-file-validate %{buildroot}%{_datadir}/applications/kde4/kbd-layout-viewer.desktop

%post
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:
fi

%files -f %{name}.lang
%{_datadir}/kservices5/kcm_fcitx.desktop
%{_libdir}/qt5/plugins/kcm_fcitx.so
%{_sysconfdir}/xdg/fcitx-skin.knsrc


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.4.3-7
- Rebuild for new 4.0 release

