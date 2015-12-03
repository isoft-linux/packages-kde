%define buildall 0
%define omit_plasma5_bits 1

Name:    kde-l10n
Summary: Internationalization support for KDE
Version: 15.11.80
Release: 5 

Url:     http://www.kde.org
License: LGPLv2
BuildArch: noarch

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#Source1: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-de-%{version}.tar.xz
#Source2: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-en_GB-%{version}.tar.xz
#Source3: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-es-%{version}.tar.xz
#Source4: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-el-%{version}.tar.xz
#Source5: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-fr-%{version}.tar.xz
Source6: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-ja-%{version}.tar.xz
Source7: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-ko-%{version}.tar.xz
#Source8: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-ru-%{version}.tar.xz
Source9: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-zh_CN-%{version}.tar.xz
Source10: http://download.kde.org/%{stable}/applications/%{version}/src/kde-l10n/%{name}-zh_TW-%{version}.tar.xz

#ksnapshot removed from applications 15.11.80
#and a new screenshot utility named spectacle introduced.
#But we still use ksnapshot now.
Source20: ksnapshot.po.ja 
Source21: ksnapshot.po.ko 
Source22: ksnapshot.po.zh_CN 
Source23: ksnapshot.po.zh_TW
Source24: libksane.po.zh_CN 
Source25: skanlite.po.zh_CN 
Source26: konsole.po.zh_CN
Source27: ark.po.zh_CN 

Source1000: subdirs-kde-l10n

BuildRequires: cmake
BuildRequires: findutils
BuildRequires: gettext
# kde4 bits
BuildRequires: kdelibs-devel >= 4.14.4
# for kde4 rpm macros
BuildRequires: kde-filesystem
# kf5 bits
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel
# not sure why this is needed -- rex
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel

Requires: kde-filesystem

%description
Internationalization support for KDE.

%package de
Summary: German language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-German = %{version}-%{release}
Obsoletes: %{name}-German < 4.14.3-2
%description de
%{summary}.

%package el
Summary: Greek language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-Greek = %{version}-%{release}
Obsoletes: %{name}-Greek < 4.14.3-2
%description el
%{summary}.

%package en_GB
Summary: British English support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-British = %{version}-%{release}
Obsoletes: %{name}-British < 4.14.3-2
%description en_GB
%{summary}.

%package es
Summary: Spanish language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-Spanish = %{version}-%{release}
Obsoletes: %{name}-Spanish < 4.14.3-2
%description es
%{summary}.

%package fr
Summary: French language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-French = %{version}-%{release}
Obsoletes: %{name}-French < 4.14.3-2
%description fr
%{summary}.

%package ja
Summary: Japanese language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-Japanese = %{version}-%{release}
Obsoletes: %{name}-Japanese < 4.14.3-2
%description ja
%{summary}.

%package ko
Summary: Korean language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-Korean = %{version}-%{release}
Obsoletes: %{name}-Korean < 4.14.3-2
%description ko
%{summary}.

%package ru
Summary: Russian language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-Russian = %{version}-%{release}
Obsoletes: %{name}-Russian < 4.14.3-2
%description ru
%{summary}.

%package zh_CN
Summary: Chinese (Simplified Chinese) language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-Chinese = %{version}-%{release}
Obsoletes: %{name}-Chinese < 4.14.3-2
%description zh_CN
%{summary}.

%package zh_TW
Summary: Chinese (Traditional) language support for KDE
Requires: %{name} = %{version}-%{release}
Provides: %{name}-Chinese-Traditional = %{version}-%{release}
Obsoletes: %{name}-Chinese-Traditional < 4.14.3-2
%description zh_TW
%{summary}.


%prep
%setup -T -q -n %{name}-%{version} -c

for i in $(cat %{SOURCE1000}) ; do
  echo $i | grep -v '^#' && \
  %{__xz} --decompress --stdout %{_sourcedir}/%{name}-$i-%{version}.tar.xz | %{__tar} -xf -
done

