%define	LIBPLOT_VERSION 4.0
%define	LIBXMI_VERSION 1.2

Summary:	GNU Plotutils -- plotting utilities
Summary(pl):	Narzêdzia do wykresów
Name:		plotutils
Version:	2.4.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/plotutils/plotutils.html
BuildRequires:	libstdc++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU plotutils (plotting utilities) package, graphics under the X
Window System. The Web page for the package is:
http://www.gnu.org/software/plotutils/plotutils.html

%description -l pl
GNU Plotutils to pakiet zawieraj±cy narzêdzia do tworzenia wykresów.
Umo¿liwiaj± one wy¶wietlanie wykresów w oknie X Window i zapisywanie w
formatach takich jak .pnm .gif .ai .ps .fig .pcl .hpgl .tek
http://www.gnu.org/software/plotutils/plotutils.html

%package -n libplot
Summary:	Libplot plotting library - from plotutils package
Summary(pl):	Libplot -- Biblioteka do kre¶lenia z pakietu plotutils
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Version:	%{LIBPLOT_VERSION}

%description -n libplot
GNU libplot: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%description -l pl -n libplot
GNU libplot: biblioteka do tworzenia dwuwymiarowej grafiki wektorowej
lub wy¶wietlania animowanych obrazów wektorowych pod X Window.

%package -n libplot-devel
Summary:	Libplot header files
Summary(pl):	Pliki nag³ówkowe dla libplot
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libplot = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description -l pl -n libplot-devel
Pliki nag³ówkowe dla libplot

%package -n libplot-static
Summary:	Libplot static libraries
Summary(pl):	Biblioteki statyczne libplot
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libplot-devel = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description -n libplot-static
libplot static libraries

%description -l pl -n libplot-static
biblioteka statyczna libplot

%package -n libplotter
Summary:	Libplot plotting library - from plotutils package
Summary(pl):	Libplot -- Biblioteka do kre¶lenia z pakietu plotutils
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Version:	%{LIBPLOT_VERSION}

%description -n libplotter
GNU libplotter: a function library for exporting two-dimensional
vector graphics files, and for displaying animated vector.

%description -l pl -n libplotter
GNU libplotter: biblioteka do tworzenia dwuwymiarowej grafiki
wektorowej lub wy¶wietlania animowanych obrazów wektorowych pod X
Window.

%package -n libplotter-devel
Summary:	Libplot header files
Summary(pl):	Pliki nag³ówkowe dla libplotter
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libplotter = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description -l pl -n libplotter-devel
Pliki nag³ówkowe dla libplotter

%package -n libplotter-static
Summary:	Libplot static libraries
Summary(pl):	Biblioteki statyczne libplotter
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libplotter-devel = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description -n libplotter-static
libplotter static libraries

%description -l pl -n libplotter-static
biblioteka statyczna libplotter

%package -n libxmi
Summary:	Libplot plotting library - from plotutils package
Summary(pl):	Libplot -- Biblioteka do kre¶lenia z pakietu plotutils
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Version:	%{LIBXMI_VERSION}

%description -n libxmi
GNU libxmi: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%description -l pl -n libxmi
GNU libxmi: biblioteka do tworzenia dwuwymiarowej grafiki wektorowej
lub wy¶wietlania animowanych obrazów wektorowych pod X Window.

%package -n libxmi-devel
Summary:	Libplot header files
Summary(pl):	Pliki nag³ówkowe dla libxmi
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libxmi = %{LIBXMI_VERSION}
Version:	%{LIBXMI_VERSION}

%description -l pl -n libxmi-devel
Pliki nag³ówkowe dla libxmi

%package -n libxmi-static
Summary:	Libplot static libraries
Summary(pl):	Biblioteki statyczne libxmi
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libxmi-devel = %{LIBXMI_VERSION}
Version:	%{LIBXMI_VERSION}

%description -n libxmi-static
libxmi static libraries

%description -l pl -n libxmi-static
biblioteka statyczna libxmi

%prep
%setup -q

%build
%configure \
	--enable-libplotter \
	--enable-libxmi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/libplot-%{LIBPLOT_VERSION},/usr/share/fonts/misc}
install doc/h-demo.c $RPM_BUILD_ROOT%{_examplesdir}/libplot-%{LIBPLOT_VERSION}
install fonts/pcf/*.pcf $RPM_BUILD_ROOT/usr/share/fonts/misc
gzip $RPM_BUILD_ROOT/usr/share/fonts/misc/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun 
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n libplot
/sbin/ldconfig

%postun -n libplot
/sbin/ldconfig

%post -n libplotter
/sbin/ldconfig

%postun -n libplotter
/sbin/ldconfig

%post -n libxmi
/sbin/ldconfig

%postun -n libxmi
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS* COMPAT* KNOWN_BUGS* NEWS* ONEWS* README* ChangeLog* PROBLEMS* THANKS* TODO* 

%attr(755,root,root) %{_bindir}/*
%{_infodir}/plotutils.info*
%{_mandir}/man1/*
%{_datadir}/ode
%{_datadir}/pic2plot
%{_datadir}/tek2plot

%files -n libplot
%defattr(644,root,root,755)
%doc doc/*.doc* doc/*.txt* doc/demo-page* doc/hershey.bib*
%attr(755,root,root) %{_libdir}/libplot.so.*.*
/usr/share/fonts/misc/*

%files -n libplot-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplot.so
%attr(755,root,root) %{_libdir}/libplot.la
%doc libplot/README*
%doc libplot/DEDICATION*
%{_examplesdir}/libplot-%{LIBPLOT_VERSION}
%{_includedir}/plot.h
%{_includedir}/plotcompat.h

%files -n libplot-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplot.a
 
%files -n libplotter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplotter.so.*.*

%files -n libplotter-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplotter.so
%attr(755,root,root) %{_libdir}/libplotter.la
%{_includedir}/plotter.h

%files -n libplotter-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplotter.a

%files -n libxmi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmi.so.*.*

%files -n libxmi-devel
%defattr(644,root,root,755)
%{_infodir}/libxmi.info*
%attr(755,root,root) %{_libdir}/libxmi.so
%attr(755,root,root) %{_libdir}/libxmi.la
%{_includedir}/xmi.h

%files -n libxmi-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmi.a
    
