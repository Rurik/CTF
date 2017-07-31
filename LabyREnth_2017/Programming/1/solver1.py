import telnetlib
import re
import queue

PASS = b"MAZE4J002PLAY"
CLIENT = telnetlib.Telnet("pwn2.ddtek.biz", 11511)

CLIENT.read_until(b"Password: ")
CLIENT.write(PASS)
print(CLIENT.read_until(b"Maze solutions must be presented as a single
line of input.\n"))

def is_boundry(l):
   return re.match(r"^\#+$", l)

def read_line():
   return CLIENT.read_until(b"\n").decode().rstrip()

def read_board():
   first_line = read_line()
   if not is_boundry(first_line):
       raise Exception("invalid board start: %s" % first_line)

   board = []
   while True:
       l = read_line()
       if is_boundry(l):
           break
       else:
           board.append(l)

   return board

WALL = "#"
SPACE = "."
START = "s"
FINISH = "f"

def solve_board(board):
   height = len(board)
   width = len(board[0])

   print("Solving board:")
   print("#" * width)
   for l in board: print(l)
   print("#" * width)

   for ypos, line in enumerate(board):
       start_x = line.find(START)
       if start_x != -1:
           start_y = ypos
           break

   visited = [[False]*width for i in range(height)]
   sq = queue.Queue()
   sq.put((start_x, start_y, ""))

   while sq:
       posx, posy, moves = sq.get()
       if posx < 0 or posx >= width or posy < 0 or posy >= height:
           continue

       if visited[posy][posx] == True:
           continue

       visited[posy][posx] = True

       if board[posy][posx] == FINISH:
           print("Solution: %s" % moves)
           return moves

       if board[posy][posx] == WALL:
           continue

       sq.put((posx+1, posy, moves+"e"))
       sq.put((posx-1, posy, moves+"w"))
       sq.put((posx, posy+1, moves+"s"))
       sq.put((posx, posy-1, moves+"n"))

while True:
   b = read_board()
   solution = solve_board(b)
   CLIENT.write(solution.encode())