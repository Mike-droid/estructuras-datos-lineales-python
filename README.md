# Curso de estructuras de datos lineales con Python

## Introducción a las estructuras de datos

### Python como base de programación

Lo que debes saber:

- [Curso básico de algoritmos y pensamiento lógico](https://platzi.com/cursos/pensamiento-logico/)
- [Curso de introducción a la terminal y línea de comandos](https://platzi.com/cursos/terminal/)
- [Curso básico de Python](https://platzi.com/cursos/python/)
- [Curso intermedio de Python](https://platzi.com/cursos/python-intermedio/)
- [Curso de pensamiento computacional con Python](https://platzi.com/cursos/python-cs/)
- [Curso de POO](https://platzi.com/clases/oop/)

En este curso veremos:

- [Arrays](https://www.youtube.com/watch?v=phRshQSU-xA)
- [Nodes](https://www.youtube.com/watch?v=652GaaDZPMw)
- [Linked Lists](https://www.youtube.com/watch?v=FU6I-VtjOes)
- [Stacks](https://www.youtube.com/watch?v=NKmasqr_Xkw)
- [Queues](https://www.youtube.com/watch?v=6zmI_BU18xk)

## Elementos de la programación en Python

Convenciones en Python

- variable
- CONSTANTE
- nombre_funcion
- nombreClase

Python tiene sus propias estructuras:

- Listas -> `[]`
- Tuplas -> `()`
- Conjuntos (sets) -> `{}`
- Diccionarios -> `{key: value}`

### Tipos de colecciones

¿Qué es una colección?

> Un grupo de cero o más elementos que pueden tratarse como una unidad conceptual.

- Non-zero value
- 0
- null
- undefined

Tenemos 2 tipos de colecciones:

- Dinámicas
- Inmutables

Las estructuras de datos lineales están ordenadas  por posición y solamente el primer elemento NO tiene predecesor. `['D1', 'D2', 'D3', 'D4', 'D5']`

Existen estructuras de datos jerárquicas, como son los árboles. Aquí de igual manera, el primer elemento NO tiene predecesor.

Otra estructura de dato son los grafos. Cada dato puede tener varios predecesores y sucesores.

Incluso existen estructuras de datos desordenadas y ordenadas.

- Colección
  - Grafos
  - Jerárquicas
    - Árbol binario
    - Montículo
  - Lineales
    - Lista
      - Lista ordenada
    - Cola
      - Cola de prioridad
    - Pila
    - String
  - Desordenadas
    - Bolsa
      - Bolsa ordenada
    - Diccionario
      - Diccionario ordenado
    - Conjunto
      - Conjunto ordenado

- [Algorithms Course - Graph Theory Tutorial from a Google Engineer](https://www.youtube.com/watch?v=09_LlHjoEiY)
- [HackerRank](https://www.youtube.com/c/HackerrankOfficial/videos?view=0&sort=p&flow=grid)

### Operaciones esenciales en colecciones

Ejemplo de función recursiva:

```python
def pyramid_sum(lower, upper, margin=0):
  blanks = " " * margin
  print(blanks, lower, upper)
  if lower > upper:
    print(blanks, 0)
    return 0
  else:
    result = lower + pyramid_sum(lower + 1, upper, margin + 4)
    print(blanks, result)
    return result


pyramid_sum(1,4)

"""resultado:
1 4
     2 4
         3 4
             4 4
                 5 4
                 0
             4
         7
     9
 10
"""
```

### Colecciones incorporadas en Python

#### Listas

- Propósito general
- Estructura más utilizada
- Tamaño dinámico
- De tipo secuencial
- Ordenable
- Se declaran con `[]` y `list()`

#### Tuplas

- Inmutable (no se pueden añadir o cambiar).
- Útiles para datos constantes.
- Más rápidas que las listas.
- Tipo secuencial.
- Se declaron con `()` y `tuple()`

#### Conjuntos / Sets

- Almacenan objetos no duplicados.
- De acceso rápido.
- Aceptan operaciones lógicas.
- Son desordenados.
- Se declaran con `{}` y `set()`

#### Diccionarios

- Pares de lalve-valor.
- Arrays asociativos (hash maps).
- Son desordenados.
- Se declaran con `{key: value}` y `dict()`

## Arrays

### Arrays en Python

Conceptos clave:

- Elemento -> Valor almacenado en las posiciones del array.
- Índice -> referencia a la posición del elemento.

Podemos hacer arrays de 1D, 2D y 3D pero no se recomienda hacer más de 2D, porque se vuelve muy complejo el computo. Los array son listas, pero las listas no son arrays.

Los arrays se usan por ejemplo en los mapas de bits, son arrays 2D.

### Crear un array

```python
import random

class Array:
  def __init__(self, capacity, fill_value=None):
    self.items = list()
    for i in range(capacity):
      self.items.append(fill_value)

  def __len__(self):
    return len(self.items)


  def __str__(self):
    return str(self.items)


  def __iter__(self):
    return iter(self.items)


  def __getitem__(self, index):
    return self.items[index]


  def __setitem__(self, index, new_item):
    self.items[index] = new_item


  def __fill_array__(self):
    for i in range(len(self.items)):
      random_number = random.randrange(0, 100)
      self.items[i] = random_number


  def __sum_values__(self):
    sum = 0
    for i in range(len(self.items)):
      if type(self.items[i]) == int:
        sum += self.items[i]
    return sum


```

### Array de dos dimensiones

```python
from my_array import Array


class Grid():
  def __init__(self, rows, columns, fill_value=None):
    self.data = Array(rows)
    for row in range(rows):
      self.data[row] = Array(columns, fill_value)


  def get_height(self):
    return len(self.data)


  def get_width(self):
    return len(self.data[0])


  def __getitem__(self, index):
    return self.data[index]


  def __str__(self):
    result = ""
    for row in range(self.get_height()):
      for column in range(self.get_width()):
        result += str(self.data[row][column]) + " "

      result += "\n"

    return str(result)


  def fill_Grid(self):
    for row in range(self.get_height()):
      Array.__fill_array__(self.data[row])
      for column in range(self.get_width()):
        Array.__fill_array__(self.data[column])


```

Cubo (con ayuda de Copilot):

```python
import random

class Cube:
  def __init__(self, length, fill_value=None):
    self.length = length
    self.cube = [[[fill_value for z in range(length)] for y in range(length)] for x in range(length)]


  def fill_cube(self):
    for x in range(self.length):
      for y in range(self.length):
        for z in range(self.length):
          self.cube[x][y][z] = random.randint(1, 100)


```

## Linked lists

### Nodos y singly linked list

- Consiste de nodos conectados a otros.
- Los más comunes son *sencillos* o *dobles*.
- No se accede por índice, sino por recorrido.

Conceptos clave:

- Data: valor almacenado en nodos.
- Next: referencia al siguiente nodo.
- Previous: referencia al nodo anterior.
- Head: referencia al primer nodo.
- Tail: referencia al último nodo.

Podemos usar las listas para crear Pilas y Colas. También para optimizar código.

Head -> [nodo1 - D1] <-> [nodo2- D2] <-> [nodo3 - D3] <- Tail

**A tomar en cuenta**: Si una lista es muy larga, tomará mucho tiempo recorrerla, esto por O(n).

### Crear nodos

Cada nodo va a tener un valor y un apuntador.

```python
class Node():
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

```

### Crear singly linked list

```python
from node import Node

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0


  def append(self, data):
    node = Node(data)

    if self.tail == None and self.head == None:
      self.head = node
      self.tail = node
    else:
      current = self.tail

      while current.next:
        current = current.next

      current.next = node
      self.tail = current.next

    self.size += 1


  def size(self):
    return str(self.size)


  def iter(self):
    current = self.tail

    while current:
      value = current.data
      current = current.next
      yield value #* Genera valores pero NO los almacena


  def delete(self, data):
    current = self.tail
    previous = self.tail

    while current:
      if current.data == data:
        if current == self.tail:
          self.tail = current.next
        else:
          previous.next = current.next
          self.size -= 1
          return current.data

      previous = current
      current = current.next


  def search(self, data):
    flag = False
    for node in self.iter():
      if data == node:
        flag = True
        print(f'Data {data} found 😎')
    if not flag:
      print(f'Data {data} not found 😞')


  def clear(self):
    self.tail = None
    self.head = None
    self.size = 0


games = SinglyLinkedList()
games.append('GTA V')
print(f'head: {games.head.data} & tail: {games.tail.data}')
games.append('Fifa')
print(f'head: {games.head.data} & tail: {games.tail.data}')
games.append('Mario')
print(f'head: {games.head.data} & tail: {games.tail.data}')

```

### Operaciones en single linked structures

Hay un dilema con las listas. No usan índices, a comparación de los arrays. Para esto, podemos usar una variable auxiliar llamada *probe*.

```python
from node import Node

# * Creación de los nodos enlazados (linked list)
head = None
for count in range(1,6):
    head = Node(count, head)


# * Recorrer e imprimir valores de la lista
probe = head
print("Recorrido de la lista:")
while probe != None:
    print(probe.data)
    probe = probe.next


# * Busqueda de un elemento
probe = head
target_item = 2
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f'Target item {target_item} has not been found')
else:
    print(f'Target item {target_item} has been found')


# * Remplazo de un elemento
probe = head
target_item = 3
new_item = "Z"

while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f"{new_item} replace the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")


# * Insertar un nuevo elemento/nodo al inicio(head)
head = Node("F", head)


# * Insertar un nuevo elemento/nodo al final(tail)
new_node = Node("K")
if head is None:
    head = new_node
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = new_node


# * Eliminar un elemento/nodo al inicio(head)
removed_item = head.data
head = head.next
print("Removed_item: ",end="")
print(removed_item)


# * Eliminar un elemento/nodo al final(tail)
removed_item = head.data
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next.data
    probe.next = None

print("Removed_item: ",end="")
print(removed_item)

# * Agregar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
# new_item = input("Enter new item: ")
# index = int(input("Enter the position to insert the new item: "))
new_item = "10"
index = 3

if head is None or index <= 0:
    head = Node(new_item, head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)

# * Agregar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)


# * Eliminar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
index = 3

if head is None or index <= 0:
    removed_item = head.data
    head = head.next
    print(removed_item)
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removed_item = probe.next.data
    probe.next = probe.next.next

    print("Removed_item: ",end="")
    print(removed_item)


```

### Operaciones a detalle

### Circular linked list

El último nodo hace referencia al primer nodo.

```python
index = 1
new_item = 'ham'
head = Node(None, None)
head.next = head
probe = head
while index > 0 and probe.next != head:
    probe = probe.next
    index -= 1

probe.next = Node(new_item, probe.next)
print(probe.next.data)
#ham

```

### Double linked list

Aquí los punteros hacen referencia al siguiente nodo y al anterior.

```python
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous


    def add_after(self, node):
        node = TwoWayNode(node)
        if self.next == None:
            self.next = node
            node.previous = self
        else:
            probe = self
            while probe.next != None:
                probe = probe.next
            probe.next = node
            node.previous = probe


    def find_node(self, data):
        if self.data == data:
            return (f'Se ha encontrado {self.data}')
        elif self.next == None:
            return (f'No existe ese dato')
        else:
            return self.next.find_node(data)

```

## Stacks

### ¿Qué son los stacks?

Se conocen como 'pilas'. Se basan en LIFO (Last In First Out), es decir, el último elemento que llega, es el primero que sale.

Sus métodos más comunes son push (insertar) y pop (remover).

Sus propiedaes más comunes son top (el elemento que está más arriba) y bottom (el elemento que está más abajo).

### Crear un stack

```python
from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0


    def push(self, data):
        node = Node(data, self.top)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1


    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return ("The stack is empty")


    def peek(self):
        return self.top.data if self.top else ("The stack is empty")


    def clear(self):
        while self.top:
            self.pop()


    def search_element(self, data):
        if self.top:
            current = self.top
            while current:
                if current.data == data:
                    return (f'Elemet {data} founded')
                current = current.next
            return (f'Elemet {data} not founded')

```

## Queues

### ¿Qué son las queues?

Tienen la misma lógica que las colas (o filas) de un puesto donde venden cosas. Siguen el principio de FIFO (First In First Out), es decir, el primero que entra es el primero que sale.

Tiene las propiedades de *rear* (último elemento) y *front* (primer elemento).

Operaciones fundamentales:

- pop(): remover front.
- add(): añadir a rear.

### Queue basada en listas

```python
# Cola basada en Lista

class ListQueue:
    def __init__(self):
        self.items = []
        self.size = len(self.items)


    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1


    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data


    def traverse(self):
        total_items = self.size
        for item in range(total_items):
            print(self.items[item])


```

### Queue basada en dos stacks

```python
class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []


    def enqueue(self, data):
        self.inbound_stack.append(data)


    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()

```

### Queue basada en nodos

```python
class TwoWayNode(object):
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def enqueue(self, data):
        new_node = TwoWayNode(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1


    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data


```

### Reto: simulador de playlist musical
