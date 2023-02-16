import sys
sys.set_int_max_str_digits(0)
while True:
    a=int(input("Enter the number, whose factorial you want: "))
    b=1
    for i in range(a,0,-1):
        b*=i
    print(b)