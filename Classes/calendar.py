from Classes.day import Day

class Calendar:
    def  __init__(self):
        self.week = []
        self.week.append(Day('Monday'  ))
        self.week.append(Day('Tuesday' ))
        self.week.append(Day('Wenesday'))
        self.week.append(Day('Thursday'))
        self.week.append(Day('Friday'  ))
        self.week.append(Day('Saturday'))

    def getWeek(self):
        return self.week

    def showCal(self):
        for day in self.week:
            day.getDay()
            print('################################')

    '''
    FIND DAYS IN WEEK WITH THE MOST SATISFIED AND CONTIGUOUS SHIFTS
    AND ADD TO NEW QUEUE. APPLY FOR EVERY DAYS
    '''
    def sortedWeek(self):
        queue   = [] # CONTAIN DAYS WITH THE MOST SATISFIED AND CONTIGUOUS SHIFTS
        visited = [] # CONTAIN VISITED DAYS
        while(len(queue) < 6):
            max = -1
            res = ''
            for day in self.week:
                if day not in visited and max < len(day.contiguousShift()):
                    max = len(day.contiguousShift())
                    res = day

            if res != '':
                queue.append(res)
                visited.append(res)

        return queue

    def setCal(self, arr):
        visited_values  = []  # CONTAIN THE VISITED VALUES
        for day in self.sortedWeek():
            '''
            SET CLASS INTO SORTED SHIFTS
            IF THERE ARE'NT ANY SATISFIED SHIFTS FROM THIS DAY -> JUMP TO THE NEXT DAY
            '''
            day.setDay(arr, visited_values)
            '''
            STOP CONDITION: WHEN LENGTH OF VISTED_VALUES ARRAY EQUAL TO LENGTH OF ARRAY OF VALUES
            '''
            if len(visited_values) == len(arr):
                break
        
        '''
        IF THERE'RE STILL VALUES WEREN'T ASSIGNED
        '''
        if len(visited_values) != len(arr):
            for day in self.week:
                for ca in day.getShifts():
                    if ca.getShiftStatus():
                        for value in arr:
                            if ca.classesDict[value[1]] and value not in visited_values:
                                ca.setShift(value[0], value[1])
                                visited_values.append(value)
                                break
        
