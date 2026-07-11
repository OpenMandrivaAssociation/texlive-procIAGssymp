%global tl_name prociagssymp
%global tl_revision 70888

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for IAG symposium papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/prociagssymp
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prociagssymp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prociagssymp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prociagssymp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides (re-)definitions of some LaTeX commands that can
be useful for the preparation of papers with the style of the
proceedings of symposia sponsored by the 'International Association of
Geodesy (IAG)' published by Springer-Verlag.

