import matplotlib.pyplot as plot


palabrasL=[] #Creamos dos listas vacías para agregar los elementos de repeticiones y palabras
frecuencias=[]
with open("GEH.txt") as f_obj: #Abrir el txt donde esta el cuento
    cuento=f_obj.read() #Es necesario leerlo
    cuento=cuento.lower() #Eliniminamos todas las letras mayúsculas
    palabras= cuento.split() #Separamos los valores
    diccionario_frecuencias={} #Creamos un diccionario de frecuencias vacío
    for palabra in palabras: #Este for va analizando todas las palabras
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra]+=1 #Con este if podemos agregar 1 cad vez que encuentre una palabra repetida
        else:
            diccionario_frecuencias[palabra]=1 #Si encuentra una palabra nueva se le asigna un valor de 1
    #print("cdt: ",diccionario_frecuencias)
    for palabra in diccionario_frecuencias: #Con este for agregamos las palabras y las frecuencias a las listas vacías
        frecuencia=diccionario_frecuencias[palabra]
        palabrasL.append(palabra)
        frecuencias.append(frecuencia)
    
plot.plot(palabrasL,frecuencias) #Cuando tenemos nuestras listas graficamos.
plot.show()


#print (palabrasL)
#print (frecuencias)


       

        