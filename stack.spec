#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x575159689BEFB442 (dev@fpcomplete.com)
#
Name     : stack
Version  : 1.9.1
Release  : 9
URL      : https://github.com/commercialhaskell/stack/releases/download/v1.9.1/stack-1.9.1-linux-x86_64.tar.gz
Source0  : https://github.com/commercialhaskell/stack/releases/download/v1.9.1/stack-1.9.1-linux-x86_64.tar.gz
Source99 : https://github.com/commercialhaskell/stack/releases/download/v1.9.1/stack-1.9.1-linux-x86_64.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: stack-bin = %{version}-%{release}
Requires: stack-license = %{version}-%{release}
Patch1: 0001-Add-Makefile-with-install-target.patch

%description
## The Haskell Tool Stack
[![Build Status](https://travis-ci.org/commercialhaskell/stack.svg?branch=master)](https://travis-ci.org/commercialhaskell/stack)
[![Windows build status](https://ci.appveyor.com/api/projects/status/c1c7uvmw6x1dupcl?svg=true)](https://ci.appveyor.com/project/snoyberg/stack)
[![Release](https://img.shields.io/github/release/commercialhaskell/stack.svg)](https://github.com/commercialhaskell/stack/releases)
[![Join the chat at https://gitter.im/commercialhaskell/stack](https://badges.gitter.im/commercialhaskell/stack.svg)](https://gitter.im/commercialhaskell/stack?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package bin
Summary: bin components for the stack package.
Group: Binaries
Requires: stack-license = %{version}-%{release}

%description bin
bin components for the stack package.


%package license
Summary: license components for the stack package.
Group: Default

%description license
license components for the stack package.


%prep
%setup -q -n stack-1.9.1-linux-x86_64
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542082494
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1542082494
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stack
cp LICENSE %{buildroot}/usr/share/package-licenses/stack/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stack

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/stack/LICENSE
