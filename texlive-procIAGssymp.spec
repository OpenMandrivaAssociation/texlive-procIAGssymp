# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/procIAGssymp
# catalog-date 2007-01-06 21:10:04 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-procIAGssymp
Version:	20070106
Release:	1
Summary:	Macros for IAG symposium papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/procIAGssymp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/procIAGssymp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/procIAGssymp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This package provides (re-)definitions of some LaTeX commands
that can be useful for the preparation of a paper with the
style of the proceeding of symposia sponsored by the
'International Association of Geodesy (IAG)' published by
Springer-Verlag.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/procIAGssymp/procIAGssymp.sty
%doc %{_texmfdistdir}/doc/latex/procIAGssymp/TestPaper.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