#restore ksnapshot
cp %{SOURCE20} %{name}-ja-%{version}/4/ja/messages/kdegraphics/ksnapshot.po
cp %{SOURCE21} %{name}-ko-%{version}/4/ko/messages/kdegraphics/ksnapshot.po
cp %{SOURCE22} %{name}-zh_CN-%{version}/4/zh_CN/messages/kdegraphics/ksnapshot.po
cp %{SOURCE23} %{name}-zh_TW-%{version}/4/zh_TW/messages/kdegraphics/ksnapshot.po
cp %{SOURCE24} %{name}-zh_CN-%{version}/5/zh_CN/messages/kdegraphics/libksane.po
cp %{SOURCE25} %{name}-zh_CN-%{version}/5/zh_CN/messages/kdegraphics/skanlite.po
cp %{SOURCE26} %{name}-zh_CN-%{version}/5/zh_CN/messages/applications/konsole.po
cp %{SOURCE27} %{name}-zh_CN-%{version}/5/zh_CN/messages/kdeutils/ark.po



%build
for i in $(cat %{SOURCE1000}) ; do
  if [ -d "%{name}-$i-%{version}" ]; then
  pushd %{name}-$i-%{version}
  for j in . *@* ; do
    if [ -d $j ] ; then
      # skip kdewebdev for now, because we're still shipping kdewebdev 3 due to Quanta
      sed -i -e 's/add_subdirectory( *kdewebdev *)/#add_subdirectory(kdewebdev)/g' 4/$i/$j/messages/CMakeLists.txt
      if [ -e 4/$i/$j/docs/CMakeLists.txt ] ; then
        sed -i -e 's/add_subdirectory( *kdewebdev *)/#add_subdirectory(kdewebdev)/g' 4/$i/$j/docs/CMakeLists.txt
      fi
      # remove lilo-config, conflicts with 3.5.10
      rm -fv 4/$i/$j/messages/kdeadmin/kcmlilo.po
      if [ -e 4/$i/$j/docs/kdeadmin/CMakeLists.txt ] ; then
        sed -i -e 's/add_subdirectory( *lilo-config *)/#add_subdirectory(lilo-config)/g' 4/$i/$j/docs/kdeadmin/CMakeLists.txt
      fi
      # remove bogus duplicated kdepim stuff from kdenetwork
      if [ -e 4/$i/$j/docs/kdenetwork/CMakeLists.txt ] ; then
        sed -i -e 's/add_subdirectory( *korn *)/#add_subdirectory(korn)/g' -e 's/add_subdirectory( *kmail *)/#add_subdirectory(kmail)/g' -e 's/add_subdirectory( *knode *)/#add_subdirectory(knode)/g' 4/$i/$j/docs/kdenetwork/CMakeLists.txt
      fi
      # some languages still ship the kpilot stuff
      # zap it so the kpilot package can ship all translations itself
      rm -fv 4/$i/$j/messages/kdepim/kpilot.po
      if [ -e 4/$i/$j/docs/kdepim/CMakeLists.txt ] ; then
        sed -i -e 's/add_subdirectory( *kpilot *)/#add_subdirectory(kpilot)/g' 4/$i/$j/docs/kdepim/CMakeLists.txt
      fi

