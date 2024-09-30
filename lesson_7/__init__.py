# Exercise 5. The Red Crayon 🖍️

# Imagine you have a box of crayons, and you're looking for a "Red" crayon.
# You pull out one crayon at a time from the box.

# Use a while loop to simulate this scenario.  As soon as you find the "Red" crayon, stop the loop.

colors = ["Blue", "Yellow", "Green", "Red", "Purple", "Orange"]
index = 0

# This should basically say: while the current color being evaluated is
# different than "Red", increment to the next color and try again.
while colors[index] != "Red":
    print(f"Found {colors[index]} crayon. Still looking for Red.")
    index += 1

print("Found the Red crayon!")