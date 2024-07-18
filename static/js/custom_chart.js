/*------------------------------------------------------------------
    File Name: custom_chart.js
    Template Name: Pluto - Responsive HTML5 Template
    Created By: html.design
    Envato Profile: https://themeforest.net/user/htmldotdesign
    Website: https://html.design
    Version: 1.0
-------------------------------------------------------------------*/

$(function () {
    
    new Chart(document.getElementById("bar_chart").getContext("2d"), getChartJs('bar'));
   
});

function getChartJs(type) {
    var config = null;
    let [circuito, numero] = obtenerDatosCircuito();
    if (type === 'bar') {
        config = {
            type: 'bar',
            data: {
                
                labels: circuito,
                datasets: [{
                    label: "Total de registros",
                    data: numero,
                    backgroundColor: 'rgba(255, 87, 34, 1)'
                }], 
            },
            options: {
                responsive: true,
                legend: false
            }
        }
    }
   
    return config;
}