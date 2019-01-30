var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
      ajax_request : false,
      complete_order_info: {},
      all_partials: {},
      current_partial : {},
      csrftoken : Cookies.get('csrftoken'),
    },
    methods : {
      sayHello: function(){
        console.log('Hola Eduardo, Estamos dentro!.')
      },
      updateLedger : function(){
        console.log('Actualizado saldo del Mayor')
      }
    },
    mounted() {
      this.$http.get('{{BASE_URL}}api/order/all-data/{{ data.complete_order_info.order.nro_pedido }}', { params: {}}).then(response => {          
      this.complete_order_info = response.body 
      this.updateLedger()
    }, response => {
      console.log('Se produjo un error, por favor recargue la página');
    });
},
})