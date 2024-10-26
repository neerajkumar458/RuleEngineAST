class Node:
    def __init__(self, node_type, value=None):
        self.type = node_type  
        self.value = value  
        self.left = None  
        self.right = None 

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"
