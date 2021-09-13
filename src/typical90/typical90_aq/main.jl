using DataStructures: deque

Pos = Tuple{Int, Int}

function bfs(g::Matrix{Bool}, w::Int, h::Int, from::Pos, to::Pos)::Int
    inf::Int = 10 ^ 6
    dx::Vector{Int} = [1, 0, -1, 0]
    dy::Vector{Int} = [0, 1, 0, -1]
    costs::Array{Int, 3} = fill(inf, (4, w, h))
    # pos, cost, dire
    q = Deque{Tuple{Pos, Int}}()

    for i in 1:4
        costs[i, from[1], from[2]] = 0
        push!(q, (from, i))
    end

    while !isempty(q)
        (x, y), pre_i = popfirst!(q)
        @inbounds for i in 1:4
            nx, ny = x + dx[i], y + dy[i]

            if !(1 <= nx <= w) || !(1 <= ny <= h)
                continue
            end

            if g[nx, ny]
                continue
            end

            cost = costs[pre_i, x, y] + ifelse(i == pre_i, 0, 1)
            if cost < costs[i, nx, ny]
                costs[i, nx, ny] = cost
                if i == pre_i # same dire
                    pushfirst!(q, ((nx, ny), i))
                else # differnt dire
                    push!(q, ((nx, ny), i))
                end
            end
        end
    end

    return minimum(costs[:, to[1], to[2]])
end

ints = () -> readline() |> split .|> e -> parse(Int, e)

function main()
    h, w = ints()
    rs, cs = ints()
    rt, ct = ints()
    g::Matrix{Bool} = zeros((w, h))
    for i in 1:h
        s = readline()
        for j in 1:w
            g[j, i] = s[j] != '.'
        end
    end

    ans = bfs(g, w, h, (cs, rs), (ct, rt))
    println(ans)
end

main()