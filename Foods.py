import random 

from Utilities import Util

class Food:
  
  def __init__(self):
    
    x = random.randiant(0, (Util.GAME_WIDTH 
        / Util.SPACE_SIZE) - 1) * Util.SPACE_SIZE
    y = random.randiant(0, (Util.GAME_HEIGHT
        / Util.SPACE_SIZE) - 1) * Util.SPACE_SIZE
    
    self.coordinates = [x, y ]
    
    Util.canvas.create_oval(x, y, x + Util.SPACE_SIZE, y + Util
        .SPACE_SIZE, fill=Util.FOOD_COLOR, tag="food")
