#### Dictionary: ordered, {}, changeable, do not allow duplicate, key-value pair


def my_dict_test():
    my_dict = {"first_name": "Tom", "last_name": "Jackson", "age": 20}
    my_dict["salary"] = 100000
    print(my_dict)
    """print(my_dict.get("address"))
    my_dict["salary"] = 200000
    print(my_dict["salary"])
    my_dict.pop("last_name")
    print(my_dict)"""
    if my_dict.get("age") > 10:
        print(my_dict)
    else:
        print("no such last_name")
    print("="*50)
    for item in my_dict.items():
        print(item)
    print("="*50)
    print(my_dict.keys())
    if "first_name" in my_dict.keys():
        print("yes")
    else:
        print("no")
    print(my_dict.values())

    #my_dict.clear()
    #print(my_dict)


    print(len(my_dict.keys()))




if __name__ == '__main__':
    my_dict_test()
