#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pillow
Version  : 8.0.1
Release  : 68
URL      : https://files.pythonhosted.org/packages/2b/06/93bf1626ef36815010e971a5ce90f49919d84ab5d2fa310329f843a74bc1/Pillow-8.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/06/93bf1626ef36815010e971a5ce90f49919d84ab5d2fa310329f843a74bc1/Pillow-8.0.1.tar.gz
Summary  : Python Imaging Library (Fork)
Group    : Development/Tools
License  : Apache-2.0 HPND MIT-CMU NTP
Requires: Pillow-license = %{version}-%{release}
Requires: Pillow-python = %{version}-%{release}
Requires: Pillow-python3 = %{version}-%{release}
Requires: black
Requires: check-manifest
Requires: jarn.viewdoc
Requires: olefile
Requires: pycodestyle
Requires: pyflakes
Requires: pyroma
BuildRequires : black
BuildRequires : buildreq-distutils3
BuildRequires : check-manifest
BuildRequires : freetype-dev
BuildRequires : jarn.viewdoc
BuildRequires : libjpeg-turbo-dev
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : olefile
BuildRequires : pkgconfig(zlib)
BuildRequires : pycodestyle
BuildRequires : pyflakes
BuildRequires : pyroma
BuildRequires : zlib-dev
Patch1: Fix-build-libdir.patch

%description
<p align="center">
<img width="248" height="250" src="https://raw.githubusercontent.com/python-pillow/pillow-logo/master/pillow-logo-248x250.png" alt="Pillow logo">
</p>

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
%setup -q -n Pillow-8.0.1
cd %{_builddir}/Pillow-8.0.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608052258
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
cp %{_builddir}/Pillow-8.0.1/LICENSE %{buildroot}/usr/share/package-licenses/Pillow/8cef48f0b79431f2c757e6e2ef8028c17b631ac8
cp %{_builddir}/Pillow-8.0.1/Tests/fonts/LICENSE.txt %{buildroot}/usr/share/package-licenses/Pillow/0c4b0c1d54897b1d3aaec810e013b177c72b11f0
cp %{_builddir}/Pillow-8.0.1/Tests/icc/LICENSE.txt %{buildroot}/usr/share/package-licenses/Pillow/371117588643c602bb8f15b280424e938c34c369
cp %{_builddir}/Pillow-8.0.1/docs/COPYING %{buildroot}/usr/share/package-licenses/Pillow/44cb32ffb23c44fe8dfe15ca89a457d5fc41c4ea
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Pillow/0c4b0c1d54897b1d3aaec810e013b177c72b11f0
/usr/share/package-licenses/Pillow/371117588643c602bb8f15b280424e938c34c369
/usr/share/package-licenses/Pillow/44cb32ffb23c44fe8dfe15ca89a457d5fc41c4ea
/usr/share/package-licenses/Pillow/8cef48f0b79431f2c757e6e2ef8028c17b631ac8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
