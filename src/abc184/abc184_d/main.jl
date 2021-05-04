# TODO
xs = parse.(Int32, split(readline()))
dp = zeros(Float32, 101, 101, 101)

function rec(i, j, k)
  if dp[i + 1, j + 1, k + 1] != 0.0
    return dp[i + 1, j + 1, k + 1]
  elseif max(i, j, k) == 100
    return 0.0
  else
    p = (rec(i + 1, j, k) + 1) * i / (i + j + k) +
      (rec(i, j + 1, k) + 1) * j / (i + j + k) +
      (rec(i, j, k + 1) + 1) * k / (i + j + k)
    dp[i + 1, j + 1, k + 1] = p
    p
  end
end

println(rec(xs...))