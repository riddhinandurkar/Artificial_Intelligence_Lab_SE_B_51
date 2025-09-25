import math

# Sample game tree represented as a list of lists (for simplicity)
# Leaf nodes are the terminal values.
# Internal nodes are lists of child nodes.

game_tree = [
    [3, 5, 6],             # First branch
    [9, 1, 2],             # Second branch
    [0, -1, 4, 5]          # Third branch
]

def minimax(node, depth, maximizingPlayer, nodes_counter):
    if depth == 0 or not isinstance(node, list):
        nodes_counter[0] += 1
        return node

    if maximizingPlayer:
        maxEval = -math.inf
        for child in node:
            eval = minimax(child, depth - 1, False, nodes_counter)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        for child in node:
            eval = minimax(child, depth - 1, True, nodes_counter)
            minEval = min(minEval, eval)
        return minEval

def alphabeta(node, depth, alpha, beta, maximizingPlayer, nodes_counter):
    if depth == 0 or not isinstance(node, list):
        nodes_counter[0] += 1
        return node

    if maximizingPlayer:
        maxEval = -math.inf
        for child in node:
            eval = alphabeta(child, depth - 1, alpha, beta, False, nodes_counter)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return maxEval
    else:
        minEval = math.inf
        for child in node:
            eval = alphabeta(child, depth - 1, alpha, beta, True, nodes_counter)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return minEval

def main():
    depth = 2  # Because tree has 2 levels: root and children

    minimax_nodes = [0]
    alpha_nodes = [0]

    optimal_minimax = minimax(game_tree, depth, True, minimax_nodes)
    optimal_alphabeta = alphabeta(game_tree, depth, -math.inf, math.inf, True, alpha_nodes)

    print(f"Optimal value (with Alpha-Beta Pruning): {optimal_alphabeta}\n")
    print("Observation Table:\n")
    print(f"{'Parameter':<20} {'Minimax':<12} {'Alpha-Beta':<12}")
    print("-" * 43)
    print(f"{'Nodes evaluated':<20} {minimax_nodes[0]:<12} {alpha_nodes[0]:<12}")
    print(f"{'Optimal value':<20} {optimal_minimax:<12} {optimal_alphabeta:<12}")

if __name__ == "__main__":
    main()

