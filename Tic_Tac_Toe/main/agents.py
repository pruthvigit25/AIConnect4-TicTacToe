from math import inf
import numpy as np
import time
import random

class Agent:
  
  def __init__(self):
    import gui           
    self.gui = gui.gui() 

  def checkmove(self,board,turn):    
    self.board = board
    self.updategame()

    checkmove = self.decision()

    self.board[checkmove[0],checkmove[1]] = turn
    self.updategame()
    return checkmove

  def updategame(self):     
    self.gui.draw_board()
    self.gui.draw_xo(self.board)

  def decision(self):  
    return self.gui.play()

  def show_end_state(self,board): 
    self.board = board
    self.updategame()
    self.gui.draw_line(board)
    time.sleep(1)


class Random:

  def checkmove(self,board,turn):
    self.board = board
    possible_moves = np.argwhere(self.board == 0)   
    checkmove = np.random.permutation(possible_moves)[0] 

    return (checkmove[0],checkmove[1])                  

############## ALGORITHMES ##############

def win_evaluation(board):    
  
  board = np.array(board) if type(board) == list else board   

  for x in range(3):
    if board[x,0] == board[x,1] == board[x,2] != 0: return board[x,0]    # -
    elif board[0,x] == board[1,x] == board[2,x] != 0: return board[0,x]  # |
    elif board[0,0] == board[1,1] == board[2,2] != 0: return board[0,0]  # \
    elif board[0,2] == board[1,1] == board[2,0] != 0: return board[0,2]  # /
  if np.count_nonzero(board) < 9: return 0  
  return 3                                  


def score_evaluation(board,turn):
  
  antiturn = 0
  if turn == 1: 
    antiturn = 2
  elif turn == 2: 
    antiturn = 1
    
  if win_evaluation(board) == antiturn:   
    score = -1
  elif win_evaluation(board) == turn:
    score = 1
  else:
    score = 0
  return score

def minimax_algorithm(board,depth,turn,maximizingPlayer=True):
  
  board = list(board)   

  if win_evaluation(board) != 0:    
    return score_evaluation(board,turn)
  if maximizingPlayer:
    best_score = -inf
    for row in range(3):
      for col in range(3):
        if board[row][col] == 0:  
          board[row][col] = 1      
          score = minimax_algorithm(board,depth-1,turn,False)     
          board[row][col] = 0     
          best_score = max(best_score,score)     
    return best_score
  else:  
    best_score = +inf
    for row in range(3):
      for col in range(3):
        if board[row][col] == 0:
          board[row][col] = 2
          score = minimax_algorithm(board,depth-1,turn,True)
          board[row][col] = 0
          best_score = min(best_score,score)
    return best_score    

def best_move(board,turn):
  best_score = -inf
  for row in range(3):
    for col in range(3):
      if board[row,col] == 0:
        board[row,col] = turn

        score = minimax_algorithm(board,list(np.ravel(board)).count(0),turn,False) 
        
        board[row,col] = 0
        best_score = max(best_score,score)
        if best_score == score:
          checkmove = (row,col)
  return checkmove

class Minimax:

  def checkmove(self,board,turn):
    return best_move(board,turn)


class Q_learning:
  
  def __init__(self,Q={},epsilon=0.3, alpha=0.2, gamma=0.9):
    self.q_table = Q
    self.epsilon = epsilon    # Exploration vs Exploitation
    self.alpha = alpha          # Learning rate
    self.gamma = gamma          # Discounting factor

  def encode(self,state):      
    s = ''
    for row in range(3):
      for col in range(3):
        s += str(state[row,col])
    return s

  def decode(self,s):          
    return np.array([[int(s[0]),int(s[1]),int(s[2])],[int(s[3]),int(s[4]),int(s[5])],[int(s[6]),int(s[7]),int(s[8])]])

  def format(self,action):       
    if type(action) == int:
      return action
    else:
      return 3*action[0] + action[1]

  def possible_actions(self,board):
    return [i for i in range(9) if self.encode(np.array(board))[i]=='0']

  def q(self,state,action):
    action = self.format(action)
    if (self.encode(state),action) not in self.q_table:
      self.q_table[(self.encode(state),action)] = 1   
    return self.q_table[(self.encode(state),action)]

  def checkmove(self,board,turn):
    self.board = board
    actions = self.possible_actions(board)
    
    if random.random() < self.epsilon:        # exploration
      self.last_move = random.choice(actions)
      self.last_move = (self.last_move//3,self.last_move%3) 
      return self.last_move
    
    q_values = [self.q(self.board, a) for a in actions]
    
    if turn == 2:   
      max_q = max(q_values)
    else:        
      max_q = min(q_values)

    if q_values.count(max_q) > 1:     
      best_actions = [i for i in range(len(actions)) if q_values[i] == max_q]
      i = np.random.permutation(best_actions)[0]
    else:
      i = q_values.index(max_q)

    self.last_move = actions[i]
    self.last_move = (self.last_move//3,self.last_move%3)
    return self.last_move

  def learn(self,S,A,S1,A1,reward):
    A = self.format(A)
    A1 = self.format(A1)

    prev = self.q(S,A)
    maxnewq = self.q(S1,A1)
    
    S = self.encode(S)
    S1 = self.encode(S1)

    self.q_table[(S,A)] = prev + self.alpha * (reward + self.gamma*maxnewq - prev)