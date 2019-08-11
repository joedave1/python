def permutethenumber(nums):
  res_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        res_perms = new_perms
  return res_perms

a = [1,2,3]
print("before permutation: ",a)
print("after permutations:\n",permutethenumber(a))
