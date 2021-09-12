
# edges -> list of adj nodes
function adj_list_from_edges(n::Int, edges::Vector{Tuple{Int, Int}}, directed::Bool = false)::Vector{Vector{Int}}
    g::Vector{Vector{Int}} = [[] for i in 1:n]
    for e in edges
        push!(g[e[1]], e[2])
        if !directed
            push!(g[e[2]], e[1])
        end
    end
    return g
end

function adj_mat_from_cost(n::Int, costs::Vector{Tuple{Int, Int, Int}})::Matrix{Int}
    g = fill(10 ^ 18, (n, n))
    for i in 1:n
        g[i, i] = 0
    end
    for (s, e, c) in costs
        g[s, e] = c
    end
    return g
end