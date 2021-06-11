
function cumsum_2d(mat::Matrix{T})::Matrix where {T}
    s = zeros(size(mat)[1] + 1, size(mat)[2] + 1)
    for y in 1:size(mat)[1]
        for x in 1:size(mat)[2]
            s[x + 1, y + 1] = s[x, y + 1] + s[x + 1, y] - s[x, y] + mat[x, y]
        end
    end
    return s
end

function sum(cumsum::Matrix{T}, s::Tuple{Int, Int}, e::Tuple{Int, Int})::Int where {T}
    return cumsum[e[1], e[2]] - cumsum[s[1], e[2]] - cumsum[e[1], s[2]] + cumsum[s[1], s[2]]
end

function is_leq_median(grid::Matrix{Int}, n::Int, k::Int, med::Int)::Bool
    """ O(N^2) """
    bit_grid = zeros(Int, (n, n))
    for y in 1:n
        for x in 1:n
            if (med <= grid[x, y])
                bit_grid[x, y] = 1
            end
        end
    end

    cs2 = cumsum_2d(bit_grid)

    for y in 1:n - k + 1
        for x in 1:n - k + 1
            s, e = (x, y), (x + k, y + k)
            if (sum(cs2, s, e) < k ^ 2 ÷ 2 + 1)
                return false
            end
        end
    end
    return true
end


function searach_med(grid::Matrix, n::Int, k::Int)::Int
    """ O(log 10^10) = O(1) """
    f, t = 0, 10 ^ 10
    while (f + 1 != t)
        m = (f + t) ÷ 2
        # @show m
        if (is_leq_median(grid, n, k, m))
            f = m
        else
            t = m
        end
    end
    return f
end

n, k = readline() |> split .|> s -> parse(Int, s)
grid = zeros(Int, (n, n))
for i in 1:n
    a = readline() |> split .|> s -> parse(Int, s)
    a = vec(a)
    grid[i, :] = a
end

println(searach_med(grid, n, k))