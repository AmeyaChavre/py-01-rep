class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
        
    
    def distance(self):
        return ( ((abs(coordinate1[0]-coordinate2[0]))**2) + ((abs(coordinate1[1]-coordinate2[1])**2)) )**0.5
    
    def slope(self):
        return (coordinate2[1]-coordinate1[1]) / (coordinate2[0]-coordinate1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(f'Distance between {coordinate1} and {coordinate2} : {li.distance()}')
print(f'Slope of line : {li.slope()}')