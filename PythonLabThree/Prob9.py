'''Write a Python function that checks whether a passed string is palindrome or not.'''
def palindrome(a):
    left_pos = 0
    right_pos = len(a) - 1

    while right_pos >= left_pos:
        if not a[left_pos] == a[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

print(palindrome('12121'))