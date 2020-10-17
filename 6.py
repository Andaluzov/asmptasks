my_file = open ('input.txt','r')
my_file.seek(0)
ll = my_file.read()
file_out = open('output.txt', 'w+')

if len(ll) == 5:
    if '-' in ll and ll[2] == '-':
         st = [word for word in ll.split('-')]
         first = abs(ord(st[0][0])-ord(st[1][0]))
         second = abs(int(st[0][1])-int(st[1][1]))

         if (first + second) == 3:
             file_out.write('Yes')
         else:
            file_out.write('No')
    else:
        file_out.write('ERROR')
else:
    file_out.write('ERROR')
file_out.close()
my_file.close()