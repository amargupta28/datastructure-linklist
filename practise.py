def overlappedInterval(Intervals):
  ans=[]
  print(type(Intervals))
  i=0
  while i < len(Intervals)-1:
    # print(i)
    print(Intervals[i])
    print((i+1)%2 ==0 and Intervals[i] > Intervals[i+1])
    if (i+1)%2 ==0 and Intervals[i] > Intervals[i+1]:
      # ans.append(Intervals[i+1])
      i+=2
    else:
      ans.append(Intervals[i])
      i+=1
    
  ans.append(Intervals[i])
  # print(ans)
  return ans

print(overlappedInterval([6,8,1,9,2,4,]))