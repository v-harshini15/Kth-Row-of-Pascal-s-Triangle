def getRow(k):
    if k < 0:
        return []

    # Initialize the row with the first element
    row = [1]

    for i in range(1, k + 1):
        # Calculate the next element using the previous row
        new_element = row[i - 1] * (k - i + 1) // i
        row.append(new_element)

    return row

# Example
k = 3
result = getRow(k)
print(result)  # Output: [1, 3, 3, 1]
