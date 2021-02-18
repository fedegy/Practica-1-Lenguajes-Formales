import os
from tkinter import *
from tkinter import filedialog

global archivo
archivo= []

cadena2 = []
archivo = []
global cadena_inicial
cadena_inicial = []

global lista_numeros
lista_numeros = []

global intlist
intlist= []


global numeros1
numeros1=[]

global lista_buscar2 
lista_buscar2 = []
lista_buscar_numero = []

global ordenar
ordenar=[]

global lista_ordenar
lista_ordenar=[]

global ordenar_final
ordenar_final=[]

global numeros_html_2
numeros_html_2=[]

global lista2
lista2=[]


global lista_ruta
lista_ruta=[]

global lista_buscar3
lista_buscar3=[]


global lista_numeros_anidados
lista_numeros_anidados=[]


global lista_numeros_anidados_buscar
lista_numeros_anidados_buscar=[]

global intlist4
intlist4=[]

global lista_numeros2_buscar
lista_numeros2_buscar=[]

def buscar_(lista,key):
    lista2=[]
    flag=False
    for i in range(len(lista)):
        if lista[i]==key:
            flag=True
            lista2.append(i)
    if flag==True:
        print("")
    else:
        return "No se encontro el número"
    return lista2
 

def ordenamiento_burbuja(lista):
    n=len(lista)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista



