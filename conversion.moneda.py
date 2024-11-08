##1.Buscar el valor actual del euro y dolar con respecto al peso mex

tipo_cambio_euro_mex=21.39
tipo_cambio_usd_mex=18.30


# #2.Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar a Mex)
opcion1= 'EUR'
opcion2= 'USD'
preguntar=input("Cual es la moneda de su origen que desea convertir, EUR o USD: ")
if preguntar.upper() == opcion1:
    print('usted desea convertir EUR/MEX')
elif preguntar.upper() == opcion2:
    print("usted desea convertir USD/MEX")
else:
    print("Esta opcion no esta disponible")
    


#3.Solicitar al usario el monto a convertir
monto_convertir=float(input('cuanto desea convertir: '))

if preguntar.upper() == opcion1:
    print(f'{monto_convertir*tipo_cambio_euro_mex} Pesos mexicanos')
elif preguntar.upper() == opcion2:
    print(f'{monto_convertir*tipo_cambio_usd_mex} pesos mexicanos')
else:
    print("Esta opcion no esta disponible")
#4.Realizar la conversionusu