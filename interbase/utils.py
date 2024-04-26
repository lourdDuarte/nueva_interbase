from renaper.models import Renaper

def contar_direcciones_actualizadas():
          total_direcciones_actualizadas = 0
          direcciones_actualizadas = Renaper.objects.raw(" select renaper.id, numerodocumento from base_datos.padron2023 as padron inner join renaper_renaper as renaper on padron.matricula = renaper.numerodocumento")
          for d in direcciones_actualizadas:
                total_direcciones_actualizadas += 1
          return total_direcciones_actualizadas


