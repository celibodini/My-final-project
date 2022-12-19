from ejemplo.models import Padres
Padres(nombre="Sabrina", apellido="Bodini", dni=123123).save()
Padres(nombre="Juan", apellido="Gonzales", dni=890890).save()
Padres(nombre="Roberto", apellido="Rodriguez", dni=345345).save()
Padres(nombre="Florencia", apellido="Rios", dni=567567).save()
print("Se cargo con éxito los usuarios de pruebas")