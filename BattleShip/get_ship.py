from typing import Iterator, List


class Get_Ship:
    def __init__(self,lists:dict) -> None:
        self.lists = lists

    def grabbing_shipinfo(self)->None:
        shipname=[]
        shiplength=[]
        for key in self:
            print(key)
            shipname.append(key)
            for value in self[key]:
                print(value)
                shiplength.append(value)

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)
###################################################################
# a = {'Mouse': '1', 'Cat': '3', 'Dog': '5'}
# Get_Ship(a)
# a.grabbing_shipinfo()
# shipname=[]
# shiplength=[]
# for key in a:
#     #print(key)
#     shipname.append(key)
#     for value in a[key]:
#         #print(value)
#         shiplength.append(value)
# print(shipname)
# print(shiplength)
