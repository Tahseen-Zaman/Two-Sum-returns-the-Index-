'''
Programe takes a list of numbers, and one target numbers.
IF  pair of numbers equals the traget, programe returns the index of pair.
for multiple solutions programe retun all indexs of instances
'''
'''
def twosumBruteforce(num,target):
  for i in range(len(num)):
    for j in range(i+1,len(num)):
      sum = num[i]+ num[i+1]
      if sum == target:
        return [i,i+1]
'''

def twoSum(nums,target):
  valueMap = dict()
  output = set()
# say we are finding 5 sum of two and 3 in 0 and  1 index
  for i, num in enumerate(nums):
    #stores the completem for each indexes
    complement = target - num # 2 = 5 - 3
    if complement in valueMap:
      #return [valueMap[complement],i]
      output.add((valueMap[complement],i))
    valueMap[num]= i  # Mapping Vaule to index just reverseing assignment of array, here Vaule is the key and index is the Value.
  return output
  
output = twoSum([1,2,2,3,4],5)
print('\n'.join(map(str,list(output))))