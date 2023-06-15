import os

Ojos1 = {
	'nombre':'Ojos1',
	'precio': {
		'monto': 2000,
	},
	'stock': {
		'cantidad': 100,
	},
	'marca': 'Loreal',
	'color': 'Marron',
	'acabado': 'Mate',
	'codigo': "451"
}

Ojos2 = {
	'nombre': 'Ojos2',
	'precio': {
		'monto': 3000,
	},
	'stock': {
		'cantidad': 150,
	},
	'marca':'Maybelline',
	'color':'Dorado',
	'acabado': 'Satinado',
	'codigo':"352",
}

Ojos3 = {
	'nombre': 'Ojos3',
	'precio': {
		'monto': 4000,
	},
	'stock': {
		'cantidad': 140,
	},
	'marca':'Revlon',
	'color':'Negro',
	'acabado': 'Metalico',
	'codigo': "567",

}



Labios1 = {
	'nombre': 'Labios1',
	'precio': {
		'monto': 2500,
	},
	'stock': {
		'cantidad': 140,
	},
	'marca':'Loreal',
	'color':'Rojo',
	'acabado': 'Mate',
	'codigo': "890",

}

Labios2 = {
	'nombre': 'Labios2',
	'precio': {
		'monto': 3450,
	},
	'stock': {
		'cantidad': 950,
	},
	'marca':'Maybelline',
	'color':'Nude',
	'acabado': 'Gloss',
	'codigo': "223",
}

Labios3 = {
	'nombre': 'Labios3',
	'precio': {
		'monto': 4200,
	},
	'stock': {
		'cantidad': 120,
	},
	'marca':'Revlon',
	'color':'Rosa',
	'acabado': 'Brillante',
	'codigo': "123"
}


Rostro1 = {
	'nombre': 'Rostro1',
	'precio': {
		'monto': 3000,
	},
	'stock': {
		'cantidad': 240,
	},
	'marca':'Revlon',
	'color':'Caramelo',
	'acabado': 'Mate',
	'codigo': "765",
}

Rostro2 = {
	'nombre': 'Rostro2',
	'precio': {
		'monto': 2900,
	},
	'stock': {
		'cantidad': 200,
	},
	'marca':'Loreal',
	'color':'Bronce',
	'acabado': 'Luminoso',
	'codigo': "891",

}

Rostro3 = {
	'nombre': 'Rostro3',
	'precio': {
		'monto': 3400,
	},
	'stock': {
		'cantidad': 80,
	},
	'marca':'Maybelline',
	'color':'Miel',
	'acabado': 'Mate',
	'codigo': "342"
}




maquillajes = [Ojos1, Ojos2, Ojos3, Labios1, Labios2, Labios3, Rostro1, Rostro2, Rostro3]
os.system('clear')

while True:


	print("\nIngresar el codigo del producto")
	icodigo = input(">> ")

	print("\ncargando...")
	active_maquillaje = {}
	maquillaje_index = 0

	for maquillaje in maquillajes:
		if maquillaje['codigo'] == icodigo:
			active_maquillaje = maquillaje.copy()
			maquillaje_index = maquillajes.index(maquillaje)

	if len(active_maquillaje) != 0:

		while True:
			print("\nOperaciones disponibles")
			print("1) Aumentar Stock")
			print("2) Aumentar Precio")
			print("3) Consultar Stock")
			print("4) Consultar Precio")
			print("5) Consultar Marca")
			print("6) Consultar Color")
			print("7) Consultar Acabado")
			print("8) Consultar Nombre del producto")
			print("9) Salir")

			option = input(">> ")

			try:
				if int(option) < 1 or int(option) > 9:
					print("Debe seleccionar una opcion valida")
					continue

				if option == "1":
					print("Aumentar Stock en:")
					aumento = input("\t>> ")

					active_maquillaje['stock']['cantidad'] += float(aumento)
					print("\nStock actualizado")

				if option == "2":
					print("Aumentar Precio en:")
					aumento = input("\t>> $ ")

					active_maquillaje['precio']['monto'] += float(aumento)
					print("\n++ Precio actualizado ++")

				if option == "3":
					print("\nConsultar Stock")
					print(f"El Stock es de: {active_maquillaje['stock']['cantidad']}")

				if option == "4":
					print("\nConsultar Precio")
					print(f"El precio es: $ {active_maquillaje['precio']['monto']}")

				if option == "5":
					print("Consultar Marca")
					brand = active_maquillaje['marca']
					print(f"La marca del producto es: {brand}")


				if option == "6":
					print("Consultar color")
					colour = active_maquillaje['color']
					print(f"El color del producto es: {colour}")

				if option == "7":
					print("Consultar acabado")
					finish = active_maquillaje['acabado']
					print(f"\tEl acabado del producto es: {finish}")

				if option == "8":
					print("Consultar nombre")
					name = active_maquillaje['nombre']
					print(f"\tEl nombre del producto es: {name}")


				if option == "9":
					os.system('clear')
					break

				print("---------------------")
			
			except ValueError:
				print("Debe ingresar numeros, no letras")
	else:
		print("\nNo se puede acceder - Codigo invalido")

