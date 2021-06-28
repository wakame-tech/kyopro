function match(n::Int, s::Vector{ComplexF64}, t::Vector{ComplexF64})::Bool
    if all(angle.(s) .≈ 0)
        return all(s .≈ t)
    end

    for i in 1:n
        # assume s[1] |-> t[i]
        θ = angle(t[i] / s[1])
        
        res = true
        for j in 1:n
            # s[j] -> ∃t[k]
            sj = (cos(θ) + im * sin(θ)) * s[j]
            res &= any(t .|> tk -> sj .≈ tk)
        end
        
        if res
            return true
        end
    end
    
    return false
end

function sort_by_angle(ps::Vector{ComplexF64})::Vector{ComplexF64}
    g = sum(ps) / length(ps)
    (ps .- g) # |> ps -> sort(ps, by=e -> angle(e))
end

read_int = readline() |> s -> parse(Int, s)
read_ints = readline() |> split .|> e -> parse(Int, e)

function main()
    n = read_int()
    s::Vector{ComplexF64} = []
    t::Vector{ComplexF64} = []
    for _ in 1:n
        a, b = read_ints()
        push!(s, complex(a, b))
    end

    for _ in 1:n
        c, d = read_ints()
        push!(t, complex(c, d))
    end

    s, t = sort_by_angle(s), sort_by_angle(t)
    println(ifelse(match(n, s, t), "Yes", "No"))
end

main()