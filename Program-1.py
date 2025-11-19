class calc:
  def opearate(self,a,b,op):
    if op=="add":
      return a+b
    elif op=="sub":
      return a-b
    elif op=="mul":
      return a*b
    elif op=="div":
      if b==0:
        return "cannot divide by zero"
      return a/b
    else:
      return "invalid operation"
a=float(input())
b=float(input())
op=input()
c=calc()
print(c.calc(a,b,op))
