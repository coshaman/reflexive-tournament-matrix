# Grundy product counterexample

This directory contains the research note and two independent exhaustive verifiers.
The proof is probabilistic: it establishes existence of a reflexive tournament
matrix of order 1937, but does not print or construct that matrix.

## Verify the indexing sanity checks

```powershell
python verify.py
```

```powershell
python verify_independent.py
```

The script exhaustively enumerates every reflexive tournament for each
`n=1,...,6`; at `n=6` it checks one representative from each simultaneous
vertex-relabeling orbit, whose 56 orbits cover all 32,768 tournaments because
the tested properties are invariant under relabeling. It checks transpose invariance of `tau`, the `M tensor M^T`
identity witness, the co-bipartite Grundy identity, the strong-product
`z_i,w_j` witnesses, and the direct-product type decomposition. The second
program uses separate brute-force implementations for `tau`, graph legality,
and product components. These checks are mutation/indexing checks only, not
evidence for the probabilistic order-1937 existence theorem.

## Compile the note

With a standard TeX installation:

```powershell
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

In this environment the equivalent one-command build is:

```powershell
$env:FONTCONFIG_FILE = (Join-Path (Get-Location) 'fontconfig-release.conf')
tectonic --keep-logs --keep-intermediates main.tex
```

The final artifact is `main.pdf`.

## Package contents

`main.tex` and `references.bib` contain the note; `verify.py` and
`verify_independent.py` are independent small-order exhaustive checks;
`research/` records the baseline, literature/venue audit, and reviewer loop.
The unrelated source archive and extracted material are retained locally but
are excluded from version control.
