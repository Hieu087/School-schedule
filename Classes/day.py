from Classes.shift import Shift
import random

def opposite(a):
    if a == True:
        return False
    return True

def setPoint(arr, value):
    # POINT SYSTEM OF EACH VALUES
    point = [10 for _ in range(len(arr))]

    for i in range(0, len(arr)):
        if list(arr[i][1])[0] == list(value[1])[0]:
            point[i] -= 3
            if list(arr[i][1])[1] == list(value[1])[1]:
                point[i] -= 3
                if list(arr[i][1])[2] == list(value[1])[2] and list(arr[i][1])[3] == list(value[1])[3]:
                    point[i] -= 4
            elif int(list(arr[i][1])[1]) in range(int(list(value[1])[1])-1, int(list(value[1])[1])+2):
                point[i] -= 2
        elif list(arr[i][1])[0] in 'ADE':
            point[i] -= 2
    
    return point

def checkDistance(room,value):
    availableRoom = {k : v for k,v in room.items() if v is True} 
    for i in range(len(availableRoom)):
        point = 10
        if list(list(list(availableRoom.items())[i])[0])[0] == list(value)[0]:
            point -= 3
            if list(list(list(availableRoom.items())[i])[0])[1] == list(value)[1]:
                point -= 3
                if list(list(list(availableRoom.items())[i])[0])[2] == list(value)[2] and list(list(list(availableRoom.items())[i])[0])[3] == list(value)[3]:
                    point -= 4
            elif int(list(list(list(availableRoom.items())[i])[0])[1]) == int(list(value)[1])+1 or int(list(list(list(availableRoom.items())[i])[0])[1]) == int(list(value)[1])-1:
                point -= 2 
        availableRoom[list(list(availableRoom.items())[i])[0]]=point    

    return availableRoom

class Day:
    def  __init__(self, day):
        self.day = day
        self.shifts = []
        self.shifts.append(Shift(1))
        self.shifts.append(Shift(2))
        self.shifts.append(Shift(3))
        self.shifts.append(Shift(4))

    def getShifts(self):
        return self.shifts

    def getDay(self):
        print(self.day.upper())
        print('Tong so ca lien ke:', len(self.contiguousShift()))
        print('------')
        for ca in self.shifts:
            print('Shift:', ca.getOrdinal())
            print('Subject:', ca.getSub())
            print('Class:', ca.getRequiredClass())
            print(ca.getShiftStatus())
            print('----------')

    '''
    FIND THE CONTIGUOUS SHIFTS
    '''
    def contiguousShift(self):
        queue1 = []  # CONTAIN THE FIRST CONTIGUOUS SHIFTS
        queue2 = []  # CONTAIN THE NEXT CONTIGUOUS SHIFTS
        broken = ''  # USE TO IDENTIFY THE SPECIAL CASE
        continues = True
        for ca in self.shifts:
            if ca.getShiftStatus():
                broken += 't'
                if continues == True:
                    queue1.append(ca)
                if continues == False:
                    queue2.append(ca)
            else:
                broken += 'f'
                # IDENTIFY THE SPECIAL CASE
                if broken == 'tff':
                    break
                continues = opposite(continues)
            
        if len(queue1) >= len(queue2):
            return queue1
        return queue2

    def beamSearch(self, arr, visited_values, currentState, k):
        # POP OUT THE FIRST VALUE OF QUEUE
        queue = []

        point    = setPoint(arr, currentState)  # INSERT POINT SYSTEM
        pointTmp = setPoint(arr, currentState)  # TEMPORARY POINT SYSTEM

        for _ in range(len(arr)):
            # FIND THE INDEX OF MINIMUM ELEMENTS IN POINT ARRAY
            indexOfMin = [i for i, e in enumerate(point) if e == min(pointTmp)]
            for i in indexOfMin:
                if arr[i] not in visited_values and arr[i] not in queue:
                    queue.append(arr[i])

            pointTmp.remove(min(pointTmp))

            if len(queue) == k:
                break   

        return queue

    def beamSearch2(self,dict,k):
        temp = min(dict.values())
        res  = [key for key in dict if dict[key] == temp] 
        ordered = sorted(res)
        seq  = ordered[:k]
        return random.choice(seq)

    '''
    SET DAY INTO SHIFTS HAVE FOUND
    '''
    def setDay(self, arr, visited_values):
        ca        = self.contiguousShift()
        firstTime = True # CHECK IF IT IS THE FIRST TIME IN THE LOOP

        for i in range(len(ca)):
            # FIND THE FIRST VALUE THAT SATISFY THE REQUEST
            if firstTime:
                for value in arr:
                    if value not in visited_values and ca[i].classesDict[value[1]]:
                        firstTime = False
                        ca[i].setShift(value[0], value[1])
                        visited_values.append(value)
                        currentState = value   # INITIAL STATE
                        break                 

            # USING THE IDEA OF BEAM SEARCH TO FIND THE NEAREST CLASSROOM FROM THE LAST CLASSROOM
            else:
                queue = self.beamSearch(arr, visited_values, currentState, 2)
                for value in queue:
                    # IF THE REQUIRED CLASS IS AVAILABLE
                    if ca[i].classesDict[value[1]]:
                        ca[i].setShift(value[0], value[1])
                        visited_values.append(value)
                        currentState = value
                        break

                    # IF THE REQUIRED CLASS ISN'T AVAILABLE -> FIND THE NEAREST CLASS INSTEAD 
                    elif len(self.beamSearch2(checkDistance(ca[i].classesDict, value[1]),2)) > 0:
                        ca[i].setShift(value[0], self.beamSearch2(checkDistance(ca[i].classesDict, value[1]),2))
                        visited_values.append(value)
                        currentState = value
                        break
                    
            if len(visited_values) == len(arr):
                break

