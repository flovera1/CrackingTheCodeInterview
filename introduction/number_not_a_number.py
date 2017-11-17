def main():
  big_num_1   = 1000
  big_num_2   = 1000
  small_num_1 = 1
  small_num_2 = 1
  
  '''
  what would these should print?
  '''
  print(big_num_1 is big_num_2)
  print(small_num_1 is small_num_2)

main()
'''
They would print false because the keyword "is" tests weather two variables refer to the same object, not
just if they are equal.

Python creates singletons for the most commonly used integers. One good reason to do this is that small 
numbers get used so frequently that if Python had to create a brand new object every time it needed a 
number, and then free the object when it goes out of scope, it would start to actually take a noticeable
amount of time.
'''
    
    