def inicio():
    while True:
        print("\n")
        print("\t1) Cargar Archivo de Entrada")
        print("\t2) Desplegar listas ordenadas")
        print("\t3) Desplegar búsquedas")
        print("\t4) Desplegar todas")
        print("\t5) Desplegar todas a archivos")
        print("\t6. Salir")
        ruta=""

        global file_path
        op = int(input("\tEliga una opción\n"))

        if op == 1:
            root=Tk()
            root.fileName=filedialog.askopenfilename()
            lista_ruta.append(root.fileName)
            archivo = open(lista_ruta[0], 'r')
            print("\t Cargando...")
            print("\t Se cargo con éxito")
  
        if op == 2:
            print("\n")
            archivo = open(lista_ruta[0], 'r')
            for i in archivo:
                try:
                    cadena2 = i.split("=")
                    numeros = cadena2[1].split(" ")
                    numeros2 = re.split(r' ', numeros[1])
                    ordenar = re.split(r',BUSCAR', numeros[1])
                    buscar = re.split(r'ORDENAR,', numeros[1])
                    if ordenar == re.split(r',BUSCAR', numeros[1]) and buscar == re.split(r'ORDENAR,', numeros[1]):
                        ordenar = re.split(r',BUSCAR', numeros[1])
                        buscar = re.split(r'ORDENAR,', numeros[1])
                    #buscar_numero = re.split(r', ', numeros[2])

                    cadena_inicial = cadena2[0].split(",")
                    lista_numeros = numeros[0].split(",")
                    lista_numeros_ordenado=numeros[0].split(",")
                    lista_ordenar = ordenar[0].split(",")
                    # lista_buscar=buscar[1].split(",")
                    #lista_buscar_numero = buscar_numero[0].split(",")

                    buscar = re.split(r' ', numeros[1])

                    if buscar == re.split(r' ', numeros[1]):
                        buscar = re.split(r' ', numeros[1])
                        lista_buscar2 = re.split(r'ORDENAR,', numeros[1])

                    """
                    """
                    if "ORDENAR" in ordenar:
                        print(cadena_inicial[0], ":", lista_numeros, " | ", "Resultado de ordenar", ":",ordenamiento_burbuja(lista_numeros_ordenado),
                              " ,", ordenar[0])

                    if "ORDENAR\n" in ordenar:
                        print(cadena_inicial[0], ":", lista_numeros, " | ", "Resultado de ordenar", ":",ordenamiento_burbuja(lista_numeros_ordenado),
                              " ,", ordenar[0])

                except:
                    print("")


        if op == 3:
            print("\n")
            archivo = open(lista_ruta[0], 'r')
            for i in archivo:
                try:
                    cadena2 = i.split("=")
                    numeros = cadena2[1].split(" ")
                    numeros2 = re.split(r' ', numeros[1])
                    ordenar = re.split(r',BUSCAR', numeros[1])
                    buscar = re.split(r'ORDENAR,', numeros[1])

                    if ordenar == re.split(r',BUSCAR', numeros[1]) and buscar == re.split(r'ORDENAR,', numeros[1]):
                        ordenar = re.split(r',BUSCAR', numeros[1])
                        buscar = re.split(r'ORDENAR,', numeros[1])
                    buscar_numero = re.split(r' ', numeros[2])
                    cadena_inicial = cadena2[0].split(",")
                    lista_numeros = numeros[0].split(",")
                    lista_ordenar = ordenar[0].split(",")
                    #lista_buscar=buscar[1].split(",")
                    lista_buscar_numero = buscar_numero[0].split(" ")

                    buscar = re.split(r' ', numeros[1])

                    if buscar == re.split(r' ', numeros[1]):
                        buscar = re.split(r' ', numeros[1])
                        lista_buscar2 = re.split(r'ORDENAR,', numeros[1])

                    lista_buscarnum = lista_buscar_numero[0]

                    intlist = [int(x) for x in lista_numeros]
                    if "BUSCAR" in lista_buscar2:
                        print(cadena_inicial[0],":", lista_numeros, " | ", " valor buscado: ", lista_buscar_numero[0], " | ","encontrado: ", str(buscar_(intlist,int(lista_buscar_numero[0]))))
                        

                except:
                    print("")

        if op==4:
            print("\n")
            archivo = open(lista_ruta[0], 'r')
            for i in archivo:
                try:
                    cadena2 = i.split("=")
                    numeros = cadena2[1].split(" ")
                    numeros2 = re.split(r' ', numeros[1])
                    ordenar = re.split(r',BUSCAR', numeros[1])
                    buscar = re.split(r'ORDENAR,', numeros[1])

                    if ordenar == re.split(r',BUSCAR', numeros[1]) and buscar == re.split(r'ORDENAR,', numeros[1]):
                        ordenar = re.split(r',BUSCAR', numeros[1])
                        buscar = re.split(r'ORDENAR,', numeros[1])
                    buscar_numero = re.split(r' ', numeros[2])
                    cadena_inicial = cadena2[0].split(",")
                    lista_numeros = numeros[0].split(",")
                    lista_ordenar = ordenar[0].split(",")
                    # lista_buscar=buscar[1].split(",")
                    lista_buscar_numero = buscar_numero[0].split(" ")

                    buscar = re.split(r' ', numeros[1])

                    if buscar == re.split(r' ', numeros[1]):
                        buscar = re.split(r' ', numeros[1])
                        lista_buscar2 = re.split(r'ORDENAR,', numeros[1])

                    lista_buscarnum = lista_buscar_numero[0]


                    
                    intlist = [int(x) for x in lista_numeros]

                    
                    
                    if "ORDENAR" in ordenar:
                        print(cadena_inicial[0], ":", lista_numeros, " | ", "Resultado de ordenar", ":", sorted(lista_numeros),
                              " ,", ordenar[0])

                    if "ORDENAR\n" in ordenar:
                        print(cadena_inicial[0], ":", lista_numeros, " | ", "Resultado de ordenar", ":", sorted(lista_numeros),
                              " ,", ordenar[0])
                   
                    if "BUSCAR" in lista_buscar2:
                        print(cadena_inicial[0], ":",lista_numeros," | ", " valor buscado: ", lista_buscar_numero[0], " | ","encontrado: ", str(buscar_(intlist,int(lista_buscar_numero[0]))))

                     
                        
    
                except:
                    print("")

        if op==5:
            print("\n")
            archivo = open(lista_ruta[0], 'r')
            for i in archivo:
                try:
                    cadena2 = i.split("=")
                    numeros = cadena2[1].split(" ")
                    numeros2 = re.split(r' ', numeros[1])
                    ordenar = re.split(r',BUSCAR', numeros[1])
                    buscar = re.split(r'ORDENAR,', numeros[1])
                    if ordenar == re.split(r',BUSCAR', numeros[1]) and buscar == re.split(r'ORDENAR,', numeros[1]):
                        ordenar = re.split(r',BUSCAR', numeros[1])
                        buscar = re.split(r'ORDENAR,', numeros[1])
                    #buscar_numero = re.split(r', ', numeros[2])

                    cadena_inicial = cadena2[0].split(",")
                    lista_numeros = numeros[0].split(",")
                    lista_numeros_ordenado = numeros[0].split(",")
                    lista_ordenar = ordenar[0].split(",")
                    # lista_buscar=buscar[1].split(",")
                    #lista_buscar_numero = buscar_numero[0].split(",")
                    lista_numeros_busqueda=numeros[0].split(",")

                    buscar = re.split(r' ', numeros[1])


                    if buscar == re.split(r' ', numeros[1]):
                        buscar = re.split(r' ', numeros[1])
                        lista_buscar2 = re.split(r'ORDENAR,', numeros[1])


                    if "BUSCAR" in lista_buscar2:
                        lista_buscar_numero = re.split(r' ', numeros[2])
                        lista_buscar_numero2 = lista_buscar_numero[0].split(",")

                    lista_buscarnum = lista_buscar_numero[0]
       

                except:
                    print("")
                    
                for j in range(len(cadena_inicial)):
                    ordenar_final.append(cadena_inicial[0])


                if "BUSCAR" in lista_buscar2:

                    for numeros_buscados in range(len(lista_buscar_numero)):
                        lista_numeros_anidados.append(lista_buscar_numero[0])

                    for numero_buscar_lista in range(len(lista_buscar_numero2)):
                        lista_numeros_anidados_buscar.append(lista_buscar_numero2[0])
         
                
                intlist4 = [int(x) for x in lista_numeros_anidados]
                lista_numeros2_buscar=[int(x) for x in lista_numeros_busqueda]
                
                numeros1.append(lista_numeros)
                numeros_html_2.append(lista_numeros_ordenado)
                

                try:
                    if "ORDENAR\n" in ordenar or "ORDENAR" in ordenar:
                        print("Generando...")
                        print("Creando html")
                        file=open("reporte0.html","w")
                        file.write("<!DOCTYPE HTML>"+"\n")
                        file.write("<html>"+"\n")
                        file.write("<head>"+"\n")
                        file.write("<link rel=stylesheet href=style.css type=text/css>")
                        file.write("<style>"+"\n")
                        file.write("table, td, th {border: 1px solid black;}table {width: 100%;border-collapse: collapse;}")
                        file.write("</style>"+"\n")
                        file.write("</head>"+"\n")
                        file.write("<body>"+"\n")
                        file.write("<h2>Práctica 1 Lenguajes Formales y de Programación</h2>"+"\n")


                        file.write("<table id=tabla1>"+"\n")
                        file.write("<thead>"+"\n")
                        file.write("<tr>"+"\n")
                        file.write("<th>Lista Original</th>"+"\n")
                        file.write("<th>Lista Ordenada</th>"+"\n")
                        file.write("</tr>"+"\n")
                        file.write("</thead>"+"\n")
                        file.write("<tbody>"+"\n")
                        for original in range(len(ordenar_final)):
                            file.write("<tr>")
                            file.write("<td>"+str(ordenar_final[original])+" "+str(numeros1[original])+" ORDENAR "+"</td>")
                            file.write("<td>"+str(ordenar_final[original])+" Ordenado "+str(ordenamiento_burbuja(numeros_html_2[original])) +"</td>")
                            file.write("</tr>")
                        file.write("</tbody>"+"\n")
                        file.write("</table>"+"\n")
                        file.write("<br/>"+"\n")

                    if "BUSCAR" in lista_buscar2 or "BUSCAR\n" in lista_buscar2:
                        #Tabla Búsquedas
                        file.write("<table id=tabla2>"+"\n")
                        file.write("<thead>"+"\n")
                        file.write("<tr>"+"\n")
                        file.write("<th>Lista a buscar</th>"+"\n")
                        file.write("<th>Posición</th>"+"\n")
                        file.write("</tr>"+"\n")
                        file.write("</thead>"+"\n")
                        file.write("<tbody>"+"\n")
                        for bus in range(len(lista_numeros_anidados)):
                            file.write("<tr>")
                            file.write("<td>"+str(ordenar_final[bus])+"="+str(numeros1[bus])+" "+" BUSCAR "+str(lista_numeros_anidados[bus])+"</td>")
                            #file.write("<td>"+str(lista_numeros_busqueda[bus])+"</td>")
                            file.write("<td>"+str(buscar_(numeros1[bus],str(intlist4[bus])))+"</td>")
                            file.write("</tr>")
                        file.write("</tbody>"+"\n")
                        file.write("</table>"+"\n")
                        file.write("</body>"+"\n")
                        file.write("</html>"+"\n") 

                        file.close()
                except:
                    print("")
            print("Se creo el reporte html correctamente")
            os.startfile("reporte0.html")


        if op==6:
            print("\t 201901073")
            print("\t Federico David")
            print("\t fede88662@gmail.com")
            print("\t Lenguajes Formales y de Programación")
            exit()
            
                                  
iniciar=inicio()

