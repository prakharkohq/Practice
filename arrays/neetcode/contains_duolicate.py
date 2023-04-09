
def contains_duplicate(arr):
    hashset = set()  # Always declare hashset or other types with opening and closing parenthesis because of
    for item in arr:
        if item in hashset:
            return True
        else:
            hashset.add(item)

    return False

print(contains_duplicate([1,2,3,3,4]))
