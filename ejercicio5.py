#==============================================================================
#SISTEMAS DE VENTAS DE UN PRODUCTO
#==============================================================================

#Declaracion de constantes
IVA = 0.16
descuento = 0.10

#==============================================================================
#Eentrada de datos
#==============================================================================

nombre_cliente = input("ingresa el nombre del cliente: ")
nombre_producto = input("ingresa el numero del producto: ")

precio_unitario = float(input("ingresa el precio unitario del producto"))
cantidad_productos = int(input("ingresa la cantidad de productos comprados: "))

#==============================================================================
#CALCULOS
#==============================================================================

subtotal = precio_unitario * cantidad_productos
monto_decuento = subtotal * descuento
subtotal_con_descuento = subtotal - monto_decuento
monto_iva = subtotal_con_descuento * IVA
total_pagar = subtotal_con_descuento + monto_iva

#===============================================================================
#MOSTRAR TIPOS DE DATOS
#===============================================================================

tipo_cliente = type(nombre_cliente)
tipo_precio = type(precio_unitario)
tipo_cantidad = type(cantidad_productos)

#===============================================================================
#TICKET DE COMPRA
#===============================================================================

print("========================================================================")
print("                           TICKET DE COMPRA                             ")
print("========================================================================")

print("datos del cliente")
print("cliente:", nombre_cliente)

print("datos del producto")
print("priducto:", nombre_producto)
print("precio unitario: $", precio_unitario)
print("cantidad:", cantidad_productos)

print("tipos de dato")
print("nombre_cliente:", tipo_cliente)
print("precio_unitario:",tipo_precio)
print("cantidad_productos", tipo_cantidad)

print("resumen de compra")
print("subtotal: $", subtotal)
print("descuento (10%): $", monto_decuento)
print("IVA (16%): $", monto_iva)
print("total a pagar: $", total_pagar)