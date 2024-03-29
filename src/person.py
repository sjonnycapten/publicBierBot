class Person:
    def __init__(self,id,name,offset):
        self.name = name
        self.id = id
        self.beerCount = 0
        self.test = 0
        self.offset = offset
    

    def GetPersonalRecords(self,records):
        persRecords =[]
        for record in records:
            if(not (type(record) is str)):
                #print(type(record))
                if (record['UID'] == self.id):
                    persRecords.append(record)
        return persRecords
    
    def GetBeerCount(self,r):
        records = self.GetPersonalRecords(r)
        count = 0
        for x in records:
            if(int(x['amount']) > -23):
                count += int(x['amount'])
        self.beerCount = count+self.offset
        return count + self.offset
    