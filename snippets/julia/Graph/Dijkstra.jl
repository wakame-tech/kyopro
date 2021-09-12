#
# Dijkstra, FloydWarshall
#
using DataStructures
include("./Util.jl")

# adj (node, weight)
Graph = Vector{Vector{Tuple{Int, Int}}}

Inf = 10 ^ 18

function dijkstra(n::Int, adj::Graph, s::Int)::Vector{Int}
    dist = fill(Inf, n)
    # (dist, node)
    hq::Vector{Tuple{Int, Int}} = [(0, s)]
    dist[s] = 0
    seen = fill(false, n)

    while !isempty(hq)
        v = heappop!(hq)[2]
        seen[v] = true
        for (to, cost) in adj[v]
            if !seen[to] && dist[to] > dist[v] + cost
                dist[to] = dist[v] + cost
                heappush!(hq, (dist[to], to))
            end
        end
    end

    return dist
end

function floyd_warshall!(n::Int, g::Matrix{Int})
    for k in 1:n, i in 1:n, j in 1:n
        g[i, j] = min(g[i, j], g[i, k] + g[k, j])
    end
end

function test_dijkstra()
    n, m = 4, 5
    inputs = [(1, 2, 1), (1, 3, 4), (2, 3, 2), (3, 4, 1), (2, 4, 5)]
    adj::Graph = [[] for _ in 1:n]
    for (s, t, c) in inputs
        push!(adj[s], (t, c))
    end
    dist = dijkstra(n, adj, 1)
    @assert dist == [0, 1, 3, 4] 
end

function test_floyd_warshall()
    costs = [
        (1, 2, 3),
        (1, 4, 5),
        (2, 1, 2),
        (2, 4, 4),
        (3, 2, 1),
        (4, 3, 2),
    ]
    n = 4
    g = adj_mat_from_cost(n, costs)
    floyd_warshall!(n, g)
    g_true = [
        0 3 7 5
        2 0 6 4
        3 1 0 5
        5 3 2 0
    ]
    @assert g == g_true
end

test_dijkstra()
test_floyd_warshall()