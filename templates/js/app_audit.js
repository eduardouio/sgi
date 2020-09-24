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
            this.closeModal()
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
            this.closeModal()
            this.$http.get('{{ data.host }}api/partial/all-data/' + id_partial + '/',
                { headers: { "X-CSRFToken": this.csrftoken } }).then(
                    response=>{
                        console.log('informacion recuperada')
                        this.show_partial = true
                        this.current_partial = response.data
                        this.title_modal = 'Detalle parcial ' + response.data.partial.ordinal_parcial + ' del pedido ' + response.data.partial.nro_pedido
                    },error=>{
                        console.log('Error en comunicacion con servidor')
                        console.dir(error)
                        alert('Error al interntar comunicarse con el servidor')
                    })
        },
        closeModal : function(){
            console.log('Cerrando modal del pedido')
            this.current_order = null
            this.current_partial = null
            this.title_modal = ''
            this.show_order = false
            this.show_partial = false
        },
    }, filters : {
        money : function(val){
                return parseFloat(val).toFixed(2)
        },
        int: function (val) {
            return parseInt(val)
        }
    },
 })