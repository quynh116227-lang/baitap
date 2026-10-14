a = int(input())
b = int(input())
c = int(input())
if a + b <= c or a + c <= b or b + c <= a:
    print("KHONG PHAI TAM GIAC")
elif a == b == c:
    print("TAM GIAC DEU")
elif a == b or a == c or b == c:
    print("TAM GIAC CAN")
elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("TAM GIAC VUONG")
else:
    print("TAM GIAC THUONG")
