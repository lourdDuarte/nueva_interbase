

var valor

$(document).ready(function() {
    $('.form-select').select2();
    $('#selectDni').change(function(){
        valor = $(this).val();
      
        BuscarPorDni(valor)
    });
   
    
   
  })

 
  
function BuscarPorDni(filter){
  
    const marcadores = [];
    
 
    coordenadas.forEach(coordenada => {
        if (filter == coordenada.id_detalle){
           
            let marcador = new ol.Feature({
                  id: coordenada.id_detalle,
                  geometry: new ol.geom.Point(
                      ol.proj.fromLonLat([coordenada.longitud, coordenada.latitud])
                  ),
              });
              marcador.setId(coordenada.id_detalle);
              marcador.setStyle(new ol.style.Style({
                    image: new ol.style.Circle({
                    radius: 15,
                    fill: new ol.style.Fill({color: 'red'})
                  })
              }));
            marcadores.push(marcador)
              

            }
            

  })

 
  
      let ultimaCapa = new ol.layer.Vector({
          source: new ol.source.Vector({
              features: marcadores, 
          }),
      });
      
      mapa.addLayer(ultimaCapa)
      
}

