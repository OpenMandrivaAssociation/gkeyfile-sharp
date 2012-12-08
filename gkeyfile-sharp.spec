%define git 662c5c1

Summary:	Mono bindings for the GKeyFile library
Name:		gkeyfile-sharp
Version:	0.1
Release:	6
# http://github.com/mono/gkeyfile-sharp/tarball/GKEYFILE_SHARP_0_1
Source0:	%{name}-%{version}.tar.gz
Patch0:		gkeyfile-sharp-0.1-fix-dllimports.patch
License:	LGPLv2+
Group:		System/Libraries
Url:		http://github.com/mono/gkeyfile-sharp

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	mono-devel
BuildRequires:	glib-sharp2 >= 2.12.9
BuildRequires:	gtk-sharp2-devel
Requires:	glib2
BuildArch:	noarch

%description
This is a Mono binding for the GKeyFile library.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Group:		Development/Other

%description devel
This is a Mono binding for the GKeyFile library.

%prep
%setup -q -n mono-%{name}-%{git}
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

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdv2011.0
+ Revision: 664847
- mass rebuild

* Sun Jan 16 2011 Götz Waschk <waschk@mandriva.org> 0.1-2
+ Revision: 631143
- fix dll import statements
- update URL

* Fri Sep 10 2010 Götz Waschk <waschk@mandriva.org> 0.1-1mdv2011.0
+ Revision: 577097
- switch to 0.1 release tarball
- update file list

* Mon Aug 30 2010 Götz Waschk <waschk@mandriva.org> 0.1-0.20100818.1mdv2011.0
+ Revision: 574372
- import gkeyfile-sharp

