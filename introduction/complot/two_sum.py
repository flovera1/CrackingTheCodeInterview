'''
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.
- What if there's no solution? assume ther's solution
- Can the list be empty? No.
- Is the list sorted? Not necessarily.

[2, 7, 11, 15], 9 -> [0, 1]

- We can 'remember' what we've seen so far using a set.
- Iterate the list and at every step, we can look back and see 
if there's a possible candidate for complement 
''' 

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i in range(len(nums)):
            compl = target-nums[i]
            if compl in hash_dict:
                return [hash_dict[compl], i]
            hash_dict[nums[i]] = i
        
def main():
    arr = [2,7,11,155]
    n   = 9
    print(twoSum(arr, n))
    
    
if __name__ == "__main__":
    main()