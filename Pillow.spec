#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pillow
Version  : 5.1.0
Release  : 55
URL      : https://pypi.python.org/packages/89/b8/2f49bf71cbd0e9485bb36f72d438421b69b7356180695ae10bd4fd3066f5/Pillow-5.1.0.tar.gz
Source0  : https://pypi.python.org/packages/89/b8/2f49bf71cbd0e9485bb36f72d438421b69b7356180695ae10bd4fd3066f5/Pillow-5.1.0.tar.gz
Summary  : Python Imaging Library (Fork)
Group    : Development/Tools
License  : NTP OFL-1.1
Requires: Pillow-python3
Requires: Pillow-python
Requires: Babel
Requires: MarkupSafe
Requires: Pygments
Requires: alabaster
Requires: cov-core
Requires: olefile
Requires: pycodestyle
Requires: pyflakes
Requires: pytz
Requires: requests
Requires: six
Requires: snowballstemmer
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(zlib)

BuildRequires : python3-dev
BuildRequires : setuptools

%description
======
        
        Python Imaging Library (Fork)
        -----------------------------

%package python
Summary: python components for the Pillow package.
Group: Default
Requires: Pillow-python3
Provides: pillow-python

%description python
python components for the Pillow package.


%package python3
Summary: python3 components for the Pillow package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Pillow package.


%prep
%setup -q -n Pillow-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528565173
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
