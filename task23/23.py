#Гадание
# натурального числа n надо посчитать сумму всех чисел,
# на которые n делится без остатка.
#В единственной строке входного файла INPUT.TXT записано натуральное число n (n ≤ 1000),
file_in = open("input.txt")
file_out = open("output.txt", "w")
n = int(file_in.readline())
summa = 0
if n >0 and n <= 1000:
    for i in range(1 , n+1):
        if n % i == 0:
            summa = summa + i
    file_out.write(str(summa))
else:
    file_out.write('Chislo  bolshe 1000 bkb vtnshe 0')
file_in.close()
file_out.close()
