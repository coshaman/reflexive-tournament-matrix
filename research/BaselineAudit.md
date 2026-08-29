# Baseline audit

Date: 2026-08-29

This audit freezes the package before the adversarial revision requested in
the pasted specification. Existing files are preserved; this document records
the state observed before any mathematical revision.

## Files and dependencies

The package contained `main.tex`, `references.bib`, `verify.py`, `README.md`,
and the compiled `main.pdf`, plus Tectonic-generated auxiliary files. The
workspace was not a Git repository, and no external Python packages were
required by `verify.py`; it used only the Python standard library. PDF builds
used Tectonic, which downloaded LaTeX packages when permitted.

## Baseline theorem claims

1. `tau(A)` is the maximum triangular witness / expanding-row sequence.
2. A reflexive random tournament matrix of order 1937 exists with
   `tau(M) <= 44`.
3. The diagonal restriction of `M tensor M^T` is an identity matrix, so its
   `tau` is at least 1937.
4. This is claimed to disprove hypergraph, total-Grundy direct-product, and
   Grundy strong-product multiplicativity.
5. An asymptotic `Omega(n/log^2 n)` violation is claimed.
6. The manuscript explicitly disclaims an explicit 1937-by-1937 matrix and
   calls the tournament/tensor mechanisms classical.

## Baseline external claims

The manuscript cited the original strong-product paper, the total-Grundy
paper and DOI, the forest-factor paper, the withdrawn 2022/2023 proof attempt,
two fooling-set/rank papers, and the 2026 semi-ladder-index paper.

## Baseline computation

`python verify.py` reported:

```text
PASS: checked 33867 reflexive tournaments for every n=1,...,6
PASS: n=6 quotient checked in 56 relabeling classes (56 classes cover 32768 tournaments)
PASS: transpose, tensor identity, K(M), and strong-product witnesses
PASS: direct-product type decomposition uses M tensor M and M tensor M^T
NOTE: no finite matrix of order 1937 is constructed by this script
```

The verifier used exact direct Grundy search for the current version, after a
mask-transition bug was corrected. It checked order-6 isomorphism-class
representatives rather than all labeled instances individually.

## Baseline PDF

`main.pdf` was six pages, letter size, and was produced by Tectonic with exit
code 0. Visual rendering showed no clipping or overlap. The build emitted
minor nonfatal overfull-box/font warnings.

## Freeze note

No baseline statement is treated as independently validated by this audit.
The next phases specifically test the mixed-clique graph argument, the exact
semi-ladder terminology, priority claims, and the direct-product translation.
