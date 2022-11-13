Name:		texlive-imakeidx
Version:	42287
Release:	1
Summary:	A package for producing multiple indexes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/imakeidx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to produce and typeset one or more
indexes simultaneously with a document. The package is known to
work in LaTeX documents processed with pdflatex, xelatatex and
lualatex. If makeindex is used for processing the index
entries, no particular setting up is needed when TeX Live is
used. Using xindy or other programs it is necessary to enable
shell escape; shell escape is also needed if splitindex is
used.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/imakeidx
%doc %{_texmfdistdir}/doc/latex/imakeidx
#- source
%doc %{_texmfdistdir}/source/latex/imakeidx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
