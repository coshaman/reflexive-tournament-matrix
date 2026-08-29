# Grundy Product Counterexample Research Note Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a self-contained LaTeX research note and reproducible sanity-check package proving, by the probabilistic method, that the hypergraph expanding-sequence product conjecture and its equivalent Grundy total-domination direct-product and Grundy domination strong-product conjectures are false.

**Architecture:** The proof is written in `main.tex` with numbered definitions, lemmas, theorems, and corollaries. `verify.py` independently implements exhaustive tournament enumeration through order six, exact expanding-sequence dynamic programming, incidence/direct/strong products, and the requested identities. `references.bib` records only metadata verified against the cited arXiv/DOI landing pages, while `README.md` gives exact build and verification commands.

**Tech Stack:** LaTeX (`pdflatex` plus `bibtex`), Python 3 standard library, arXiv/DOI metadata.

**Spec:** `C:\Users\owner\.codex\attachments\57421b90-473a-4e52-bc5e-77eefc119b8f\pasted-text-1.txt`

## Global Constraints

- The finite counterexample is existential; do not claim an explicit 1937x1937 matrix.
- Prove the complete overlap argument for the random reflexive tournament matrix.
- Use the exact identity block for `M tensor M^T`, and distinguish it from `M tensor M` in the direct-product decomposition.
- State the novelty as repurposing the classical random fooling-set/tournament and tensor identity mechanisms for the expanding-sequence/semi-ladder parameter.
- Treat computation only as a mutation/indexing sanity check, never as evidence for the order-1937 existence theorem.
- Verify all inequality directions, Kronecker indices, and bibliography metadata before delivery.

### Task 1: Draft the mathematical note

**Files:**
- Create: `main.tex`
- Create: `references.bib`

**Interfaces:**
- `main.tex` cites bibliography keys from `references.bib`.
- The proof must expose the random theorem, both graph corollaries, asymptotic theorem, and related-work distinctions.

- [ ] **Step 1:** Write definitions and the transpose lemma, including the triangular-witness characterization of expanding-row/hyperedge sequences.
- [ ] **Step 2:** Write the random-tournament union bound with all four overlap cases and the `n=1937`, `k=45` calculation.
- [ ] **Step 3:** Write the tensor identity, hypergraph counterexample, co-bipartite construction, strong-product witness, and connectedness/order statement.
- [ ] **Step 4:** Write the incidence-graph direct-product component decomposition and the `2t^2+2n` lower bound.
- [ ] **Step 5:** Write the asymptotic logarithmic expansion and related-work section with cautious novelty language.
- [ ] **Step 6:** Add verified bibliography entries for all seven requested sources, including the 2018 DMGT DOI entry and explicit withdrawal status for the 2022/2023 attempt.

### Task 2: Build the exhaustive verifier

**Files:**
- Create: `verify.py`

**Interfaces:**
- `tau(matrix) -> int` computes the exact maximum triangular witness length.
- `transpose(matrix)`, `tensor(a,b)`, `incidence_graph(matrix)`, and graph-product helpers use explicit row-major index formulas.
- `main()` exhaustively checks all tournaments through `n=6` and prints a concise pass summary.

- [ ] **Step 1:** Implement exact `tau` by enumerating injective row/column tuples for small matrices.
- [ ] **Step 2:** Implement tournament generation, transpose symmetry, and diagonal tensor witness checks.
- [ ] **Step 3:** Implement `K(M)` and exact Grundy domination checks by legal-sequence dynamic programming; verify `gamma_gr(K(M))=tau(M)` for every tournament through six.
- [ ] **Step 4:** Implement strong-product neighborhoods and verify the `z_i,w_j` identity and legal witness.
- [ ] **Step 5:** Implement incidence/direct-product component classification and verify the two tensor factors are `M tensor M` and `M tensor M^T`.
- [ ] **Step 6:** Add assertions for all requested inequalities and a clear statement that the script does not certify the existential order-1937 object.

### Task 3: Add reproducibility instructions

**Files:**
- Create: `README.md`

**Interfaces:**
- Commands must be copy-pastable from the package directory.

- [ ] **Step 1:** Document `python verify.py` and expected output.
- [ ] **Step 2:** Document the `pdflatex`/`bibtex` compilation sequence and generated `main.pdf`.
- [ ] **Step 3:** Document the logical status of the exhaustive check versus the probabilistic proof.

### Task 4: Verify and compile

**Files:**
- Generated: `main.aux`, `main.bbl`, `main.log`, `main.out`, `main.pdf`, `main.toc`

- [ ] **Step 1:** Run `python verify.py`; inspect exit status and every assertion summary.
- [ ] **Step 2:** Compile twice with `pdflatex` around `bibtex`; inspect log for undefined citations/references and overfull critical content.
- [ ] **Step 3:** Extract PDF text or inspect page count to confirm the delivered PDF contains all major sections and theorem labels.
- [ ] **Step 4:** Re-read the spec and check every requested artifact, proof, citation, warning, and inequality before claiming completion.
