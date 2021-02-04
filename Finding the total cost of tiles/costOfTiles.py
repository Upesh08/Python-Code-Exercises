# Finding Cost of Tile to Cover W x H Floor
# In this program, we will be calculating the total cost of tiles that would take to cover a floor plan of width and height, using the details of tiles and floor entered by the user. 
# Developer: Upesh Maharana 
# Dated: 2021/02/03

def calculateCostOfTiles(aof,aot,cot):
    """
    This method calculates the total cost of tiles by dividing the area of floor with the area of tile to get the total number of tiles and then finding the total cost of required tiles.
    Parameter(s):
    aof - Area of the floor.
    aot - Area of the tile.
    cot - Cost of a tile.
    """
    total_Tiles = aof/aot
    total_Cost = total_Tiles * cot
    return total_Cost


def findArea(w,h):
    """
    This function calculates the area by multiplying width and height. 
    Parameter(s): 
    w - Width of a structure
    h - Height of a structure
    """
    area = w * h
    return area

def Main():
    """
    This function is the main function of the program. It takes input from the user and calls multiple functions to fetch the cost.
    """
    try: 
        floorWidth = int(input("Enter the width of the Floor"))
        floorHeight = int(input("Enter the height of the Floor"))
        tileWidth = int(input("Enter the width of the Tile"))
        tileHeight = int(input("Enter the height of the Tile"))
        tileCost = int(input("Enter the cost of the Tile"))
       
        if floorWidth>0 and floorHeight> 0 and tileWidth>0 and tileHeight > 0 and tileCost > 0: 
            floorArea = findArea(floorWidth,floorHeight)
            tileArea = findArea(tileWidth,tileHeight)
            TCost = calculateCostOfTiles(floorArea,tileArea,tileCost)
            print("Total Cost of the tiles require to fill the floor is:",TCost)
        else:
            print("Invalid Details. Please enter valid data next time.")
    except:
        print("Wrong input given. Please enter a positive number next time.")
    
    
if __name__ == "__main__":
    Main()
