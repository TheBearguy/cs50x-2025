# Adversarial search:
# 2 players, each trying to win
# win => (fairly winning by individual moves + restricting the other player from winning)
# if win = 1, draw = 0, lose = -1
# in general, player A = to maximise the score, player B = to minimize the score

# Optimization -> Alpha Beta Pruning
# Optimization -> Depth Limited minimax algorithm -> searches for limited steps ahead in the tree, (not till the end / terminating state)
# If all the states are not considered then we wont really have proper scores as defined previously(1, 0, -1) but rather now we have to calculate what the expected score will be for a particular state
# Evaluation fn -> functin that estimates the expected utility of the game from a given state
import math
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # base case: target depth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]
    # X's turn
    if (maxturn):
        return max(minimax(curDepth+1, nodeIndex*2, False, scores, targetDepth), minimax(curDepth+1, nodeIndex*2+1, False, scores, targetDepth))

    else:
        return min(minimax(curDepth+1, nodeIndex*2, True, scores, targetDepth), minimax(curDepth+1, nodeIndex*2+1, True, scores, targetDepth))


# Driver code:
scores = [-1, 0, 1]
treeDepth = math.log(len(scores), 2)
print(f"The Optimal value is: {minimax(0 ,0, True, scores, treeDepth)} ")



MAX, MIN = 1000, -1000

# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimaxAlphaBeta(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):

    # Terminating condition. i.e
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:

        best = MIN

        # Recur for left and right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        # Recur for left and
        # right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

# Driver Code
if __name__ == "__main__":

    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))
