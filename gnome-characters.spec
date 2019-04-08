#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-characters
Version  : 3.32.1
Release  : 23
URL      : https://download.gnome.org/sources/gnome-characters/3.32/gnome-characters-3.32.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-characters/3.32/gnome-characters-3.32.1.tar.xz
Summary  : A character map application
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+
Requires: gnome-characters-bin = %{version}-%{release}
Requires: gnome-characters-data = %{version}-%{release}
Requires: gnome-characters-lib = %{version}-%{release}
Requires: gnome-characters-license = %{version}-%{release}
Requires: gnome-characters-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gjs-dev
BuildRequires : libunistring-dev

%description
Characters is a simple utility application to find and insert unusual
characters.

%package bin
Summary: bin components for the gnome-characters package.
Group: Binaries
Requires: gnome-characters-data = %{version}-%{release}
Requires: gnome-characters-license = %{version}-%{release}

%description bin
bin components for the gnome-characters package.


%package data
Summary: data components for the gnome-characters package.
Group: Data

%description data
data components for the gnome-characters package.


%package lib
Summary: lib components for the gnome-characters package.
Group: Libraries
Requires: gnome-characters-data = %{version}-%{release}
Requires: gnome-characters-license = %{version}-%{release}

%description lib
lib components for the gnome-characters package.


%package license
Summary: license components for the gnome-characters package.
Group: Default

%description license
license components for the gnome-characters package.


%package locales
Summary: locales components for the gnome-characters package.
Group: Default

%description locales
locales components for the gnome-characters package.


%prep
%setup -q -n gnome-characters-3.32.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554734105
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-characters
cp COPYING %{buildroot}/usr/share/package-licenses/gnome-characters/COPYING
cp COPYINGv2 %{buildroot}/usr/share/package-licenses/gnome-characters/COPYINGv2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang org.gnome.Characters

%files
%defattr(-,root,root,-)
/usr/lib64/org.gnome.Characters/girepository-1.0/Gc-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-characters

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Characters.desktop
/usr/share/dbus-1/services/org.gnome.Characters.BackgroundService.service
/usr/share/dbus-1/services/org.gnome.Characters.service
/usr/share/glib-2.0/schemas/org.gnome.Characters.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Characters.search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Characters.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Characters-symbolic.svg
/usr/share/metainfo/org.gnome.Characters.appdata.xml
/usr/share/org.gnome.Characters/gir-1.0/Gc-1.0.gir
/usr/share/org.gnome.Characters/org.gnome.Characters
/usr/share/org.gnome.Characters/org.gnome.Characters.BackgroundService
/usr/share/org.gnome.Characters/org.gnome.Characters.BackgroundService.data.gresource
/usr/share/org.gnome.Characters/org.gnome.Characters.BackgroundService.src.gresource
/usr/share/org.gnome.Characters/org.gnome.Characters.data.gresource
/usr/share/org.gnome.Characters/org.gnome.Characters.src.gresource

%files lib
%defattr(-,root,root,-)
/usr/lib64/org.gnome.Characters/libgc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-characters/COPYING
/usr/share/package-licenses/gnome-characters/COPYINGv2

%files locales -f org.gnome.Characters.lang
%defattr(-,root,root,-)

