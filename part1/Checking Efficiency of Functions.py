
import timeit
state =[6, 2, 3, 4, 5, 1, 7, 8, 9, 10, 16, 12, 13, 14, 15, 11]
goal_state = [i for i in range(1,17)]
import copy
def heu1():
    return max([sum([1 for i in range(0,16,5) if goal_state[i] != state[i]]),
                sum([1 for i in range(3,13,3) if goal_state[i] != state[i]])])


def heu2():
    state =[6, 2, 3, 4, 5, 1, 7, 8, 9, 10, 16, 12, 13, 14, 15, 11]
    goalDiagElements = [1,6,11,16]
    
    mapGoalDiagElems = [(0,0),(1,1),(2,2),(3,3)]
    curPositionDiagElems = [state.index(i) for i in goalDiagElements]
    cartIndexForCurDiagElems = [(int(index/4),index%4) for index in curPositionDiagElems]
    movements = sum([abs(cartIndexCur[0]-cartIndexGoal[0])+abs(cartIndexCur[0]-cartIndexGoal[0])  
                    for cartIndexCur,cartIndexGoal in zip(cartIndexForCurDiagElems,mapGoalDiagElems)])
    
    
timeit.timeit(heu1) #4.6172454739029485
timeit.timeit(heu2) #7.57951648469642

def dropMove(boardState,player):
    
    for column in boardState:
        if len(boardState[column]) < heightOfBoard:
            boardStateCopy = copy.deepcopy(boardState) ##think how slow could be this function
        
            boardStateCopy[column].append(player)
            if boardStateCopy != boardState:
                yield boardStateCopy
def test():
    [i for i in dropMove(boardState,'x')]


timeit.timeit(test) #53.64996997864753

boardState2 = [['o', 'x', 'x', 'o', 'x'],['x', 'x', 'o', 'o'],['o', 'x', 'o', 'o']]
len(boardState2)
def dropMove2(boardState,player):
    for column in range(widthOfBoard):
        if len(boardState[column]) < heightOfBoard:
            newBoardState = boardState[0:column]+[boardState[column]+[player]]+boardState[column+1:]
            if newBoardState != boardState:
                yield newBoardState

def test2():
    return [i for i in dropMove2(boardState2,'x')]
timeit.timeit(test2)

test2()



myList = [i for i in range(100)]

def loopFunc():
    global myList
    number =50
    for numbers in myList:
        if numbers == number:
            break
        
        
        
def listFind():
    global myList
    myList.index(50)


timeit.timeit(loopFunc) # 2.476608806973954
timeit.timeit(listFind)






[i for i in range(10,0,-1)]




'oooo.xoxx.xxox.ooxo.xxxooxoxoxoxoooxoxoo'









