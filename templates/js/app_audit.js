/**
 * aplicaicion de auditoria
 * revision y aprobacion de facturas
 */
var app = new Vue({
    el : '#app',
    delimiters : ['${','}'],
    data : {
        current_order : null,
        current_partial  : null,
        show_order : false,
        show_partial : false,
        title_modal : '',
    }, methods : {
        loadOrder : function(nro_order){
            console.log('cargando informacion completa del pedido')
            this.$http.get('{{ data.host }}api/order/all-data/' + nro_order + '/', 
            {headers: {"X-CSRFToken":this.csrftoken }}).then(
                response => {
                    console.log('Obteniendo informacion completa del pedido')
                    this.current_order = response.data
                    this.title_modal = 'Detalle pedido ' + response.data.order.nro_pedido + ' ' + response.data.order.proveedor
                    this.show_order = true
            this.show_partial = false
                }, error => {
                    console.log('Error en solicitud')
                    console.dir(error)
                })
        },
        loadPartial : function(id_partial){
            console.log('Cargando informacion completa del parcial')

        }
    }
 })