my_file = open('input.txt')
ll = my_file.read()
file_out = open('output.txt', 'w')

p = False
str_abc = 'ABCDEFGH'

if len(ll) < 5:
    p = True
if len(ll) > 5:
    if len(ll) == 6 and ll[5] == '\n':
        p = False
    else:
        p = True

if not p:
    if ll[2] != '-':
        p = True

    if ll[0] in str_abc and ll[3] in str_abc:
        first = abs(ord(ll[0])-ord(ll[3]))
    else:
        p = True

    if ll[1] in '12345678' and ll[4] in '12345678':
        second = abs(int(ll[1])-int(ll[4]))
    else:
        p = True

if p:
    file_out.write('ERROR')
else:
    if(first + second) == 3 and first != 0 and second != 0:
        file_out.write('YES')
    else:
        file_out.write('NO')

file_out.close()
my_file.close()