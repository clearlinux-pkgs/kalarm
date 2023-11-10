#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: 250a666
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kalarm
Version  : 23.08.3
Release  : 66
URL      : https://download.kde.org/stable/release-service/23.08.3/src/kalarm-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/kalarm-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/kalarm-23.08.3.tar.xz.sig
Summary  : Personal alarm scheduler
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kalarm-bin = %{version}-%{release}
Requires: kalarm-data = %{version}-%{release}
Requires: kalarm-lib = %{version}-%{release}
Requires: kalarm-license = %{version}-%{release}
Requires: kalarm-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kholidays-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kidletime-dev
BuildRequires : kimap-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : mailcommon-dev
BuildRequires : messagelib-dev
BuildRequires : phonon-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
BuildRequires : qtx11extras-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KAlarm
======
KAlarm is a personal alarm message, audio, command and email scheduler.

%package bin
Summary: bin components for the kalarm package.
Group: Binaries
Requires: kalarm-data = %{version}-%{release}
Requires: kalarm-license = %{version}-%{release}

%description bin
bin components for the kalarm package.


%package data
Summary: data components for the kalarm package.
Group: Data

%description data
data components for the kalarm package.


%package doc
Summary: doc components for the kalarm package.
Group: Documentation

%description doc
doc components for the kalarm package.


%package lib
Summary: lib components for the kalarm package.
Group: Libraries
Requires: kalarm-data = %{version}-%{release}
Requires: kalarm-license = %{version}-%{release}

%description lib
lib components for the kalarm package.


%package license
Summary: license components for the kalarm package.
Group: Default

%description license
license components for the kalarm package.


%package locales
Summary: locales components for the kalarm package.
Group: Default

%description locales
locales components for the kalarm package.


