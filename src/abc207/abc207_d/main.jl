using LinearAlgebra
using Statistics

const Pos = Vector{Float64}

function barycenter(poses::Vector{Pos})::Pos
    # poses: List[np.ndarray] の重心
    return mean(poses)
end


function rot(p::Pos, theta::Float64)::Pos
    # 点 p: np.ndarray(2x1) を 点 c: np.ndarray(2x1) を中心に theta[rad] 回転する
    r = [
        cos(theta) -sin(theta)
        sin(theta) cos(theta)
    ]
    return r * p
end


function match(n::Int, s::Vector{Pos}, t::Vector{Pos})::Bool
    first_non_zero_index = findfirst(e -> !all(e .≈ zeros(size(e))), s)

    if isnothing(first_non_zero_index)
        return all(map(e -> e .≈ [0.0, 0.0], t))
    end

    for i in 1:n
        # assume s[0] map to t[i] by rotating θ
        theta = atan(t[i][2], t[i][1]) - atan(s[first_non_zero_index][2], s[first_non_zero_index][1])
        res = true
        for j in 1:n
            # s[j] -> ∃t[k]
            sj = rot(s[j], theta)
            res &= any(t .|> tk -> all(sj .≈ tk))
        end
        
        if res
            return true
        end
    end
    
    return false
end


function solve(n::Int, s::Vector{Pos}, t::Vector{Pos})::Bool
    sg, tg = barycenter(s), barycenter(t)
    s, t = map(e -> e .- sg, s), map(e -> e .- tg, t)
    return match(n, s, t)
end


function main()
    n = readline() |> s -> parse(Int, s)
    s::Vector{Pos} = []
    t::Vector{Pos} = []
    for i in 1:n
        a, b = readline() |> split .|> e -> parse(Int, e)
        push!(s, vec([a b]))
    end

    for i in 1:n
        c, d = readline() |> split .|> e -> parse(Int, e)
        push!(t, vec([c d]))
    end

    println(ifelse(solve(n, s, t), "Yes", "No"))
end

main()