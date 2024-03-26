import random

sym = {0:'+', 1:'-', 2:'*', 3:'/'}

def generateEq():
  op = random.randint(0,3)

  # add
  if(op == 0):
    num1 = random.randint(2,100)
    num2 = random.randint(2,100)
    ans = num1+num2

  # sub (no negatives)
  if(op == 1):
    num1 = random.randint(2,100)
    num2 = random.randint(2,num1)
    ans = num1 - num2

  # mult (prod max is 200)
  if(op == 2):
    ans = 201
    while (ans > 200):
      num1 = random.randint(2,100)
      num2 = random.randint(2,20)
      ans = num1 * num2

  # div (all int, divisor max is 20)
  if(op == 3):
    num1 = 201
    while (num1 > 200):
      ans = random.randint(2,100)
      num2 = random.randint(2,20)
      num1 = ans * num2
  
  eq = f'{num1} {sym[op]} {num2} = '
  return (eq, ans)