#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Type-driven code generation for OCaml
Summary(pl.UTF-8):	Generowanie kodu dla OCamla sterowane typami
Name:		ocaml-ppx_deriving
Version:	5.2.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ocaml-ppx/ppx_deriving/releases
Source0:	https://github.com/ocaml-ppx/ppx_deriving/releases/download/v%{version}/ppx_deriving-v%{version}.tbz
# Source0-md5:	041756e958b3ab1c1d76162d24ec7bd8
URL:		https://github.com/ocaml-ppx/ppx_deriving
BuildRequires:	cppo
BuildRequires:	ocaml >= 1:4.05.0
BuildRequires:	ocaml-dune >= 1.6.3
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ppx_derivers-devel
BuildRequires:	ocaml-ppxlib-devel >= 0.20.0
BuildRequires:	ocaml-result-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_deriving provides common infrastructure for generating code based
on type definitions, and a set of useful plugins for common tasks.

This package contains files needed to run bytecode executables using
ppx_deriving library.

%description -l pl.UTF-8
ppx_deriving zapewnia wspólną infrastrukturę do generowania kodu w
oparciu o definicje typów oraz przydatne wtyczki do częstych zadań.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_deriving.

%package devel
Summary:	Type-driven code generation for OCaml - development part
Summary(pl.UTF-8):	Generowanie kodu dla OCamla sterowane typami - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-ppx_derivers-devel
Requires:	ocaml-ppxlib-devel >= 0.20.0
Requires:	ocaml-result-devel

%description devel
This package contains files needed to develop OCaml programs using
ppx_deriving library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_deriving.

