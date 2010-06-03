#
Summary:	Qt implementation of the DBusMenu spec
Summary(pl.UTF-8):	Implementacja Qt specyfikacji DBusMenu
Name:		libdbusmenu-qt
Version:	0.3.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://people.canonical.com/~agateau/dbusmenu/%{name}-%{version}.tar.bz2
# Source0-md5:	5c0628166e50325bb7e9babdf280755a
URL:		http://people.canonical.com/~agateau/dbusmenu/
BuildRequires:	QtCore-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides a Qt implementation of the DBusMenu spec.

%description -l pl.UTF-8
Ta biblioteka dostarcza implementację Qt specyfikacji DBusMenu.

%package devel
Summary:	Header files for dbusmenu-qt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dbusmenu-qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for dbusmenu-qt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dbusmenu-qt.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libdbusmenu-qt.so.?
%attr(755,root,root) %{_libdir}/libdbusmenu-qt.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbusmenu-qt.so
%{_includedir}/dbusmenu-qt
%{_pkgconfigdir}/dbusmenu-qt.pc
