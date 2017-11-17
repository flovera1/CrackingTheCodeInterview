from _operator import length_hint
def isEditDistance(s1, s2):
    
    #find the lengths of the stringStart
    m = len(s1)
    n = len(s2)
    
    #if the difference between lengths is more than 1,    
    #then strings can't be at one distance'
    
    if abs(m -n) > 1:
        return False
    
    count = 0   #count of isEditDistanceOne
    
    i = 0
    j = 0
    while i < m and j < n:
        # if current characters don't match
        if s1[i] != s2[j]:
            if count == 1:
                return False
            #if the length of one string is more,
            # then only possible edit is to remove a 
            # character.
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else: # both strings have the same length
                i += 1
                j += 1
                
            #increment the number of creditscount += 1
            count += 1
        else:
            i += 1
            j += 1
            
        
    #if last character is extra in any string
    if i < m or j < n:
        count += 1
        
    return count == 1

b1 = isEditDistance('pale', 'pale')
print('value ' + str(b1)) 

