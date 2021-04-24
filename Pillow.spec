#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pillow
Version  : 8.2.0
Release  : 74
URL      : https://files.pythonhosted.org/packages/21/23/af6bac2a601be6670064a817273d4190b79df6f74d8012926a39bc7aa77f/Pillow-8.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/23/af6bac2a601be6670064a817273d4190b79df6f74d8012926a39bc7aa77f/Pillow-8.2.0.tar.gz
Summary  : Python Imaging Library (Fork)
Group    : Development/Tools
License  : HPND MIT-CMU NTP
Requires: Pillow-license = %{version}-%{release}
Requires: Pillow-python = %{version}-%{release}
Requires: Pillow-python3 = %{version}-%{release}
Requires: black
Requires: check-manifest
Requires: olefile
Requires: packaging
Requires: pyroma
BuildRequires : black
BuildRequires : buildreq-distutils3
BuildRequires : check-manifest
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : olefile
BuildRequires : packaging
BuildRequires : pkgconfig(zlib)
BuildRequires : pyroma
BuildRequires : zlib-dev
Patch1: Fix-build-libdir.patch

%description
Raqm
====
[![Linux & macOS build](https://travis-ci.org/HOST-Oman/libraqm.svg?branch=master)](https://travis-ci.org/HOST-Oman/libraqm)
[![Windows build](https://img.shields.io/appveyor/ci/HOSTOman/libraqm/master.svg)](https://ci.appveyor.com/project/HOSTOman/libraqm)

%package license
Summary: license components for the Pillow package.
Group: Default

%description license
license components for the Pillow package.


%package python
Summary: python components for the Pillow package.
Group: Default
Requires: Pillow-python3 = %{version}-%{release}
Provides: pillow-python

%description python
python components for the Pillow package.


%package python3
Summary: python3 components for the Pillow package.
Group: Default
Requires: python3-core
Provides: pypi(pillow)

%description python3
python3 components for the Pillow package.


%prep
%setup -q -n Pillow-8.2.0
cd %{_builddir}/Pillow-8.2.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617378602
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Pillow
cp %{_builddir}/Pillow-8.2.0/LICENSE %{buildroot}/usr/share/package-licenses/Pillow/efa73e04a33de84f89c1f957fa8dd8adbddd5949
cp %{_builddir}/Pillow-8.2.0/Tests/icc/LICENSE.txt %{buildroot}/usr/share/package-licenses/Pillow/371117588643c602bb8f15b280424e938c34c369
cp %{_builddir}/Pillow-8.2.0/docs/COPYING %{buildroot}/usr/share/package-licenses/Pillow/edd04741ed099f904917132d92f686c5e4a90095
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Pillow/371117588643c602bb8f15b280424e938c34c369
/usr/share/package-licenses/Pillow/edd04741ed099f904917132d92f686c5e4a90095
/usr/share/package-licenses/Pillow/efa73e04a33de84f89c1f957fa8dd8adbddd5949

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
