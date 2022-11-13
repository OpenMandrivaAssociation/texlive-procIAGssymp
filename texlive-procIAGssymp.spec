Name:		texlive-procIAGssymp
Version:	63242
Release:	1
Summary:	Macros for IAG symposium papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/procIAGssymp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prociagssymp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prociagssymp.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/prociagssymp
%doc %{_texmfdistdir}/doc/latex/prociagssymp

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
