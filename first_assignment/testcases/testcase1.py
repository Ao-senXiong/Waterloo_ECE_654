import sys
sys.path.insert(0, '/Users/ocen/Documents/GitHub/Waterloo_ECE_654/first_assignment')
from main import analyze_ast
source = "aaaaaaaaaaaaa = 1"
try:
    analyze_ast(source)
    print("Test case 1 failed, exception expected")
except Exception as e:
    if str(e) == "Identifier with length equal to 13 found":
        print("Test case 1 passed")
    else:
        print("Test case 1 failed, unexpected exception")