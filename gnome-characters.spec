#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-characters
Version  : 3.26.2
Release  : 12
URL      : https://download.gnome.org/sources/gnome-characters/3.26/gnome-characters-3.26.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-characters/3.26/gnome-characters-3.26.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+
Requires: gnome-characters-bin
Requires: gnome-characters-lib
Requires: gnome-characters-data
Requires: gnome-characters-locales
BuildRequires : gettext
BuildRequires : gjs-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangoft2)

%description
Characters is a simple utility application to find and insert unusual
characters.

%package bin
Summary: bin components for the gnome-characters package.
Group: Binaries
Requires: gnome-characters-data

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
Requires: gnome-characters-data

%description lib
lib components for the gnome-characters package.


%package locales
Summary: locales components for the gnome-characters package.
Group: Default

%description locales
locales components for the gnome-characters package.


%prep
%setup -q -n gnome-characters-3.26.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509981440
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1509981440
rm -rf %{buildroot}
%make_install
%find_lang org.gnome.Characters

%files
%defattr(-,root,root,-)
/usr/lib64/org.gnome.Characters/girepository-1.0/Gc-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-characters

%files data
%defattr(-,root,root,-)
/usr/share/appdata/org.gnome.Characters.appdata.xml
/usr/share/applications/org.gnome.Characters.desktop
/usr/share/dbus-1/services/org.gnome.Characters.BackgroundService.service
/usr/share/dbus-1/services/org.gnome.Characters.service
/usr/share/glib-2.0/schemas/org.gnome.Characters.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Characters.search-provider.ini
/usr/share/icons/hicolor/16x16/apps/gnome-characters.png
/usr/share/icons/hicolor/22x22/apps/gnome-characters.png
/usr/share/icons/hicolor/256x256/apps/gnome-characters.png
/usr/share/icons/hicolor/32x32/apps/gnome-characters.png
/usr/share/icons/hicolor/48x48/apps/gnome-characters.png
/usr/share/icons/hicolor/symbolic/apps/gnome-characters-symbolic.svg
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

%files locales -f org.gnome.Characters.lang
%defattr(-,root,root,-)

