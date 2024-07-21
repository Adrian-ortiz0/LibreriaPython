import json
import time
import os
from datetime import datetime
#guardar y leer la base de datos de la bilioteca

def leer_datos_biblioteca():
    try:
        with open("data.json","r") as file:
            archivo = json.load(file)
            return archivo
            print("holis, archivos aqui <3")

    except FileNotFoundError:
        #CREA
        return {
            "usuarios":{
                "clientes":{},
                "admins":{
                    "adminmarino":{
                        "password":"JuanPapitoElMejor"
                    }
                }
                       },
            "libros":{
                       }
        }

def guardar_datos_biblioteca(data):
    with open("data.json","w") as guardar:
        json.dump(data,guardar,indent=4)
    print("\nGUARDANDO...\n")
    
#limpiar sistema
def clear():
    if os.name == 'nt':  # Si el sistema es Windows
        os.system('cls')
    else:  # Para sistemas tipo Unix (Linux, Mac)
        os.system('clear')

#tiempo de espera hasta que oprima una tecla.
def wait_for_keypress():
    print("Presiona cualquier tecla para continuar...")
    os.system('pause >nul')
    
def generadorID(data):
    # Obtener el último ID usado desde los datos
    ultimo_id = data.get("ultimo_id_libro", 0)
    nuevo_id = ultimo_id + 1
    data["ultimo_id_libro"] = nuevo_id
    return nuevo_id

#--------------------------------------------------------------------------


logo = """\033[96m
______________________________________________________________________________________________

███╗░░░███╗░█████╗░██████╗░██╗███╗░░██╗░█████╗░████████╗███████╗░█████╗░░█████╗░
████╗░████║██╔══██╗██╔══██╗██║████╗░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
██╔████╔██║███████║██████╔╝██║██╔██╗██║██║░░██║░░░██║░░░█████╗░░██║░░╚═╝███████║
██║╚██╔╝██║██╔══██║██╔══██╗██║██║╚████║██║░░██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
██║░╚═╝░██║██║░░██║██║░░██║██║██║░╚███║╚█████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝
______________________________________________________________________________________________
                                                                                                                                                                                            
        \033[96m"""

def main_principal_ingreso():
    while True:
        clear()
        print(logo,"\n")
        print("Estas a punto de introducirte en el mundo de los libros.\n")
        print("¿Quieres reservar libros? INSCRIBETE YA...")
        print("______________________________________________________________________________________________")
        op=input("1. ¿Ya estas registrado?(INGRESAR)\n2. Incribete para reservar\n3. Admin\n4. Salir de Marinoteca\n\nDIGITA TU OPCION: ")
        if op =="1":
            clear()
            security_cliente()
        elif op=="2":
            clear()
            registrar_usuario()
        elif op=="3":
            clear()
            security_admin()
        elif op=="4":
            clear()
            print("GRACIAS POR USAR NUESTROS SERVICIOS.")
            time.sleep(2)
            clear()
            print("Vuelve pronto, te esperamos...")
            time.sleep(1)
            clear()
            print("ADIOS.")
            time.sleep(2)
            clear()
            break
        

def security_admin():
    data=leer_datos_biblioteca()    
    admin = data["usuarios"]["admins"]
    bandera=True
    while bandera:
        try:
            print("************************************************************************")
            print(" BIENVENIDO, ESTE ES EL SISTEMA DE INGRESO PARA ADMINISTRADORES")
            print("************************************************************************")
            print("\n¿Deseas ingresar como Admin? \n1. Si\n2. No\n")
            interaccion = input("Seleccione una opcion: ")
            print("********************************************************")
            if interaccion =="1":
                admin=input("ingrese su usuario como adeministrador: ")
                for verificacion in data["usuarios"]["admins"]:
                    if admin == verificacion:
                        contraseña =input("Digite la clave: ")
                        if contraseña == data["usuarios"]["admins"][verificacion]["password"]:
                            print("\nCARGANDO SISTEMA...")
                            time.sleep(2)
                            clear()
                            main_admin_biblioteca()
                            
                        else:
                            print("********************************************************")
                            print("\nCONTRASEÑA INCORRECTA, INTENTALO NUEVAMENTE.\n")
                            print("********************************************************")
                            time.sleep(2)
                            clear()          
            elif interaccion =="2":
                time.sleep(2)
                clear()
                return
            else:
                clear()
                print("la opcion que ingresaste no es vaida.") 
                time.sleep(2)
                clear()
        except Exception:
            clear()
            print("\nla opcion que ingresaste no es valida\n")
            time.sleep(2)
            clear()

