#нужно в заданном наборе целых чисел
# найти сумму всех положительных элементов,
# затем найти где в заданной последовательности находятся
# максимальный и минимальный элемент и вычислить произведение чисел,
# расположенных в этой последовательности между ними.
# Так же известно, что минимальный и максимальный элемент
# встречаются в заданном множестве чисел только один раз и не являются соседними.

file_in = open("input.txt")
file_out = open("output.txt", "w")
n = int(file_in.readline())

list_new = [int(number) for number in file_in.readline().split(' ')]
summ_polozh = 0
#сумма полож єлементов
for i in range(n):
    if list_new[i] > 0:
        summ_polozh = summ_polozh + list_new[i]

#поиск макс и мин элемента
maks = list_new[0]
nom_maks = 0

minim = list_new[0]
nom_minim = 0
for i in range(1,n):
    if list_new[i] > maks:
        maks = list_new[i]
        nom_maks = i
    if list_new[i] < minim:
        minim = list_new[i]
        nom_minim = i

mult_elem = 1
if nom_minim < nom_maks:
    a1 = nom_minim
    a2 = nom_maks
if nom_minim > nom_maks:
    a2 = nom_minim
    a1= nom_maks

for i in range(a1+1,a2):
    mult_elem = mult_elem * list_new[i]

file_out.write(str(summ_polozh)+' '+str(mult_elem))
file_in.close()
file_out.close()
