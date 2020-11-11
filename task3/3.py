# test data for input file:
# 4255
# 5
# 75
# В единственной строке входного файла INPUT.TXT
# записано одно натуральное число А,
# оканчивающееся на цифру 5, не превышающее 4*105.
file_in = open("input.txt")
file_out = open("output.txt", "w")
x = int(file_in.readline())
stroka = str(x)

if x > 0 and x < 4*100000:
    last_x = stroka[-1]
    if last_x == '5':

        chislo = '0'+stroka[:-1]
        a = int(chislo)
        rez = int(str(a*(a+1))+'25')
    else:
        rez = x*x
else:
    rez = ''

file_out.write(str(rez))
file_in.close()
file_out.close()


