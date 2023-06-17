# see m4/${libname}.m4 />= for required version of particular library
%define		libcdata_ver	20230108
%define		libcerror_ver	20120425
%define		libcnotify_ver	20120425
%define		libcthreads_ver	20160404
%define		libfcache_ver	20191109
Summary:	Library to provide generic file data functions
Summary(pl.UTF-8):	Biblioteka udostępniająca ogólne funkcje obsługi danych w plikach
Name:		libfdata
Version:	20230319
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libfdata/releases
Source0:	https://github.com/libyal/libfdata/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	b796c47a1fdf84b7178b04861497b7ad
URL:		https://github.com/libyal/libfdata/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libfcache >= %{libfcache_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfdata is a library to provide generic file data functions.

%description -l pl.UTF-8
libfdata to biblioteka udostępniająca ogólne funkcje obsługi danych w
plikach.

%package devel
Summary:	Header files for libfdata library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libfcache-devel >= %{libfcache_ver}

%description devel
Header files for libfdata library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfdata.

%package static
Summary:	Static libfdata library
Summary(pl.UTF-8):	Statyczna biblioteka libfdata
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfdata library.

%description static -l pl.UTF-8
Statyczna biblioteka libfdata.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfdata.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libfdata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfdata.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfdata.so
%{_includedir}/libfdata
%{_includedir}/libfdata.h
%{_pkgconfigdir}/libfdata.pc
%{_mandir}/man3/libfdata.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfdata.a
