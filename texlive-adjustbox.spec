# revision 24593
# category Package
# catalog-ctan /macros/latex/contrib/adjustbox
# catalog-date 2011-11-14 19:03:15 +0100
# catalog-license lppl1.3
# catalog-version 0.8
Name:		texlive-adjustbox
Version:	0.8
Release:	3
Summary:	Apply graphics package macros to general boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/adjustbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides several macros to adjust boxed content.
One purpose is to supplement the standard 'graphics' package,
which defines the macros \resizebox, \scalebox and \rotatebox ,
with the macros\trimbox and \clipbox. The main feature is the
general \adjustbox macro which extends the "key=value"
interface of \includegraphics from the graphics package and
applies it to general text content. Additional provided box
macros are \lapbox, \marginbox, \minsizebox, \maxsizebox and
\phantombox. All macros use the collectbox package to read the
content as a box and not as a macro argument. This allows for
all forms of content including special material like verbatim
content. A special feature of collectbox is used to provide
matching environments with the identical names as the macros.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/adjustbox/adjcalc.sty
%{_texmfdistdir}/tex/latex/adjustbox/adjdvips.def
%{_texmfdistdir}/tex/latex/adjustbox/adjgrfx.sty
%{_texmfdistdir}/tex/latex/adjustbox/adjpdftex.def
%{_texmfdistdir}/tex/latex/adjustbox/adjpgf.def
%{_texmfdistdir}/tex/latex/adjustbox/adjustbox.sty
%{_texmfdistdir}/tex/latex/adjustbox/adjxetex.def
%doc %{_texmfdistdir}/doc/latex/adjustbox/README
%doc %{_texmfdistdir}/doc/latex/adjustbox/adjustbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/adjustbox/adjustbox.dtx
%doc %{_texmfdistdir}/source/latex/adjustbox/adjustbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.8-2
+ Revision: 749088
- Rebuild to reduce used resources

* Tue Nov 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.8-1
+ Revision: 732494
- texlive-adjustbox

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7-1
+ Revision: 729624
- texlive-adjustbox

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.6-1
+ Revision: 717796
- texlive-adjustbox
- texlive-adjustbox
- texlive-adjustbox
- texlive-adjustbox
- texlive-adjustbox

