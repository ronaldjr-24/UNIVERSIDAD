# se realiza la lectura del archivo utilizanto con metodo "r"
notas=open("my_notes.txt","r")
linea1=notas.readline()
linea2=notas.readline()
linea3=notas.readline()
print(linea1)
print(linea2)
print(linea3)
notas.close()
# para cerrar el archivo se utiliza.close()