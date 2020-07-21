# infile = open('Read.txt','r')
#
# newopen = open('Read2.txt', 'w')
# for line in infile :
#
#     if 'SET CURRENT' in line:
#         line = line.replace('.' , '')
#
#     else:
#         newopen.write(line)
#
# newopen.close()


newopen = open('Read2.txt', 'r')

print(newopen.read())
newopen.close()





