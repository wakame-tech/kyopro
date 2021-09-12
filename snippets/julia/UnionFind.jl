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

function union!(u::UnionFind, x::Int, y::Int)
    x, y = find!(u, x), find!(u, y)

    if x == y
        return
    end

    if u.parents[x] > u.parents[y]
        x, y = y, x
    end

    u.parents[x] += u.parents[y]
    u.parents[y] = x
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