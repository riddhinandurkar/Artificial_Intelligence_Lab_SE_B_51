class Node:
def __init__(self, name, value=None, left=None, right=None):
self.name = name
self.value = value
self.left = left
self.right = right
def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
"""Alpha-Beta pruning with pruning print statements."""
if depth == 0 or (node.left is None and node.right is None):
print(f"Visited leaf {node.name} → value = {node.value}")
return node.value
if maximizingPlayer:
value = float("-inf")
print(f"MAX node {node.name}, depth {depth}, α={alpha}, β={beta}")
if node.left:
value = max(value, alpha_beta(node.left, depth - 1, alpha, beta, False))
alpha = max(alpha, value)
if beta <= alpha:
print(f"⛔ Pruning at {node.name} after left child")
return value
if node.right:
value = max(value, alpha_beta(node.right, depth - 1, alpha, beta, False))
alpha = max(alpha, value)
if beta <= alpha:
print(f"⛔ Pruning at {node.name} after right child")
return value
return value
else:
value = float("inf")
print(f"MIN node {node.name}, depth {depth}, α={alpha}, β={beta}")
if node.left:
value = min(value, alpha_beta(node.left, depth - 1, alpha, beta, True))
beta = min(beta, value)
if beta <= alpha:
print(f"⛔ Pruning at {node.name} after left child")
return value
if node.right:
value = min(value, alpha_beta(node.right, depth - 1, alpha, beta, True))
beta = min(beta, value)
if beta <= alpha:
print(f"⛔ Pruning at {node.name} after right child")
return value
return value
def print_tree(node, level=0, prefix="Root: "):
"""Pretty print the binary tree structure."""
if node is not None:
print(" " * (4 * level) + prefix + f"{node.name}", end="")
if node.value is not None:
print(f" ({node.value})") # Leaf value
else:
print()
if node.left:
print_tree(node.left, level + 1, "L--- ")
if node.right:
print_tree(node.right, level + 1, "R--- ")
# ------------------------------
# Build Example Binary Tree
# ------------------------------
D = Node("D", value=3)
E = Node("E", value=5)
F = Node("F", value=6)
G = Node("G", value=9)
B = Node("B", left=D, right=E) # Min
C = Node("C", left=F, right=G) # Min
A = Node("A", left=B, right=C) # Max
# ------------------------------
# Print Tree
# ------------------------------
print("Binary Tree Structure:\n")
print_tree(A)
# ------------------------------
# Run Alpha-Beta with Logs
# ------------------------------
print("\nAlpha-Beta Execution Trace:\n")
best_value = alpha_beta(A, 2, float("-inf"), float("inf"), True)
print("\n✅ Best achievable value for the maximizing player:", best_value)
