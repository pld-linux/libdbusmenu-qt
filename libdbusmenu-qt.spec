#
# Conditional build:
%bcond_without	qt5		# do not build Qt5 version
Summary:	Qt implementation of the DBusMenu spec
Summary(pl.UTF-8):	Implementacja Qt specyfikacji DBusMenu
Name:		libdbusmenu-qt
Version:	0.9.3
Release:	0.20150604.2
License:	LGPL v2+
Group:		Libraries
Source0:	%{name}_%{version}+15.10.20150604.orig.tar.gz
# Source0-md5:	d6fe90fe530a926b9db505da11e2c354
URL:		https://launchpad.net/libdbusmenu-qt/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtDBus-devel >= 4
# for <QtGui/QKeySequence>
BuildRequires:	QtGui-devel >= 4

%if %{with qt5}
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
%endif

BuildRequires:	cmake >= 2.8.0
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qjson-devel >= 0.7.1
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
%if %{with qt5}
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
%endif
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for dbusmenu-qt library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki dbusmenu-qt.

%package -n libdbusmenu-qt5
Summary:	Qt5 implementation of the DBusMenu spec
Summary(pl.UTF-8):	Implementacja Qt5 specyfikacji DBusMenu
Version:	0.9.3
Release:	0.20150604.1
License:	LGPL v2+
Group:		Libraries

%description -n libdbusmenu-qt5
This library provides a Qt5 implementation of the DBusMenu spec.

%description -n libdbusmenu-qt5 -l pl.UTF-8
Ta biblioteka dostarcza implementację Qt5 specyfikacji DBusMenu.

%package -n libdbusmenu-qt5-devel
Summary:	Header files for dbusmenu-qt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dbusmenu-qt
Group:		Development/Libraries
Requires:	Qt5Core-devel >= 5
Requires:	Qt5DBus-devel >= 5
Requires:	libdbusmenu-qt5 = %{version}-%{release}

%description -n libdbusmenu-qt5-devel
Header files for dbusmenu-qt5 library.

%description -n libdbusmenu-qt5-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dbusmenu-qt5.

%package -n libdbusmenu-qt5-apidocs
Summary:	dbusmenu-qt5 API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki dbusmenu-qt5
Group:		Documentation

%description -n libdbusmenu-qt5-apidocs
API documentation for dbusmenu-qt5 library.

%description -n libdbusmenu-qt5-apidocs -l pl.UTF-8
Dokumentacja API biblioteki dbusmenu-qt5.

%prep
%setup -q -n %{name}-%{version}+15.10.20150604

%build
install -d build4
cd build4
%cmake -DUSE_QT4=ON \
	..

%{__make}

%if %{with qt5}
cd -
install -d build5
cd build5
%cmake -DUSE_QT5=ON \
	..
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build4 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C build5 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun	 -p /sbin/ldconfig

%if %{with qt5}
%post	-n libdbusmenu-qt5 -p /sbin/ldconfig
%postun	-n libdbusmenu-qt5 -p /sbin/ldconfig
%endif

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %ghost %{_libdir}/libdbusmenu-qt.so.2
%attr(755,root,root) %{_libdir}/libdbusmenu-qt.so.2.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/dbusmenu-qt
%{_libdir}/cmake/dbusmenu-qt
%{_libdir}/libdbusmenu-qt.so
%{_pkgconfigdir}/dbusmenu-qt.pc

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/libdbusmenu-qt-doc

%if %{with qt5}
%files -n libdbusmenu-qt5
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %ghost %{_libdir}/libdbusmenu-qt5.so.2
%attr(755,root,root) %{_libdir}/libdbusmenu-qt5.so.2.*.*

%files -n libdbusmenu-qt5-devel
%defattr(644,root,root,755)
%{_includedir}/dbusmenu-qt5
%{_libdir}/cmake/dbusmenu-qt5
%{_libdir}/libdbusmenu-qt5.so
%{_pkgconfigdir}/dbusmenu-qt5.pc

%files -n libdbusmenu-qt5-apidocs
%defattr(644,root,root,755)
%{_docdir}/libdbusmenu-qt5-doc
%endif
