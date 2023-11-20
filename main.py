from grafo import *

if __name__ == "__main__":

    grafo = GrafoNoDirigido()
    num_relaciones = 0

    print("Bienvenido al sistema de análisis de relaciones sociales en mensajes\n")
    while True:
        try:
            num_relaciones = int(input("Ingresa por favor el número de relaciones que deseas generar\n"))
            if num_relaciones < 1:
                print("Número de relaciones no válida")
            else:
                break
        except ValueError:
            print("No se ingresó un valor numérico entero")

    grafo.generar_json(num_relaciones)

    print("\n"+"-"*50+"\n")
    grafo.relacion_fuerte()

    print("\n" + "-" * 50 + "\n")
    grafo.mas_amigos()

    print("\n" + "-" * 50 + "\n")
    grafo.mejores_amigos()
