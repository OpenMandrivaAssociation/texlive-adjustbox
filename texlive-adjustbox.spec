%global tl_name adjustbox
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3c
Release:	%{tl_revision}.1
Summary:	Graphics package-alike macros for general boxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/adjustbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adjustbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(collectbox)
Requires:	texlive(graphics)
Requires:	texlive(xkeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides several macros to adjust boxed content. One purpose
is to supplement the standard graphics package, which defines the macros
\resizebox, \scalebox and \rotatebox , with the macros\trimbox and
\clipbox. The main feature is the general \adjustbox macro which extends
the "key=value" interface of \includegraphics from the graphics package
and applies it to general text content. Additional provided box macros
are \lapbox, \marginbox, \minsizebox, \maxsizebox and \phantombox. All
macros use the collectbox package to read the content as a box and not
as a macro argument. This allows for all forms of content including
special material like verbatim content. A special feature of collectbox
is used to provide matching environments with the identical names as the
macros.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/adjustbox
%dir %{_datadir}/texmf-dist/source/latex/adjustbox
%dir %{_datadir}/texmf-dist/tex/latex/adjustbox
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/DEPENDS.txt
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/adjcalc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/adjustbox.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/box.tex
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/compare.tex
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/margin.tex
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/margin2.tex
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/trim.tex
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/trim2.tex
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/trim3.tex
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/trimclip.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/viewport.tex
%doc %{_datadir}/texmf-dist/doc/latex/adjustbox/viewport2.tex
%doc %{_datadir}/texmf-dist/source/latex/adjustbox/adjcalc.dtx
%doc %{_datadir}/texmf-dist/source/latex/adjustbox/adjustbox.dtx
%doc %{_datadir}/texmf-dist/source/latex/adjustbox/adjustbox.ins
%doc %{_datadir}/texmf-dist/source/latex/adjustbox/trimclip.dtx
%{_datadir}/texmf-dist/tex/latex/adjustbox/adjcalc.sty
%{_datadir}/texmf-dist/tex/latex/adjustbox/adjustbox.sty
%{_datadir}/texmf-dist/tex/latex/adjustbox/tc-dvips.def
%{_datadir}/texmf-dist/tex/latex/adjustbox/tc-luatex.def
%{_datadir}/texmf-dist/tex/latex/adjustbox/tc-pdftex.def
%{_datadir}/texmf-dist/tex/latex/adjustbox/tc-pgf.def
%{_datadir}/texmf-dist/tex/latex/adjustbox/tc-xetex.def
%{_datadir}/texmf-dist/tex/latex/adjustbox/trimclip.sty
