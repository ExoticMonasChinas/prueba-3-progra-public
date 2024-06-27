registro_de_libro= {}
lista_de_libros = []
libros_registrados = {}
cantidad = 0
Género = "Ficcion" , "Accion" , "ciencia"
registro_de_ventast = []
def registro_de_libro():
    numero_de_libro = int(input("ingrese el numero del libro el cual va a registrar "))
    Título = (input("ingrese el titulo del libro "))
    Autor  = (input("Ingrese el autor del libro "))
    Género = (input("ingrese el genero del libro "))
    Precio = (input("ingrese el precio del libro "))
    libros_registrados["libro nuevo", numero_de_libro] = {"nombre del libro": Título,"Autor": Autor,"Genero": Género,"Precio":Precio}
    print("libro registrado")
    print(numero_de_libro)

def listar_libros():
    print("libros registrados en el sistema")
    print(libros_registrados)

def registrar_venta():
    print("registro de venta de libros")
    Título= input("ingrese el Título del libro vendido ")
    Precio = int(input("ingrese el precio por el que fue vendido "))
    cantidad = int(input("ingrese a cantidad vendida del libro "))
    Génerov = input(f"ingrese el genero del cual se vendio, de los Géneros que estan en el sistema son {Género} ")
    if Título in libros_registrados:
        print("el libro esta en la lista de los libros registrados en el sistema")
        print(f"el precio del libro por unidad es {Precio}")
        registro_de_ventast[libros_registrados] = Título,Género,Precio  
def imprimir_reporte_de_ventas():
    print("desea imprimir todos los reportes de venta?")
    print("escriba textualmentes yes o no")
    print("en caso de que usted escriba no, se imprimiran los nombres por genero")
    op =(input())
    if op == "yes":
        print(libros_registrados)
    else:
        print(Género)
while True:
    try:
        print("-----Menú-----")
        print("1.Registrar libro")
        print("2.Listar todos los libros")
        print("3.Registrar venta")
        print("4.Imprimir reporte de ventas")
        print("5.Generar txt")
        print("6.Salir del Programa")
    except:
        ("ingrese una opcion valida")
    opcion=(input("seleccione una opcion "))

    if opcion =="1":
        registro_de_libro()
    elif opcion == "2":
        listar_libros()
    elif opcion == "3":
        registrar_venta()
    elif opcion == "4":
        imprimir_reporte_de_ventas()
    elif opcion == "5":
        print("Ingrese el txt")
    elif opcion == "6":
        print("Graciias por usar nuestro programa, hasta luego nwn")
        break
