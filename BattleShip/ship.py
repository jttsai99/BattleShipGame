class Ship(object):
    def __init__(self,name:str,marker:str,length:int,orientation:str,coordinates:tuple):
        self.name = name
        self.marker = marker
        self.length = length
        self.orientation = orientation
        self.coordinates = coordinates
        self.ship_coordinates = self.set_ship_coordinates(self.length,self.orientation,self.coordinates)
        pass

    def __str__(self) -> str:
        return "The name is {},the marker is {}, the length is {}, the orientation is {}, and the coordinates are {}".format(self.name,self.marker,self.length,self.orientation,self.coordinates)


#takes in the object's length orientation and coordinates to create a list of all coordinates for ONE ship
    def set_ship_coordinates(self,length, orientation, coordinates)->list:
        counter = 0
        if orientation == "horizontal":
            self.list_coords = [self.coordinates]
            for i in range(self.length):
                self.list_coords.append((self.coordinates[0], self.coordinates[1] + counter))
                counter += 1
            print(self.list_coords)
            return self.list_coords

        elif orientation == "vertical":
            self.list_coords = [self.coordinates]
            for i in range(self.length):
                self.list_coords.append((self.coordinates[0] + counter, self.coordinates[1]))
                counter += 1
            print(self.list_coords)
            return self.list_coords


#gets the current ship's name
    def get_ship_name(self)->str:
        return self.name

# gets the current ship's marker
    def get_ship_marker(self)->str:
        return self.marker

# gets the current ship's length
    def get_ship_length(self)->int:
        return self.length

#gets the current ship's orientation
    def get_ship_orientaion(self)->str:
        return self.orientation

#gets the current ship's coordinates
    def get_ship_starting_coordinates(self)->tuple:
        return self.coordinates


# a = Ship("Mouse","M",2,"horizontal",(5,2))
# print(a)
# length = a.get_ship_length()
# orientation = a.get_ship_orientaion()
# coordinates = a.get_ship_starting_coordinates()

#this needs to return some type of list of coordinates for one individual boat
#we will write the rest in board i think