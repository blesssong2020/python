#### File: ls, pwd

def my_file_read():
   f = open("sample.txt", "r")
   contents = f.readlines()
   for x in contents:
       words = x.split()
       if len(words)>0:
           print(words[-1])

   f.close()

def my_file_read_2():
    with open("sample.txt", "r") as f:
        lines = f.readlines()
        for x in lines:
            print(x)

    print("done")

def my_file_write():
    with open("example.txt","w") as f: #a, append
        f.write("xxxx0hellow world, apple \n bananas, \n trees")

def my_copy():
    with open("sample.txt", "r") as f_1, open("sample_copy.txt", "w") as f_2:
        lines = f_1.readlines()
        for x in lines:
            f_2.write(x)

    with open("sample_copy.txt", "r") as f_2:
        print("="*40)
        print(f_2.readlines())

def my_file_processing():
    with open("sample.txt", "r") as f:
        lines = f.readlines()
        all_words = []
        for x in lines:
            if x:
                words = x.split()
                for w in words:
                    all_words.append(w)
        word_freq = {}
        for w in all_words:
            if w in word_freq:
                word_freq[w] += 1
            else:
                word_freq[w] = 1
        print("original length of word_freq:", len(word_freq))

        result_dict = {}
        while len(word_freq) > 0:
            min_val = min(word_freq.values())
            new_key = list(word_freq.keys())[list(word_freq.values()).index(min_val)]
            #result_dict[new_key] = min_val
            new_dict = {new_key:min_val}
            result_dict.update(new_dict)
            word_freq.pop(new_key)
        print("length of new sorted dictionary:", len(result_dict))
        print(result_dict)

    with open("result.txt", "w") as f_2:
        for item in word_freq.items():
            f_2.write(str(item))
            f_2.write("\n")





if __name__ == '__main__':
    #my_file_read()
    #my_file_read_2()
    #my_file_write()
    my_file_processing()
