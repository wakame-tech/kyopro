# 
# UnionFind
#
mutable struct UnionFind
    n::Int
    parents::Vector{Int}

    function UnionFind(n::Int)
        new(n, [-1 for i in 1:n])
    end
end

function find!(u::UnionFind, x::Int)::Int
    if u.parents[x] < 0
        return x
    else
        u.parents[x] = find!(u, u.parents[x])
        return u.parents[x]
    end
end

function union!(u::UnionFind, x::Int, y::Int)::Bool
    x, y = find!(u, x), find!(u, y)

    if x == y
        return false
    end

    if u.parents[x] > u.parents[y]
        x, y = y, x
    end

    u.parents[x] += u.parents[y]
    u.parents[y] = x
    return true
end

function size(u::UnionFind, x::Int)::Int
    return -u.parents[find(u, x)]
end

function same(u::UnionFind, x::Int, y::Int)::Bool
    return find!(u, x) == find!(u, y)
end

function members(u::UnionFind, x::Int)::Vector{Int}
    root = find!(u, x)
    return [i for i in 1:u.n if find!(u, i) == root]
end

function roots(u::UnionFind)::Vector{Int}
    return [i for (i, x) in emumerate(u.parents) if x < 0]
end

function groups(u::UnionFind)::Dict{Int,Vector{Int}}
    res = Dict{Int,Vector{Int}}()
    for i in 1:u.n
        r = find!(u, i)
        if !(r in keys(res))
            res[r] = [i]
        else
            res[r] += [i]
        end
    end
    return res
end

function Base.string(u::UnionFind)::String
    join(["$k: $v" for (k, v) in groups(u)], ",\n")
end

function Base.show(io::IO, u::UnionFind)
    println(io, string(u))
end

ints = () -> readline() |> split .|> s -> parse(Int, s)

# 最小全域木を求める
function kruskal(n::Int, weighted_edges::Vector{Tuple{Int, Int, Int}})::Int
    sort!(weighted_edges, by=e -> e[3])
    uf = UnionFind(n)
    ans = 0
    for (f, t, c) in weighted_edges
        # 非負辺だけ
        if !union!(uf, f, t)  && c > 0
            ans += c
        end
    end
    return ans
end

function main()
    n, m = ints()
    edges::Vector{Tuple{Int, Int, Int}} = []
    for i in 1:m
        a, b, c = ints()
        push!(edges, (a, b, c))
    end
    ans = kruskal(n, edges)
    print(ans)
end

main()