# k=0
# dict={}
# for i in range (2,10):
#     for j in range(2,100):
#         if j%i==0:
#             k+=1
#             dict[i]=k
#     k=0
# print (dict)

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
#
# import random
# a=int(input("Введите длину массива: "))
# k=0
# q=[]
# i = [random.randrange(1,20) for i in range(0,a)]
# print ("Массив чисел:",i)
# for j in i:
#     if j%2==0:
#         q.append(k)
#         k+=1
#     else:
#         k+=1
# print("Массив индексов четных элементов:",q)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# import random
#
# k=0
# q=[]
# w=[]
# while k<10:
#     z = random.randrange(0, 10)
#     if z not in q:
# #         q.append(z)
# #         k+=1
# # print("До",q)
# # k = q.index(min(q))
# # min=min(q)
# g = q.index(max(q))
# q[k]=max(q)
# q[g]=min
# print("После",q)
#4. Определить, какое число в массиве встречается чаще всего
# import random
# q=[]
# freq=[]
# i = [random.randint(1,10) for i in range(0,10)]
# print (i)
# for j in i:
#     if j not in q:
#         q.append(j)
#         freq.append(i.count(j))
# print (q,"Уникальные элементы")
# for j in q:
#     if i.count(j) == max(freq):
#         print("Число",j,"Встречается в данном массиве",max(freq),"раз")

# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
# import random
# k=0
# arr=[]
# minus_arr=[]
# while k<10:
#     z = random.randrange(-10, 10)
#     if z not in arr:
#         arr.append(z)
#         k+=1
#         if z<0:
#             minus_arr.append(z)
# print (arr)
# #print (minus_arr)
# print ("Самый большой отрицательный элемент равен",max(minus_arr),"его индекс равен",arr.index(max(minus_arr)))

#6. В одномерном массиве найти сумму элементов,
#находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.
# import random
# k=0
# arr=[]
# while k<10:
#     z = random.randrange(-10, 10)
#     if z not in arr:
#         arr.append(z)
#         k+=1
# min=arr.index(min(arr))
# max=arr.index(max(arr))
# print(arr)
# k=0
# if min-max==1 or max-min==1:
#     print("Сумма равна '0'")
# elif min<max:
#     for j in range(min+1,max):
#         k+=arr[j]
# elif min>max:
#     for j in range(max+1,min):
#         k += arr[j]
# print ("Cумма равна =",k)

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
# import random
# i=[random.randrange(-10,10) for i in range(1,11)]
# print(i,"Массив целых чисел")
# b=min(i)
# if i.count(min(i)) > 1:
#     print("Наименьшими элементами массива являются", min(i), "и", min(i))
# else:
#     i.remove(min(i))
#     print ("Наименьшими элементами массива являются",min(i),"и", b)

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу





