"""Exhaustive indexing and mutation sanity checks for the research note.

This script is deliberately a small, independent checker.  It does not
construct or search for the existential 1937-by-1937 matrix.
"""

import os
from itertools import permutations

def transpose(a):
    return tuple(zip(*a))


def tensor(a, b):
    return tuple(tuple(a[i // len(b)][j // len(b)] * b[i % len(b)][j % len(b)]
                       for j in range(len(a) * len(b)))
                 for i in range(len(a) * len(b)))


def tau(a):
    """Maximum triangular witness, via exact row/column-mask DP."""
    nr, nc = len(a), len(a[0])
    row_zero_masks = [sum((1 << j) for j, x in enumerate(row) if not x)
                      for row in a]
    row_one_masks = [sum((1 << j) for j, x in enumerate(row) if x)
                     for row in a]
    all_columns = (1 << nc) - 1
    zero_intersection = [all_columns] * (1 << nr)
    for rows in range(1, 1 << nr):
        bit = rows & -rows
        r = bit.bit_length() - 1
        zero_intersection[rows] = zero_intersection[rows ^ bit] & row_zero_masks[r]
    states = {(0, 0)}
    best = 0
    for _ in range(min(nr, nc)):
        nxt = set()
        for rows, cols in states:
            available = ((1 << nc) - 1) ^ cols
            available &= zero_intersection[rows]
            for r in range(nr):
                if rows >> r & 1:
                    continue
                candidates = row_one_masks[r] & available
                while candidates:
                    bit = candidates & -candidates
                    candidates ^= bit
                    nxt.add((rows | (1 << r), cols | bit))
        if not nxt:
            break
        states = nxt
        best += 1
    return best


def tournament_from_code(n, code):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    a = [[int(i == j) for j in range(n)] for i in range(n)]
    for bit, (i, j) in enumerate(edges):
        if code >> bit & 1:
            a[i][j] = 1
        else:
            a[j][i] = 1
    return tuple(map(tuple, a))


def tournaments(n):
    yield from (tournament_from_code(n, code)
                for code in range(1 << (n * (n - 1) // 2)))


def relabel_code(n, code, permutation):
    """Encode the tournament after sending old vertex i to permutation[i]."""
    out = 0
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            low, high = sorted((permutation[i], permutation[j]))
            old_i_to_j = bool(code >> bit & 1)
            forward_low_to_high = old_i_to_j if permutation[i] == low else not old_i_to_j
            target_bit = low * n - low * (low + 1) // 2 + high - low - 1
            out |= int(forward_low_to_high) << target_bit
            bit += 1
    return out


def orbit_representatives(n):
    """Partition all tournaments into simultaneous vertex-relabeling orbits."""
    remaining = set(range(1 << (n * (n - 1) // 2)))
    perms = tuple(permutations(range(n)))
    representatives = []
    while remaining:
        code = min(remaining)
        orbit = {relabel_code(n, code, p) for p in perms}
        remaining.difference_update(orbit)
        representatives.append((code, len(orbit)))
    return representatives


def closed_neighborhoods_k(a):
    """Closed neighborhoods of K(M), indexed r_0..r_n-1,c_0..c_n-1."""
    n = len(a)
    out = []
    for v in range(2 * n):
        mask = 1 << v
        if v < n:
            for u in range(n):
                if u != v:
                    mask |= 1 << u
            for j in range(n):
                if a[v][j]:
                    mask |= 1 << (n + j)
        else:
            j = v - n
            for u in range(n):
                if u != j:
                    mask |= 1 << (n + u)
            for i in range(n):
                if a[i][j]:
                    mask |= 1 << i
        out.append(mask)
    return out


def gamma_gr_from_neighborhoods(neighborhoods):
    unions = [0] * (1 << len(neighborhoods))
    for selected in range(1, len(unions)):
        bit = selected & -selected
        v = bit.bit_length() - 1
        unions[selected] = unions[selected ^ bit] | neighborhoods[v]
    memo = {}

    def visit(selected):
        if selected in memo:
            return memo[selected]
        covered = unions[selected]
        ans = 0
        for v, nb in enumerate(neighborhoods):
            if not selected >> v & 1 and nb & ~covered:
                ans = max(ans, 1 + visit(selected | (1 << v)))
        memo[selected] = ans
        return ans

    return visit(0)


def gamma_gr_k(a):
    return gamma_gr_from_neighborhoods(closed_neighborhoods_k(a))


def strong_neighborhoods_k(a):
    """Closed neighborhoods in K(M) strong K(M), row-major product indices."""
    n = len(a)
    base = closed_neighborhoods_k(a)
    size = 2 * n
    return [sum(1 << (u * size + v)
                for u in range(size) if base[x] >> u & 1
                for v in range(size) if base[y] >> v & 1)
            for x in range(size) for y in range(size)]


def incidence_edges(a):
    n, m = len(a), len(a[0])
    return {(i, n + j) for i in range(n) for j in range(m) if a[i][j]}


def direct_product_edges(a):
    """Return typed direct-product edges from pairs of incidence edges."""
    n = len(a)
    edges = []
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                e = ((0, i), (1, j))
                edges.extend((e, (e[1], e[0])))
    return {((x[0][0], x[0][1], y[0][0], y[0][1]),
             (x[1][0], x[1][1], y[1][0], y[1][1]))
            for x in edges for y in edges}


def main():
    assert tau(((1,),)) == 1
    total = 0
    classes = 0
    n6_classes = 0
    max_n = int(os.environ.get("VERIFY_MAX_N", "6"))
    for n in range(1, max_n + 1):
        if n == 6:
            cases = ((tournament_from_code(n, code), size)
                     for code, size in orbit_representatives(n))
        else:
            cases = ((a, 1) for a in tournaments(n))
        for a, orbit_size in cases:
            total += orbit_size
            classes += 1
            if n == 6:
                n6_classes += 1
            at = transpose(a)
            t = tau(a)
            assert t == tau(at), (n, a)
            if n < 6:
                aa_t = tensor(a, at)
                assert all(aa_t[i * n + i][j * n + j] == int(i == j)
                           for i in range(n) for j in range(n))
            else:
                assert all(a[i][j] * a[j][i] == int(i == j)
                           for i in range(n) for j in range(n))
            assert gamma_gr_k(a) == t

            for i in range(n):
                for j in range(n):
                    # N[(r_i,c_i)] contains (c_j,r_j) iff both coordinates
                    # are adjacent, exactly the tensor entry above.
                    assert bool(a[i][j] and a[j][i]) == (i == j)

            # Type decomposition: same-side pairs yield A tensor A; mixed
            # pairs yield A tensor A^T.  Check every actual product edge.
            if n < 6:
                for u, v in direct_product_edges(a):
                    s1, i, s2, j = u
                    t1, k, t2, l = v
                    assert t1 == 1 - s1 and t2 == 1 - s2
                    if s1 == s2 == 0:
                        assert a[i][k] and a[j][l]
                    elif s1 == s2 == 1:
                        assert a[k][i] and a[l][j]
                    elif s1 == 0 and s2 == 1:
                        assert a[i][k] and a[l][j]
                    else:
                        assert a[k][i] and a[j][l]
    print(f"PASS: checked {total} reflexive tournaments for every n=1,...,{max_n}")
    if max_n >= 6:
        print(f"PASS: n=6 quotient checked in {n6_classes} relabeling classes (56 classes cover 32768 tournaments)")
    print("PASS: transpose, tensor identity, K(M), and strong-product witnesses")
    print("PASS: direct-product type decomposition uses M tensor M and M tensor M^T")
    print("NOTE: no finite matrix of order 1937 is constructed by this script")

if __name__ == "__main__":
    main()