def security_cliente():
    data=leer_datos_biblioteca()    
    
    # users=data[usuarios][clientes]
    bandera=True
    while bandera:
        try:
            print("************************************************************************")
            print(" BIENVENIDO, ESTE ES EL SISTEMA DE INGRESO DE PERSONAS")
            print("************************************************************************")
            print("\n¿Deseas ingresar como persona? \n1. Si\n2. No\n")
            interaccion = input("Seleccione una opcion: ")
            print("********************************************************")
            if interaccion =="1":
                persona = input("ingrese su numero de identificacion: ")
                for verificacion in data["usuarios"]["clientes"]:
                    if persona == verificacion:
                        contraseña =input("Digite la clave: ")
                        if contraseña == data["usuarios"]["clientes"][persona]["password"]:
                            print("\nCARGANDO SISTEMA...")
                            time.sleep(2)
                            clear()
                            main_cliente_biblioteca()
                            
                        else:
                            print("********************************************************")
                            print("\nCONTRASEÑA INCORRECTA, INTENTALO NUEVAMENTE.\n")
                            print("********************************************************")
                            time.sleep(2)
                            clear()          
            elif interaccion =="2":
                time.sleep(2)
                clear()
                return
            else:
                clear()
                print("la opcion que ingresaste no es vaida, seleccione 1 o 2.") 
                time.sleep(2)
                clear()
        except Exception:
            clear()
            print("\nla opcion que ingresaste no es valida\n")
            time.sleep(2)
            clear()




#---------------------------------------------------------
#---------------------------ADMIN


#index del admin (muestra todos los menus )
def main_admin_biblioteca():
    while True:
        print("************************************************************************")
        print("                          MARINOTECA - ADMIN")
        print("************************************************************************\n")
        print("********************************************************")
        print("                INSCRIPCION DE CLIENTE")
        print("********************************************************")
        print("1. Registrar usuario")
        print("2. Eliminar usuario")
        
        print("********************************************************")
        print("                        LIBROS")
        print("********************************************************")
        print("3. Agregar libro")
        print("4. Eliminar libro")
        print("5. Agregar copias")
        print("6. Mostrar todos los libros")
        print("7. Mostrar libros por genero")
        print("8. Mostar libros por autor")
        
        print("********************************************************")
        print("                       RESERVA")
        print("********************************************************")
        print("9. mostrar libros disponibles")
        print("10. mostrar clientes con libros en uso")
        print("11. Reservar libro manualmente")
        print("12. Devolucion de libro")
        
        print("***********************************************")
        print("13. REGRESAR --> Menu principal")
        print("***********************************************\n")
        try:
            opt=int(input("ingrese su opcion: "))
            if opt==1:
                clear()
                registrar_usuario()
            elif opt==2:
                clear()
                eliminar_usuario()
            elif opt==3:
                clear()
                agregar_libro()
            elif opt==4:
                clear()
                eliminar_libro()
            elif opt==5:
                clear()
                agregar_copias()
            elif opt==6:
                clear()
                mostrar_todos()
            elif opt==7:
                clear()
                mostrar_genero()
            elif opt==8:
                clear()
                mostrar_autor()
            elif opt==9:
                clear()
                mostrar_disponibles()
            elif opt==10:
                clear()
                clientes_con_libros()
            elif opt==11:
                clear()
                reservar_manualmente()
            elif opt==12:
                clear()
                devolver_libro()
            elif opt==13:
                clear()
                return
            else:
                print("La opcion que ingresaste no esta disponible.")
                time.sleep(2)
                clear()
        except Exception:
            print("Error introducciste un valor no valido")
            time.sleep(1)
            clear()


#registrar usuario

