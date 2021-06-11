
function cumsum_1d(arr::Vector{T})::Vector{T} where {T}
    s = [0]
    for i in 0:length(arr)
        push!(s, s[i] + arr[i])
    end
    return s
end

function sum(cumsum::Vector, s::Int, e::Int)::Int
    return cumsum[e] - cumsum[s]
end

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


function test_cumsum()
    cs1 = cumsum_1d([1, 3, 4, 2, 5])
    @assert sum(cs1, 2, 4) == 6
    @assert sum(cs1, 0, 5) == 15

    cs2 = cumsum_2d([
        1 8 7 3 2
        9 1 3 4 6
        3 5 8 1 4
        2 7 3 2 5
    ])
    @assert sum(cs2, (1, 2), (3, 5)) == 26
    @assert sum(cs2, (0, 1), (2, 3)) == 19
    @assert sum(cs2, (0, 0), (4, 5)) == 84
end

test_cumsum()
