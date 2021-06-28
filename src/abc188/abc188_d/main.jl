read_int() = readline() |> s -> parse(Int, s)
read_ints() = readline() |> split .|> e -> parse(Int, e)

function main()
    n, p = read_ints()
    days = Dict{Int, Int}()
    for _ in 1:n
        a, b, c = read_ints()
        days[a] = get(days, a, 0) + c
        days[b + 1] = get(days, b + 1, 0) - c
    end

    ans, cost, pre_i = 0, 0, 0
    for i in sort(collect(keys(days)))
        ans += min(cost, p) * (i - pre_i)
        cost += days[i]
        pre_i = i
    end
    println(ans)
end

main()