
function tl(a::Matrix{Bool})::Tuple{Int, Int}
    for i in 1:size(a, 1), j in 1:size(a, 2)
        if a[i, j]
            return (i, j)
        end
    end
end

function get_el(n::Int, a::Matrix{Bool}, i::Int, j::Int)::Bool
    if i in 1:n && j in 1:n
        return a[i, j]
    else
        return false
    end
end

function match(n::Int, s::Matrix{Bool}, t::Matrix{Bool})::Bool
    if count(s) != count(t)
        return false
    end

    stx, sty = tl(s)
    ttx, tty = tl(t)
    dx, dy = ttx - stx, tty - sty
    for i in 1:size(s, 1), j in 1:size(s, 2)
        if s[i, j] != get_el(n, t, i + dx, j + dy)
            return false
        end
    end
    return true
end
 
function main()
    n = readline() |> s -> parse(Int, s)
    s::Matrix{Bool} = zeros(n, n)
    t::Matrix{Bool} = zeros(n, n)

    for y in 1:n
        l = readline()
        for (x, c) in enumerate(l)
            if c == '#'
                s[x, y] = true
            end
        end
    end

    for y in 1:n
        l = readline()
        for (x, c) in enumerate(l)
            if c == '#'
                t[x, y] = true
            end
        end
    end

    for rot in [identity, rotr90, rotl90, rot180]
        if match(n, rot(s), t)
            println("Yes")
            return
        end
    end
    println("No")
end
 
main()