%if 0%{?omit_plasma5_bits}
      # Remove translations shipped by Plasma 5 and KDE Frameworks 5
      # Each Plasma 5 and KF5 app/library ship their own translations in their tarballs, so they
      # often conflict with kde-l10n, since most of the catalogs still have the same name

      # Provided by plasma-workspace and plasma-desktop
      sed -i -e 's/add_subdirectory( *kde-workspace *)/#add_subdirectory(kde-workspace)/g' 4/$i/$j/messages/CMakeLists.txt
      if [ -e 4/$i/$j/docs/CMakeLists.txt ]; then
        sed -i -e 's/add_subdirectory( *kde-workspace *)/#add_subdirectory(kde-workspace)/g' 4/$i/$j/docs/CMakeLists.txt
      fi
      rm -fv 4/$i/$j/messages/kde-runtime/{attica_kde,knetattach,drkonqi,phonon_kde,soliduiserver}.po
      rm -fv 4/$i/$j/messages/kde-runtime/kcm{_emoticons,_phonon,componentchooser,icons,kded,notify}.po
      rm -fv 4/$i/$j/messages/kde-runtime/kio_{applications,remote}.po
      rm -fv 4/$i/$j/messages/kdelibs/{kcm_baloofile,plasma_runner_baloosearchrunner}.po
      rm -fv 4/$i/$j/messages/kdelibs/{kio_baloosearch,baloo_file_extractor,baloo_file,kio_tags,kio_timeline,balooshow,baloosearch}.po
      rm -fv 4/$i/$j/messages/applications/useraccount.po
      if [ -e 4/$i/$j/docs/kde-runtime/CMakeLists.txt ]; then
        sed -i -e 's/add_subdirectory( *kcontrol *)/#add_subdirectory(kcontrol)/g' 4/$i/$j/docs/kde-runtime/CMakeLists.txt
        sed -i -e 's/add_subdirectory( *kdesu *)/#add_subdirectory(kdesu)/g' 4/$i/$j/docs/kde-runtime/CMakeLists.txt
        sed -i -e 's/add_subdirectory( *khelpcenter *)/#add_subdirectory(khelpcenter)/g' 4/$i/$j/docs/kde-runtime/CMakeLists.txt
        sed -i -e 's/add_subdirectory( *knetattach *)/#add_subdirectory(knetattach)/g' 4/$i/$j/docs/kde-runtime/CMakeLists.txt
      fi
      # Provided by kdeplasma-addons
      sed -i -e 's/add_subdirectory( *kdeplasma-addons *)/#add_subdirectory(kdeplasma-addons)/g' 4/$i/$j/messages/CMakeLists.txt
      # Provided by kf5-kfilemetada
      rm -fv 4/$i/$j/messages/kdelibs/kfilemetadata.po
      # Provided by kcmlocale 
      rm -fv 4/$i/$j/messages/kde-runtime/kcmlocale.po
      # Provided by kde-cli-tools
      rm -fv 4/$i/$j/messages/kde-runtime/{filetypes,kcmshell,kdesu,kioclient,kmimetypefinder,kstart,ktraderclient}.po
      # Provided by khelpcenter
      rm -fv 4/$i/$j/messages/kde-runtime/{htmlsearch,kcmhtmlsearch,khelpcenter}.po
      # Provided by ktp-desktop-applets
      rm -fv 4/$i/$j/messages/kdenetwork/plasma_applet_org.kde.ktp-{contact,presence}.po
%endif

    fi
  done
  mkdir %{_target_platform}
  pushd %{_target_platform}
  %{cmake_kde4} -DKDE_INSTALL_DATADIR:PATH=%{_kf5_datadir} ..
  popd
  make %{?_smp_mflags} -C %{_target_platform}
  popd
  fi
done


%install
for i in $(cat %{SOURCE1000}) ; do
  if [ -d %{name}-$i-%{version}/%{_target_platform} ]; then
  make install/fast DESTDIR=%{buildroot} -C %{name}-$i-%{version}/%{_target_platform}
  fi
done

