from functions import analyze_ast
source = """
a = 1
b = 2
c = 3
d = 4
"""
result = analyze_ast(source)
if result == "Static analysis successful, no issues found.":
    print("Test case 7 passed")
else:
    print("Test case 7 failed, unexpected result")