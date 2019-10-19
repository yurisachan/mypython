class Computer():
    
    shape="rectangle"
    
    def __init__(it,name,color,price):
        it.name=name
        it.color=color
        it.price=price
        
    @classmethod
    def game(it):
        return "game over"

    def display(it):
        print(it.price)

tokoy=Computer("Tokoy","black",8000)
tokoy.display()
print(tokoy.game())
print(tokoy.color)
print(Computer.shape)
print(tokoy.shape)
print(Computer.game())
