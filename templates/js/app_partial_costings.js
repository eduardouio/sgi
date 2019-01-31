var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
      ajax_request : true,
      complete_order_info: {},
      all_partials: [],
      current_partial : null,      
      current_ordinal_parcial : parseInt('{{ data.ordinal_partial }}'),
      nro_order : '{{ data.complete_order_info.order }}',
      current_order_invoice : {},
      csrftoken : Cookies.get('csrftoken'),
      current_expense : null,
      show_expense : false,
      current_paid : null,
      current_selected_partial : null,
      show_order_invoice : false,
      show_origin_expense : false,
      show_taxes : false,
      current_ledger : {
        'tipo' : 'inicial',
        'nro_pedido' : '{{ data.complete_order_info.order.nro_pedido }}',
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
      contabilized : function(paid){
        console.log('Envio actualizacion de pago')
        if (paid.paid.bg_mayor){
            paid.paid.bg_mayor = 0
            this.current_expense.legder -= parseFloat(paid.paid.valor)
        }else{
            paid.paid.bg_mayor = 1
            this.current_expense.legder += parseFloat(paid.paid.valor)
        }            
        this.$http.put('{{BASE_URL}}api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
            this.updateLedger()
          }, response => {
            alert('Se produjo un error, por favor recargue la página');
          });
    },

    updateLedger: function(){
        console.log('actualizando mayor')
        if (typeof(this.complete_order_info.expenses) != 'object'){                
          console.log('[Debug] El pedido no tiene gastos')
          return false
      }
        var ledger = 0
        for (var x = 0 ; x < (this.complete_order_info.expenses.length);x++){
            var item = this.complete_order_info.expenses[x]
            ledger += parseFloat(item.legder)
        }    
        this.current_ledger.mayor_sgi = 0
        this.current_ledger.mayor_sgi = Math.round((parseFloat(this.init_ledger) + parseFloat(ledger))*100)/100
      
    },
      selectPartial : function(){
        console.dir(this.current_partial)
        if ((this.current_partial === null) && (this.all_partials.length === parseInt('{{ data.ordinal_partial }}'))){
          console.log('Marcando el parcial Activo {{data.ordinal_partial}}')
          this.current_partial = this.all_partials[0]
          this.current_order_invoice = this.complete_order_info.order_invoice
          this.ajax_request = false
        }
      },
      showOrderInvoice : function(){
        console.log('mostrando factura del pedido')
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = true
        return true
      },
      showOriginExpense : function(){
        console.log('Mostrando Gastos en Origen')
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = true
        this.show_order_invoice = false
      },
      selectExpense : function(item){
        console.log('Seleccionando Gasto', item)
        this.show_expense = true
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.current_expense = item
      },
      contabilized : function(paid){
        console.log('Envio actualizacion de pago')
        if (paid.paid.bg_mayor){
            paid.paid.bg_mayor = 0
            this.current_expense.legder -= parseFloat(paid.paid.valor)
        }else{
            paid.paid.bg_mayor = 1
            this.current_expense.legder += parseFloat(paid.paid.valor)
        }            
        this.$http.put('{{BASE_URL}}api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
            this.updateLedger()
          }, response => {
            alert('Se produjo un error, por favor recargue la página');
          });
    },
    get_paid_invoice : function(id_paid){
      this.$http.get('{{BASE_URL}}api/paid-invoice/all/' + id_paid  + '/', {params: {}}).then(response => {          
          this.current_paid = response.data;
        }, response => {
          alert('Se produjo un error, por favor recargue la página');
        });
  },
    },
    mounted() {
      this.$http.get('{{BASE_URL}}api/order/all-data/{{ data.complete_order_info.order.nro_pedido }}', { params: {}}).then(response => {
      this.complete_order_info = response.body 
      var x = 0
      response.body.partials.forEach(el => {
        if (x < parseInt('{{ data.ordinal_partial }}')) {
          this.$http.get('{{BASE_URL}}api/partial/all-data/' + el.id_parcial + '/',{ params: {}}).then(resp => {
          this.all_partials.push(resp.body)
          this.updateLedger()
          this.selectPartial()
          })
          x=x+1
      }
        })        
    }, response => {
      alert('Ocurrio un error al cargar la aplicacion, por recargue la pagina')
    });
  },
  filters : {
    money : function(number){
      return parseFloat(number).toFixed(2)
    },
    int_val : function(number){
      return parseInt(number)
    }
  }
})