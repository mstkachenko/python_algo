

Задача №1
import sys
a=int(input("Введите трехзначное чиcло: "))
if a>999 or a<100:
    print("Это не трехзначное число")
    sys.exit()
else:
    print
    print("Сумма равна ", int(((a-a%100)/100)+((a%100-a%10)/10)+(a%10)))
    print("Произведение равно ", int(((a-a%100)/100)*((a%100-a%10)/10)*(a%10)))


Задача №2
a=5
b=6
print("Логическое 'И': ", bin(a&b)," - двоичный вид, ", int(bin(a&b),2)," - десятичный вид")
print("Логическое 'ИЛИ': ", bin(a|b)," - двоичный вид, ", int(bin(a|b),2)," - десятичный вид")
print("Логическое 'НЕ': ", bin(~a)," - двоичный вид, ", int(bin(~a),2)," - десятичный вид")
print("Исключающее 'ИЛИ': ", bin(a^b)," - двоичный вид, ", int(bin(a^b),2)," - десятичный вид")
print("Сдвиг 5 вправо: ", bin(a>>1)," - на один знак, ", bin(a>>2)," - на два знака")
print("Сдвиг 5 влево: ", bin(a<<1)," - на один знак, ", bin(a<<2)," - на два знака")

Задача №3
import sys
x1=int(input("Введите координату X первой точки: "))
y1=int(input("Введите координату Y первой точки: "))
x2=int(input("Введите координату X второй точки: "))
y2=int(input("Введите координату Y второй точки: "))

if x1==x2 and y1==y2:
    print("Заданы 2 одинаковые точки")
    # sys.exit()
elif x1==x2 and y1!=y2:
    print("x =",x1)
elif x1!=x2 and y1==x2:
    print("y =", y1)
elif x1!=x2 and y1!=y2:
    print("y =",int((y1-y2)/(x1-x2)),"* x +","(",int(y1-x1*((y1-y2)/(x1-x2))),")")

Задача №4

import random

a=int(input("Введите тип переменных (1 - целые числа, 2 - вещественные числа, 3 - символы): "))
if a == 1:
    a=int(input("Введите a: "))
    b=int(input("Введите b: "))
    if a < b:
        print("Между",a,"и",b,"есть целое число" ,randint(a,b))
    elif a==b:
        print("Это есть целое число", a)
    elif a > b:
        a = a + b
        b=a-b
        a=a-b
        print("Между", a, "и", b, "есть целое число", randint(a, b))
elif a==2:
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    if a < b:
        print("Между", a, "и", b, "есть целое число", random.random(a, b))
    elif a == b:
        print("Между", a, "и", b, "есть целое число", a)
    elif a > b:
        a = a + b
        b = a - b
        a = a - b
        print("Между", a, "и", b, "есть целое число", random.randrange(a, b))


else:
    print ("не то")


Задача №5 Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
import string
a=input("Введите первую букву: ")
b=input("Введите вторую букву: ")

abc={string.ascii_lowercase[pos-1]:pos for pos in range(1,len(string.ascii_lowercase)+1)}

if a==b:
    print("Вы ввели одну и туже букву")
else:
    if a and b in abc.keys():
        print("Первая буква стоит на",abc[a],"месте")
        print("Вторая буква стоит на", abc[b], "месте")
        print("Между буквами находится",(abs(abc[a]-abc[b])-1),"букв")

Задача№ 6 Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string
c=int(input("Введите номер буквы: "))
abc={pos:string.ascii_lowercase[pos-1] for pos in range(1,len(string.ascii_lowercase)+1)}
if c in abc.keys():
    print(abc[c])


Задача№ 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a=int(input("Введите длину первого отрезка: "))
b=int(input("Введите длину первого отрезка: "))
c=int(input("Введите длину первого отрезка: "))

if (a+b>c) and (b+c>a) and (c+a>b):
    if (a==b) and (a==c) and (c==b):
        print('Треугольник равносторонний')
    elif (a==b) or (b==c) or (a==c):
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Из этих отрезков треугольник не составить')

Задача №9
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=int(input("Введите третье число: "))
massive=[a,b,c]
if a==b or a==c or b==c:
    print("Наедалово")
else:
    if max(massive) > a and min(massive) < a:
        print(a," - среднее число")
    elif max(massive) > b and min(massive) < b:
        print(b, " - среднее число")
    else:
        print(c, " - среднее число")