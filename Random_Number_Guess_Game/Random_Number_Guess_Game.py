import random
lb=int(input("Enter a lower bound:"))
ub=int(input("Enter a upper bound:"))

print("You have only 5 chances to guess the number")
chances=5
c=0
num=random.randint(lb,ub)
for i in range(chances):
  gn=int(input("Guess the number:"))
  if num==gn:
    print(f"Congratulations you did it with {i+1} attempt")
    c=1
    break1
  elif num>gn:
    print("You guess too low")
  else:
    print("You guess too high")
if c==0:
  print("Your chances are over")
  print(f"The number is {num}")
