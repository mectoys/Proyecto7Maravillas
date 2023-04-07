import csv
import os.path

import folium

tiletype = "OpenStreetMap"


def SaveLocation():
    dirname = os.path.dirname(__file__)
    dirmap = r"map\SieteMaravillas.html"
    savelocation = os.path.join(dirname, dirmap)
    return savelocation


def MostrarMapaSieteMaravillas():
    m = folium.Map(location=[0, 0], zoom_start=3, tiles=tiletype)
    # Abrir la bd de tipo csv
    with open('..\\data\\data.csv', 'r') as fmap:
        readermap = csv.reader(fmap)
        # Función next() retorna el sgte. item de un iterador
        next(readermap, None)
        ListDuplicate = []
        # Insertar en la lista si es maravilla moderna o antigua
        for row in readermap:
            ListDuplicate.append(row[0])

    with open('..\\data\\data.csv', 'r') as fmaravilla:
        readermaravilla = list(csv.reader(fmaravilla))
        # Bucle donde recorrermo maravilla moderna o Antigua
        for maravilla in list(dict.fromkeys(ListDuplicate)):
            feature_group = folium.FeatureGroup(maravilla, show=False)
            datafiltrada = list(filter(lambda k: maravilla in k, readermaravilla))
            for filamaravilla in datafiltrada:
                # Agrega el ícono
                icon = folium.features.CustomIcon(filamaravilla[4], icon_size=(48, 48))
                # Agregar popup que admite código HTML
                htmlcode = """<div style="font-family: courier new; color: blue">
                                                 <img src={0} alt={1} width="230" height="172">
                                                 <br /><span><h5>{2}</h5></span> """.format(filamaravilla[5],
                                                                                            filamaravilla[1],
                                                                                            filamaravilla[6])
                feature_group.add_child(
                    folium.Marker([float(filamaravilla[2]), float(filamaravilla[3])], popup=htmlcode
                                  , tooltip=filamaravilla[1], icon=icon))
            feature_group.add_to(m)
        folium.LayerControl().add_to(m)
        m.save(SaveLocation())


if __name__ == '__main__':
    MostrarMapaSieteMaravillas()
