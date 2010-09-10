%define name gkeyfile-sharp
%define version 0.1
%define git 662c5c1
%define release %mkrel 1

Summary: Mono bindings for the GKeyFile library
Name: %{name}
Version: %{version}
Release: %{release}
# http://github.com/mono/gkeyfile-sharp/tarball/GKEYFILE_SHARP_0_1
Source0: %{name}-%{version}.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: http://gitorious.org/gkeyfile-sharp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-devel
BuildRequires: glib2-devel
BuildRequires: glib-sharp2 >= 2.12.9
BuildRequires: gtk-sharp2-devel
Requires: glib2
#gw filter out deps from *.dll.config
%define _requires_exceptions ^lib.*0$

%description
This is a Mono binding for the GKeyFile library.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/Other

%description devel
This is a Mono binding for the GKeyFile library.

%prep
%setup -q -n mono-%name-%git
./autogen.sh

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
%make

%install
rm -rf %{buildroot}
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS
%_prefix/lib/mono/%name
%_prefix/lib/mono/gac/%name

%files devel
%defattr(-,root,root)
%_datadir/pkgconfig/%name.pc
