class TotalInfoVO:

    def __init__(self, infoID, year, month, day, containerID, quantity):
        self.infoID = infoID
        self.year = year
        self.month = month
        self.day = day
        self.containerID = containerID
        self.quantity = quantity

    def getInfoID(self):
        return self.infoID

    def setInfoID(self, infoID):
        self.infoID = infoID


    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year


    def getMonth(self):
        return self.month

    def setMonth(self, month):
        self.month = month

    def getDay(self):
        return self.day

    def setDay(self, day):
        self.day = day

    def getContainerID(self):
        return self.containerID

    def setContainerID(self, containerID):
        self.containerID = containerID

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

