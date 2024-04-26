from django.shortcuts import render
from renaper.models import Renaper
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, TemplateView
from django.db.models import Count
from interbase.utils import *
# Create your views here.

class DatosTemplateView(TemplateView):
    
    template_name = "datos_personas/listado.html"
    
    def get_context_data(self, **kwargs):
        
        template_name = "datos_personas/listado.html"
        context = super().get_context_data(**kwargs)


        return context
    
    def post(self, request, *args, **kwargs):

        numero_documento = request.POST.get('numerodocumento')
        apellido = request.POST.get('apellido')
        nombre = request.POST.get('nombres')
        datos_renaper = Renaper.objects.values('id', 'numerodocumento', 'apellido', 'nombres')
        if (numero_documento): 
                datos_renaper = datos_renaper.filter(numerodocumento = numero_documento)
        if (apellido): 
                datos_renaper = datos_renaper.filter(apellido__icontains = apellido)
        if (nombre):
                datos_renaper = datos_renaper.filter(nombres__icontains = nombre)

        context = self.get_context_data()
        if (numero_documento or apellido or nombre ):
                context['datos_renaper']= datos_renaper
            
        

            
        return render (request, 'datos_personas/listado.html', context)
    
    def detalle_persona(request,pk):
        
        data = Renaper.objects.filter(id=pk)
        dni = 0
        
        context = {'data_persona':data}

        for d in context['data_persona']:
             dni = d.numerodocumento
        
        ultima_direccion = Renaper.objects.raw(" select id, domicilio from base_datos.padron2023 where matricula = '"+dni+"'")
        
        context_direccion = {'ultima_direccion': ultima_direccion}
        context.update(context_direccion)
        
        
        return render (request,'datos_personas/detalle.html',context)
    
   
    def panel_resumen(request):
          
          total_registros = Renaper.objects.count()
          total_femenino = Renaper.objects.filter(sexo='F').count()
          total_masculino = Renaper.objects.filter(sexo='M').count()
          total_direcciones = contar_direcciones_actualizadas()
          
          
          context ={'total_registro': total_registros, 
                    'total_femenino': total_femenino, 
                    'total_masculino': total_masculino, 
                    'total_direcciones_actualizadas':total_direcciones}
          
          return render (request,'dashboard.html', context)
   
    

    def mapa_ubicaciones(request):
        
        ubicaciones =  Renaper.objects.raw(" SELECT id, numerodocumento, longitud, latitud, sexo"
                            + " FROM  renaper_renaper where longitud != '' and longitud != 'NULL' ")
        partidos = Renaper.objects.raw(" SELECT * FROM renaper_partido")
        partido =  Renaper.objects.raw(" SELECT p.id, numerodocumento, longitud, latitud, partido_id"
                            + " FROM  renaper_renaper INNER JOIN renaper_partido as p on p.id = partido_id "
                            + " where longitud != '' and longitud != 'NULL' ")
        
        context = {'ubicacion': ubicaciones,
                  
                   'partidos':partido,
                   'partido': partido}
        
        return render (request, 'mapas/mapa-ubicaciones.html', context)
    
    