# (hard)link kdeedu-data content for both kde4/kf5 locations
if [ -d  %{buildroot}%{_kde4_appsdir}/kvtml ]; then
for i in %{buildroot}%{_kde4_appsdir}/kvtml/* ; do
  j=$(basename $i)
  mkdir -p %{buildroot}%{_kf5_datadir}/apps/kvtml/${j}
  cp -alf  %{buildroot}%{_kde4_appsdir}/kvtml/${j}/* \
           %{buildroot}%{_kf5_datadir}/apps/kvtml/${j}/ ||:
done
fi
if [ -d  %{buildroot}%{_kf5_datadir}/apps/kvtml ]; then
for i in %{buildroot}%{_kf5_datadir}/apps/kvtml/* ; do
  j=$(basename $i)
  mkdir -p  %{buildroot}%{_kde4_appsdir}/kvtml/${j}
    cp -alf %{buildroot}%{_kf5_datadir}/apps/kvtml/${j}/* \
            %{buildroot}%{_kde4_appsdir}/kvtml/${j}/ ||:
done
fi
if [ -d  %{buildroot}%{_kde4_appsdir}/khangman ]; then
mkdir -p %{buildroot}%{_kf5_datadir}/khangman
cp -alf  %{buildroot}%{_kde4_appsdir}/khangman/* \
         %{buildroot}%{_kf5_datadir}/khangman/ ||:
fi
if [ -d  %{buildroot}%{_kf5_datadir}/khangman ]; then
mkdir -p %{buildroot}%{_kde4_appsdir}/khangman
cp -alf %{buildroot}%{_kf5_datadir}/khangman/* \
        %{buildroot}%{_kde4_appsdir}/khangman/ ||:
fi

## unpackaged files
# get rid of flags (which should be included in kde-runtime-flags?), currently:
# kde-l10n-km-4.5.1/messages/flag.png
# kde-l10n-th-4.5.1/messages/flag.png
# kde-l10n-zh_CN-4.5.1/messages/flag.png
# (get this fixed upstream) -- Rex
rm -rfv  %{buildroot}%{_datadir}/locale/*/flag.png
# -tr includes some script, pretty sure it's a translator's tool
# not intended to be installed
rm -fv %{buildroot}%{_datadir}/locale/tr/ceviri_uygula.sh
# conflicts with kf5-ki18n
rm -rfv %{buildroot}%{_datadir}/locale/*/LC_SCRIPTS/ki18n5/


%files
# empty

#%files de
#%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
#%lang(de) %{_datadir}/locale/de/LC_SCRIPTS/
#%lang(de) %{_datadir}/locale/de/entry.desktop
#%lang(de) %{_kde4_appsdir}/autocorrect/de_DE.xml
#%lang(de) %{_kde4_appsdir}/kajongg/voices/de/
#%lang(de) %{_kf5_datadir}/klettres/de/
#%lang(de) %{_kde4_appsdir}/ktuberling/sounds/de*
#%lang(de) %{_kde4_appsdir}/khangman/de.txt
#%lang(de) %{_kf5_datadir}/khangman/de.txt
#%lang(de) %{_kde4_appsdir}/kvtml/de/
#%lang(de) %{_kf5_datadir}/apps/kvtml/de/
#%lang(de) %{_kde4_appsdir}/step/objinfo/l10n/de/
#%lang(de) %{_kde4_docdir}/HTML/de/*
#%lang(de) %{_mandir}/de/*/*
#
#%files el
#%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*
#%lang(el) %{_datadir}/locale/el/entry.desktop
#%lang(el) %{_kde4_appsdir}/ktuberling/sounds/el*
#%lang(el) %{_kde4_appsdir}/kvtml/el
#%lang(el) %{_kf5_datadir}/apps/kvtml/el
#%lang(el) %{_kde4_docdir}/HTML/el/*
#%lang(el) %{_mandir}/el/*/*
#
#%files en_GB
#%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/*
#%lang(en_GB) %{_datadir}/locale/en_GB/entry.desktop
#%lang(en_GB) %{_kf5_datadir}/klettres/en_GB/
#%lang(en_GB) %{_kde4_appsdir}/kvtml/en_GB/
#%lang(en_GB) %{_kf5_datadir}/apps/kvtml/en_GB/
#%lang(en_GB) %{_kde4_docdir}/HTML/en_GB/*
#%lang(en_GB) %{_kf5_datadir}/katepart/syntax/logohighlightstyle.en_GB.xml
#%lang(en_GB) %{_kf5_datadir}/kturtle/data/logokeywords.en_GB.xml
#%lang(en_GB) %{_kf5_datadir}/kturtle/examples/en_GB/
#
#%files es
#%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
#%lang(es) %{_datadir}/locale/es/entry.desktop
#%lang(es) %{_kde4_appsdir}/autocorrect/es.xml
#%lang(es) %{_kde4_appsdir}/ktuberling/sounds/es*
#%lang(es) %{_kde4_appsdir}/khangman/es.txt
#%lang(es) %{_kf5_datadir}/khangman/es.txt
#%lang(es) %{_kf5_datadir}/klettres/es/
#%lang(es) %{_kde4_appsdir}/kvtml/es/
#%lang(es) %{_kf5_datadir}/apps/kvtml/es/
#%lang(es) %{_kde4_docdir}/HTML/es/*
#%lang(es) %{_mandir}/es/*/*
#
#%files fr
#%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
#%lang(fr) %{_datadir}/locale/fr/LC_SCRIPTS/
#%lang(fr) %{_datadir}/locale/fr/entry.desktop
#%lang(fr) %{_kde4_appsdir}/autocorrect/fr.xml
#%lang(fr) %{_kde4_appsdir}/khangman/fr.txt
#%lang(fr) %{_kf5_datadir}/khangman/fr.txt
#%lang(fr) %{_kde4_appsdir}/ktuberling/sounds/fr*
#%lang(fr) %{_kde4_appsdir}/kvtml/fr/
#%lang(fr) %{_kf5_datadir}/apps/kvtml/fr/
#%lang(fr) %{_kde4_docdir}/HTML/fr/*
#%lang(fr) %{_mandir}/fr/*/*

