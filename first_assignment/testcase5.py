from functions import analyze_ast
source = "aaaaaaaaa = 1"
result = analyze_ast(source)

if result == "Static analysis successful, no issues found.":
    print("Test case 5 passed")
else:
    print("Test case 5 failed, unexpected result")