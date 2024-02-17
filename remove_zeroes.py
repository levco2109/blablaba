def remove_zeroes(nums: list[int]) -> int:
  """Переносим все 0 конец и возвращаем индекс первого нуля"""
  zero_index = 0

  for i in range(len(nums)):
    if nums[i] != 0:
      nums[zero_index], nums[i] = nums[i], nums[zero_index]
      zero_index += 1
  return zero_index
nums = [0,42,21,0,100,0,5,1,0,7,3,0,404,0]
zero_index = remove_zeroes(nums)
print(nums[:zero_index])
print(zero_index)

assert zero_index == 8
assert nums[:zero_index] == [42,21,100,5,1,7,3,404]


nums2 = []
new_len2 = remove_zeroes(nums2)
assert new_len2 == 0
assert nums2 == []

nums3 = [0, 0, 0, 0, 0]
new_len3 = remove_zeroes(nums3)
assert new_len3 == 0
assert nums3 == [0, 0, 0, 0, 0]

nums4 = [1, 2, 3, 4, 5]
new_len4 = remove_zeroes(nums4)
assert new_len4 == 5
assert nums4 == [1, 2, 3, 4, 5]

nums5 = [1, 2, 3, 4, 5, 0]
new_len5 = remove_zeroes(nums5)
assert new_len5 == 5
assert nums5 == [1, 2, 3, 4, 5, 0]

nums6 = [0, 1, 2, 3, 4, 5]
new_len6 = remove_zeroes(nums6)
assert new_len6 == 5
assert nums6 == [1, 2, 3, 4, 5, 0]

nums7 = [1, 0, 2, 0, 3, 0, 4]
new_len7 = remove_zeroes(nums7)
assert new_len7 == 4
assert nums7 == [1, 2, 3, 4, 0, 0, 0]