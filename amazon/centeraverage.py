def centered_average(nums):
  nums.remove(min(nums))
  print(nums)
  nums.remove(max(nums))
  print(nums)
  output=0
  for i in nums:
    output+=i
  
  output = output/len(nums)
  return output

print(centered_average([1, 2, 3, 4, 100]))