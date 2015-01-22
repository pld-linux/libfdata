Summary:	Library to provide generic file data functions
Summary(pl.UTF-8):	Biblioteka udostępniająca ogólne funkcje obsługi danych w plikach
Name:		libfdata
Version:	20150104
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libfdata/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3d308065c27c965c6ebd07073402d466
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libfdata/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcdata-devel >= 20130407
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libfcache-devel >= 20140912
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcdata >= 20130407
Requires:	libcerror >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcstring >= 20120425
Requires:	libcthreads >= 20130509
Requires:	libfcache >= 20140912
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
Requires:	libcdata-devel >= 20130407
Requires:	libcerror-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509
Requires:	libfcache-devel >= 20140912

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
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
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
