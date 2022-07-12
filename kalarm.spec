#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kalarm
Version  : 22.04.3
Release  : 48
URL      : https://download.kde.org/stable/release-service/22.04.3/src/kalarm-22.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.3/src/kalarm-22.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.3/src/kalarm-22.04.3.tar.xz.sig
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
BuildRequires : kalarmcal-dev
BuildRequires : kauth-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcmutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcontacts-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kguiaddons-dev
BuildRequires : kholidays-dev
BuildRequires : ki18n-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kidletime-dev
BuildRequires : kimap-dev
BuildRequires : kio-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kservice-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : mailcommon-dev
BuildRequires : messagelib-dev
BuildRequires : phonon-dev
BuildRequires : pimcommon-dev
BuildRequires : qtx11extras-dev

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
%setup -q -n kalarm-22.04.3
cd %{_builddir}/kalarm-22.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657590876
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657590876
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kalarm
cp %{_builddir}/kalarm-22.04.3/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kalarm/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
cp %{_builddir}/kalarm-22.04.3/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kalarm/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kalarm-22.04.3/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kalarm/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kalarm-22.04.3/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kalarm/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/kalarm-22.04.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kalarm/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kalarm-22.04.3/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kalarm/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang kalarm

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/kalarm_helper

%files bin
%defattr(-,root,root,-)
/usr/bin/kalarm
/usr/bin/kalarmautostart

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kalarm.desktop
/usr/share/config.kcfg/kalarmconfig.kcfg
/usr/share/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
/usr/share/dbus-1/system-services/org.kde.kalarm.rtcwake.service
/usr/share/dbus-1/system.d/org.kde.kalarm.rtcwake.conf
/usr/share/icons/hicolor/128x128/apps/kalarm.png
/usr/share/icons/hicolor/16x16/apps/kalarm.png
/usr/share/icons/hicolor/22x22/apps/kalarm.png
/usr/share/icons/hicolor/32x32/apps/kalarm.png
/usr/share/icons/hicolor/48x48/apps/kalarm.png
/usr/share/icons/hicolor/64x64/apps/kalarm.png
/usr/share/kalarm/icons/oxygen/16x16/actions/document-new-from-template.png
/usr/share/kalarm/icons/oxygen/16x16/actions/new-audio-alarm.png
/usr/share/kalarm/icons/oxygen/16x16/actions/new-command-alarm.png
/usr/share/kalarm/icons/oxygen/22x22/actions/document-new-from-template.png
/usr/share/kalarm/icons/oxygen/22x22/actions/kalarm-disabled.png
/usr/share/kalarm/icons/oxygen/22x22/actions/kalarm-partdisabled.png
/usr/share/kalarm/icons/oxygen/22x22/actions/kalarm.png
/usr/share/kalarm/icons/oxygen/22x22/actions/new-audio-alarm.png
/usr/share/kalarm/icons/oxygen/22x22/actions/new-command-alarm.png
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
/usr/lib64/libkalarmprivate.so.5
/usr/lib64/libkalarmprivate.so.5.20.3

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

