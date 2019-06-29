'''
Write a method to replace all spaces in a string with '%20': You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith      ", 13
Output: "Mr%20J ohn%20Smith"
'''
MyList = list(map(str, raw_input().split(",")))

def urlify(string, length):
    new_string = ''
    for i in range(0, length):
        if string[i]==' ':
            new_string = new_string + '%20'
        else:
            new_string = new_string + string[i]

    return new_string

def urlify2(string, length):
    return string[:length].replace(' ', '%20')

print(urlify(MyList[0], int(MyList[1])))
print(urlify2(MyList[0], int(MyList[1])))



