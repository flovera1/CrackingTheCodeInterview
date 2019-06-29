'''
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
become smaller than the original string, your method should return the original string. 
You can assume the string has only uppercase and lower case letters (a-z).
'''

def StrCompress(string):
    count = 1
    new = ''
    for i in range (len(string)):
        if i <len(string)-1:
            if string[i] == string[i+1]:
                count += 1
            else:
                new += string[i]+str(count)
                count = 1
        else:
            new +=string[i]+str(count)
            if len(string) <= len(new):
                return string
            return new

print(StrCompress('aabcccccaaa'))