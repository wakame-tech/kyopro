
using DataStructures
include("../UnionFind.jl")

# 最小全域木を求める
function kruskal(n::Int, weighted_edges::Vector{Tuple{Int, Int, Int}})::Int
    sort!(weighted_edges, by=e -> e[3])
    uf = UnionFind(n)
    ans = 0
    for (f, t, c) in weighted_edges
        if union!(uf, f, t)
            ans += c
        end
    end

    return ans
end

function kruskal_test()
    # <https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_A>
    n = 5
    m = [
        -1 2 3 1 -1
        2 -1 -1 4 -1
        3 -1 -1 1 1
        1 4 1 -1 3
        -1 -1 1 3 -1
    ]
    edges::Vector{Tuple{Int, Int, Int}} = []
    for i in 1:n
        for j in i:n
            if m[i, j] != -1
                push!(edges, (i, j, m[i, j]))
            end
        end
    end
    @assert kruskal(n, edges) == 5
end

kruskal_test()