# TODO why there is still spaces in the dictinary
import re


# TODO these could be in single regex operation if i was smarter 
def remove_special_char(s):
    return re.sub('[^A-Za-z0-9 \']+', '', s,)

def remove_extra_spaces(s):
    return re.sub('\s+',' ',s)

if __name__ == '__main__':
    dictionary = dict()
    file = open("alice.txt", "r")

    for line in file:
        line = remove_special_char(line)
        line = remove_extra_spaces(line)
        line = line.strip()
        line = line.lower() 
        words = line.split(" ") 
  
        for word in words: 
            if word in dictionary: 
                dictionary[word] = dictionary[word] + 1
            else: 
                dictionary[word] = 1
    
    file.close()

    sorted_dictionary=dict(sorted(dictionary.items(),key= lambda x:x[1]))

    for key in list(sorted_dictionary.keys()):
        if (sorted_dictionary[key] > 100):
            print(key, ":", sorted_dictionary[key]) 
