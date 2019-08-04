
list1=[1,2,3,4]
pos=3-1
index=0
len1=len(list1)
while len1>0:
  index=(pos+index)%len1
  print(list1.pop(index))
  len1-=1
