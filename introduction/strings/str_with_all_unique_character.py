def unique(s):
    return len(set(s)) == len(s) 

def unique2(str):
    uchars = []
    for c in str:
        if c in uchars:
            return False
        else:
            uchars.append(c)
    return True


s1 = 'abcd'
s2 = 'abca'
boolean1 = unique2(s1)
boolean2 = unique2(s2)

print('boolean 1 ' + str(boolean1))
print('boolean 2 ' + str(boolean2))