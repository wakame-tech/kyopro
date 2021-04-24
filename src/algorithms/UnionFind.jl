# UnionFind.jl
struct UnionFind
  parent::Vector{Int}

  function UnionFind(n::Int)
    new([i for i in 1:n])
  end
end

function root(u::UnionFind, x::Int)::Int
  if u.parent[x] == x 
    return x
  end
  px = root(u, u.parent[x])
  u.parent[x] = px
  px
end

function unite!(u::UnionFind, a::Int, b::Int)
  pa, pb = root(u, a), root(u, b)
  if pa == pb
    return
  end
  u.parent[pa] = pb
end

function same(u::UnionFind, a::Int, b::Int)::Bool
  root(u, a) == root(u, b)
end