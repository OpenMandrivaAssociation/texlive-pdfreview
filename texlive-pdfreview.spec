Name:		texlive-pdfreview
Version:	50100
Release:	2
Summary:	Annotate PDF files with margin notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfreview
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfreview.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfreview.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package lets you add comments in the page margins of PDF
files, e.g. when reviewing manuscripts or grading reports. The
PDF file to be annotated is included, one page at a time, as
graphics, in a manner similar to the pdfpages package. Notes
are placed in the margin next to the included graphics using a
grid of help lines. Alternatively, only numbers are placed in
the page margins, and the notes are collected into a numbered
list at the end of the document. Note that this package is not
intended for adding notes directly to the LaTeX source of the
document that is being reviewed; instead, the document
undergoing review is already in PDF format and remains
unchanged. Also note that this package does not produce the
usual PDF "sticky notes" that must be opened by clicking on
them; instead, the notes are simply shown as text. This package
depends on the following other LaTeX package: adjustbox, calc,
geometry, graphicx, grffile, ifthen, kvoptions, tikz, ulem, and
xstring.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pdfreview
%doc %{_texmfdistdir}/doc/latex/pdfreview

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
