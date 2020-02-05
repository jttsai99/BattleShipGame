from .get_ship import Get_Ship
class Ship(object):
    def __init__(self,name,length,orientation,coordinates):
        self.name = name
        self.length = length
        self.orientation = orientation
        pass
    def __str__(self) -> str:
        return(self.name,self.length)

    def ship_coordinates(self,orientation):
        #indship =[]
       # if orientation == "horizontal":
         #   for
        pass