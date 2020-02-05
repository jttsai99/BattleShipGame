from .player import Player
class Ship(object):
    def __init__(self,name:str,length):
        self.name = name
        self.length = length
        self.orientation = orientation
        self.coordinates = coordinates
        self.indshipcoordinates = self.ship_coordinate(length,orientation,coordinates)
        pass
    def __str__(self) -> str:
        return(self.name)

    def ship_coordinates(self,length, orientation, coordinates):
        counter = 1
        if orientation == "horizontal":
            self.name_coords = [self.coordinates]
            for i in range(self.length):
                self.name_coords.append((self.coordinates[0], self.coordinates[1] + counter))
                counter += 1
            return self.name_coords

        elif orientation == "vertical":
            self.name_coords = [self.coordinates]
            for i in range(self.length):
                self.name_coords.append((self.coordinates[0] + counter, self.coordinates[1]))
                counter += 1
            return self.name_coords


# a = Ship("mouse",2,"horizonal",5,2)
# a.ship_coordinates("horizontal",5,2)
# print(a)