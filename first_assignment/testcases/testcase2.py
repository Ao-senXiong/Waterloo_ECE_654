import sys
sys.path.insert(0, '/Users/ocen/Documents/GitHub/Waterloo_ECE_654/first_assignment')
from main import analyze_ast

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