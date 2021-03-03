# Dictionary


Importamos `json` para poder cargar archivos `.json` y  de `difflib` importamos ` get_close_matches`.

Creamos la función `translate` para obtener el significado de la palabra buscada.
    * 1º Buscamos la palabra introducida por teclado tal cual `sino` esta:
    * 2ª Usamos `.title()` para poner la primera letra de la palabra en mayúsculas
    ~~~python
    word = smog
    print(word.title())
    Smog
    ~~~
    * 3º Usamos `upper()` para buscar si la palabra está en mayúsculas.
    ~~~python
    word.upper()
    ~~~
    * 4º `get_close_matches()`  Encuentra coincidencias cercanas entre una cadena y una lista de cadenas
    ~~~python
    get_close_matches(word, data.keys())
    ~~~
    Y te da la opción por si te has equivocado a la hora de escribir la palabra.