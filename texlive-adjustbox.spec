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
BuildSystem:	texlive
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

