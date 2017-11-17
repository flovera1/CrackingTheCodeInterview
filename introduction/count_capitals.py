'''
The function "count" returns the value: count.
But it's inefficient because actually the problem requires to have no limit size for the file (the file can be huge). 
The count function puts the whole file inside a variable and that could be huge and it's bad code.

So we created a second function: count_better. This one uses the concept of traversing the file line by line
until the file is finished. This idea is idea is quite common that there's a standard library function for it
called: iter(). We'll need the two-argument form of iter(), where the first argument is our function 
to call repeatedly, and the second argument is the value that tells us when to stop (also called the sentinel).
readline() returns an empty string ONLY when it hits the end of the file, so it'll be our sentinel.

'''

def count(file):
    with open(file) as fh:
        count = 0
        text  = fh.read()
        for character in text:
            if character.isupper():
                count += 1
        
        return count
    
def count_better(file):
    with open(file) as fh:
        count = 0
        for line in iter(fh.readline, ''):
            for character in line:
                if character.isupper():
                    count += 1
                    
        return count