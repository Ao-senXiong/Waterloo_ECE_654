import sys
sys.path.insert(0, '/Users/ocen/Documents/GitHub/Waterloo_ECE_654/first_assignment')
from main import analyze_ast

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