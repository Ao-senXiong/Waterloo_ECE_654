from functions import analyze_ast
source = """
if True:
    for i in range(10):
        if i % 2 == 0:
            while True:
                if i % 3 == 0:
                    print("Too much nesting")
"""
try:
    analyze_ast(source)
    print("Test case 6 failed, exception expected")
except Exception as e:
    if str(e) == "Control structure nesting exceeds 4":
        print("Test case 6 passed")
    else:
        print("Test case 6 failed, unexpected exception")