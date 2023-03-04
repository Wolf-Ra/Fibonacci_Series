F1=0
F2=1
n=int(input("Enter the number of times to do Fibonacci series : "))
print("",F1,"",F2 , end =" ")
for i in range(n-2):
    F3=F1+F2
    F1=F2
    F2=F3
    print(F3 , end =" ")