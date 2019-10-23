# used to quickly clean and import ham data, from the ENRON dataset
# emails downloaded from http://www2.aueb.gr/users/ion/data/enron-spam/ 
import re
import os
import pickle

# regex to seperate header and body from email 
def get_header_body(s):
    p = re.compile("^[\s\S]*?(?=\n{2,}|$)")
    result = p.search(s)
    return result.group(0), s.replace(result.group(0), '')



all_ham = []
count = 0
# recursively look in all folders and sub folders
for root, dirs, files in os.walk(os.getcwd()+"/ham"):
    print(root)
    for file in files:
        count = count + 1
        print ('{0}\r'.format(count))
        print(file)
        with open((os.path.join(root, file)), 'r', encoding ='ISO-8859-1') as file:
            data = file.read()
            header, body = get_header_body(data)
            tup = ('ham', header, body)
            all_ham.append(tup)


# save as pickle file
with open('hamfile', 'wb') as fp:
    pickle.dump(all_ham, fp)

with open ('hamfile', 'rb') as fp:
    ham_list = pickle.load(fp)

# info     
print(ham_list[0])
print(len(ham_list))