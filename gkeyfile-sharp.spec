%define git 662c5c1

Summary:	Mono bindings for the GKeyFile library
Name:		gkeyfile-sharp
Version:	0.1
Release:	6
License:	LGPLv2+
Group:		System/Libraries
Url:		http://github.com/mono/gkeyfile-sharp
# http://github.com/mono/gkeyfile-sharp/tarball/GKEYFILE_SHARP_0_1
Source0:	%{name}-%{version}.tar.gz
Patch0:		gkeyfile-sharp-0.1-fix-dllimports.patch
BuildArch:	noarch

BuildRequires:	pkgconfig(gapi-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glib-sharp-2.0)
BuildRequires:	pkgconfig(mono)
Requires:	glib2

%description
This is a Mono binding for the GKeyFile library.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Group:		Development/Other

%description devel
This is a Mono binding for the GKeyFile library.

%prep
%setup -qn mono-%{name}-%{git}
%apply_patches
./autogen.sh

%build
./configure --prefix=%{_prefix} --libdir=%{_prefix}/lib
%make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc AUTHORS
%{_prefix}/lib/mono/%{name}
%{_prefix}/lib/mono/gac/%{name}

%files devel
%{_datadir}/pkgconfig/%{name}.pc

