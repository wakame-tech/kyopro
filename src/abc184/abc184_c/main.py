r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
dx, dy = abs(r2 - r1), abs(c2 - c1)

def solve(dx, dy):
  turn = 0
  if dx == 0 and dy == 0:
      return turn
  while True:
    print(f'{turn}: {dx} {dy}')

    if dx + dy<= 3:
      turn += 1
      break
    elif dx == dy:
      turn += 1
      break
    elif dx == 0:
      turn += 1
      dx, dy = dy // 2, dy - (dy // 2)
    else:
      turn += 1
      d = min(dx, dy)
      dx -= d
      dy -= d
      
  return turn

print(solve(dx, dy))