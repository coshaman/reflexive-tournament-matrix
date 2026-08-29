# Top-tier review-bar audit

Date: 2026-08-29

This document records the external criteria used for the adversarial review.
They are calibration evidence, not a prediction of any editor's decision.

## Journal of Combinatorial Theory, Series B

The official Elsevier journal description places Series B in graph,
hypergraph, and matroid theory and says its standards are very high. It says
accepted papers are generally expected to solve or make an important step
toward an open problem, develop a new proof technique, or substantially
advance knowledge. It also describes an editorial pre-screen before detailed
refereeing.

Source: https://shop.elsevier.com/journals/journal-of-combinatorial-theory-series-b/0095-8956

Implication for this project: correctness of the counterexample is necessary,
but a classical first-moment argument applied to a new parameter must also
demonstrate a defensible advance and careful priority positioning.

## Combinatorica

Springer's official journal page describes Combinatorica as covering
combinatorics and theory of computing, emphasizing general techniques and
unifying principles, and explicitly listing randomization and explicit
construction in combinatorics and algorithms.

Source: https://link.springer.com/journal/493

Implication: the manuscript should foreground the reusable tensor obstruction
and the exact parameter translation, not only the numerical example.

## SODA

The official SODA 2027 submission page says selection considers whether the
results and presentation yield new insights for efficient algorithms and
welcomes discrete mathematics. It requires a clear early presentation of
merits, importance in prior work, and key technical/conceptual ideas, and says
proofs should permit the main claims to be fully verified.

Source: https://www.siam.org/conferences-events/siam-conferences/soda27/submissions/

Implication: the computational package must be reproducible, and the first
pages must state the exact conjectures, contribution, and limits of the
existential construction.

## STOC/FOCS-style theory standard

The official ACM SIGACT STOC best-paper criteria identify as top-rated work
that introduces a strong new technique, solves a long-standing open problem,
or introduces and solves an interesting and important new problem.

Source: https://www.sigact.sigact.hosting.acm.org/prizes/best_paper.html

The IEEE FOCS criteria page was inaccessible in this environment, so no claim
about a current FOCS policy is made here. The STOC source is used as the
available official SIGACT proxy, not as a substitute quotation of FOCS rules.

## General peer-review criteria

Elsevier's official reviewer guidance describes validity, significance,
originality, scientific value, correct citation, and adherence to journal
practice as review considerations.

Source: https://researcheracademy.elsevier.com/uploads/2018-04/Understanding%20the%20Publishing%20Process_Apr2018_Web.pdf

## Working review rubric

The internal reviewers therefore apply five gates: (i) every central lemma is
proved from the stated definitions; (ii) every historical and priority claim
is source-supported; (iii) the contribution is more than a relabeling of a
classical mechanism; (iv) computation independently checks implementation
rather than proving the probabilistic existence result; and (v) the exposition
makes the exact scope and limitations clear within the opening pages.
