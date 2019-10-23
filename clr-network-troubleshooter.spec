#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-network-troubleshooter
Version  : v7
Release  : 7
URL      : https://github.com/clearlinux/clr-network-troubleshooter/archive/v7/clr-network-troubleshooter-v7.tar.gz
Source0  : https://github.com/clearlinux/clr-network-troubleshooter/archive/v7/clr-network-troubleshooter-v7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clr-network-troubleshooter-bin = %{version}-%{release}
Requires: clr-network-troubleshooter-license = %{version}-%{release}
Requires: bind-utils
Requires: curl
Requires: iputils
Requires: perl
BuildRequires : bind-utils
BuildRequires : curl
BuildRequires : iputils
BuildRequires : perl

%description
# clr-network-troubleshooter
This is a tool to perform basic networking tests on a Clear Linux system. It attempts to diagnose common issues and provide suggested actions to resolve them.

%package bin
Summary: bin components for the clr-network-troubleshooter package.
Group: Binaries
Requires: clr-network-troubleshooter-license = %{version}-%{release}

%description bin
bin components for the clr-network-troubleshooter package.


%package license
Summary: license components for the clr-network-troubleshooter package.
Group: Default

%description license
license components for the clr-network-troubleshooter package.


%prep
%setup -q -n clr-network-troubleshooter-7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571867990
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1571867990
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-network-troubleshooter
cp %{_builddir}/clr-network-troubleshooter-7/COPYING %{buildroot}/usr/share/package-licenses/clr-network-troubleshooter/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-network-troubleshooter

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-network-troubleshooter/4cc77b90af91e615a64ae04893fdffa7939db84c
