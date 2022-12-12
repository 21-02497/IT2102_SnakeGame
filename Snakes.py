from Utilities import Util

class Snakes:
  
  def __init__(self):
    self.body_size = Util.BODY_PARTS
    self.coordinates = []
    self.squares = []
    
    for i in range(0, Util.BODY_PARTS):
      self.coordinates.append([0, 0])
      
    for x, y in self.coordinates:
      square = Util.canvas.create_rectangle(x, y, x + Util.SPACE_SIZE, y + Util.SPACE_SIZE, fill=Util.SNAKE_COLOR, tag="snake")
      self.squares.append(square)
