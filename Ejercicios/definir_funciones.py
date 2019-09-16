def num_mayor(x, y, z):
   if x > y and x > z:
       salida = x
   elif y > x and y > z:
       salida = y
   else:
       salida = z
   return salida

print(num_mayor(180,60,992))