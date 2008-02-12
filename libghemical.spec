%define	major		0
%define	libname		%mklibname ghemical %major
%define develname	%mklibname ghemical -d

Name:		libghemical
Summary:	Libraries for the Ghemical chemistry package
Version:	2.10
Release:	%mkrel 8
Source0:	http://www.uku.fi/~thassine/projects/download/%{name}-%{version}.tar.gz
URL:		http://www.uku.fi/~thassine/ghemical/
License:	GPL+
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	f2c flex
BuildRequires:	libSC-devel
BuildRequires:	mopac7-devel
BuildRequires:	openbabel-devel
BuildRequires:	blas-devel
BuildRequires:	lapack-devel

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

%package -n	%{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	ghemical-devel = %{version}-%{release} 
Obsoletes:	ghemical-devel
Obsoletes:	%{mklibname ghemical 0 -d}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

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
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files data
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
