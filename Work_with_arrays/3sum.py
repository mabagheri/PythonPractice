a = [2, 0, -1, 0, 1, 2, -1, -4]

n = len(a)
d = set()
result = []
for i in range(n):
    for j in range(i + 1, n):
        unsorted = (a[i], a[j], -(a[i] + a[j]))
        # Find the tuple that uniquely represents those three numbers.
        unique_tuple = tuple(sorted(unsorted))
        if unique_tuple in d:
            # # Already in the results.
            continue
        d.add(unique_tuple)
        for k in range(j + 1, n):
            if a[i] + a[j] + a[k] == 0:
                result.append((a[i], a[j], a[k]))
print(result)


# A simple Python 3 program
# to find three elements whose
# sum is equal to zero

# function to print triplets with 0 sum
def findTriplets(arr, n):
    found = False
    for i in range(n - 1):

        # Find all pairs with sum
        # equals to "-arr[i]"
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])

    if not found:
        print("No Triplet Found")

arr = [0, -1, 2, -3, 1]
n = len(a)
findTriplets(a, n)
