# bad_words = ['LURADM']
#
# with open('Read.txt') as oldfile, open('Read2.txt', 'w') as newfile:
#     for line in oldfile:
#         if not any(bad_word in line for bad_word in bad_words):
#             newfile.write(line)

f=open('Read2.txt','r')
print(f.read())