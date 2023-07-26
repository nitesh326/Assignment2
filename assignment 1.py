n=int(input("enter the number:"))
c=0
a=0
b=1
if n==0 or n==1:
    print("yes it belongs FibonacciSequence")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes it belongs to fibonacci sequence")
    else:
        print(" No it does not belong to fibonacci Sequence")
