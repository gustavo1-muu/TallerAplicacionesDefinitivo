import cx_Oracle
import os
from dao.areasdao import AreasDao
from dao.usuariosdao import UsuariosDao
from dao.clientesdao import ClientesDao
from dao.criticidadesdao import CriticidadesDao
from dao.tiposdao import TiposDao
from dao.tiquetsdao import TiquetDao
def main():
    cx_Oracle.init_oracle_client(lib_dir=r"c:/instantclient_21_10/")
    areasdao = AreasDao()
    usuariosdao = UsuariosDao()
    clientesdao = ClientesDao()
    criticidadesdao = CriticidadesDao()
    tipo = TiposDao()
    tiquet = TiquetDao()

    user = input("\n\nIngrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    if usuariosdao.verificar_usuario(user, password) == 1:
        print("\n¡Usuario válido!\n\n")
        while True:
            print("\n Menú de Administrador:")
            print("\n 1. Tiquets")
            print("\n 2. Usuarios")
            print("\n 3. Clientes")
            print("\n 4. Criticidades")
            print("\n 5. Tipos")
            print("\n 6. Areas")
            print("\n 7. Salir")
            eleccionAdmin = input("\n¿Qué menú desea ver?: ")

            if eleccionAdmin == "1":#Tiquets
                os.system("cls")
                print("\nMenú de Tiquets:")
                print("\n 1. Mostrar Tiquets")
                print("\n 2. Añadir Tiquet")
                print("\n 3. Editar Tiquet")
                print("\n 4. Eliminar Tiquet")
                eleccionAdmin2 = input("\n¿Qué quiere hacer?: ")

                if eleccionAdmin2 == "1":#Listo
                    os.system("cls")
                    tiquet.mostrar_tiquets()
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "2":
                    os.system("cls")
                    new_tiquet_id = input("\nIngrese el ID del nuevo Tiquet: ")
                    new_tiquet_usuario_creador = input("\nIngrese el ID del Usuario Creador del nuevo Tiquet: ")
                    new_tiquet_usuario_asignado = input("\nIngrese el ID del Usuario Asignado del nuevo Tiquet: ")
                    new_tiquet_cliente_asignado = input("\nIngrese el ID del Cliente Asignado del nuevo Tiquet: ")
                    new_tiquet_tipo_tiquet = input("\nIngrese el ID del Tipo Tiquet del nuevo Tiquet (\n1. Soporte Técnico\n2. Quejas\n3. Felicitaciones): ")
                    new_tiquet_criticidad = input("\nIngrese el ID del Criticidad del nuevo Tiquet (\n1. Baja\n2.\nMedia\n3. Alta\n4. Crítica ): ")
                    new_tiquet_area_destino = input("\nIngrese el ID del Area Destino del nuevo Tiquet(\n1. Atención al Cliente\n2. Facturación y Pagos\n3 .Ventas y consultas): ")
                    new_tiquet_detalles_servicio = input("\nIngrese los Detalles de Servicio del nuevo Tiquet: ")
                    new_tiquet_detalles_problema = input("\nIngrese los Detalles de Problema del nuevo Tiquet: ")
                    new_tiquet_estado = input("\nIngrese el ID del Estado del nuevo Tiquet (1 para PENDIENTE, 0 para FINALIZADO): ")
                    new_tiquet_observacion = input("\nEscriba una Observacion para el nuevo Tiquet: ")
                    tiquet.anadir_tiquet(new_tiquet_id, new_tiquet_usuario_creador, new_tiquet_usuario_asignado, new_tiquet_cliente_asignado, new_tiquet_tipo_tiquet, new_tiquet_criticidad, new_tiquet_area_destino, new_tiquet_detalles_servicio, new_tiquet_detalles_problema, new_tiquet_estado, new_tiquet_observacion)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "3":
                    os.system("cls")
                    id_tiquet_editar = input("\nIngrese el ID del Tiquet que desea editar: ")
                    usuario_creador_tiquet_editar = input("\nIngrese el ID del Usuario Creador nuevo del Tiquet: ")
                    usuario_asignado_tiquet_editar = input("\nIngrese el ID del Usuario Asignado nuevo del Tiquet: ")
                    cliente_asignado_tiquet_editar = input("\nIngrese el ID del Cliente Asignado nuevo del Tiquet: ")
                    tipo_tiquet_tiquet_editar = input("\nIngrese el ID del Tipo Tiquet nuevo del Tiquet: ")
                    criticidad_tiquet_editar = input("\nIngrese el ID del Criticidad nueva del Tiquet: ")
                    area_destino_tiquet_editar = input("\nIngrese el ID del Area Destino nueva del Tiquet: ")
                    detalles_servicio_tiquet_editar = input("\nIngrese los Detalles de Servicio del Tiquet: ")
                    detalles_problema_tiquet_editar = input("\nIngrese los Detalles de Problema del Tiquet: ")
                    estado_tiquet_editar = input("\nIngrese el nuevo Estado del Tiquet (1 para PENDIENTE, 0 para FINALIZADO): ")
                    observacion_tiquet_editar = input("\nEscriba una Observacion para el Tiquet: ")
                    tiquet.editar_tiquet(id_tiquet_editar, usuario_creador_tiquet_editar, usuario_asignado_tiquet_editar, cliente_asignado_tiquet_editar, tipo_tiquet_tiquet_editar, criticidad_tiquet_editar, area_destino_tiquet_editar, detalles_servicio_tiquet_editar, detalles_problema_tiquet_editar, estado_tiquet_editar, observacion_tiquet_editar)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "4":#Listo
                    os.system("cls")
                    id_tiquet_borrar = input("\nIngrese el ID del Tiquet que desea borrar: ")
                    tiquet.eliminar_tiquet(id_tiquet_borrar)   
                    print("Presiona Enter para continuar...")
                    input() 

            elif eleccionAdmin == "2":#Usuarios----LISTOLISTOLISTOLISTOLISTOLISTOLISTOLISTOLISTOLISTOLISTOLISTOLISTO
                os.system("cls")
                print("\nMenú de Usuarios:")
                print("\n 1. Mostrar Usuarios")
                print("\n 2. Añadir Usuario")
                print("\n 3. Editar Usuario")
                print("\n 4. Eliminar Usuario")
                eleccionAdmin2 = input("\n¿Qué quiere hacer?: ")

                if eleccionAdmin2 == "1":#Listo
                    os.system("cls")
                    usuariosdao.mostrar_usuarios()
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "2":
                    os.system("cls")
                    new_user_id = input("\nIngrese el ID del nuevo Usuario: ")
                    new_user_name = input("\nIngrese el nombre del nuevo Usuario: ")
                    new_user_password = input("\nIngrese la contraseña del nuevo Usuario: ")
                    new_user_type = input("\nIngrese el tipo de usuario del nuevo Usuario: ")
                    if new_user_type != 'admin' and new_user_type != 'user':
                        print("Tipo de usuario no válido.")
                    else:
                        usuariosdao.anadir_usuario(new_user_id, new_user_name, new_user_password, new_user_type)
                        print("Presiona Enter para continuar...")
                        input()

                elif eleccionAdmin2 == "3":
                    os.system("cls")
                    id_user_editar = input("\nIngrese el ID del Usuario que desea editar: ")
                    user_new_name_edit = input("\nIngrese el nuevo nombre del Usuario: ")
                    user_new_password_edit = input("\nIngrese la nueva contraseña del Usuario: ")
                    user_new_type_edit = input("\nIngrese el nuevo tipo de usuario del Usuario: ")
                    if user_new_type_edit != 'admin' and user_new_type_edit != 'user':
                        print("Tipo de usuario no válido.")
                    else:
                        usuariosdao.editar_usuario(id_user_editar, user_new_name_edit, user_new_password_edit, user_new_type_edit)
                        print("Presiona Enter para continuar...")
                        input()

                elif eleccionAdmin2 == "4":#Listo
                    os.system("cls")
                    id_user_borrar = input("\nIngrese el ID del Usuario que desea borrar: ")
                    usuariosdao.eliminar_usuario(id_user_borrar)
                    print("Presiona Enter para continuar...")
                    input()

            elif eleccionAdmin == "3":#Clientes
                os.system("cls")
                print("\nMenú de Clientes:")
                print("\n 1. Mostrar Clientes")
                print("\n 2. Añadir Clientes")
                print("\n 3. Editar Clientes")
                print("\n 4. Eliminar Clientes")
                eleccionAdmin2 = input("\n¿Qué quiere hacer?: ")
                
                if eleccionAdmin2 == "1":#Listo
                    os.system("cls")
                    clientesdao.mostrar_clientes()
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "2":
                    os.system("cls")
                    new_client_id = input("\nIngrese el ID del nuevo Cliente: ")
                    new_client_rut = input("\nIngrese el rut del nuevo Cliente: ")
                    new_client_name = input("\nIngrese el nombre del nuevo Cliente: ")
                    new_client_phone = input("\nIngrese el número de teléfono del nuevo Cliente (Sólo números): ")
                    new_client_email = input("\nIngrese el correo electrónico del nuevo Cliente: ")
                    clientesdao.añadir_clientes(new_client_id, new_client_rut, new_client_name, new_client_phone, new_client_email)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "3":
                    os.system("cls")
                    id_client_editar = input("\nIngrese el ID del Cliente que desea editar: ")
                    rut_client_editar = input("\nIngrese el nuevo rut del Cliente: ")
                    nombre_client_editar = input("\nIngrese el nuevo nombre del Cliente: ")
                    telefono_client_editar = input("\nIngrese el nuevo número de teléfono del Cliente (Sólo números): ")
                    correo_client_editar = input("\nIngrese el nuevo correo electrónico del Cliente: ")
                    clientesdao.editar_clientes(id_client_editar, rut_client_editar, nombre_client_editar, telefono_client_editar, correo_client_editar)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "4":#Listo
                    os.system("cls")
                    id_client_borrar = input("\nIngrese el ID del Cliente que desea borrar: ")
                    clientesdao.eliminar_clientes(id_client_borrar)
                    print("Presiona Enter para continuar...")
                    input()

            elif eleccionAdmin == "4":#Criticidades
                os.system("cls")
                print("\nMenú de Criticidades:")
                print("\n 1. Mostrar Criticidades")
                print("\n 2. Añadir Criticidades")
                print("\n 3. Editar Criticidades")
                print("\n 4. Eliminar Criticidades")
                eleccionAdmin2 = input("\n¿Qué quiere hacer?: ")

                if eleccionAdmin2 == "1":#Listo
                    os.system("cls")
                    criticidadesdao.mostrar_criticidades()
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "2":
                    os.system("cls")
                    new_criticidad_id = input("\nIngrese el ID de la nueva Criticidad: ")
                    new_criticidad_nombre = input("\nIngrese el nombre de la nueva Criticidad: ")
                    criticidadesdao.añadir_criticidades(new_criticidad_id, new_criticidad_nombre)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "3":
                    os.system("cls")
                    id_criticidad_editar = input("\nIngrese el ID de la Criticidad que desea editar: ")
                    name_criticidad_editar = input("\nIngrese el nuevo nombre de la Criticidad: ")
                    criticidadesdao.editar_criticidades(id_criticidad_editar, name_criticidad_editar)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "4":#Listo
                    os.system("cls")
                    id_criticidad_borrar = input("\nIngrese el ID de la Criticidad que desea borrar: ")
                    criticidadesdao.eliminar_criticidades(id_criticidad_borrar)
                    print("Presiona Enter para continuar...")
                    input()

            elif eleccionAdmin == "5":#Tipos
                os.system("cls")
                print("\nMenú de Tipos:")
                print("\n 1. Mostrar Tipos")
                print("\n 2. Añadir Tipos")
                print("\n 3. Editar Tipos")
                print("\n 4. Eliminar Tipos")
                eleccionAdmin2 = input("\n¿Qué quiere hacer?: ")

                if eleccionAdmin2 == "1":#Listo
                    os.system("cls")
                    tipo.mostrar_tipos()
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "2":
                    os.system("cls")
                    new_tipo_id = input("\nIngrese el ID del nuevo Tipo de Tiquet: ")
                    new_tipo_nombre = input("\nIngrese el nombre del nuevo Tipo de Tiquet: ")
                    tipo.anadir_tipos(new_tipo_id, new_tipo_nombre)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "3":
                    os.system("cls")
                    id_tipo_editar = input("\nIngrese el ID del Tipo de Tiquet que desea editar: ")
                    nombre_tipo_editar = input("\nIngrese el nuevo nombre del Tipo de Tiquet: ")
                    tipo.editar_tipos(id_tipo_editar, nombre_tipo_editar)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "4":#Listo
                    os.system("cls")
                    id_tipo_borrar = input("\nIngrese el ID del Tipo de Tiquet que desea borrar: ")
                    tipo.eliminar_tipos(id_tipo_borrar)
                    print("Presiona Enter para continuar...")
                    input()

            elif eleccionAdmin == "6":#Areas
                os.system("cls")
                print("\nMenú de Areas:")
                print("\n 1. Mostrar Areas")
                print("\n 2. Añadir Areas")
                print("\n 3. Editar Areas")
                print("\n 4. Eliminar Areas")
                eleccionAdmin2 = input("\n¿Qué quiere hacer?: ")

                if eleccionAdmin2 == "1":#Listo
                    os.system("cls")
                    areasdao.mostrar_areas()
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "2":
                    os.system("cls")
                    new_area_id = input("\nIngrese el ID de la nueva Area: ")
                    new_area_nombre = input("\nIngrese el nombre de la nueva Area: ")
                    areasdao.añadir_area(new_area_id, new_area_nombre)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "3":
                    os.system("cls")
                    id_area_editar = input("\nIngrese el ID de la Area que desea editar: ")
                    nombre_area_editar = input("\nIngrese el nuevo nombre de la Area: ")
                    areasdao.editar_area(id_area_editar, nombre_area_editar)
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionAdmin2 == "4":#Listo
                    os.system("cls")
                    id_area_borrar = input("\nIngrese el ID del Área que desea borrar: ")
                    areasdao.eliminar_area(id_area_borrar)
                    print("Presiona Enter para continuar...")
                    input()

            elif eleccionAdmin == "7":#Salir
                os.system("cls")
                print("Ádios!")
                break

    elif usuariosdao.verificar_usuario(user, password) == 2:
        print("\n¡Usuario válido!\n\n")
        while True:
            print("\n Menú de Usuario:")
            print("\n 1. Tiquets")
            print("\n 2. Salir")
            eleccionUser = input("\n¿Qué menú deseas hacer?: ")

            if eleccionUser == "1":
                os.system("cls")
                print("\nMenú de Tiquets:")
                print("\n 1. Mostrar Tiquets")
                print("\n 2. Añadir Tiquet")
           
                eleccionUser2 = input("\n¿Qué quiere hacer?: ")

                if eleccionUser2 == "1":#Listo
                    os.system("cls")
                    tiquet.mostrar_tiquets()
                    print("Presiona Enter para continuar...")
                    input()

                elif eleccionUser2 == "2":
                    os.system("cls")
                    new_tiquet_id = input("\nIngrese el ID del nuevo Tiquet: ")
                    new_tiquet_usuario_creador = input("\nIngrese el ID del Usuario Creador del nuevo Tiquet: ")
                    new_tiquet_usuario_asignado = input("\nIngrese el ID del Usuario Asignado del nuevo Tiquet: ")
                    new_tiquet_cliente_asignado = input("\nIngrese el ID del Cliente Asignado del nuevo Tiquet: ")
                    new_tiquet_tipo_tiquet = input("\nIngrese el ID del Tipo Tiquet del nuevo Tiquet (\n1. Soporte Técnico\n2. Quejas\n3. Felicitaciones): ")
                    new_tiquet_criticidad = input("\nIngrese el ID del Criticidad del nuevo Tiquet (\n1. Baja\n2.\nMedia\n3. Alta\n4. Crítica ): ")
                    new_tiquet_area_destino = input("\nIngrese el ID del Area Destino del nuevo Tiquet(\n1. Atención al Cliente\n2. Facturación y Pagos\n3 .Ventas y consultas): ")
                    new_tiquet_detalles_servicio = input("\nIngrese los Detalles de Servicio del nuevo Tiquet: ")
                    new_tiquet_detalles_problema = input("\nIngrese los Detalles de Problema del nuevo Tiquet: ")
                    new_tiquet_estado = input("\nIngrese el ID del Estado del nuevo Tiquet (1 para PENDIENTE, 0 para FINALIZADO): ")
                    new_tiquet_observacion = input("\nEscriba una Observacion para el nuevo Tiquet: ")
                    tiquet.anadir_tiquet(new_tiquet_id, new_tiquet_usuario_creador, new_tiquet_usuario_asignado, new_tiquet_cliente_asignado, new_tiquet_tipo_tiquet, new_tiquet_criticidad, new_tiquet_area_destino, new_tiquet_detalles_servicio, new_tiquet_detalles_problema, new_tiquet_estado, new_tiquet_observacion) 
                    print("Presiona Enter para continuar...")
                    input()

            elif eleccionUser == "2":
                os.system("cls")
                print("Ádios!")
                break

if __name__ == "__main__":
    main()