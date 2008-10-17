Summary:	qpackagekit
Summary(pl.UTF-8):	qpackagekit
Name:		qpackagekit
Version:	0.3.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://maison.mymadcat.com/~madcat/qpackagekit/%{name}-%{version}.tar.gz
# Source0-md5:	6d2a380ea59056b09cad68191cdde860
URL:		http://
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qpackagekit

%description -l pl.UTF-8
qpackagekit

%package devel
Summary:	qpackagekit - header files and development documentation
Summary(pl.UTF-8):	qpackagekit - pliki nagłówkowe i dokumentacja do qpackagekit
Group:		X11/Development/Libraries

%description devel
This package contains header files and development documentation for
qpackagekit.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących qpackagekit.

%prep
%setup -q

%build
export QTDIR=%{_prefix}
mkdir build
cd build
%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		../
%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpackagekit-qt.so.?
%attr(755,root,root) %{_libdir}/libpackagekit-qt.so.*.*
%dir %{_includedir}/packagekit-qt
%{_includedir}/packagekit-qt/QPackageKit

%files devel
%defattr(644,root,root,755)
%{_includedir}/packagekit-qt/client.h
%{_includedir}/packagekit-qt/package.h
%{_includedir}/packagekit-qt/transaction.h
%attr(755,root,root) %{_libdir}/libpackagekit-qt.so
%{_datadir}/cmake/Modules/FindQPackageKit.cmake
