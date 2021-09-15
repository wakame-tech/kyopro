combinations(a) = Iterators.flatten([combinations(a, k) for k = 1:length(a)])

struct Combinations
    n::Int
    t::Int
end

Base.length(c::Combinations) = binomial(c.n, c.t)

Base.eltype(::Type{Combinations}) = Vector{Int}

function combinations(a, t::Integer)
    if t < 0
        # generate 0 combinations for negative argument
        t = length(a) + 1
    end
    reorder(c) = [a[ci] for ci in c]
    (reorder(c) for c in Combinations(length(a), t))
end

function Base.iterate(c::Combinations, s=[min(c.t - 1, i) for i in 1:c.t])
    if c.t == 0 # special case to generate 1 result for t==0
        isempty(s) && return (s, [1])
        return
    end
    for i in c.t:-1:1
        s[i] += 1
        if s[i] > (c.n - (c.t - i))
            continue
        end
        for j in i + 1:c.t
            s[j] = s[j - 1] + 1
        end
        break
    end
    s[1] > c.n - c.t + 1 && return
    (s, s)
end

ints = () -> readline() |> split .|> e -> parse(Int64, e)

function main()
    n, k, p = ints()
    a = ints()
    # n, k, p = 6, 3, 15
    # a = [2, 7, 5, 3, 6, 6]

    n1 = ceil(n ÷ 2)
    n2 = n - n1
    t1, t2 = Vector{Vector{Int64}}(), Vector{Vector{Int64}}()
    for i in 1:n1
        row = combinations(a[1:n1], i) |> collect .|> sum |> sort
        push!(t1, row)
    end
    for i in 1:n2
        row = combinations(a[n1 + 1:end], i) |> collect .|> sum |> sort
        push!(t2, row)
    end

    # @show n, k, p, a
    # @show t1
    # @show t2

    ans = 0
    # k == 1 はみるだけ
    if k == 1
        ans = 0
        if !isempty(t1)
            ans += filter(e -> e <= p, t1[1]) |> length
        end
        if !isempty(t2)
            ans += filter(e -> e <= p, t2[1]) |> length
        end
        println(ans)
        return
    end

    # 例外
    if k <= length(t2)
        ans += filter(e -> e <= p, t2[k]) |> length
    end
    if k <= length(t1)
        ans += filter(e -> e <= p, t1[k]) |> length
    end

    for (i, r1) in enumerate(t1)
        # 選べる個数
        rest = k - i
        # @show i, rest
        if !(rest in 1:length(t2))
            continue
        end
        r2 = t2[rest]
        for e in r1
            cnt = searchsortedlast(r2, p - e)
            # @show e, p - e, cnt
            ans += cnt
        end
    end
    println(ans)
end

main()