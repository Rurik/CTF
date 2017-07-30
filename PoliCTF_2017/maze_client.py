from socket import create_connection
import Queue


MAZE_SERVER = ('tower.chall.polictf.it', 31337)
RECV_SIZE = 8192

WALL = ('|', '_', ' ')
SPACE = " "
START = ">"
FINISH = "X"

def solve_board(board):
   height = len(board)
   width = len(board[0])

   print("Solving board:")
   #print("#" * width)
   for l in board: print(l)
   #print("#" * width)

   start_x = start_y = 0
   #for ypos, line in enumerate(board):
   #    start_x = line.find(START)
   #    if start_x != -1:
   #        start_y = ypos
   #        break

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
           #print("Solution: %s" % moves)
           return moves

       if board[posy][posx] in WALL:
           continue

       sq.put((posx+1, posy, moves+">"))
       sq.put((posx-1, posy, moves+"<"))
       sq.put((posx, posy+1, moves+"V"))
       sq.put((posx, posy-1, moves+"^"))


def main():
    maze_map = list()
    conn = create_connection(MAZE_SERVER, 1)
    maze_raw = ''
    for i in range(69):
        try:
            response = str(conn.recv(8192))
        except:
            continue
        maze_raw += response
#        print(response)
    maze_raw += response
    print(maze_raw)
    print(len(maze_raw))

    quit()
    print(maze_raw)
    for i in maze_raw.split('\n'):
        print(len(i))
    quit()
    print(len(maze_map))
    print(maze_map[10])
    quit()

    """
    maze = list()
    start = False
    for i in str(response).split('\\n'):
        if 'Now' in i:
            start = True
        if start:
            if len(i) > 10:
                if i[0] == '#':
                    maze.append(i)# += i + '\n'
    solution = solve_board(maze)
    print(solution)
    """
    
    while True:
        print(response)
        quit()
        maze = list()
        start = False
        for i in str(response).split('\\n'):
            if 'Now' in i:
                start = True
            if start:
                if len(i) > 10:
                    if i[0] == '#':
                        maze.append(i)# += i + '\n'

        if "Now " not in str(response):
            break

        #response_lines = response.splitlines()
        #find_delim = [x for x in response_lines if x.startswith('Now')][0]
        #maze_lines = response_lines[response_lines.index(find_delim)+2:-1]
        #maze_text = '\n'.join(maze_lines)

        # Do your thing here with either maze_text or maze_lines.
        solution = solve_board(maze)
        print(solution)
        #print(unicode(solution))
        #solution = raw_input("Your solution: ")
        #if not len(solution):
        #    return
        conn.send(solution.encode(encoding='utf-8'))

        response = conn.recv(RECV_SIZE)
    print(response)

if __name__ == '__main__':
    main()
