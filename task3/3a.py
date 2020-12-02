#способ возведения в квадрат натуральных чисел, оканчивающихся на цифру 5.
# В единственной строке входного файла INPUT.TXT
# записано одно натуральное число А,
# оканчивающееся на цифру 5, не превышающее 4*105.
file_in = open("input.txt")
file_out = open("output.txt", "w")
x = int(file_in.readline())

if x >0 and x < 4*100000:
    a = x//10
    if a == 0:
        rez = str(x * x)
    else:
        b = x-(a*10)
        if b == 5:
            rez = str(a*(a+1))+'25'
        else:
            rez = str(x*x)
else:
    rez=''

file_out.write(rez)
file_in.close()
file_out.close()

