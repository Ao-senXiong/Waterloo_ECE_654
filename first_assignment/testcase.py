from functions import analyze_ast

source = "aaaaaaaaaaaaa = 1"
try:
    analyze_ast(source)
    print("Test case 1 failed, exception expected")
except Exception as e:
    if str(e) == "Identifier with length equal to 13 found":
        print("Test case 1 passed")
    else:
        print("Test case 1 failed, unexpected exception")

source = """
if True:
    if True:
        if True:
            if True:
                print("Too much nesting")
"""
try:
    analyze_ast(source)
    print("Test case 2 failed, exception expected")
except Exception as e:
    if str(e) == "Control structure nesting exceeds 4":
        print("Test case 2 passed")
    else:
        print("Test case 2 failed, unexpected exception")

source = """
a = 1
b = 2
c = 3
"""
result = analyze_ast(source)
if result == "Static analysis successful, no issues found.":
    print("Test case 3 passed")
else:
    print("Test case 3 failed, unexpected result")

source = """
for i in range(10):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
"""
result = analyze_ast(source)
if result == "Static analysis successful, no issues found.":
    print("Test case 4 passed")
else:
    print("Test case 4 failed, unexpected result")


source = "aaaaaaaaa = 1"
result = analyze_ast(source)

if result == "Static analysis successful, no issues found.":
    print("Test case 5 passed")
else:
    print("Test case 5 failed, unexpected result")