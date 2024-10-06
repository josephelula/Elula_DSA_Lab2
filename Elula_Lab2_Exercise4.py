
# Function for inverted right triangle
def inverted_right_triangle(n):
    # Loop from n down to 1
    for i in range(n, 0, -1):
        print("*" * i)

# Height of the triangle
height = int(input("Enter the height of triangle: "))
inverted_right_triangle(height)