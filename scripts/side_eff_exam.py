array = [1, 2, 3, 4]
def reversi(arr):
    """Reverses a list."""
    for i in range(len(arr) // 2):
        arr[-i - 1], arr[i] = arr[i], arr[-i - 1]
    return arr

def good_reversi(arr):
    """Reverses a list."""
    for i in range(len(arr) // 2):
        arr[-i - 1], arr[i] = arr[i], arr[-i - 1]
    return None

def better_reversi(arr):
    """Reverses a list."""
    reved = []
    for i in range(len(arr)):
        reved.append(arr[len(arr) - 1 - i])
    return reved

print(array)
print(reversi(array))
print(array)
print(good_reversi(array))
print(array)
print(better_reversi(array))
