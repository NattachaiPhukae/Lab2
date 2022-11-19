# from ex4
arr2D = [['Number ID', 'Name', 'Count', 'Status']]
arr2D.append([1, 'Rubber', 0, 'Out of stock'])
arr2D.append([2, 'Ruler', 5, 'In stock'])
arr2D.append([3, 'Pencil', 1, 'In stock'])

# ex5
arr2D.append([4, 'Pen', 10, 'In stock'])
arr2D.append([5, 'Colour pencil', 5, 'In stock'])
arr2D.append([6, 'A4 Paper', 0, 'Out stock'])

print()
print("List of items in stock:")
for i in range(len(arr2D)):
    arr = arr2D[i]
    if arr[3] == 'In stock':
        print(arr)
print()
print("List of items out of stock:")
for i in range(len(arr2D)):
    arr = arr2D[i]
    if arr[3] == 'Out of stock':
        print(arr)

for i in range(len(arr2D)):
    arr = arr2D[i]
    name = arr[1]
    if name == "Ruler":
        if arr[2] > 1:
            arr[2] -= 1
        else:
            arr[2] = 0
            arr[3] = "Out of stock"
    if name == "Pencil":
        if arr[2] > 1:
            arr[2] -= 1
        else:
            arr[2] = 0
            arr[3] = "Out of stock"
    if name == "Pen":
        if arr[2] > 2:
            arr[2] -= 2
        else:
            arr[2] = 0
            arr[3] = "Out of stock"
    if name == "Colour pencil":
        if arr[2] > 1:
            arr[2] -= 1
        else:
            arr[2] = 0
            arr[3] = "Out of stock"

print()
print("List of items in stock:")
for i in range(len(arr2D)):
    arr = arr2D[i]
    print(arr)
