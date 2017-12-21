class NormalItem(Item, Interfaz):
   
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)


    def update_quality(self):
    	Interfaz.update_quality(self)