%files ja
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/*
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/
%lang(ja) %{_datadir}/locale/ja/entry.desktop
%lang(ja) %{_kde4_docdir}/HTML/ja/*

%files ko
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/*
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/
%lang(ko) %{_datadir}/locale/ko/entry.desktop
%lang(ko) %{_kde4_docdir}/HTML/ko/*

#%files ru
#%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*
#%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/
#%lang(ru) %{_datadir}/locale/ru/entry.desktop
#%lang(ru) %{_kde4_appsdir}/autocorrect/ru_RU.xml
#%lang(ru) %{_kde4_appsdir}/kvtml/ru/
#%lang(ru) %{_kf5_datadir}/apps/kvtml/ru/
#%lang(ru) %{_kf5_datadir}/klettres/ru/
#%lang(ru) %{_kde4_appsdir}/ktuberling/sounds/ru*
#%lang(ru) %{_kde4_docdir}/HTML/ru/*
#%lang(ru) %{_kf5_datadir}/katepart/syntax/logohighlightstyle.ru.xml
##lang(ru) %{_kde4_appsdir}/kturtle/data/logokeywords.ru.xml
##lang(ru) %{_kde4_appsdir}/kturtle/examples/ru/*.logo
#%lang(ru) %{_mandir}/ru/*/*

%files zh_CN
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_SCRIPTS/
%lang(zh_CN) %{_datadir}/locale/zh_CN/charset
%lang(zh_CN) %{_datadir}/locale/zh_CN/entry.desktop
%lang(zh_CN) %{_kde4_appsdir}/kvtml/zh_CN/
%lang(zh_CN) %{_kf5_datadir}/apps/kvtml/zh_CN/
%lang(zh_CN) %{_kde4_appsdir}/step/objinfo/l10n/zh_CN/
%lang(zh_CN) %{_kde4_docdir}/HTML/zh_CN/*

%files zh_TW
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*
%lang(zh_TW) %{_datadir}/locale/zh_TW/entry.desktop
%lang(zh_TW) %{_kde4_docdir}/HTML/zh_TW/*


%changelog
* Thu Dec 03 2015 <kun.li@i-soft.com.cn> - 15.11.80-5
- add konsole.po ark.po localization 

* Mon Nov 30 2015 <kun.li@i-soft.com.cn> - 15.11.80-3
- rebuilt add libksane.po  skanlite.po localization

* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-5
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

