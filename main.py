# Get the first item in a list that matches condition - Python

my_list = [1, 3, 7, 14, 29, 35, 105]

first_match = next(
    (item for item in my_list if item > 14),
    None
)
print(first_match)  # 👉️ 29