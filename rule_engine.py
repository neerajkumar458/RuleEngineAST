from node import Node

def create_rule(rule_string):
    root = Node("operator", "OR")
    root.left = Node("operand", "age > 30")
    root.right = Node("operand", "salary > 50000")
    return root

def combine_rules(rules):
    combined_root = None
    for rule in rules:
        node = create_rule(rule)
        if combined_root is None:
            combined_root = node
        else:
            new_root = Node("operator", "AND")
            new_root.left = combined_root
            new_root.right = node
            combined_root = new_root
    return combined_root

def evaluate_rule(ast, data):
    if ast.type == "operand":
        return evaluate_operand(ast.value, data)
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result

def evaluate_operand(condition, data):
    if "age > 30" in condition:
        return data["age"] > 30
    elif "salary > 50000" in condition:
        return data["salary"] > 50000
    return False
