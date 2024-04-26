
//variables para el modal con los datos de persona
var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');
  



//Inicializacion del mapa. Documentacion: https://openlayers.org/en/v3.20.1/examples/vector-wfs.html

ZOOM = 15;
const overlay = new ol.Overlay({
    element: container,
    autoPan: true,
    autoPanAnimation: {
            duration: 300,
    }       
});

var raster = new ol.layer.Tile({
  source: new ol.source.OSM()
});

var source = new ol.source.Vector({wrapX: false});

var vector = new ol.layer.Vector({
  source: source
});


const mapa = new ol.Map({
target: 'mapa', 
layers: [
new ol.layer.Tile({
    source: new ol.source.OSM("Wikimedia",
  ["https://maps.wikimedia.org/osm-intl/${z}/${x}/${y}.png"],
  {
  attribution: "© OpenStreetMap and contributors, under an open license. Wikimedia's new style (beta)",
  "tileOptions": { "crossOriginKeyword": null }
  })
  }),
  raster, vector
],
overlays: [overlay],
view: new ol.View({
  center: ol.proj.fromLonLat([-58.174346900170235, -26.184853611236456]),
  zoom: ZOOM,
})
});






// **************  Abrir detalle de persona seleccinada en el mapa ******************** //

mapa.on('click', function (e) 
{
  mapa.forEachFeatureAtPixel(e.pixel, function (feature, layer) {

  if(feature.getId()){
    
    detalle = feature.getId()
    window.open('/detalle/'+detalle+'/','_blank');

  }

 
});

});
