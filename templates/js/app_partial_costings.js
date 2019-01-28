var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
      complete_order_info: {},
      all_partial: {},
      current_partial : {},
      init_ledger : 0,      
      diferecia_mayores : 0.0,
      ajax_request : true,
      systems_ledger : 0,
      current_ledger : {
        'tipo' : 'inicial',
        'nro_pedido' : '',
        'id_parcial' : 0,
        'costo_producto' : 0,
        'facturas_sgi' : 0,
        'mayor_sap' : 0,
        'mayor_sgi' : 0,
        'precio_entrega' : 0,
        'provisiones_sap' : 0,
        'provisiones_sgi' : 0,
        'reliquidacion_ice' : 0,
      },
      csrftoken : Cookies.get('csrftoken'),
    },
    methods : {
      sayHello: function(){
        console.log('Hola Eduardo, Estamos dentro!.')
      }
    },
    mounted() {
      this.$http.get('{{BASE_URL}}api/order/all-data/', {params: {}}).then(response => {          
      this.order_data = response.body 
      this.ajax_request = false
      this.updateLedger()
    }, response => {
      console.log('Se produjo un error, por favor recargue la página');
    });
},
})