Summary:	GNU Plotutils and libplot -- plotting utilities
Summary(pl):	Narzêdzia do wykresów wraz z bibliotek± libplot
Name:		plotutils
Version:	2.2
Release:	1
Copyright:	GPL
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source:		%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/plotutils/plotutils.html
BuildPrereq:	libstdc++
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GNU plotutils (plotting utilities) package,                         
including GNU libplot: a function library for exporting                         
two-dimensional vector graphics files, and for displaying animated vector                      
graphics under the X Window System.  The Web page for the package is:                          
http://www.gnu.org/software/plotutils/plotutils.html .  

%description -l pl
GNU Plotutils to pakiet zawieraj±cy GNU libplot: bibliotekê do tworzenia
dwuwymiarowej grafiki wektorowej lub wy¶wietalnia animowanych obrazów
wektorowych pod X Window. Plotutils umo¿liwiaj± tak¿e przetwarzanie plików
w formacie GNU metafile do formatów .pnm .gif .ai .ps .fig .pcl .hpgl .tek

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

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*so

gzip -9nf $RPM_BUILD_ROOT/usr/share/{info/*.info*,man/man1/*} \
	AUTHORS COMPAT COPYING KNOWN_BUGS NEWS ONEWS README ChangeLog \
	PROBLEMS THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info /usr/share/info/%{name}.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/share/info/%{name}.info.gz /etc/info-dir
fi

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/lib*so
/usr/include/*
/usr/share/info/*.info*
/usr/share/man/man1/*
/usr/share/libplot
/usr/share/ode
/usr/share/tek2plot
    
%changelog
* Fri May 14 1999 Rafa³ Kleger-Rudomin <klakier@pg.gda.pl>
- Initial version for PLD.
