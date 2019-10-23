# used to quickly clean and import spam data from 2000
# emails downloaded from http://untroubled.org/spam/ 
import re
import os
import pickle

# regex to seperate header and body from email 
def get_header_body(s):
    p = re.compile("\n\n(.*\s)*")
    result = p.search(s)
    return s.replace(result.group(0), ''), result.group(0)

all_spam = []
count = 0
# recursively look in all folders and sub folders
for root, dirs, files in os.walk(os.getcwd()+"/oldspam"):
    print(root)
    for file in files:
        count = count + 1
        print ('{0}\r'.format(count))
        print(file)
        with open((os.path.join(root, file)), 'r', encoding ='ISO-8859-1') as file:
            data = file.read()
            header, body = get_header_body(data)
            tup = ('spam', header, body)
            all_spam.append(tup)

# write into a pickle file
with open('oldspamfile', 'wb') as fp:
    pickle.dump(all_spam, fp)

with open ('oldspamfile', 'rb') as fp:
    ham_list = pickle.load(fp)

#info
print(ham_list[0])
print(len(ham_list))