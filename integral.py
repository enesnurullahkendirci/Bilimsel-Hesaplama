def f(x):
    return (x**2)

x1 = 0
x2 = 100

# aralığın kaç parçaya bölüneceği
n = int(input("hassasiyet: "))
h = (x2-x1)/n
integral = 0

for i in range(n):
    integral += f(x1+i*h) * h
print(integral)

integral = 0
for i in range(1,n+1):
    integral += f(x1+i*h) * h
print(integral)

integral = 0
for i in range(n):
    integral += f(x1+h/2+i*h)*h
print(integral)

integral = 0
for i in range(n):
    integral += (f(x1+i*h)+f(x1+(i+1)*h))*h/2
print(integral)