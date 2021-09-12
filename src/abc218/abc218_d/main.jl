function main()
    n = readline() |> s -> parse(Int, s)
    pos::Vector{Tuple{Int,Int}} = []
    for _ in 1:n
        x, y = readline() |> split .|> s -> parse(Int, s)
        push!(pos, (x, y))
    end

    sort!(pos)
    ans = 0

    for tl in pos
        for br in pos
            if tl[1] >= br[1] || tl[2] >= br[2]
                continue
            end
            tr, bl = (br[1], tl[2]), (tl[1], br[2])
            if !isempty(searchsorted(pos, tr)) && !isempty(searchsorted(pos, bl))
                ans += 1
            end
        end
    end

    println(ans)
end

main()