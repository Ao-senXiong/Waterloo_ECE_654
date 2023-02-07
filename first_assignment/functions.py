import ast

def check_length(node):
    if isinstance(node, ast.Name) and len(node.id) == 13:
        raise Exception("Identifier with length equal to 13 found")

def check_nesting(node, depth=1):
    if depth > 4:
        raise Exception("Control structure nesting exceeds 4")
    if isinstance(node, (ast.If, ast.For, ast.While)):
        for child in ast.iter_child_nodes(node):
            check_nesting(child, depth + 1)

def analyze_ast(source):
    tree = ast.parse(source)
    for node in ast.walk(tree):
        check_length(node)
        check_nesting(node)
    return "Static analysis successful, no issues found."

# source = open("testcases/ast_example_indentifier.py", "r")
# analyze_ast(source)