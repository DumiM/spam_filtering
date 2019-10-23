# used to quickly clean and import spam data from 2019
# emails downloaded from http://untroubled.org/spam/ 
import re
import os
import pickle

# regex to seperate header and body from email 
def get_header_body(s):   
    p = re.compile("(Content-Transfer-Encoding)(.*\s)")
    result = p.search(s)
    return result.group(0), s.replace(result.group(0), '')



all_spam = []
count = 0
# recursively look in all folders and sub folders
for root, dirs, files in os.walk(os.getcwd()+"/spam"):
    print(root)
    for file in files:
        count = count + 1
        print ('{0}\r'.format(count))
        print(file)
        with open((os.path.join(root, file)), 'r', encoding ='ISO-8859-1') as file:
            data = file.read()
            if "base64" not in data:   # skip if base 64 email             
                p = re.compile("(Content-Transfer-Encoding)(.*\s)")
                pos_array = []
                # encoding and regex error skipping
                for m in p.finditer(data):
                    pos_array.append((m.start(), m.end(), m.group()))
                try:     # this is based on the format of the email files    
                    if len(pos_array) > 1:                
                        header = data[:pos_array[1][1]]
                        body = data[pos_array[1][1]:]
                    else:                
                        header = data[:pos_array[0][1]]
                        body = data[pos_array[0][1]:]
                except:
                    print("error")
                tup = ('spam', header, body)
                all_spam.append(tup)

# write into a pickle file
with open('2019spamfile', 'wb') as fp:
    pickle.dump(all_spam, fp)

with open ('2019spamfile', 'rb') as fp:
    ham_list = pickle.load(fp)

# info  
print(ham_list[1][2])
print(len(ham_list))