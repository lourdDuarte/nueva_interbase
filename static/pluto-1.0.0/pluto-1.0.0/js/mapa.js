$(document).ready(function() {
    $('.form-select').select2();
    $('#selectDni').change(function(){
        valor = $(this).val();
        console.log(valor);
        returnFilter(valor)
    });
    
    $('#selectSexo').change(function(){
        valor = $(this).val();
        // console.log(valor);
        returnFilter(valor)
    });
    
  })