def registrar_usuario():
    while True:        
        data=leer_datos_biblioteca()
        print("********************************************************")
        print("                    Pagina de registro")
        print("********************************************************")
        nombres = input("Ingrese sus nombres: ")
        apellidos = input("Ingrese sus apellidos: ")
        
        try:
            documento = int(input("Ingrese el número de documento de identificación: "))
        except ValueError:
            print("Número de documento inválido. Por favor, ingrese un número.")
            continue
        
        if data["usuarios"]["clientes"].get(str(documento), None) is None:
            direccion = input("Ingrese la dirección de residencia: ")
            
            try:
                telefonos_movil = int(input("Ingrese el número de teléfono móvil: "))
            except ValueError:
                print("Número de teléfono móvil inválido. Por favor, ingrese un número.")
                continue    
            password = input("Ingrese la contraseña: ")
            data["usuarios"]["clientes"][str(documento)] = {
                "Nombres": nombres,
                "Apellidos": apellidos,
                "Direccion": direccion,
                "Telefonos movil": telefonos_movil,
                "password":password,
                "libros":[]
            }


            print("***********************************************")
            guardar_datos_biblioteca(data)
            print("Registro guardado correctamente.")
            time.sleep(2)
            wait_for_keypress()
            clear()
            print("***********************************************")
            return
        else:
            print("***********************************************")
            print("Este usuario ya se encuentra registrado.")
            time.sleep(2)
            clear()
            print("***********************************************")
            return
        
def eliminar_usuario():
    while True:        
        data=leer_datos_biblioteca()
        print("********************************************************")
        print("                    Pagina de eliminación")
        print("********************************************************")
        try:
            documento = input("Ingrese el número de identificación del usuario a eliminar: ")
            if documento not in data["usuarios"]["clientes"]:      
                print("El usuario a eliminar no existe!")
                time.sleep(2)
                clear()
                print("***********************************************")
                break
            else:  
                nombre_usuario_eliminado = data["usuarios"]["clientes"][documento]["Nombres"]
                while True:
                    try:
                        eleccion = int(input(f"¿Estás seguro de que deseas eliminar al usuario: {nombre_usuario_eliminado}? (1. Sí / 2. No) "))
                        if eleccion == 1:
                            usuario_eliminado = data["usuarios"]["clientes"].pop(documento, None)
                            if usuario_eliminado:        
                                print("Usuario eliminado con éxito!")
                                print("***********************************************")
                                guardar_datos_biblioteca(data)
                                print("Datos actualizados correctamente.")
                                time.sleep(2)
                                wait_for_keypress()
                                clear()
                                print("***********************************************")
                                break
                        elif eleccion == 2:
                            print("Usuario no eliminado!")
                            print("***********************************************")
                            time.sleep(2)
                            clear()
                            print("***********************************************")
                            break
                        else:
                            print("Por favor, ingrese 1 para Sí o 2 para No.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese 1 para Sí o 2 para No.")
                break     
        except ValueError:
            print("Número de documento inválido. Por favor, ingrese un número.")
            continue
    

def agregar_libro():
        while True:      
            data=leer_datos_biblioteca()
            print("********************************************************")
            print("                    Pagina de registro de libro")
            print("********************************************************")
            titulo = input("Ingrese el titulo: ")
            autor = input("Ingrese el nombre del autor: ")
            
            if not any(libro for libro in data["libros"].values() if libro["Titulo"] == titulo and libro["Autor"] == autor):
                categoria = input("Ingrese la categoria: ")
                fecha_publi = input("Ingrese la fecha de publicación (YYYY-MM-DD): ")
                try:
                    datetime.strptime(fecha_publi, "%Y-%m-%d")
                except ValueError:
                    print("La fecha debe estar en el formato YYYY-MM-DD.")
                    continue
                
                try:
                    cantidad = int(input("Ingrese la cantidad: "))
                except ValueError:
                    print("La cantidad debe ser un número entero.")
                    continue
                id_libro = str(generadorID(data))  #genera id
                data["libros"][id_libro] = {
                    "Titulo": titulo,
                    "Autor": autor,
                    "Categoria": categoria,
                    "Telefonos movil": fecha_publi,
                    "Cantidad":cantidad,
                    "Disponibilidad":True
                }
                print("***********************************************")
                guardar_datos_biblioteca(data)
                print(f"Registro del libro con ID:({id_libro}) fue guardado correctamente.")
                time.sleep(2)
                wait_for_keypress()
                clear()
                print("***********************************************")
                return
            else:
                print("***********************************************")
                print("Este libro ya se encuentra registrado.")
                time.sleep(2)
                clear()
                print("***********************************************")
                return

