function cumsum_2d(mat::Matrix{T})::Matrix where {T}
    s = zeros(T, size(mat)[1] + 1, size(mat)[2] + 1)
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

function main()
    n, k = readline() |> split .|> s -> parse(Int, s)
    siz = 5000
    d::Matrix{Int} = zeros(siz, siz)
    for i in 1:n
        a, b = readline() |> split .|> s -> parse(Int, s)
        d[a, b] += 1
    end

    cs = cumsum_2d(d)

    ans = 0
    for a in 1:siz - k
        for b in 1:siz - k
            ans = max(ans, sum(cs, (a, b), (a + k + 1, b + k + 1)))
        end
    end

    println(ans)
end

main()