"""Independent brute-force cross-checks; intentionally shares no code with verify.py."""

from itertools import permutations


def matrix(n, code):
    a = [[i == j for j in range(n)] for i in range(n)]
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j], a[j][i] = bool(code & (1 << bit)), not bool(code & (1 << bit))
            bit += 1
    return tuple(tuple(row) for row in a)


def brute_tau(a):
    """Backtracking over ordered row/column choices, with direct cell tests."""
    n = len(a)
    answer = 0

    def extend(rows, cols):
        nonlocal answer
        answer = max(answer, len(rows))
        for r in range(n):
            if r in rows:
                continue
            for c in range(n):
                if c in cols or not a[r][c]:
                    continue
                if all(a[old][c] == 0 for old in rows):
                    extend(rows + (r,), cols + (c,))

    extend((), ())
    return answer


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a)))


def closed_k(a):
    n = len(a)
    graph = [set(range(n)) for _ in range(n)] + [set(range(n, 2 * n)) for _ in range(n)]
    for i in range(n):
        graph[i].update(n + j for j in range(n) if a[i][j])
        graph[n + i].update(j for j in range(n) if a[j][i])
    return [sum(1 << u for u in (set([v]) | graph[v])) for v in range(2 * n)]


def open_incidence(a):
    n = len(a)
    graph = [0] * (2 * n)
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                graph[i] |= 1 << (n + j)
                graph[n + j] |= 1 << i
    return graph


def max_legal(neighborhoods):
    memo = {}

    def go(chosen, covered):
        if chosen in memo:
            return memo[chosen]
        best = chosen.bit_count()
        for v, nb in enumerate(neighborhoods):
            if not chosen & (1 << v) and nb & ~covered:
                best = max(best, go(chosen | (1 << v), covered | nb))
        memo[chosen] = best
        return best

    return go(0, 0)


def relabel_code(n, code, p):
    out = 0
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            lo, hi = sorted((p[i], p[j]))
            forward = bool(code & (1 << bit))
            if p[i] != lo:
                forward = not forward
            target = lo * n - lo * (lo + 1) // 2 + hi - lo - 1
            out |= int(forward) << target
            bit += 1
    return out


def representatives(n):
    left = set(range(1 << (n * (n - 1) // 2)))
    ps = tuple(permutations(range(n)))
    while left:
        c = min(left)
        orb = {relabel_code(n, c, p) for p in ps}
        left -= orb
        yield c, len(orb)


def component_signature(a):
    """Check the two type components of the direct incidence product."""
    n = len(a)
    e = [((0, i), (1, j)) for i in range(n) for j in range(n) if a[i][j]]
    vertices = [(s, i, t, j) for s in (0, 1) for i in range(n)
                for t in (0, 1) for j in range(n)]
    adj = {v: set() for v in vertices}
    for x in e + [(b, a_) for a_, b in e]:
        for y in e + [(d, c) for c, d in e]:
            u = (x[0][0], x[0][1], y[0][0], y[0][1])
            v = (x[1][0], x[1][1], y[1][0], y[1][1])
            adj[u].add(v)
            adj[v].add(u)
    # Every product edge changes each coordinate side, so the two invariant
    # type classes are (left,left)/(right,right) and the two mixed classes.
    for u, ns in adj.items():
        for v in ns:
            assert (u[0] == u[2]) == (v[0] == v[2])
            s1, i, s2, j = u
            _, k, _, l = v
            if s1 == s2 == 0:
                assert a[i][k] and a[j][l]
            elif s1 == s2 == 1:
                assert a[k][i] and a[l][j]
            elif s1 == 0:
                assert a[i][k] and a[l][j]
            else:
                assert a[k][i] and a[j][l]
    return True


def main():
    total = 0
    for n in range(1, 7):
        cases = list(representatives(n)) if n == 6 else [(c, 1) for c in range(1 << (n * (n - 1) // 2))]
        for code, orbit_size in cases:
            a = matrix(n, code)
            total += orbit_size
            t = brute_tau(a)
            assert t == brute_tau(transpose(a))
            assert max_legal(closed_k(a)) == t
            assert max_legal(open_incidence(a)) == 2 * t
            assert component_signature(a)
            for i in range(n):
                for j in range(n):
                    assert (a[i][j] and a[j][i]) == (i == j)
    assert total == 33867
    assert sum(size for _, size in representatives(6)) == 32768
    print("PASS: independent verifier covered 33867 tournaments; n=6 orbit sizes sum to 32768")
    print("PASS: brute tau, transpose, K(M), incidence total-Grundy, and direct-product components")


if __name__ == "__main__":
    main()
