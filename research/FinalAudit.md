# Final release audit

Date: 2026-08-29

## Mathematical result

- Matrix: reflexive tournament matrix `M` of order `n = 1937`.
- Parameter: `tau(M) <= 44`, while `tau(M tensor M^T) >= 1937`.
- Multiplicative violation: at least `1937 / 44^2 > 1`.
- Asymptotic statement: for every fixed epsilon > 0 and all sufficiently
  large `n`, an existential tournament has `tau(M) = O(log n)` and the
  tensor violation is `Omega(n/log^2 n)`.
- Graph translations: a connected co-bipartite `K(M)` on 3874 vertices gives a
  strong-product violation; `B(M)` gives a bipartite direct-product violation.

## Verification

`verify.py` and the independently implemented `verify_independent.py` both
pass all 33,867 labeled tournaments for orders 1 through 6, with the order-6
quotient covering all 32,768 tournaments in 56 relabeling classes. These are
finite indexing/mutation checks; neither constructs the existential matrix of
order 1937.

## Review and positioning

Round-1 scores recorded from six independent reviewers were 4, 3, 4, 2, 2,
and 3 (mean 3.0/5). The common mathematical weakness was exposition in the
`K(M)` translation, now expanded. The common publication weakness was novelty:
the first-moment and tensor ingredients are classical and priority is not
established. Final status is therefore `SPECIALIST_LEVEL`.

## Artifact

The clean Tectonic build produces `main.pdf` with 7 letter-size pages. All
seven rendered pages were visually inspected; no clipping or overlap was
found. Minor overfull-box warnings remain in the abstract and transpose lemma
paragraphs, without visible layout damage.
