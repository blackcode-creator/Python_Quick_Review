#
# # Generating coordinates
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# Challenge:
numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)