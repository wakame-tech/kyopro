# 
# MinCostFlow
#
using DataStructures

mutable struct Edge
    from::Int
    to::Int
    cap::Int
    cost::Int
    rev::Union{Edge,Nothing}
end

function Base.string(e::Edge)
    "$(e.from) -> $(e.to) cap/cost $(e.cap)/$(e.cost)"
end

function Base.show(io::IO, e::Edge)
    print(io, string(e))
end

mutable struct MinCostFlow
    n::Int
    g::Vector{Vector{Edge}}

    function MinCostFlow(n::Int)
        new(n, [[] for i in 1:n])
    end
end


function add_edge!(mcf::MinCostFlow, from::Int, to::Int, cap::Int, cost::Int)
    fwd = Edge(from, to, cap, cost, nothing)
    bwd = Edge(to, from, 0, -cost, fwd)
    fwd.rev = bwd

    push!(mcf.g[from], fwd)
    push!(mcf.g[to], bwd)
end

function edges(mcf::MinCostFlow)::Vector{Edge}
    edges = []
    for from in 1:mcf.n
        for e in mcf.g[from]
            push!(edges, e)
        end
    end
    return edges    
end

Inf = 10 ^ 18

function flow(mcf::MinCostFlow, s::Int, t::Int, f::Int)::Union{Int,Nothing}
    """
    flows from s to t, amount=f
    """
    res = 0
    h = zeros(Int, mcf.n)
    prv_v = zeros(Int, mcf.n)
    prv_e::Vector{Union{Edge,Nothing}} = [nothing for i in 1:mcf.n]
    d0::Vector{Int} = [Inf for i in 1:mcf.n]
    dist::Vector{Int} = [Inf for i in 1:mcf.n]

    while f != 0
        dist[:] = d0
        dist[s] = 0
        # (cost, value) heap
        que::Vector{Tuple{Int,Int}} = [(0, s)]
        while !isempty(que)
            cost, v = heappop!(que)
            if dist[v] < cost
                continue
            end
            r0 = dist[v] + h[v]
            for e in mcf.g[v]
                if e.cap > 0 && r0 + e.cost - h[e.to] < dist[e.to]
                    dist[e.to] = r = r0 + e.cost - h[e.to]
                    prv_v[e.to] = v
                    prv_e[e.to] = e
                    heappush!(que, (r, e.to))
                end
            end
        end

        if dist[t] == Inf
            return nothing
        end

        for i in 1:mcf.n
            h[i] += dist[i]
        end

        d, v = f, t
        while v != s
            d = min(d, prv_e[v].cap)
            v = prv_v[v]
        end

        f -= d
        res += d * h[t]
        v = t
        while v != s
            e = prv_e[v]
            e.cap -= d
            e.rev.cap += d
            v = prv_v[v]
        end
    end

    return res
end

function test_min_cost_flow()
    n, m, a = 4, 5, 2
    qs = [
        # from, to, cap, cost
        [1, 2, 2, 1],
        [1, 3, 1, 2],
        [2, 3, 1, 1],
        [2, 4, 1, 3],
        [3, 4, 2, 1],
    ]

    mcf = MinCostFlow(n)
    for q in qs
        add_edge!(mcf, q[1], q[2], q[3], q[4])
    end

    res = flow(mcf, 1, n, a)
    @assert res == 6
end

test_min_cost_flow()