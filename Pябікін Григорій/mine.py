# int float
# str
# turple [1,2] [0] = [1,2] 
# bool
# set

names = set()
print(names)

names.add("Olen")
print(names)
names.pop()
names.add("Rooms")
names.add("Lom")
names.add("Olen")
print(names)
names.clear()
print(names)

devices1 = {1, 2, 3, 4, 4}
devices2 = {1, 1, 2, 2}
print(devices1 & devices2) # OБЩЕЕ ЗНАЧЕННЯ
print(devices1 ^ devices2)
1
print(sum(devices1 & devices2))
print(sum(devices1 ^ devices2))

print(devices1 - devices2)
device3 = devices1.difference(devices2)
print(device3)
device4 = device3.copy()
print(device4)
#практичне завдання
nums1 = set()
nums2 = set()

nums1.add("3")
nums1.add("4")
nums2.add("5")
nums2.add("6")

nums2.clear()

nums3 = nums2.difference(nums1)
print(nums3)




















