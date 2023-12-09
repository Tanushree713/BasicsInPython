def CountOperation(arr):
#     count = 0 
#     i = 0
#     j = len(arr) - 1
#     while i < j:
#        if arr[i] == arr[j]:
#          i += 1
#          j -= 1
#        elif arr[i] < arr[j]:  #{ i = 2 , j = 4 , where i < j }
#         arr[i+1] = arr[i+1] + arr[i] # {indx2 = 6}
#         count += 1
#        else :
#         arr[j-1] = arr[j-1] + arr[j]
#         count += 1

#     return count       
# nums = [1, 2 , 4 , 1] 
# result = CountOperation(nums)