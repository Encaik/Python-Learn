str = ['1', '2', '3']
file = open('txt.txt', 'a')
for a in str:
    file.write(a)
file.close()