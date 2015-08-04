
Name:    oxygen-gtk2
Summary: Oxygen GTK+2 theme
Version: 1.4.6
Release: 3

License: LGPLv2+
Group:   User Interface/Desktops
URL:     https://projects.kde.org/projects/playground/artwork/oxygen-gtk
Source0: http://download.kde.org/stable/oxygen-gtk2/%{version}/src/%{name}-%{version}.tar.bz2

## upstream patches

BuildRequires: cmake
BuildRequires: gtk2-devel

%description
Oxygen-Gtk is a port of the default KDE widget theme (Oxygen), to gtk.

It's primary goal is to ensure visual consistency between gtk-based and
qt-based applications running under KDE. A secondary objective is to also
have a stand-alone nice looking gtk theme that would behave well on other
Desktop Environments.

Unlike other attempts made to port the KDE oxygen theme to gtk, this
attempt does not depend on Qt (via some Qt to Gtk conversion engine), 
nor does render the widget appearance via hard-coded pixmaps, which 
otherwise breaks every time some setting is changed in KDE.


%prep
%setup -q



%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} -DOXYGEN_FORCE_KDE_ICONS_AND_FONTS=0  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/oxygen-gtk-demo
%{_libdir}/gtk-2.0/*/engines/liboxygen-gtk.so
%{_datadir}/themes/oxygen-gtk/


%changelog
