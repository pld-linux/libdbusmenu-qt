Summary:	Qt implementation of the DBusMenu spec
Summary(pl.UTF-8):	Implementacja Qt specyfikacji DBusMenu
Name:		libdbusmenu-qt
Version:	0.9.2
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	https://launchpad.net/libdbusmenu-qt/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	9a49484927669cd2ec91b3bf9ba8b79e
URL:		https://launchpad.net/libdbusmenu-qt/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtDBus-devel >= 4
# for <QtGui/QKeySequence>
BuildRequires:	QtGui-devel >= 4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qjson-devel >= 0.7.1
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
BuildRequires:	rpmbuild(macros) >= 1.605
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
Requires:	QtCore-devel >= 4
Requires:	QtDBus-devel >= 4

%description devel
Header files for dbusmenu-qt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dbusmenu-qt.

%package apidocs
Summary:	dbusmenu-qt API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki dbusmenu-qt
Group:		Documentation

%description apidocs
API documentation for dbusmenu-qt library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki dbusmenu-qt.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

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
%doc NEWS README
%attr(755,root,root) %{_libdir}/libdbusmenu-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbusmenu-qt.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbusmenu-qt.so
%{_includedir}/dbusmenu-qt
%{_pkgconfigdir}/dbusmenu-qt.pc

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/dbusmenu-qt
