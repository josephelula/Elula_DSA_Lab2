
# Funtion for hollow square
def hollow_square(n):
    # Loop through each row
    for i in range(n):
        # If it's the first or last row print all stars
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
            print("x" + " " * (n - 2) + "x")

# Side length of the square
side_length = int(input("Enter the side length of the square: "))
hollow_square(side_length)