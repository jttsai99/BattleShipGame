class Ship(object):
    def __init__(self,name:str,marker:str,length,orientaion,coordinates):
        self.name = name
        self.marker = marker
        self.length = length
        self.orientation = orientaion
        self.coordinates = coordinates
        self.ship_coordinates = self.ship_coordinates(length,orientaion,coordinates)
        pass
    def __str__(self) -> str:
        return "The name is {},the marker is {}, the length is {}, the orientation is {}, and the coordinates are {}".format(self.name,self.marker,self.length,self.orientation,self.coordinates)


#takes in the object's length orientation and coordinates to create a list of all coordinates for ONE ship
    def ship_coordinates(self,length, orientation, coordinates)->list:
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


#a = Ship("M",2,"horizonal",(5,2))
#print(a)

#this needs to return some type of list of coordinates for one individual boat
#we will write the rest in board i think