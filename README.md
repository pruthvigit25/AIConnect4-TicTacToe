# Board Game Comparison: Tic Tac Toe and Connect4

Implementation of two popular board games, Tic Tac Toe and Connect4, using Minimax and Reinforcement Learning algorithms. We compare the performance of these algorithms in the games. Tic Tac Toe is a game with a smaller number of possible movements, while Connect4 has a much larger space. Both games have been used by AI researchers to explore various AI techniques, including game theory, heuristic search, and reinforcement learning. The effectiveness of AI algorithms in these games has paved the way for their implementation in more complex games and real-world issues.

## Algorithms

1. Minimax (with alpha-beta pruning):
   - Minimax with alpha-beta pruning is a decision-making algorithm in two-player games.
   - It minimizes the maximum possible loss by selecting the move that ensures the smallest maximum possible loss.
   - The algorithm models the game tree to a specified depth and evaluates the results of each possible move.
   - Alpha-beta pruning is used to reduce the number of nodes analyzed by removing irrelevant branches from the game tree.
   - Alpha represents the highest known value to the maximizer, and beta represents the highest known value to the minimizer.

2. Q-learning:
   - Q-learning is a model-free reinforcement learning algorithm that uses a Q-table to store the expected reward for each action in each state.
   - The algorithm discovers the optimal policy for the game by modifying the Q-values in the table based on the rewards received and actions taken.
   - Q-values are updated using the Bellman equation, which combines the immediate reward and the expected future reward.
   - Q-learning can determine the best policy without knowing the optimal policy beforehand.

## Choice of Hyperparameters

In Q-learning, the hyperparameters that affect the algorithm's performance and behavior are:
- Epsilon: Determines the exploration-exploitation balance. A higher value means more exploration.
- Alpha: Regulates the rate of learning. It determines the importance of new and older information.
- Gamma: Regulates the discount factor. It determines the importance of future and immediate rewards.

## Implementations and Results

### Tic Tac Toe MinMax and QLearning
- Tic Tac Toe MinMax (Alpha Beta): Implemented using PyQt5 library for the GUI. Allows a player to play against the MinMax algorithm.
- Tic Tac Toe QLearning: Implemented using a Q-learning algorithm. The agent's moves are based on learned Q-values.

### Connect4 MinMax and QLearning
- Connect4 MinMax: Implemented using Pygame library for the GUI. The AI uses the MinMax algorithm with alpha-beta pruning.
- Connect4 QLearning: Implemented using Q-learning algorithm. The AI player makes moves based on learned Q-values.

## Conclusion

The implementation of Minimax and Q-learning algorithms in Tic Tac Toe and Connect4 games shows their effectiveness in decision-making and learning. The Minimax algorithm with alpha-beta pruning provides optimal moves, while the Q-learning algorithm learns the optimal policy without prior knowledge. The choice of hyperparameters can significantly affect the algorithm's behavior and performance. Overall, these algorithms contribute to AI research and can be applied to more complex games and real-world problems.

