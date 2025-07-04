def factorial(n):
  if n<=1:
    return 1
  return(n*factorial(n-1))
  num=int(input("enter a number to find the factorial value :"))
  print("the factorial value is :",factorial(num))
