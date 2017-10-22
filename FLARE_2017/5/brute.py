import pexpect
import time

answers = list()
answers.append(['B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'B5', 'E5', 'B6', 'E6', 'B7', 'E7'])
answers.append(['B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'E5', 'E6', 'E7', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8'])
answers.append(('A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B8', 'C1', 'D1', 'E1', 'E5', 'E6', 'E7', 'E8', 'F1', 'F8', 'G1', 'G8', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7'))
answers.append(['D5', 'E5', 'F5', 'G5', 'H5', 'H6', 'H7', 'D8', 'E8', 'F8', 'G8', 'H8'])
answers.append(['B4', 'F4', 'B5', 'E5', 'F5', 'B6', 'D6', 'F6', 'B7', 'C7', 'F7', 'B8', 'F8'])
answers.append(['A1', 'B1', 'C1', 'D1', 'E1', 'A2', 'C2', 'A3', 'C3', 'D3', 'B4', 'E4'])
answers.append(['D5', 'E5', 'F5', 'G5', 'H5', 'D6', 'F6', 'H6', 'D7', 'F7', 'H7'])
answers.append(['F1', 'B2', 'G2', 'B3', 'G3', 'B4', 'C4', 'D4', 'E4', 'F4', 'B5', 'B6'])
answers.append(['D3', 'E3', 'F3', 'G4', 'H5', 'G6', 'D7', 'E7', 'F7'])
answers.append(['E2', 'F2', 'G2', 'D3', 'H3', 'D4', 'H4', 'E5', 'F5', 'G5'])

#FHGuzReJvo


def run_board(proc, boardnum):
    result = []
    solved = False
    indexed = ''
    try:
        indexed = answers[boardnum]
        print('Answer found: {}'.format(indexed))
    except:
        pass

    if indexed:
        start = True
        for entry in answers[boardnum]:
            proc.sendline(entry)
            index = proc.expect(['Nice', "You sunk", pexpect.TIMEOUT], timeout=2)
            print('1 {}'.format(index))
            print(proc.before)
        index = proc.expect(['Nice', "You sunk", pexpect.TIMEOUT], timeout=2)
        print('2 {}'.format(index))
        print(proc.before)
        print(proc.before)
        return
    
    #print('Fuck it we doin it live')
    #proc.interact()
    #quit()

    print('Board {} not indexed. Starting brute force'.format(boardnum))
    time.sleep(1)
    for i in range(1, 9):
        for j in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
#            print('{}{}'.format(j, i))
#            time.sleep(0.5)
            proc.sendline('{}{}'.format(j, i))
            try:
                index = proc.expect(['You misse', 'Nice', 'You sunk', 'xyzzy', pexpect.TIMEOUT], timeout=10)
            except pexpect.exceptions.EOF:
                print(proc.before)
                print('Unexpected pexpect error. Results so far:')
                print(result)
                quit()
#            print(proc.before[0:5], index)
            if index == 0:
                print('{}{} = Miss'.format(j, i))
            elif index == 1:
                print('{}{} = Hit'.format(j, i))
                result += ['{}{}'.format(j, i)]
            elif index == 2:
                print('answers.append({})'.format(result))
                quit()
            elif index == 3:
                print('Should not get here I think. Only for first pass?')
            elif index == 4:
                print('Timeout')

    

def main():
    proc = pexpect.spawn('./pewpewboat')
    
    proc.logfile_read = open('pewpew.txt', 'w')
 
    for boardnum in xrange(50):
        print(proc.before)
        print('Starting board {}'.format(boardnum))
	result = run_board(proc, boardnum)


 
 
if __name__ == '__main__':
    main()
