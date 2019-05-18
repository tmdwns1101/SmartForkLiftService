class CashContainerVO:
    def __init__(self,containerID, containerName, quantity):
        self.containerID = containerID
        self.containerName = containerName
        self.quantity = quantity


    def getContainerID(self):
        return self.containerID

    def setContainerID(self, containerID):
        self.containerID = containerID


    def getContainerName(self):
        return self.containerName

    def setContainerName(self, containerName):
        self.containerName = containerName


    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity