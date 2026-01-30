def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)


# Solution: A straightforward (and totally fine) solution is to replace the original print call with:

# if total_candies == 1:
#     print("Splitting 1 candy")
# else:
#     print("Splitting", total_candies, "candies")
# # Here's a slightly more succinct solution using a conditional expression:

# print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")