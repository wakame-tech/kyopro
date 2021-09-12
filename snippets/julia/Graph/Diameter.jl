#
# Graph Diameter
#
using DataStructures
include("./Util.jl")

Inf = 10 ^ 18
function diameter(n::Int, g::Vector{Vector{Int}})::Int
    function bfs!(n::Int, g::Vector{Vector{Int}}, s::Int)::Tuple{Int, Int}
        dist = fill(Inf, n)
        flags = fill(false, n)
        q = Deque{Int}()
        push!(q, s)
        dist[s] = 0
        while !isempty(q)
            u = popfirst!(q)
            for v in g[u]
                if !flags[v] && dist[v] > dist[u] + 1
                    dist[v] = dist[u] + 1
                    flags[v] = true
                    push!(q, v)
                end
            end
        end

        return findmax(dist)
    end

    _, i = bfs!(n, g, 1)
    r, _ = bfs!(n, g, i)
    return r
end

function test_diameter()
    n = 5
    edges = [
        (1, 2),
        (2, 3),
        (3, 4),
        (3, 5),
    ]
    g = adj_list_from_edges(n, edges)
    r = diameter(n, g)
    @assert r == 3
end

test_diameter()