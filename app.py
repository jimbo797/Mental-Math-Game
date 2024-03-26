import time
import genEq

duration = int(input('Duration in seconds: '))

start = time.time()

score = 0

while time.time() < start + duration:
  eq, ans = genEq.generateEq()
  res = input(eq)

  if(res == ans.__str__()):
    score += 1
  else:
    print("Incorrect, answer was", ans)

print("Score:", score)