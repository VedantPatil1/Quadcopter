import inspect
from config import ComponentConfig
#from Database.SQLiteManager import GetSpecification


def GetSpecificationValues():
    return {"codeName": "TEXT", "weight": "INTEGER"}


def DisplaySpecs(Component):
    print(Component.name, " Specifications \u2193 \n")
    for i in inspect.getmembers(Component):
        if not i[0].startswith('_'):
            if not inspect.ismethod(i[1]):
                print("=>", i)


# Flight Module Components
class Propeller():
    def __init__(self, codeName):
        self.name = "Motor"
        # Gets values from config.py and passes as class atributes
        self.specList = ComponentConfig[self.name]
        for spec in self.specList:
            setattr(self, spec, self.specList[spec])
            print(spec)
        self.codeName = codeName

    def importValues(self):
        values = GetSpecificationValues(self.name)
        for spec in self.specList:
            spec = values[spec]
            print(spec)

    def DisplaySpecs(self):
        self.importValues()
        DisplaySpecs(self)


class Motor:
    def __init__(self, codeName):
        self.name = "Motor"
        # Gets values from config.py and passes as class atributes
        self.specList = ComponentConfig[self.name]
        for spec in self.specList:
            setattr(self, spec, self.specList[spec])
            print(spec)
        self.codeName = codeName

    def importValues(self):
        values = GetSpecificationValues(self.name)
        for spec in self.specList:
            spec = values[spec]
            print(spec)

    def DisplaySpecs(self):
        self.importValues()
        DisplaySpecs(self)


class Esc():
    def __init__(self, codeName):
        self.name = "Esc"
        # Gets values from config.py and passes as class atributes
        self.specList = ComponentConfig[self.name]
        for spec in self.specList:
            setattr(self, spec, self.specList[spec])
            print(spec)
        self.codeName = codeName

    def importValues(self):
        values = GetSpecificationValues(self.name)
        for spec in self.specList:
            spec = values[spec]
            print(spec)

    def DisplaySpecs(self):
        self.importValues()
        DisplaySpecs(self)


class Battery():
    def __init__(self, codeName):
        self.name = "Battery"
        # Gets values from config.py and passes as class atributes
        self.specList = ComponentConfig[self.name]
        for spec in self.specList:
            setattr(self, spec, self.specList[spec])
            print(spec)
        self.codeName = codeName

    def importValues(self):
        values = GetSpecificationValues(self.name)
        for spec in self.specList:
            spec = values[spec]
            print(spec)

    def DisplaySpecs(self):
        self.importValues()
        DisplaySpecs(self)
    ter

    def __init__(self, codeName):
        self.name = "Flight Controller"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.breadth = ""
        self.length = ""
        self.heigth = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)


class PDM():
    def __init__(self, codeName):
        self.name = "PDM"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.pitch = ""
        self.diameter = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)


class Frame():
    def __init__(self, codeName):
        self.name = "Propeller"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.pitch = ""
        self.diameter = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)


# Communication Module components
class Reciever():
    def __init__(self, codeName):
        self.name = "Propeller"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.pitch = ""
        self.diameter = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)


class Transmitter():
    def __init__(self, codeName):
        self.name = "Propeller"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.pitch = ""
        self.diameter = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)


# On-board Sensors
class GPS():
    def __init__(self, codeName):
        self.name = "Propeller"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.pitch = ""
        self.diameter = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)


class Camera():
    def __init__(self, codeName):
        self.name = "Propeller"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.pitch = ""
        self.diameter = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)


class Lidar():
    def __init__(self, codeName):
        self.name = "Propeller"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.pitch = ""
        self.diameter = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)


# Accessories
class Sprinkler():
    def __init__(self, codeName):
        self.name = "Propeller"
        self.codeName = codeName
        Specifications = GetSpecification(self.name, codeName)
        self.weight = ""
        self.cost = ""
        self.pitch = ""
        self.diameter = ""

    def DisplaySpecs(self):
        DisplaySpecs(self)
