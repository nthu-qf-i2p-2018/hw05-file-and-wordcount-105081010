import string
import json
import csv
import pickle


def main(filename):
    lines=open(filename).readlines()
    #需要換檔案名?
    for line in lines:
        line=line.strip()
        words= line.split()
    
        for word in words:
            word.strip(string.punctuation)
            all_words.append(word)

#句點後按tab 可以找函式
#string.ascii_letters

    from collections import Counter
    word_counter= Counter(all_words)
    word_counter.most_common()

    csv_file= open('word_count.csv','w')

    with open('word_count.csv','w') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(word_counter.most_common())
    
    json.dump(word_counter.most_common(), open('word_count.json','w'))

    pickle.dump(word_counter, open('word_count.pkl','wb'))

if __name__ == '__main__':
    main("i_have_a_dream.txt")

