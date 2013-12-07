# revision 26555
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-adjustbox
Epoch:		1
Version:	20131013
Release:	3
Summary:	TeXLive adjustbox package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive adjustbox package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/adjustbox/adjcalc.sty
%{_texmfdistdir}/tex/latex/adjustbox/adjustbox.sty
%{_texmfdistdir}/tex/latex/adjustbox/tc-dvips.def
%{_texmfdistdir}/tex/latex/adjustbox/tc-pdftex.def
%{_texmfdistdir}/tex/latex/adjustbox/tc-pgf.def
%{_texmfdistdir}/tex/latex/adjustbox/tc-xetex.def
%{_texmfdistdir}/tex/latex/adjustbox/trimclip.sty
%doc %{_texmfdistdir}/doc/latex/adjustbox/README
%doc %{_texmfdistdir}/doc/latex/adjustbox/adjcalc.pdf
%doc %{_texmfdistdir}/doc/latex/adjustbox/adjustbox.pdf
%doc %{_texmfdistdir}/doc/latex/adjustbox/trimclip.pdf
#- source
%doc %{_texmfdistdir}/source/latex/adjustbox/adjcalc.dtx
%doc %{_texmfdistdir}/source/latex/adjustbox/adjustbox.dtx
%doc %{_texmfdistdir}/source/latex/adjustbox/adjustbox.ins
%doc %{_texmfdistdir}/source/latex/adjustbox/trimclip.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
