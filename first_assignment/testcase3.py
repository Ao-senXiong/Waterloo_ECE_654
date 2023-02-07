from functions import analyze_ast

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