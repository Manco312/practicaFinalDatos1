import json
import random


class Nodo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.grado = 0

    def __str__(self):
        return f'[({self.id}) {self.nombre}\t]'

    def __gt__(self, other):
        return self.grado > other.grado


class Arista:
    def __init__(self, nodo_inicio, nodo_destino, peso):
        self.nodo_inicio = nodo_inicio
        self.nodo_destino = nodo_destino
        self.peso = peso

    def __str__(self):
        return f'AMISTAD: [{self.nodo_inicio} --- {self.nodo_destino}:: PESO:{self.peso}]'

    def __gt__(self, other):
        return self.peso > other.peso


class GrafoNoDirigido:
    def __init__(self):
        self.nodos = {}     # diccionario "HashTable"
        self.aristas = []   # lista

    def generar_json(self, cantidad):
        # Número de relaciones que deseas generar
        n = cantidad

        # Lista para almacenar las relaciones
        relaciones = []

        # Generar n relaciones y agregarlas a la lista
        for _ in range(n):
            id_emisor = random.randint(0, 13)
            id_receptor = random.randint(0, 13)
            while id_emisor == id_receptor:
                id_receptor = random.randint(0, 13)
            relacion = self.generar_relacion(id_emisor, id_receptor)
            relaciones.append(relacion)

        # Guardar la lista de relaciones en un archivo JSON
        with open("historial_comunicaciones.json", "w") as archivo_json:
            json.dump(relaciones, archivo_json, indent=2)

        print(f"Se han generado y guardado {n} relaciones en el archivo 'relaciones.json'.")

        print("Se ha generado el grafo de la siguiente manera:")
        self.mostrar_grafo()

    # Función para generar una relación de forma aleatoria
    def generar_relacion(self, id_emisor, id_receptor):
        nombres = ["Juan", "Maria", "Luis", "Ana", "Pedro", "Edison", "Gertrudis", "Rafaella", "Tulio", "Laura",
                   "Carlos", "Miguel", "Elena", "Sofia"]
        mensaje = f"Hola {nombres[id_receptor]}, soy {nombres[id_emisor]}. Amigos!!!."

        relacion = {
            "id_emisor": id_emisor,
            "nombre_emisor": nombres[id_emisor],
            "id_receptor": id_receptor,
            "nombre_receptor": nombres[id_receptor],
            "mensaje": mensaje
        }

        if id_emisor not in self.nodos:
            self.agregar_nodo(Nodo(id_emisor, nombres[id_emisor]))

        if id_receptor not in self.nodos:
            self.agregar_nodo(Nodo(id_receptor, nombres[id_receptor]))

        found = False
        if len(self.aristas) != 0:
            for item in self.aristas:
                if (item.nodo_inicio.id == id_emisor and item.nodo_destino.id == id_receptor) or (item.nodo_inicio.id == id_receptor and item.nodo_destino.id == id_emisor):
                    item.peso += 1
                    found = True

        if not found:
            self.agregar_arista(self.nodos[id_emisor], self.nodos[id_receptor], 1)
            self.nodos[id_emisor].grado += 1
            self.nodos[id_receptor].grado += 1

        return relacion

    def agregar_nodo(self, nodo):
        self.nodos[nodo.id] = nodo

    def agregar_arista(self, nodo_inicio, nodo_destino, peso):
        if nodo_inicio.id in self.nodos and nodo_destino.id in self.nodos:
            arista = Arista(nodo_inicio, nodo_destino, peso)
            self.aristas.append(arista)

    def mostrar_grafo(self):
        for arista in self.aristas:
            print(f"{arista}")

    def relacion_fuerte(self):
        peso_mayor = max(self.aristas).peso
        print("Estas son la(s) relacion(es) más fuerte(s)\n")
        for item in self.aristas:
            if item.peso == peso_mayor:
                print(f'La relación entre {item.nodo_inicio.nombre} y {item.nodo_destino.nombre} con un valor de {item.peso}')

    def mas_amigos(self):
        numamigos_mayor = max(self.nodos.values()).grado
        print("Estas son la(s) persona(s) con más amigos\n")
        for item in self.nodos:
            if self.nodos[item].grado == numamigos_mayor:
                print(f'{self.nodos[item].nombre} con {self.nodos[item].grado} amigos')

    def mejores_amigos(self):
        for nodo in self.nodos.values():
            PesoAristaMayor = None
            for arista in self.aristas:
                if arista.nodo_inicio.id == nodo.id or arista.nodo_destino.id == nodo.id:
                    if PesoAristaMayor is None:
                        PesoAristaMayor = arista.peso
                    elif arista.peso > PesoAristaMayor:
                        PesoAristaMayor = arista.peso
            for arista in self.aristas:
                if arista.peso == PesoAristaMayor and arista.nodo_inicio.id == nodo.id:
                    print(f'El mejor amigo de {arista.nodo_inicio.nombre} es {arista.nodo_destino.nombre} con un total de {arista.peso} mensajes')
                elif arista.peso == PesoAristaMayor and arista.nodo_destino.id == nodo.id:
                    print(f'El mejor amigo de {arista.nodo_destino.nombre} es {arista.nodo_inicio.nombre} con un total de {arista.peso} mensajes')
                