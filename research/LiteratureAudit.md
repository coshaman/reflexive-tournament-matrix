# Literature and priority audit

Date: 2026-08-29

## Established source facts

- Brešar et al., *On Grundy total domination number in product graphs*, arXiv:1712.08780 and its published Discussiones Mathematicae Graph Theory version, states the direct-product lower bound and conjectures equality. The same paper gives the hypergraph edge-covering formulation and explains the incidence-graph equivalence to the graph product questions.
- Brešar et al., *Dominating sequences in grid-like and toroidal graphs*, EJC 23 (2016), is the source of the strong-product conjecture used here.
- Bell et al., EJC 28 (2021), proves the strong-product equality for forests. Herrman--Smith arXiv:2212.04565v2 is marked withdrawn and records an error in the attempted general proof.
- Chalermsook, Laekhanukit, and Nanongkai, SODA 2013, explicitly relate the relevant maximum expanding-sequence matrix pattern to a semi-induced matching. This is not automatically identical to every later standard definition of semi-ladder index.
- The tensor identity for a reflexive tournament, `M[i,j] M[j,i] = delta[i,j]`, is a classical fooling-set construction. The present note's contribution is its application to the Grundy/expanding-sequence product parameter, not a new tensor mechanism.

## Priority conclusion

Searches covered the original conjecture papers, their citations, graph-product/semi-induced-matching terminology, fooling-set literature, forest results, and the withdrawn proof attempt. No located source supplied a counterexample to these conjectures. That negative search is not proof of priority. Accordingly, the paper makes no “first” claim and says only that it provides a counterexample.

## Terminology decision

The paper uses “expanding sequence” and, where useful, “semi-induced matching.” It does not assert an unqualified equivalence with the standard semi-ladder index.

## Venue audit

The official JCTB scope and editorial guidance emphasize important open problems, new proof techniques, or substantial advances; Combinatorica emphasizes general techniques and unifying principles; SODA asks for clear new insights and fully verifiable proofs; SIGACT's STOC best-paper criteria emphasize strong new techniques or important open problems. The present result is mathematically meaningful but uses a classical first-moment/tensor mechanism, so the realistic positioning is specialist combinatorics rather than an unsupported top-tier priority claim. Sources and the detailed rubric are in `research/TopTierCriteria.md`.
