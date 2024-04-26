//Interaccion con el mapa. Documentacion: https://openlayers.org/en/latest/examples/draw-and-modify-features.html

var typeSelect = document.getElementById('type');

var draw; // global so we can remove it later
function addInteraction() {
  var value = typeSelect.value;
  if (value == 'Circle') {
    draw = new ol.interaction.Draw({
      source: source,
      type: /** @type {ol.geom.GeometryType} */ (typeSelect.value)
    });
    mapa.addInteraction(draw);
  }
}


/**
 * Handle change event.
 */
typeSelect.onchange = function() {
  mapa.removeInteraction(draw);
  addInteraction();
};






function removeMap(){
$('#exampleModal').modal('show'); // abrir
location.reload()
}




// ---- Cerrar modal
closer.onclick = function() {
    overlay.setPosition(undefined);
    closer.blur();
    return false;
};

