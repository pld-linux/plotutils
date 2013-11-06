%define		LIBPLOT_VERSION	4.4
%define		LIBXMI_VERSION	1.3
Summary:	GNU Plotutils -- plotting utilities
Summary(pl.UTF-8):	Narzędzia do wykresów
Name:		plotutils
Version:	2.6
# Don't decrease release if LIBPLOT/LIBXMI versions are not increased, as then
# those subpackages get then lower release
Release:	15
License:	GPL v3+
Group:		Applications/Graphics
Source0:	http://ftp.gnu.org/gnu/plotutils/%{name}-%{version}.tar.gz
# Source0-md5:	c08a424bd2438c80a786a7f4b5bb6a40
Patch0:		%{name}-info.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-libpng15.patch
Patch3:		%{name}-format.patch
URL:		http://www.gnu.org/software/plotutils/plotutils.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
Requires:	libplot = %{LIBPLOT_VERSION}-%{release}
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

%description -l pl.UTF-8
GNU Plotutils to pakiet zawierający narzędzia do tworzenia wykresów.
Składa się z biblioteki GNU libplot, przykładowych programów
działających z linii poleceń oraz aplikacji. GNU libplot to biblioteka
do tworzenia plików z grafiką wektorową 2D i odtwarzania animowanej
grafiki wektorowej w środowisku X Window System. libplot potrafi
zapisywać w formatach m.in. GIF, PNM, Adobe Illustrator, Postscript,
Fig, PCL 5, HP-GL i GP-GL/2, Tektronix i GNU metafile. Obsługuje wiele
fontów Postscriptowych, PCL i Hershey. Oddzielna biblioteka libplotter
daje interfejs C++ do funkcji libplot. Programy przykładowe to graph,
plot, tek2plot, pic2plot i plotfont; pierwszy służy do rysowania, trzy
kolejne do konwersji między różnymi formatami, ostatni do wyświetlania
fontów. Aplikacje zawarte w pakiecie plotutils to spline, double oraz
ode, przydatne do rysunków naukowych. spline tworzy interpolację
splajnami dostarczonych danych o dowolnej liczbie wymiarów. ode jest
interaktywnym programem do rozwiązywania układów równań różniczkowych.

%package -n libplot
Summary:	libplot plotting library - from plotutils package
Summary(pl.UTF-8):	libplot -- Biblioteka do kreślenia z pakietu plotutils
Version:	%{LIBPLOT_VERSION}
Group:		Libraries
Requires(post,postun):	fontpostinst

%description -n libplot
GNU libplot: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%description -n libplot -l pl.UTF-8
GNU libplot: biblioteka do tworzenia dwuwymiarowej grafiki wektorowej
lub wyświetlania animowanych obrazów wektorowych pod X Window.

%package -n libplot-devel
Summary:	libplot header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla libplot
Version:	%{LIBPLOT_VERSION}
Group:		Development/Libraries
Requires:	libplot = %{LIBPLOT_VERSION}-%{release}
Requires:	libpng-devel
Requires:	xorg-lib-libXaw-devel
Requires:	xorg-lib-libXext-devel

%description -n libplot-devel
libplot header files.

%description -n libplot-devel -l pl.UTF-8
Pliki nagłówkowe dla libplot.

%package -n libplot-static
Summary:	libplot static library
Summary(pl.UTF-8):	Biblioteka statyczna libplot
Version:	%{LIBPLOT_VERSION}
Group:		Development/Libraries
Requires:	libplot-devel = %{LIBPLOT_VERSION}-%{release}

%description -n libplot-static
libplot static library.

%description -n libplot-static -l pl.UTF-8
Biblioteka statyczna libplot.

%package -n libplotter
Summary:	libplotter plotting library - from plotutils package
Summary(pl.UTF-8):	libplotter - biblioteka do kreślenia z pakietu plotutils
Version:	%{LIBPLOT_VERSION}
Group:		Libraries

%description -n libplotter
GNU libplotter: a function library for exporting two-dimensional
vector graphics files, and for displaying animated vector.

%description -n libplotter -l pl.UTF-8
GNU libplotter: biblioteka do tworzenia dwuwymiarowej grafiki
wektorowej lub wyświetlania animowanych obrazów wektorowych pod X
Window.

%package -n libplotter-devel
Summary:	libplotter header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla libplotter
Version:	%{LIBPLOT_VERSION}
Group:		Development/Libraries
Requires:	libplotter = %{LIBPLOT_VERSION}-%{release}
Requires:	libpng-devel
Requires:	libstdc++-devel
Requires:	xorg-lib-libXaw-devel
Requires:	xorg-lib-libXext-devel

%description -n libplotter-devel
libplotter header files.

