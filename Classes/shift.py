import random

class Shift:
    def __init__(self, ordinal):
        self.ordinal       = ordinal
        self.subject       = ''
        self.requiredClass = ''
        self.shiftStatus   = random.choice([True, False])
        self.classesDict   = {}

        self.insertClass('A')
        self.insertClass('B')
        self.insertClass('C')
        self.insertClass('D')
        self.insertClass('E')

    def insertClass(self, block):
        if block == 'A':
            end = 800
        else:
            end = 700
        for i in range(200, end, 100):
            for j in range(1,13):
                key = block + str(i+j)
                self.classesDict[key] = random.choice([True, False])
        
    '''
    GET
    '''
    def getOrdinal(self):
        return self.ordinal

    def getSub(self):
        return self.subject

    def getRequiredClass(self):
        return self.requiredClass

    def getShiftStatus(self):
        return self.shiftStatus

    '''
    SET
    '''   
    def setShift(self, sub, cla):
        self.subject = sub
        self.requiredClass  = cla
