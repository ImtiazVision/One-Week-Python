# Local scope: Variables defined in a function are scoped/available  to that function. They are not available outside that function. 

def square(num):
  ans = num ** 2 # here, ans is only available inside square function
  print(ans)
square(8) 