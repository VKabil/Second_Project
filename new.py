
#Create Target Array in the Given Order

nums = [0,1,2,3,4]
index = [0,1,2,2,1]

target_index=[]
for i in range(len(nums)):
    target_index.insert(index[i], nums[i])

print(target_index)