%prep
%setup -q -n kalarm-23.08.3
cd %{_builddir}/kalarm-23.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699589285
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1699589285
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kalarm
cp %{_builddir}/kalarm-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kalarm/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/kalarm-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kalarm/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kalarm-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kalarm/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kalarm-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kalarm/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kalarm-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kalarm/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kalarm-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kalarm/20079e8f79713dce80ab09774505773c926afa2a || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kalarm
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kauth/kalarm_helper
/usr/lib64/libexec/kauth/kalarm_helper

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kalarm
/V3/usr/bin/kalarmautostart
/usr/bin/kalarm
/usr/bin/kalarmautostart

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kalarm.desktop
/usr/share/config.kcfg/kalarmconfig.kcfg
/usr/share/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
/usr/share/dbus-1/system-services/org.kde.kalarm.rtcwake.service
/usr/share/dbus-1/system.d/org.kde.kalarm.rtcwake.conf
/usr/share/icons/breeze-dark/actions/16/show-today.svg
/usr/share/icons/breeze-dark/actions/22/show-today.svg
/usr/share/icons/breeze/actions/16/show-today.svg
/usr/share/icons/breeze/actions/22/show-today.svg
/usr/share/icons/hicolor/128x128/apps/kalarm.png
/usr/share/icons/hicolor/16x16/apps/kalarm.png
/usr/share/icons/hicolor/22x22/apps/kalarm.png
/usr/share/icons/hicolor/32x32/apps/kalarm.png
/usr/share/icons/hicolor/48x48/apps/kalarm.png
/usr/share/icons/hicolor/64x64/apps/kalarm.png
/usr/share/kalarm/icons/oxygen/16x16/actions/document-new-from-template.png
/usr/share/kalarm/icons/oxygen/16x16/actions/new-audio-alarm.png
/usr/share/kalarm/icons/oxygen/16x16/actions/new-command-alarm.png
/usr/share/kalarm/icons/oxygen/16x16/actions/show-today.svg
/usr/share/kalarm/icons/oxygen/22x22/actions/document-new-from-template.png
/usr/share/kalarm/icons/oxygen/22x22/actions/kalarm-disabled.png
/usr/share/kalarm/icons/oxygen/22x22/actions/kalarm-partdisabled.png
/usr/share/kalarm/icons/oxygen/22x22/actions/kalarm.png
/usr/share/kalarm/icons/oxygen/22x22/actions/new-audio-alarm.png
/usr/share/kalarm/icons/oxygen/22x22/actions/new-command-alarm.png
/usr/share/kalarm/icons/oxygen/22x22/actions/show-today.svg
/usr/share/knotifications5/kalarm.notifyrc
/usr/share/kxmlgui5/kalarm/kalarmui.rc
/usr/share/metainfo/org.kde.kalarm.appdata.xml
/usr/share/polkit-1/actions/org.kde.kalarm.rtcwake.policy
/usr/share/qlogging-categories5/kalarm.categories
/usr/share/qlogging-categories5/kalarm.renamecategories
/usr/share/xdg/autostart/kalarm.autostart.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kalarm/alarmmessage.png
/usr/share/doc/HTML/ca/kalarm/editwindow-simple.png
/usr/share/doc/HTML/ca/kalarm/editwindow.png
/usr/share/doc/HTML/ca/kalarm/index.cache.bz2
/usr/share/doc/HTML/ca/kalarm/index.docbook
/usr/share/doc/HTML/ca/kalarm/mainwindow-calendars.png
/usr/share/doc/HTML/ca/kalarm/mainwindow.png
/usr/share/doc/HTML/de/kalarm/index.cache.bz2
/usr/share/doc/HTML/de/kalarm/index.docbook
/usr/share/doc/HTML/en/kalarm/alarmmessage.png
/usr/share/doc/HTML/en/kalarm/editwindow-simple.png
/usr/share/doc/HTML/en/kalarm/editwindow.png
/usr/share/doc/HTML/en/kalarm/index.cache.bz2
/usr/share/doc/HTML/en/kalarm/index.docbook
/usr/share/doc/HTML/en/kalarm/mainwindow-calendars.png
/usr/share/doc/HTML/en/kalarm/mainwindow.png
/usr/share/doc/HTML/en/kalarm/spinbox.png
/usr/share/doc/HTML/es/kalarm/index.cache.bz2
/usr/share/doc/HTML/es/kalarm/index.docbook
/usr/share/doc/HTML/et/kalarm/index.cache.bz2
/usr/share/doc/HTML/et/kalarm/index.docbook
/usr/share/doc/HTML/it/kalarm/index.cache.bz2
/usr/share/doc/HTML/it/kalarm/index.docbook
/usr/share/doc/HTML/nl/kalarm/index.cache.bz2
/usr/share/doc/HTML/nl/kalarm/index.docbook
/usr/share/doc/HTML/pt/kalarm/index.cache.bz2
/usr/share/doc/HTML/pt/kalarm/index.docbook
/usr/share/doc/HTML/pt_BR/kalarm/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kalarm/index.docbook
/usr/share/doc/HTML/ru/kalarm/index.cache.bz2
/usr/share/doc/HTML/ru/kalarm/index.docbook
/usr/share/doc/HTML/sv/kalarm/index.cache.bz2
/usr/share/doc/HTML/sv/kalarm/index.docbook
/usr/share/doc/HTML/uk/kalarm/index.cache.bz2
/usr/share/doc/HTML/uk/kalarm/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkalarmcalendar.so.5.24.3
/V3/usr/lib64/libkalarmplugin.so.5.24.3
/V3/usr/lib64/qt5/plugins/pim5/kalarm/akonadiplugin.so
/usr/lib64/libkalarmcalendar.so.5
/usr/lib64/libkalarmcalendar.so.5.24.3
/usr/lib64/libkalarmplugin.so.5
/usr/lib64/libkalarmplugin.so.5.24.3
/usr/lib64/qt5/plugins/pim5/kalarm/akonadiplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kalarm/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kalarm/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kalarm/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kalarm/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kalarm/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/kalarm/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kalarm.lang
%defattr(-,root,root,-)

