#
# SCC
#
include("./Util.jl")

function scc(n::Int, edges::Vector{Tuple{Int, Int}})::Tuple{Int, Vector{Union{Int, Nothing}}}
    g = adj_list_from_edges(n, edges, true)
    g_t = adj_list_from_edges(n, [(t, f) for (f, t) in edges], true)

    order::Vector{Int} = []
    visited::Vector{Bool} = fill(false, n)
    group_indice::Vector{Union{Int, Nothing}} = fill(nothing, n)

    function dfs(v::Int)
        visited[v] = true
        for u in g[v]
            if !visited[u]
                dfs(u)
            end
        end
        push!(order, v)
    end

    function rdfs(s::Int, cnt::Int)
        group_indice[s] = cnt
        visited[s] = true
        for t in g_t[s]
            if !visited[t]
                rdfs(t, cnt)
            end
        end
    end

    for i in 1:n
        if !visited[i]
            dfs(i)
        end
    end

    visited = fill(false, n)
    cnt = 0

    for s in reverse(order)
        if !visited[s]
            rdfs(s, cnt)
            cnt += 1
        end
    end

    return cnt, group_indice
end

function test_scc()
    n = 9
    edges = [
        (1, 2),
        (2, 7),
        (7, 1),
        (4, 2),
        (5, 4),
        (9, 5),
        (6, 9),
        (4, 6),
        (6, 8),
        (8, 3),
        (3, 8),
    ]
    _, groups = scc(n, edges)
    @assert groups == [2, 2, 1, 0, 0, 0, 2, 1, 0]
end

test_scc()