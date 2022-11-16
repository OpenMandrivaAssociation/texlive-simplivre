Name:		texlive-simplivre
Version:	64280
Release:	1
Summary:	Write your books in a simple and clear way
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simplivre
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplivre.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplivre.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class for typesetting books with
a simple and clear design. Currently, it has native support for
Chinese (simplified and traditional), English, French, German,
Italian, Japanese, Portuguese (European and Brazilian), Russian
and Spanish typesetting. It compiles with either XeLaTeX or
LuaLaTeX. This is part of the minimalist class series and
depends on minimalist.sty from the minimalist package. The
package name "simplivre" is taken from the French words
"simple" and "livre" (= "book").

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/simplivre
%doc %{_texmfdistdir}/doc/latex/simplivre

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