%prep
%setup -q -n ppx_deriving-v%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr src_examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_deriving/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_deriving

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.txt README.md
%dir %{_libdir}/ocaml/ppx_deriving
%{_libdir}/ocaml/ppx_deriving/META
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/ppx_deriving
%dir %{_libdir}/ocaml/ppx_deriving/api
%{_libdir}/ocaml/ppx_deriving/api/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/create
%{_libdir}/ocaml/ppx_deriving/create/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/enum
%{_libdir}/ocaml/ppx_deriving/enum/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/eq
%{_libdir}/ocaml/ppx_deriving/eq/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/fold
%{_libdir}/ocaml/ppx_deriving/fold/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/iter
%{_libdir}/ocaml/ppx_deriving/iter/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/make
%{_libdir}/ocaml/ppx_deriving/make/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/map
%{_libdir}/ocaml/ppx_deriving/map/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/ord
%{_libdir}/ocaml/ppx_deriving/ord/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/runtime
%{_libdir}/ocaml/ppx_deriving/runtime/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/show
%{_libdir}/ocaml/ppx_deriving/show/*.cma
%dir %{_libdir}/ocaml/ppx_deriving/std
%{_libdir}/ocaml/ppx_deriving/std/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/api/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/create/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/enum/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/eq/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/fold/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/iter/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/make/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/map/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/ord/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/runtime/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/show/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_deriving/std/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_deriving/api/*.cmi
%{_libdir}/ocaml/ppx_deriving/api/*.cmt
%{_libdir}/ocaml/ppx_deriving/api/*.cmti
%{_libdir}/ocaml/ppx_deriving/api/*.mli
%{_libdir}/ocaml/ppx_deriving/create/*.cmi
%{_libdir}/ocaml/ppx_deriving/create/*.cmt
%{_libdir}/ocaml/ppx_deriving/enum/*.cmi
%{_libdir}/ocaml/ppx_deriving/enum/*.cmt
%{_libdir}/ocaml/ppx_deriving/eq/*.cmi
%{_libdir}/ocaml/ppx_deriving/eq/*.cmt
%{_libdir}/ocaml/ppx_deriving/fold/*.cmi
%{_libdir}/ocaml/ppx_deriving/fold/*.cmt
%{_libdir}/ocaml/ppx_deriving/iter/*.cmi
%{_libdir}/ocaml/ppx_deriving/iter/*.cmt
%{_libdir}/ocaml/ppx_deriving/make/*.cmi
%{_libdir}/ocaml/ppx_deriving/make/*.cmt
%{_libdir}/ocaml/ppx_deriving/map/*.cmi
%{_libdir}/ocaml/ppx_deriving/map/*.cmt
%{_libdir}/ocaml/ppx_deriving/ord/*.cmi
%{_libdir}/ocaml/ppx_deriving/ord/*.cmt
%{_libdir}/ocaml/ppx_deriving/runtime/*.cmi
%{_libdir}/ocaml/ppx_deriving/runtime/*.cmt
%{_libdir}/ocaml/ppx_deriving/runtime/*.cmti
%{_libdir}/ocaml/ppx_deriving/runtime/*.mli
%{_libdir}/ocaml/ppx_deriving/show/*.cmi
%{_libdir}/ocaml/ppx_deriving/show/*.cmt
%{_libdir}/ocaml/ppx_deriving/std/*.cmi
%{_libdir}/ocaml/ppx_deriving/std/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_deriving/api/ppx_deriving_api.a
%{_libdir}/ocaml/ppx_deriving/api/*.cmx
%{_libdir}/ocaml/ppx_deriving/api/*.cmxa
%{_libdir}/ocaml/ppx_deriving/create/ppx_deriving_create.a
%{_libdir}/ocaml/ppx_deriving/create/*.cmx
%{_libdir}/ocaml/ppx_deriving/create/*.cmxa
%{_libdir}/ocaml/ppx_deriving/enum/ppx_deriving_enum.a
%{_libdir}/ocaml/ppx_deriving/enum/*.cmx
%{_libdir}/ocaml/ppx_deriving/enum/*.cmxa
%{_libdir}/ocaml/ppx_deriving/eq/ppx_deriving_eq.a
%{_libdir}/ocaml/ppx_deriving/eq/*.cmx
%{_libdir}/ocaml/ppx_deriving/eq/*.cmxa
%{_libdir}/ocaml/ppx_deriving/fold/ppx_deriving_fold.a
%{_libdir}/ocaml/ppx_deriving/fold/*.cmx
%{_libdir}/ocaml/ppx_deriving/fold/*.cmxa
%{_libdir}/ocaml/ppx_deriving/iter/ppx_deriving_iter.a
%{_libdir}/ocaml/ppx_deriving/iter/*.cmx
%{_libdir}/ocaml/ppx_deriving/iter/*.cmxa
%{_libdir}/ocaml/ppx_deriving/make/ppx_deriving_make.a
%{_libdir}/ocaml/ppx_deriving/make/*.cmx
%{_libdir}/ocaml/ppx_deriving/make/*.cmxa
%{_libdir}/ocaml/ppx_deriving/map/ppx_deriving_map.a
%{_libdir}/ocaml/ppx_deriving/map/*.cmx
%{_libdir}/ocaml/ppx_deriving/map/*.cmxa
%{_libdir}/ocaml/ppx_deriving/ord/ppx_deriving_ord.a
%{_libdir}/ocaml/ppx_deriving/ord/*.cmx
%{_libdir}/ocaml/ppx_deriving/ord/*.cmxa
%{_libdir}/ocaml/ppx_deriving/runtime/ppx_deriving_runtime.a
%{_libdir}/ocaml/ppx_deriving/runtime/*.cmx
%{_libdir}/ocaml/ppx_deriving/runtime/*.cmxa
%{_libdir}/ocaml/ppx_deriving/show/ppx_deriving_show.a
%{_libdir}/ocaml/ppx_deriving/show/*.cmx
%{_libdir}/ocaml/ppx_deriving/show/*.cmxa
%{_libdir}/ocaml/ppx_deriving/std/ppx_deriving_std.a
%{_libdir}/ocaml/ppx_deriving/std/*.cmx
%{_libdir}/ocaml/ppx_deriving/std/*.cmxa
%endif
%{_libdir}/ocaml/ppx_deriving/dune-package
%{_libdir}/ocaml/ppx_deriving/opam
%{_examplesdir}/%{name}-%{version}
