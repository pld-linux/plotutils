%define	LIBPLOT_VERSION 4.0
%define	LIBXMI_VERSION 1.2

Summary:	GNU Plotutils -- plotting utilities
Summary(pl):	Narzêdzia do wykresów
Name:		plotutils
Version:	2.4.1
Release:	6
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	8da2cc2ed5a837cad0753c7843ef18ee
Patch0:		%{name}-info.patch
Patch1:		%{name}-c++.patch
URL:		http://www.gnu.org/software/plotutils/plotutils.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	texinfo
Requires:	libplot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU plotting utilities include: (1) GNU libplot, a shared library
for exporting 2-D vector graphics files and for performing vector
graphics animation under the X Window System. Its output file formats
include pseudo-GIF, PNM, Adobe Illustrator, Postscript (editable with
the free 'idraw' drawing editor), Fig (editable with the free g'
drawing editor), PCL 5, HP-GL and HP-GL/2, Tektronix, and GNU metafile
format. Many Postscript, PCL, and Hershey fonts are supported. A
separate class library, 'libplotter', provides a C++ binding to
libplot's functionality. (2) Sample command-line applications 'graph',
'plot', 'tek2plot', 'pic2plot', and 'plotfont', which are built on top
of GNU libplot. 'graph' is a powerful utility for XY plotting, 'plot'
translates GNU metafiles to other formats, 'tek2plot' translates
legacy Tektronix data, 'pic2plot' translates box-and-arrow diagrams in
the pic language, and 'plotfont' plots character maps. (3)
Command-line applications 'spline', 'double', and 'ode', which are
useful in scientific plotting. 'spline' does spline interpolation of
input data of arbitrary dimensionality. It uses cubic splines, splines
under tension, or cubic Bessel interpolation. 'ode' is an interactive
program that can integrate a user-specified system of ordinary
differential equations.

%description -l pl
GNU Plotutils to pakiet zawieraj±cy narzêdzia do tworzenia wykresów.
Sk³ada siê z biblioteki GNU libplot, przyk³adowych programów
dzia³aj±cych z linii poleceñ oraz aplikacji. GNU libplot to biblioteka
do tworzenia plików z grafik± wektorow± 2D i odtwarzania animowanej
grafiki wektorowej w ¶rodowisku X Window System. libplot potrafi
zapisywaæ w formatach m.in. GIF, PNM, Adobe Illustrator, Postscript,
Fig, PCL 5, HP-GL i GP-GL/2, Tektronix i GNU metafile. Obs³uguje wiele
fontów Postscriptowych, PCL i Hershey. Oddzielna biblioteka libplotter
daje interfejs C++ do funkcji libplot. Programy przyk³adowe to graph,
plot, tek2plot, pic2plot i plotfont; pierwszy s³u¿y do rysowania, trzy
kolejne do konwersji miêdzy ró¿nymi formatami, ostatni do wy¶wietlania
fontów. Aplikacje zawarte w pakiecie plotutils to spline, double oraz
ode, przydatne do rysunków naukowych. spline tworzy interpolacjê
splajnami dostarczonych danych o dowolnej liczbie wymiarów. ode jest
interaktywnym programem do rozwi±zywania uk³adów równañ ró¿niczkowych.

%package -n libplot
Summary:	libplot plotting library - from plotutils package
Summary(pl):	libplot -- Biblioteka do kre¶lenia z pakietu plotutils
Group:		Development/Libraries
Version:	%{LIBPLOT_VERSION}

%description -n libplot
GNU libplot: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%description -n libplot -l pl
GNU libplot: biblioteka do tworzenia dwuwymiarowej grafiki wektorowej
lub wy¶wietlania animowanych obrazów wektorowych pod X Window.

%package -n libplot-devel
Summary:	libplot header files
Summary(pl):	Pliki nag³ówkowe dla libplot
Group:		Development/Libraries
Requires:	libplot = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description -n libplot-devel
libplot header files.

%description -n libplot-devel -l pl
Pliki nag³ówkowe dla libplot.

%package -n libplot-static
Summary:	libplot static libraries
Summary(pl):	Biblioteki statyczne libplot
Group:		Development/Libraries
Requires:	libplot-devel = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description -n libplot-static
libplot static libraries.

%description -n libplot-static -l pl
Biblioteka statyczna libplot.

%package -n libplotter
Summary:	libplotter plotting library - from plotutils package
Summary(pl):	libplotter - biblioteka do kre¶lenia z pakietu plotutils
Group:		Development/Libraries
Version:	%{LIBPLOT_VERSION}

%description -n libplotter
GNU libplotter: a function library for exporting two-dimensional
vector graphics files, and for displaying animated vector.

%description -n libplotter -l pl
GNU libplotter: biblioteka do tworzenia dwuwymiarowej grafiki
wektorowej lub wy¶wietlania animowanych obrazów wektorowych pod X
Window.

%package -n libplotter-devel
Summary:	libplotter header files
Summary(pl):	Pliki nag³ówkowe dla libplotter
Group:		Development/Libraries
Requires:	libplotter = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description -n libplotter-devel
libplotter header files.

%description -n libplotter-devel -l pl
Pliki nag³ówkowe dla libplotter.

%package -n libplotter-static
Summary:	libplotter static libraries
Summary(pl):	Biblioteki statyczne libplotter
Group:		Development/Libraries
Requires:	libplotter-devel = %{LIBPLOT_VERSION}
Version:	%{LIBPLOT_VERSION}

%description -n libplotter-static
libplotter static libraries.

%description -n libplotter-static -l pl
Biblioteka statyczna libplotter.

%package -n libxmi
Summary:	libxmi library - from plotutils package
Summary(pl):	libxmi - biblioteka z pakietu plotutils
Group:		Development/Libraries
Version:	%{LIBXMI_VERSION}

%description -n libxmi
GNU libxmi: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%description -n libxmi -l pl
GNU libxmi: biblioteka do tworzenia dwuwymiarowej grafiki wektorowej
lub wy¶wietlania animowanych obrazów wektorowych pod X Window.

%package -n libxmi-devel
Summary:	libxmi header files
Summary(pl):	Pliki nag³ówkowe dla libxmi
Group:		Development/Libraries
Requires:	libxmi = %{LIBXMI_VERSION}
Version:	%{LIBXMI_VERSION}

%description -n libxmi-devel
libxmi header files.

%description -n libxmi-devel -l pl
Pliki nag³ówkowe dla libxmi.

%package -n libxmi-static
Summary:	Libxmi static libraries
Summary(pl):	Biblioteki statyczne libxmi
Group:		Development/Libraries
Requires:	libxmi-devel = %{LIBXMI_VERSION}
Version:	%{LIBXMI_VERSION}

%description -n libxmi-static
libxmi static libraries.

%description -n libxmi-static -l pl
Biblioteka statyczna libxmi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--enable-libplotter \
	--enable-libxmi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/libplot-%{LIBPLOT_VERSION},%{_fontsdir}/misc}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/h-demo.c $RPM_BUILD_ROOT%{_examplesdir}/libplot-%{LIBPLOT_VERSION}
install fonts/pcf/*.pcf $RPM_BUILD_ROOT%{_fontsdir}/misc

gzip -9nf $RPM_BUILD_ROOT%{_fontsdir}/misc/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n libxmi-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n libxmi-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post   -n libplot
/sbin/ldconfig
[ ! -x /usr/X11R6/bin/mkfontdir ] || /usr/X11R6/bin/mkfontdir %{_fontsdir}/misc

%postun -n libplot
/sbin/ldconfig
[ ! -x /usr/X11R6/bin/mkfontdir ] || /usr/X11R6/bin/mkfontdir %{_fontsdir}/misc

%post   -n libplotter -p /sbin/ldconfig
%postun -n libplotter -p /sbin/ldconfig

%post   -n libxmi -p /sbin/ldconfig
%postun -n libxmi -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COMPAT KNOWN_BUGS NEWS ONEWS PROBLEMS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/plotutils.info*
%{_mandir}/man1/*
%{_datadir}/ode
%{_datadir}/pic2plot
%{_datadir}/tek2plot

%files -n libplot
%defattr(644,root,root,755)
%doc doc/{demo-page,*.doc,*.txt,*.bib}
%doc libplot/{DEDICATION,HUMOR,README*,VERSION}
%attr(755,root,root) %{_libdir}/libplot.so.*.*
%{_fontsdir}/misc/*

%files -n libplot-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplot.so
%{_libdir}/libplot.la
%{_examplesdir}/libplot-%{LIBPLOT_VERSION}
%{_includedir}/plot.h
%{_includedir}/plotcompat.h

%files -n libplot-static
%defattr(644,root,root,755)
%{_libdir}/libplot.a

%files -n libplotter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplotter.so.*.*

%files -n libplotter-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplotter.so
%{_libdir}/libplotter.la
%{_includedir}/plotter.h

%files -n libplotter-static
%defattr(644,root,root,755)
%{_libdir}/libplotter.a

%files -n libxmi
%defattr(644,root,root,755)
%doc libxmi/{AUTHORS,NEWS,README*,TODO,VERSION}
%attr(755,root,root) %{_libdir}/libxmi.so.*.*

%files -n libxmi-devel
%defattr(644,root,root,755)
%{_infodir}/libxmi.info*
%attr(755,root,root) %{_libdir}/libxmi.so
%{_libdir}/libxmi.la
%{_includedir}/xmi.h

%files -n libxmi-static
%defattr(644,root,root,755)
%{_libdir}/libxmi.a
