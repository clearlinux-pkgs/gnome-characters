#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-characters
Version  : 45.0
Release  : 40
URL      : https://download.gnome.org/sources/gnome-characters/45/gnome-characters-45.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-characters/45/gnome-characters-45.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+
Requires: gnome-characters-bin = %{version}-%{release}
Requires: gnome-characters-data = %{version}-%{release}
Requires: gnome-characters-lib = %{version}-%{release}
Requires: gnome-characters-license = %{version}-%{release}
Requires: gnome-characters-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gjs-dev
BuildRequires : libunistring-dev
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : xvfb-run
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n gnome-characters-45.0
cd %{_builddir}/gnome-characters-45.0
pushd ..
cp -a gnome-characters-45.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695679902
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-characters
cp %{_builddir}/gnome-characters-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-characters/915beadc8cf04bf13ad0e1768e9d593f0c3e83a7 || :
cp %{_builddir}/gnome-characters-%{version}/COPYINGv2 %{buildroot}/usr/share/package-licenses/gnome-characters/4cc77b90af91e615a64ae04893fdffa7939db84c || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang org.gnome.Characters
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/org.gnome.Characters/girepository-1.0/Gc-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-characters

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Characters.desktop
/usr/share/dbus-1/services/org.gnome.Characters.service
/usr/share/glib-2.0/schemas/org.gnome.Characters.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Characters.search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Characters.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Characters-symbolic.svg
/usr/share/metainfo/org.gnome.Characters.appdata.xml
/usr/share/org.gnome.Characters/gir-1.0/Gc-1.0.gir
/usr/share/org.gnome.Characters/org.gnome.Characters
/usr/share/org.gnome.Characters/org.gnome.Characters.data.gresource
/usr/share/org.gnome.Characters/org.gnome.Characters.src.gresource

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/org.gnome.Characters/libgc.so
/usr/lib64/org.gnome.Characters/libgc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-characters/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnome-characters/915beadc8cf04bf13ad0e1768e9d593f0c3e83a7

%files locales -f org.gnome.Characters.lang
%defattr(-,root,root,-)

