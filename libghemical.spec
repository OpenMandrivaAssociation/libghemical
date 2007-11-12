%define	name	libghemical
%define	version	2.10
%define	release	%mkrel 4

%define	major	0
%define	libname	%mklibname ghemical %major

Name:		%{name}
Summary:	Libraries for the Ghemical chemistry package
Version:	%{version}
Release:	%{release}

Source0:	http://www.uku.fi/~thassine/projects/download/%{name}-%{version}.tar.gz

URL:		http://www.uku.fi/~thassine/ghemical/
License:	GPL
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	f2c
BuildRequires:	libSC-devel mopac7-devel openbabel-devel blas-devel lapack-devel

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
Requires:	%{name}-data = %{version}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{libname}-devel
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	libghemical-devel = %{version}-%{release}
Provides:	ghemical-devel = %{version}-%{release} 
Obsoletes:	ghemical-devel

%description -n	%{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q 

%build
libtoolize --copy --force
aclocal
autoconf
%configure2_5x	--enable-mopac7 \
		--enable-mpqc \
		--enable-openbabel 
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files data
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%{_datadir}/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
