# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/procIAGssymp
# catalog-date 2007-01-06 21:10:04 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-procIAGssymp
Version:	20070106
Release:	3
Summary:	Macros for IAG symposium papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/procIAGssymp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/procIAGssymp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/procIAGssymp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides (re-)definitions of some LaTeX commands
that can be useful for the preparation of a paper with the
style of the proceeding of symposia sponsored by the
'International Association of Geodesy (IAG)' published by
Springer-Verlag.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/procIAGssymp/procIAGssymp.sty
%doc %{_texmfdistdir}/doc/latex/procIAGssymp/TestPaper.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070106-2
+ Revision: 755069
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070106-1
+ Revision: 719303
- texlive-procIAGssymp
- texlive-procIAGssymp
- texlive-procIAGssymp
- texlive-procIAGssymp

