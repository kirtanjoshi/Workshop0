# Task 1

def sum_nested_list(nested_list):
 """
 Calculate the sum of all numbers in a nested list.
 This function takes a list that may contain integers and other nested lists.
 It recursively traverses the list and sums all the integers, no matter how deeply
 nested they are.
 Args:
 nested_list (list): A list that may contain integers or other lists of integers.
 Returns:
 18
5CS037 Worksheet-0 SimanGiri
 int: Thetotalsumofallintegersinthenestedlist,includingthoseinsublists
 .
 Example:
 >>>sum_nested_list([1,[2,[3,4],5],6,[7,8]])
 36
 >>>sum_nested_list([1,[2,3],[4,[5]]])
 15
 """
 total=0
 for element in nested_list:
    if isinstance(element,list):#Checkiftheelementisalist
        total+=sum_nested_list(element)#Recursivelysumthenestedlist
    else:
        total+=element #Addthenumbertothetotal
 return total



nested_list = [1,[2,[3,4],5],6,[7,8]]
result =sum_nested_list(nested_list)
print("The total sum is :",result)


# Task 2
def generate_permutations(s):
    
    # Recursive case: generate permutations for the rest of the string
    permutations = []
    for i in range(len(s)):
        # Extract the current character
        current_char = s[i]
        # Generate permutations for the remaining characters
        remaining_chars = s[:i] + s[i+1:]
        for permutation in generate_permutations(remaining_chars):
            permutations.append(current_char + permutation)
    
    return permutations

user_input = input("Enter any alphabet: ")
result = generate_permutations(user_input)

print("All permutations of the string are:")
for perm in result:
    print(perm)


# Task 3
def calculate_directory_size(directory):
    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict):  # Check if the value is a subdirectory
            total_size += calculate_directory_size(value)  # Recursive call for subdirectory
        else:  # Value is the size of a file
            total_size += value
    return total_size

# Example usage
#Sampledirectorystructure
directory_structure={
    "file1.txt":200,
    "file2.txt":300,
    "subdir1":{
        "file3.txt":400,
        "file4.txt":100
    },
    "subdir2":{
        "subsubdir1":{
            "file5.txt":250
    },
 "file6.txt": 150
 }
 }

print(calculate_directory_size(directory_structure)) 

