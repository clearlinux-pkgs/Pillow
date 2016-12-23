#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pillow
Version  : 3.4.2
Release  : 28
URL      : http://pypi.debian.net/Pillow/Pillow-3.4.2.tar.gz
Source0  : http://pypi.debian.net/Pillow/Pillow-3.4.2.tar.gz
Summary  : Python Imaging Library (Fork)
Group    : Development/Tools
License  : HPND MIT
Requires: Pillow-bin
Requires: Pillow-python
BuildRequires : Sphinx-python
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pkgconfig(zlib)
BuildRequires : pyflakes-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Pillow
======
Python Imaging Library (Fork)
-----------------------------
Pillow is the friendly PIL fork by `Alex Clark and Contributors <https://github.com/python-pillow/Pillow/graphs/contributors>`_. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

%package bin
Summary: bin components for the Pillow package.
Group: Binaries

%description bin
bin components for the Pillow package.


%package python
Summary: python components for the Pillow package.
Group: Default
Provides: pillow-python
Requires: Sphinx-python
Requires: nose-python
Requires: pep8
Requires: pyflakes-python

%description python
python components for the Pillow package.


%prep
%setup -q -n Pillow-3.4.2

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/createfontdatachunk.py
/usr/bin/enhancer.py
/usr/bin/explode.py
/usr/bin/gifmaker.py
/usr/bin/painter.py
/usr/bin/pilconvert.py
/usr/bin/pildriver.py
/usr/bin/pilfile.py
/usr/bin/pilfont.py
/usr/bin/pilprint.py
/usr/bin/player.py
/usr/bin/thresholder.py
/usr/bin/viewer.py

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
