# # Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. 
# Run through 
# the UPER problem solving framework while going through your thought process.

# Understand: That I have to find the smallest number within the list of lists and return that as a total
# sum of all the minimum numbers as shown above

array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
end_result_numbers = []

def sort_min(arr):
    for i in arr:
        current_arr = arr[i]
        x = current_arr.sort()
        end_result_numbers.append(x)
    for a in end_result:
        total = sum(end_result_numbers)
        
        