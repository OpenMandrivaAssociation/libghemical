%define releasedate 20111012

Name:			libghemical
Version:		3.0.0
Release:		1

%define	major		5
%define	libname		%mklibname ghemical %major
%define develname	%mklibname ghemical -d

Summary:	Libraries for the Ghemical chemistry package
Source0:	http://www.bioinformatics.org/ghemical/download/release%{releasedate}/%{name}-%{version}.tar.gz
Patch0:		libghemical-3.0.0-rosa-linkage.patch
URL:		http://www.bioinformatics.org/ghemical/ghemical/index.html
License:	GPLv2+
Group:		Sciences/Chemistry
BuildRequires:	f2c flex
BuildRequires:	SC-devel
BuildRequires:	mopac7-devel
BuildRequires:	openbabel-devel
BuildRequires:	blas-devel
BuildRequires:	lapack-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	intltool

%description
Library and data files for the ghemical computation chemistry package.

%package	data
Summary:	Data files for the ghemical library
Group:		Sciences/Chemistry

%description data
Data files for the ghemical library.

%package -n	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides:	%{name} = %{EVRD}
Requires:	%{name}-data = %{version}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{name} = %{version}
Provides:	ghemical-devel = %{EVRD} 

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%patch0 -p1
#autoreconf
./autogen.sh

%build
%configure2_5x	--enable-mopac7 \
		--enable-mpqc \
		--enable-openbabel

%make
							
%install
%makeinstall_std

%find_lang %{name}

%files data -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.99.1-7mdv2011.0
+ Revision: 609750
- rebuild

* Fri Jan 15 2010 Jérôme Brenier <incubusss@mandriva.org> 2.99.1-6mdv2010.1
+ Revision: 491772
- rebuild

* Fri Jan 15 2010 Jérôme Brenier <incubusss@mandriva.org> 2.99.1-5mdv2010.1
+ Revision: 491572
- rebuild

* Fri Oct 16 2009 Guillaume Bedot <littletux@mandriva.org> 2.99.1-4mdv2010.0
+ Revision: 457836
- rebuild

* Wed Oct 14 2009 Guillaume Bedot <littletux@mandriva.org> 2.99.1-3mdv2010.0
+ Revision: 457438
- rebuild

* Wed Oct 14 2009 Guillaume Bedot <littletux@mandriva.org> 2.99.1-2mdv2010.0
+ Revision: 457274
- some cleanup

* Tue Sep 15 2009 Guillaume Bedot <littletux@mandriva.org> 2.99.1-1mdv2010.0
+ Revision: 443021
- Added translations, buildrequire intltool
- Fixed license
- Updated %%major
- Release 2.99.1
- dropped merged patch

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 2.98-3mdv2010.0
+ Revision: 438605
- rebuild

* Mon Jan 12 2009 Guillaume Bedot <littletux@mandriva.org> 2.98-2mdv2009.1
+ Revision: 328798
- Rebuild (with libmopac7)

* Mon Aug 11 2008 Emmanuel Andry <eandry@mandriva.org> 2.98-1mdv2009.0
+ Revision: 270741
- br mesaglut?\195-devel
- New version
- changed major
- add p1 from archlinux to fix missing requires
- disable mopac7, breaks build (to fix)

* Sun Jul 06 2008 Funda Wang <fwang@mandriva.org> 2.96-1mdv2009.0
+ Revision: 232059
- add gcc 4.3 patch

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Mar 06 2008 Guillaume Bedot <littletux@mandriva.org> 2.96-1mdv2008.1
+ Revision: 180594
- 2.96

* Tue Feb 12 2008 Adam Williamson <awilliamson@mandriva.org> 2.10-8mdv2008.1
+ Revision: 166395
- need a rebuild for fixed mpqc on 2008 (same issue was already fixed in Cooker); pushing to Cooker too to keep the packages in sync

* Tue Jan 08 2008 Adam Williamson <awilliamson@mandriva.org> 2.10-7mdv2008.1
+ Revision: 146785
- rebuild for fixed sc-config (libSC)

* Sat Jan 05 2008 Adam Williamson <awilliamson@mandriva.org> 2.10-6mdv2008.1
+ Revision: 145793
- new devel policy
- minor spec cleanup

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 30 2007 Lev Givon <lev@mandriva.org> 2.10-4mdv2008.1
+ Revision: 114067
- Bump release to rebuild against lapack 3.1.1.

  + Austin Acton <austin@mandriva.org>
    - rebuild for openbabel
    - Import libghemical



* Tue Aug 22 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.10-2mdv2007.0
- require on version of data package

* Tue Aug 22 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.10-1mdv2007.0
- 2.10
- enable mpqc support
- fix mixed-use-of-spaces-and-tabs

* Tue Jun 20 2006 Lenny Cartier <lenny@mandriva.com> 2.00-2mdv2007.0
- rebuild

* Tue Apr 25 2006 Lenny Cartier <lenny@mandriva.com> 2.00-1mdk
- 2.00

* Mon Apr  3 2006 Austin Acton <austin@mandriva.org> 1.92-0.20060331.2mdk
- lib requires data

* Fri Mar 31 2006 Austin Acton <austin@mandriva.org> 1.92-0.20060331.1mdk
- new cvs checkout

* Thu Feb 09 2006 Lenny Cartier <lenny@mandriva.com> 1.91-2.20060209.1mdk
- update to 20060209

* Fri Aug 12 2005 Austin Acton <austin@mandrake.org> 1.90-1mdk
- initial package
- steal a nice patch from debian
