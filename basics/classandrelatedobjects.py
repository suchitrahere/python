class Automobile:
    """This class helps to get Automobile data by showing logo name, wheel count and brand name"""
    def __init__(self, wheels, brand):
        self.wheelCount = wheels
        self.brandName = brand

    def addLogo(self, logoname):
        """Add or update logoname for an automobile"""
        self.logoName = logoname

    def getAutomobile(self):
        return {
            "logoName": self.logoName,
            "wheels":   self.wheelCount,
            "brand":   self.brandName
        }


audi =Automobile(4,'audix')
audi.addLogo('auddii')
print(audi.getAutomobile())

help(Automobile)