%description -n libplotter-devel -l pl.UTF-8
Pliki nagłówkowe dla libplotter.

%package -n libplotter-static
Summary:	libplotter static library
Summary(pl.UTF-8):	Biblioteka statyczna libplotter
Version:	%{LIBPLOT_VERSION}
Group:		Development/Libraries
Requires:	libplotter-devel = %{LIBPLOT_VERSION}-%{release}

%description -n libplotter-static
libplotter static library.

%description -n libplotter-static -l pl.UTF-8
Biblioteka statyczna libplotter.

%package -n libxmi
Summary:	libxmi library - from plotutils package
Summary(pl.UTF-8):	libxmi - biblioteka z pakietu plotutils
Version:	%{LIBXMI_VERSION}
Group:		Libraries

%description -n libxmi
GNU libxmi: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%description -n libxmi -l pl.UTF-8
GNU libxmi: biblioteka do tworzenia dwuwymiarowej grafiki wektorowej
lub wyświetlania animowanych obrazów wektorowych pod X Window.

%package -n libxmi-devel
Summary:	libxmi header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla libxmi
Version:	%{LIBXMI_VERSION}
Group:		Development/Libraries
Requires:	libxmi = %{LIBXMI_VERSION}-%{release}

%description -n libxmi-devel
libxmi header files.

%description -n libxmi-devel -l pl.UTF-8
Pliki nagłówkowe dla libxmi.

%package -n libxmi-static
Summary:	Libxmi static library
Summary(pl.UTF-8):	Biblioteka statyczna libxmi
Version:	%{LIBXMI_VERSION}
Group:		Development/Libraries
Requires:	libxmi-devel = %{LIBXMI_VERSION}-%{release}

%description -n libxmi-static
libxmi static library.

%description -n libxmi-static -l pl.UTF-8
Biblioteka statyczna libxmi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libplotter \
	--enable-libxmi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/libplot-%{LIBPLOT_VERSION},%{_fontsdir}/misc}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install doc/h-demo.c $RPM_BUILD_ROOT%{_examplesdir}/libplot-%{LIBPLOT_VERSION}
install fonts/pcf/*.pcf $RPM_BUILD_ROOT%{_fontsdir}/misc

gzip -9nf $RPM_BUILD_ROOT%{_fontsdir}/misc/*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n libxmi-devel	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n libxmi-devel	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n libplot
/sbin/ldconfig
fontpostinst misc

%postun	-n libplot
/sbin/ldconfig
fontpostinst misc

%post	-n libplotter -p /sbin/ldconfig
%postun	-n libplotter -p /sbin/ldconfig

%post	-n libxmi -p /sbin/ldconfig
%postun	-n libxmi -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COMPAT KNOWN_BUGS NEWS ONEWS PROBLEMS README THANKS TODO
%attr(755,root,root) %{_bindir}/double
%attr(755,root,root) %{_bindir}/graph
%attr(755,root,root) %{_bindir}/hersheydemo
%attr(755,root,root) %{_bindir}/ode
%attr(755,root,root) %{_bindir}/pic2plot
%attr(755,root,root) %{_bindir}/plot
%attr(755,root,root) %{_bindir}/plotfont
%attr(755,root,root) %{_bindir}/spline
%attr(755,root,root) %{_bindir}/tek2plot
%{_infodir}/plotutils.info*
%{_mandir}/man1/ode.1*
%{_mandir}/man1/plot.1*
%{_mandir}/man1/plotfont.1*
%{_mandir}/man1/spline.1*
%{_mandir}/man1/tek2plot.1*
%{_datadir}/ode
%{_datadir}/pic2plot
%{_datadir}/tek2plot

%files -n libplot
%defattr(644,root,root,755)
%doc doc/{*.txt,*.bib}
%doc libplot/{DEDICATION,HUMOR,README*,VERSION}
%attr(755,root,root) %{_libdir}/libplot.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplot.so.2
%{_fontsdir}/misc/tekfont*.pcf.gz

%files -n libplot-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplot.so
%{_libdir}/libplot.la
%{_includedir}/plot.h
%{_includedir}/plotcompat.h
%{_examplesdir}/libplot-%{LIBPLOT_VERSION}

%files -n libplot-static
%defattr(644,root,root,755)
%{_libdir}/libplot.a

%files -n libplotter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplotter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplotter.so.2

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
%attr(755,root,root) %{_libdir}/libxmi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmi.so.0

%files -n libxmi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmi.so
%{_libdir}/libxmi.la
%{_includedir}/xmi.h
%{_infodir}/libxmi.info*

%files -n libxmi-static
%defattr(644,root,root,755)
%{_libdir}/libxmi.a
