from scripts.Rectangle import Rectangle
from scripts.square import Square
from scripts.triangle import Triangle

r=1

Shape=input("Enter the Shape")
if(Shape=="SQUARE"):
      Square.Sqre(r)
elif(Shape=="TRIANGLE"):
     Triangle.Tri(r)
elif(Shape=="RECTANGLE"):
     Rectangle.rectangle(r)
else:
   print("ERROR")
