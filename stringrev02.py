def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1
input_str = 'ABCDEF'
if __name__ == "__main__":
    print('Reverse string using while loop =',reverse_join_reversed_iter(input_str))
