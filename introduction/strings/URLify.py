def urlify(string):
    return "%20".join(string.split(" "))

def urlify(in_string, in_string_length):
    return in_string[:in_string_length].replace(' ', '%20')

string1 = "Mr John Smith     "
lgt =  13

string2 = urlify(string1, lgt)

print(string2)