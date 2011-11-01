Name:		texlive-adjustbox
Version:	0.6
Release:	1
Summary:	Apply graphics package macros to general boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/adjustbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/adjustbox/adjcalc.sty
%{_texmfdistdir}/tex/latex/adjustbox/adjgrfx.sty
%{_texmfdistdir}/tex/latex/adjustbox/adjpgf.def
%{_texmfdistdir}/tex/latex/adjustbox/adjustbox.sty
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
