### String,

def check_string_type():
    s = "hello world"
    print(type(s))


def my_string_fun():
    s = "my string"
    print(s[5:-1])
    #s[0] = "t"
    # string is immutable
    print(s)

def my_string_function2():
    s1 = "Hello world,"
    s2 = "string 2!"
    s3 = s1 + " " + s2
    s1 = s1 + " " + s2
    print(s1)
    word = s1.split()
    print(word)
    s3 = s1.join(word)
    print(s3)
    print(s1.lower())
    print(s1.upper())
    number1 = 10
    number2 = number1 + 100
    number3 = number2 + 100
    s = "       september {2}, {1}, {0}    ".format(number1, number2, number3)
    print(s)
    print(len(s))
    print(len(s.strip()))
    print(s.count("1"))
    print(s.find("21"))
    s = "3999"
    print(s.isdigit())
    s = "smart"
    print(s.isalpha())


def change_uppercase(s):
    new_str = s.upper()
    my_list = new_str.split()
    print( my_list )
    return my_list


def my_count(c, s):
    cnt = 0
    for x in s:
        if c == x:
            cnt += 1
    return cnt

def my_final_function(s):
    for j in range(len(s)):
        if my_count(s[j], s) == 1:
            return j
    return -1

def my_alter_function(s):
    dict = {}
    for x in s:
        if x in dict.keys():
            dict[x] += 1
        else:
            dict[x] = 1

    for i in range(len(s)):
        if dict[s[i]] == 1:
            return i
    return -1

def my_dict():
    dict = {"s":10, "z":3}
    dict["s"] += 1
    print(dict["s"])

def leet_code_151(s):
    # split string to words
    # remove empty element in words list
    # reverse element in words list
    # join words by " "
    # return

    words = s.strip().split()
    non_emp_words = []
    for x in words:
        if len(x) > 0:
            non_emp_words.append(x)

    non_emp_words.reverse()
    #print(non_emp_words)

    return " ".join(non_emp_words)

def leet_125(s):
    new_list =[]
    for x in s:
        if x.isalnum():
            new_list.append(x.lower())

    for i in range(int(len(new_list)/2)):
        if new_list[i] != new_list[len(new_list)-1-i]:
            return False
    return True

def leet_443(s):
    new_string = ""
    new_list = []
    i = 0
    while i < len(s):
        temp = 1
        current_str = s[i]
        while i+1 < len(s) and current_str == s[i+1]:
            temp += 1
            i += 1
        i += 1
        if temp > 1:
            new_string = new_string + current_str + str(temp)
        else:
            new_string = new_string + current_str
    for x in new_string:
        new_list.append(x)
    return len(new_list), new_list

def leet_443_2(l):
    final_list = []
    new_list = []
    i = 0
    new_str = ""
    while i < len(l):
        temp = 1
        current_element = l[i]
        while i+1 < len(l) and current_element == l[i+1]:
            temp += 1
            i += 1
        i += 1
        if temp > 1:
            new_list.append(current_element)
            new_list.append(str(temp))
        else:
            new_list.append(current_element)
    for x in new_list:
        new_str += x
    for x in new_str:
        final_list.append(x)
    return len(final_list), final_list


if __name__ == '__main__':
    #check_string_type()
    #my_string_function2()
    #change_uppercase("smart john")
    #print(my_final_function("aabbs"))
    #my_dict()
    #print(my_alter_function("aabbs"))
    #print((leet_125("  1112211   ")))
    print(leet_443_2(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))
