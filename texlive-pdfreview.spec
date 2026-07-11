%global tl_name pdfreview
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Annotate PDF files with margin notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfreview
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfreview.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfreview.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package lets you add comments in the page margins of PDF files,
e.g. when reviewing manuscripts or grading reports. The PDF file to be
annotated is included, one page at a time, as graphics, in a manner
similar to the pdfpages package. Notes are placed in the margin next to
the included graphics using a grid of help lines. Alternatively, only
numbers are placed in the page margins, and the notes are collected into
a numbered list at the end of the document. Note that this package is
not intended for adding notes directly to the LaTeX source of the
document that is being reviewed; instead, the document undergoing review
is already in PDF format and remains unchanged. Also note that this
package does not produce the usual PDF "sticky notes" that must be
opened by clicking on them; instead, the notes are simply shown as text.
This package depends on the following other LaTeX package: adjustbox,
calc, geometry, graphicx, grffile, ifthen, kvoptions, tikz, ulem, and
xstring.

