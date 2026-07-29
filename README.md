# Taller 3, Matemáticas Discretas I

**Universidad Nacional de Colombia**
Criptografía, grafos, álgebra de Boole, Shannon y un primer vistazo cuántico

## Integrantes

| Nombre | Correo |
|---|---|
| Jean Carlo Triana Guzmán | jetrianag@unal.edu.co |
| Diego Alejandro Rodríguez Sandoval | dirodriguezsa@unal.edu.co |

**Docente:** Jhoan Sebastian Tenjo García

## Descripción

Este repositorio contiene la solución a los 10 ejercicios del Taller 3, organizados en tres bloques:

- **Bloque A — Criptografía:** cifrado César, RSA de juguete y MPC básico (suma secreta).
- **Bloque B — Grafos:** ruta más corta con Dijkstra, cierre de una estación y coloreo de grafos.
- **Bloque C — Álgebra de Boole, Shannon y computación cuántica:** tablas de verdad, simplificación booleana, entropía de Shannon y un simulador cuántico de un qubit.

Cada punto está implementado como un módulo de Python independiente, con al menos tres pruebas automatizadas que verifican su correcto funcionamiento (ver carpeta `tests/`).

## Lenguaje usado

**Python 3** (probado con Python 3.12 / 3.13). No se usan librerías externas: todos los programas se implementan únicamente con la librería estándar (`math`, `random`, `heapq`, `itertools`). Por esta razón no hay dependencias que instalar — ver el archivo `requirements.txt` incluido, que lo indica explícitamente.

## Estructura del repositorio

```
.
├── README.md
├── requirements.txt
├── src/
│   ├── cripto/
│   │   ├── cesar.py                   # Punto 1: Cifrado César
│   │   ├── rsa.py                     # Punto 2: RSA de juguete
│   │   └── mpc_basico.py              # Punto 3: MPC básico (suma secreta)
│   ├── grafos/
│   │   ├── grafo.py                   # Clase grafo + algoritmo de Dijkstra
│   │   ├── dijkstra.py                # Punto 4: Ruta más corta (caso de prueba)
│   │   ├── cerrar_estacion.py         # Punto 5: Cierre de una estación
│   │   └── coloreo_grafos.py          # Punto 6: Coloreo de grafos
│   └── boole_shannon_compucuantic/
│       ├── tablas_verdad.py           # Punto 7: Tablas de verdad y circuitos lógicos
│       ├── simplificacion_booleana.py # Punto 8: Simplificación booleana
│       ├── shannon.py                 # Punto 9: Entropía de Shannon
│       └── simulador_cuantico.py      # Punto 10: Primer simulador cuántico
├── tests/                             # Pruebas de cada punto (unittest / pytest)
└── docs/
    └── taller3_programacion_discreta.pdf   # Documento de explicación (este PDF)
```

> Nota: el punto 4 (Dijkstra) está implementado dentro de `src/grafos/grafo.py` como el método `grafo.dijkstra()`; el archivo `dijkstra.py` es el script que arma el grafo de prueba (8 vértices, 12 aristas) y ejecuta ese método. Los puntos 7 a 10 se agruparon en una sola carpeta (`boole_shannon_compucuantic/`) en lugar de separarlos en `boole/` y `cuantica/`, ya que el taller indica que esa separación por carpetas es opcional.

## Instrucciones para ejecutar

Clonar el repositorio y ubicarse en la raíz del proyecto. No se requiere instalar nada adicional, solo tener Python 3.

Copiar y pegar el siguiente comando en la terminal del IDE: git clone https://github.com/jetrianag/taller-3-matematicas-discretas.git

### Bloque A — Criptografía

```bash
python3 src/cripto/cesar.py        # menú interactivo: cifrar, descifrar, fuerza bruta
python3 src/cripto/rsa.py          # menú interactivo: generar llaves, cifrar, descifrar
python3 src/cripto/mpc_basico.py   # menú interactivo: simular el protocolo de suma secreta
```

### Bloque B — Grafos

```bash
cd src/grafos
python3 dijkstra.py           # corre el grafo de prueba y muestra la ruta más corta Museo -> Universidad
python3 cerrar_estacion.py    # simula el cierre del vértice "Centro" y compara distancias antes/después
python3 coloreo_grafos.py     # menú interactivo: colorea el grafo de ejemplo (10 cursos)
```

Los scripts de `grafos/` importan `grafo.py` con una ruta relativa, por lo que deben ejecutarse desde dentro de `src/grafos/`.

### Bloque C — Boole, Shannon y computación cuántica

```bash
python3 src/boole_shannon_compucuantic/tablas_verdad.py            # genera las tablas de verdad y pide una entrada manual
python3 src/boole_shannon_compucuantic/simplificacion_booleana.py  # corre los casos de prueba de simplificación
python3 src/boole_shannon_compucuantic/shannon.py                  # pide dos textos y compara su entropía
python3 src/boole_shannon_compucuantic/simulador_cuantico.py       # corre los 3 casos de prueba obligatorios (X, H, HH)
```

### Ejecutar las pruebas

Todas las pruebas se pueden correr con `pytest` (recomendado) o con el módulo `unittest` de la librería estándar:

```bash
pip install pytest --break-system-packages   # si no lo tienen instalado
pytest tests/ -v

# alternativa sin instalar nada adicional:
python3 -m unittest discover -s tests -p "*.py" -v
```

Con esto se ejecutan las 33 pruebas automatizadas del proyecto (mínimo 3 por punto, como pide el taller).

## Lista de ejercicios desarrollados

| # | Ejercicio | Archivo principal | Pruebas |
|---|---|---|---|
| 1 | Cifrado César | `src/cripto/cesar.py` | `tests/cesar_test.py` |
| 2 | RSA de juguete | `src/cripto/rsa.py` | `tests/rsa_test.py` |
| 3 | MPC básico (suma secreta) | `src/cripto/mpc_basico.py` | `tests/mpc_basico_test.py` |
| 4 | Ruta más corta (Dijkstra) | `src/grafos/grafo.py`, `dijkstra.py` | `tests/dijkstra_test.py` |
| 5 | Cierre de una estación | `src/grafos/cerrar_estacion.py` | `tests/cerrar_estacion_test.py` |
| 6 | Coloreo de grafos | `src/grafos/coloreo_grafos.py` | `tests/coloreo_grafos.py` |
| 7 | Tablas de verdad y circuitos lógicos | `src/boole_shannon_compucuantic/tablas_verdad.py` | `tests/tablas_verdad_test.py` |
| 8 | Simplificación booleana | `src/boole_shannon_compucuantic/simplificacion_booleana.py` | `tests/simplificacion_booleana_test.py` |
| 9 | Entropía de Shannon | `src/boole_shannon_compucuantic/shannon.py` | `tests/shannon_test.py` |
| 10 | Primer simulador cuántico | `src/boole_shannon_compucuantic/simulador_cuantico.py` | `tests/simulador_cuantico_test.py` |

## Documentación matemática

La explicación de cada punto (qué problema resuelve, qué idea matemática usa, cómo se ejecuta, qué pruebas se hicieron y qué limitaciones tiene) está en `docs/taller3_programacion_discreta.pdf`.

## Uso de herramientas de asistencia

Se usó un asistente de IA (Claude, de Anthropic) como apoyo puntual para redactar este README y el documento de explicación en LaTeX a partir del código ya escrito, y para revisar la consistencia entre el código, las pruebas y el enunciado. Todo el código fue escrito, entendido y puede ser explicado por los integrantes del grupo.
