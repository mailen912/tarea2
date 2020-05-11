import hangman
import reversegam
import tictactoeModificado
import json
import PySimpleGUI as sg

	
def main(args):
	
	sigo_jugando = True
	while sigo_jugando:
		
		print('''
		Elegí con qué juego querés jugar:
		1.- Ahorcado
		2.- Ta-TE-TI
		3.- Otello
		4.- Salir''')

		opcion = input()
		if opcion == '1':
			hangman.main()
			juego='Ahorcado'
		elif opcion == '2':
			tictactoeModificado.main()
			juego='Ta-TE-TI'
		elif opcion == '3':
			reversegam.main()
			juego='Otello'
		elif opcion == '4':
			sigo_jugando = False
		return juego

def guardar_datos(juego):
	layout=[[sg.Text('Ingrese su nombre:'),sg.Input(key='nom')],
	        [sg.Text('Ingrese su apellido:'),sg.Input(key='ape')],
	        [sg.Text('Sin guardar            ',key='k')],
	        [sg.Button('Finalizar'),sg.Button('Salir')]]
	window=sg.Window('Guardar',layout)
	while True:
		event,values=window.Read()
		if event in (None or 'Salir'):
			break
		elif event in ('Finalizar'):
			datos={'nombre':values['nom'],'apellido':values['ape'],'juego':juego}
			archivo=open('Datos_juego.txt','w')
			json.dump(datos,archivo,indent=4)
			archivo.close()
			texto=window.FindElement('k')
			texto.Update('Datos Guardados')
	
		
if __name__ == '__main__':
    import sys
    juego=main(sys.argv)
    guardar_datos(juego)
    

