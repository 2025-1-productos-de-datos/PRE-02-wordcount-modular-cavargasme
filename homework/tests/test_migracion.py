# """
# Este código debería tener lo mínimo que permita garantizar que existe el archivo
# results.tsv en la carpeta data/output. Esta verificación es lo mínimo que se debería
# hacer para que uno pueda sentirse tranquilo inicialmene con la ejecución del código.
# Sin embargo, vale la pena que se realicen algunas pruebas de escritorio para verificar
# que el resultado de la ejecución sea coherente.

# Importante. En los asserts, la verificación de los casos de escritorio se realizan de esa
# forma, usando con get, para que por defecto se regresa el valor cero. Esto es relevante
# porque posiblemente esas palabras de prueba no existan en el archivo results.tsv, pero eso
# no necesariamente implica que el código funcione mal.
# """

# import os

# from ..src.wordcount import main


# def test_migracion():

#     main()

#     if not os.path.exists("data/output/results.tsv"):
#         raise FileNotFoundError("El archivo results.tsv no existe.")

#     results = {}

#     with open("data/output/results.tsv", "r", encoding="utf-8") as f:
#         lines = f.readlines()
#     for line in lines:
#         key, value = line.strip().split("\t")
#         results[key] = value

#     assert results.get("computational", 0) == "3"
#     assert results.get("analytics", 0) == "5"
