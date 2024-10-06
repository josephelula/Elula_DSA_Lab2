
# Function to compute cube of integers
def cube(num):
    if num == 0:
        return 0
    return num * num * num

# Input what is the size of the array
size = int(input("Enter the size of the array: "))

# Input the elements of the array
arr = list(map(int, input(f"Enter the elements separated by space: ").split()))

# Display the cube of the element
for num in arr:
    print(cube(num))