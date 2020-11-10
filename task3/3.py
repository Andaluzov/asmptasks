# test data for input file:
# 4255
# 5
# 75
# В единственной строке входного файла INPUT.TXT
# записано одно натуральное число А,
# оканчивающееся на цифру 5, не превышающее 4*105.

with open('input.txt', 'r') as file_in:
    x = int(file_in.readline())
p = False
stroka = str(x)
# test
if x > 0 and x <= 4*100000:
    last_x = stroka[-1]
    if last_x == '5':
        p = True
        chislo = '0'+stroka[:-1]
        a = int(chislo)
        rez = int(str(a*(a+1))+'25')

if p:
    with open('output.txt', 'w') as file_out:
        file_out.write(str(rez))
else:
    with open('output.txt', 'w') as file_out:
        file_out.write('')




