# revision 26275
# category Package
# catalog-ctan /macros/latex/contrib/imakeidx
# catalog-date 2012-05-09 14:48:06 +0200
# catalog-license lppl1.3
# catalog-version 1.0a
Name:		texlive-imakeidx
Version:	1.0a
Release:	2
Summary:	A package for producing multiple indexes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/imakeidx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imakeidx.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to produce and typeset one or more
indexes simultaneously with a document. The package is known to
work in LaTeX documents processed with pdflatex, xelatatex and
lualatex. If makeindex is used for processing the index
entries, no particular setting up is needed when TeX Live 2010
is used. Using xindy or other programs it is necessary to
enable shell escape; shell escape is also needed if splitindex
is used.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/imakeidx/imakeidx.sty
%doc %{_texmfdistdir}/doc/latex/imakeidx/README
%doc %{_texmfdistdir}/doc/latex/imakeidx/imakeidx.pdf
#- source
%doc %{_texmfdistdir}/source/latex/imakeidx/imakeidx.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 804851
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752732
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718710
- texlive-imakeidx
- texlive-imakeidx
- texlive-imakeidx
- texlive-imakeidx

