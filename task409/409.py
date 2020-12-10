file_in = open("input.txt")
file_out = open("output.txt", "w")
n = int(file_in.readline())
step = 1
list_new = [int(number) for number in file_in.readline().split(' ')]
s_earth = 0
for i in range(1,n):
    s_earth = s_earth + (list_new[i-1] + list_new[i])/2*step
h_row = s_earth / (n-1)
file_out.write("{0:.10f}".format(h_row))
file_in.close()
file_out.close()
