Name:			libghemical
Version:		2.99.1
Release:		%mkrel 6

%define	major		5
%define	libname		%mklibname ghemical %major
%define develname	%mklibname ghemical -d

Summary:	Libraries for the Ghemical chemistry package
Source0:	http://www.uku.fi/~thassine/projects/download/%{name}-%{version}.tar.gz
URL:		http://www.uku.fi/~thassine/ghemical/
License:	GPLv2+
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	f2c flex
BuildRequires:	libSC-devel
BuildRequires:	mopac7-devel
BuildRequires:	openbabel-devel
BuildRequires:	blas-devel
BuildRequires:	lapack-devel
BuildRequires:	mesaglut-devel
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
Provides:	%{name} = %{version}-%{release}
Requires:	%{name}-data = %{version}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{name} = %{version}
Provides:	ghemical-devel = %{version}-%{release} 
Obsoletes:	ghemical-devel < %{version}-%{release}
Obsoletes:	%{mklibname ghemical 0 -d} <= %{version}-%{release}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x	--enable-mopac7 \
		--enable-mpqc \
		--enable-openbabel

%make
							
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}
%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files data -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%{_datadir}/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

