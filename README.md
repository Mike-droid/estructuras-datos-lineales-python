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
