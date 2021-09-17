import matplotlib.pyplot as plot
palabras=[]
frecuencias=[]
with open("GEH.txt") as f_obj:
    cuento=f_obj.read()
    cuento=cuento.lower()
    palabras= cuento.split()
    diccionario_frecuencias={}
    for palabra in palabras:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra]+=1
        else:
            diccionario_frecuencias[palabra]=1
    for palabra in diccionario_frecuencias:
        frecuencia=diccionario_frecuencias[palabra]
        palabras.append({palabra})
        frecuencias.append({frecuencia})
       
print(palabras)
print(frecuencias)
        