def eliminar_libro():
    while True:
        data=leer_datos_biblioteca()
        print("********************************************************")
        print("                    Pagina de eliminacion de libro")
        print("********************************************************")
        try:
            id_libro = input("Ingrese el ID del libro que desea eliminar: ")
            if id_libro in data["libros"]:
                libro = data["libros"][id_libro]
                print(f"Libro encontrado: Titulo: {(libro["Titulo"])}, Autor: {(libro["Autor"])}, Cantidad: {(libro["Cantidad"])}")

                eliminar_todo = input("Desea eliminar todas las unidades de este libro? (1. Si - 2. No) :")
                if eliminar_todo == "1":
                    data["libros"].pop(id_libro)
                    print(f"El libro con ID{id_libro} fue eliminado correctamente.")
                else:
                    try:
                        cantidad_a_eliminar = int(input("Ingrese la cantidad a eliminar: "))
                        if cantidad_a_eliminar >= libro["Cantidad"]:
                            data["libros"].pop(id_libro)
                            print(f"Se eliminaron todas las unidades del libro con ID: {id_libro} ya que la cantidad a eliminar es igual o mayor a las existencias.")
                        else:
                            data["libros"][id_libro]["Cantidad"] -=cantidad_a_eliminar
                            print(f"Cantidad actualizada. Quedan {"Cantidad"} unidades del libro con ID: {id_libro}")
                    except ValueError:
                        print("La cantidad a eliminar debe ser un numero entero")
                        continue
                guardar_datos_biblioteca(data)
                time.sleep(2)
                wait_for_keypress()
                clear()
                print("********************************************************")
                return
        except ValueError:
            print("No se encontró un libro con el ID proporcionado.")

def agregar_copias():
    while True:
        data = leer_datos_biblioteca()
        print("********************************************************")
        print("                    Pagina de agregar copias de libro")
        print("********************************************************")
        id_libro = input("Ingrese el ID del libro: ")

        if id_libro not in data["libros"]:
            print("No se encontró un libro con el ID proporcionado.")
        else:
            try:
                cant_adicional = int(input("Ingrese la cantidad de copias para adicionar: "))
                data["libros"][id_libro]["Cantidad"] += cant_adicional
                cant_total = data["libros"][id_libro]["Cantidad"]
                print(f"Se agregaron {cant_adicional} copias del libro con ID: {id_libro}.")
                print(f"Cantidad total {cant_total}")
                guardar_datos_biblioteca(data)
            except ValueError:
                print("La cantidad a agregar debe ser un numero entero")
                continue
        time.sleep(2)
        wait_for_keypress()
        clear()
        print("********************************************************")
        return


# def mostrar_genero():


        
#---------------------------------------------------------
#-------------------------CLIENTE


def main_cliente_biblioteca():
    while True:
        print("************************************************************************")
        print("                          MARINOTECA - BIENVENIDO USUARIO")
        print("************************************************************************\n")
        print("********************************************************")
        print("                   BUSQUEDA LIBROS")
        print("********************************************************")
        print("1. Buscar libro")
        
        print("********************************************************")
        print("                       RESERVA")
        print("********************************************************")
        print("2. Reservar libro")
        
        print("***********************************************")
        print("3. REGRESAR --> Menu principal")
        print("***********************************************\n")
        try:
            opt=int(input("ingrese su opcion: "))
            if opt==1:
                clear()
                registrar_usuario()
            elif opt==2:
                clear()
            elif opt==3:
                clear()
            elif opt==4:
                clear()
                return
            
            else:
                print("La opcion que ingresaste no esta disponible.")
                time.sleep(2)
                clear()
        except Exception:
            print("Error introducciste un valor no valido")
            time.sleep(1)
            clear()

main_principal_ingreso()