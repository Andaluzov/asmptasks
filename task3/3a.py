with open('input.txt', 'r') as file_in:
    x = int(file_in.readline())
p = False

if x >0 and x < 4*100000:
    a = x//10
    b = x-(a*10)

    if b == 5:
        p = True
        rez = str(a*(a+1))+'25'

if p:
    with open('output.txt', 'w') as file_out:
        file_out.write(rez)
else:
    with open('output.txt', 'w') as file_out:
        file_out.write('')

