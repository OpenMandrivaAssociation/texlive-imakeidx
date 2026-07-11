%global tl_name imakeidx
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3e
Release:	%{tl_revision}.1
Summary:	A package for producing multiple indexes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/imakeidx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to produce and typeset one or more indexes
simultaneously with a document. The package is known to work in LaTeX
documents processed with pdfLaTeX, XeLaTeX and LuaLaTeX. If makeindex is
used for processing the index entries, no particular setting up is
needed when TeX Live is used. Using xindy or other programs it is
necessary to enable shell escape; shell escape is also needed if
splitindex is used.

