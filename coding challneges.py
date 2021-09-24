####################CHALLENGE NUMBER 01################################################
#Write a function that reverses a string. The input
#string is given as an array of characters s.

def reverseString(str):
    copyOfString = str.copy() #this is a copy, so we can use it as a reference
    sizeOfList = len(str) -1
    for i in range(len(str)):
        str[sizeOfList - i] = copyOfString[i]

    return str



reverseString(["h","e","l","l","o"])

#######CHALLENGE NUMBER 02########################################################

#Given an array of integers nums and an integer target,
#return indices of the two numbers such that they add up to target.

def twoSum(nums,target):
    for i in range(len(nums)):
        for x in range(len(nums)):
            if [i] != [x]:
                num1 = nums[i]
                num2 = nums[x]
                sumOfNumbers = num1 + num2
                if sumOfNumbers == target:
                    return [i,x]
                
print(twoSum([3,4,7,3],6))