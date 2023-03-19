nums = [2, 5, 3, 7, 3, 8]
target = 12
new_list = []
for i in range(len(nums)):
    for m in range(i + 1, len(nums)):
        if nums[i] + nums[m] == target:
            new_list.append(i)
            new_list.append(m)
if len(new_list) == 0:
    new_list = None
print(new_list)