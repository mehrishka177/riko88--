class pair_elements:
    
        def twoSum(self, nums, target):
                lookup = {}
    
                for i, num in enumerate(nums):
                       if target - num in lookup:
                               return (lookup[target - num], i)
                       lookup[num]  = i

value = int(input("Enter sum for which you want to make this reaserch :"))
print("index1=%d, index2=%d"%
pair_elements().twoSum((10,20,30,40,50,60,70),value))
            