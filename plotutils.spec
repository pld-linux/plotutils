%define	LIBPLOT_VERSION 2.0

Summary:	GNU Plotutils -- plotting utilities
Summary(pl):	Narzêdzia do wykresów
Name:		plotutils
Version:	2.2
Release:	1
Copyright:	GPL
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source:		%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/plotutils/plotutils.html
Requires:	libplot
BuildPrereq:	libstdc++
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GNU plotutils (plotting utilities) package,
graphics under the X Window System.  The Web page for the package is:
http://www.gnu.org/software/plotutils/plotutils.html

%description -l pl
GNU Plotutils to pakiet zawieraj±cy narzêdzia do tworzenia wykresów.
Umo¿liwiaj± one wy¶wietlanie wykresów w oknie X Window i zapisywanie
w formatach takich jak .pnm .gif .ai .ps .fig .pcl .hpgl .tek
http://www.gnu.org/software/plotutils/plotutils.html

################################################################
%package libplot
Summary:	Libplot plotting library - from plotutils package
Summary(pl):	Libplot -- Biblioteka do kre¶lenia z pakietu plotutils
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Version:	%{LIBPLOT_VERSION}

%description libplot
GNU libplot: a function library for exporting two-dimensional
vector graphics files, and for displaying animated vector.

%description -l pl libplot
GNU libplot: biblioteka do tworzenia dwuwymiarowej grafiki wektorowej lub
wy¶wietlania animowanych obrazów wektorowych pod X Window.

##################################################################
%package libplot-devel
Summary:	Libplot header files
Summary(pl):	Pliki nag³ówkowe dla libplot
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Version:	%{LIBPLOT_VERSION}

%description -l pl libplot-devel
Pliki nag³ówkowe dla libplot

#################################################################
%package libplot-static
Summary:	Libplot static libraries
Summary(pl):	Biblioteki statyczne libplot
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	plotutils-libplot-devel = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description libplot-static
libplot static libraries

%description -l pl libplot-static
biblioteka statyczna libplot

##################################
%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=/usr 
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/{info/*.info*,man/man1/*} \
	AUTHORS COMPAT COPYING KNOWN_BUGS NEWS ONEWS README ChangeLog \
	PROBLEMS THANKS TODO \
	libplot\README*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/%{name}.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/%{name}.info.gz /etc/info-dir
fi

%postun -p /sbin/ldconfig

#######################################
%files
%defattr(644,root,root,755)
%doc *.gz doc
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/*
%{_datadir}/libplot
%{_datadir}/ode
%{_datadir}/tek2plot

#####################################
%files libplot
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

#####################################
%files libplot-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%doc libplot/README*.gz
%{_includedir}/*

#####################################
%files libplot-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
    

%changelog
* Sat May 15 1999 Rafa³ Kleger-Rudomin <klakier@pg.gda.pl>
- Added plotutils-libplot, -devel, -static 
* Fri May 14 1999 Rafa³ Kleger-Rudomin <klakier@pg.gda.pl>
- Initial version for PLD.
