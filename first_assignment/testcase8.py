import sys
sys.path.insert(0, '/Users/ocen/Documents/GitHub/Waterloo_ECE_654/first_assignment')
from main import analyze_ast
source = """
if True:
    print("Hello")
else:
    print("World")
"""
result = analyze_ast(source)
if result == "Static analysis successful, no issues found.":
    print("Test case 8 passed")
else:
    print("Test case 8 failed, unexpected result")