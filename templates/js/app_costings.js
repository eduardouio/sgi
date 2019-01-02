var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
      order_data: {},
      current_expense : null,
      current_order_invoice : {},
      current_taxes: {},
      current_paid : null,
      init_ledger : parseFloat('{{ order.init_ledger }}'.replace(',','.')),
      mayor_sgi : 0.0,
      mayor_sap : 0.0,
      diferecia_mayores : 0.0,
      ajax_request : true,
      show_expense : false,
      show_order_invoice : false,
      show_taxes : false,
      csrftoken : Cookies.get('csrftoken'),
    },
    methods : {    
        select_expense : function(item){
            this.show_expense = true
            this.show_order_invoice  = false
            this.show_taxes = false
            return this.current_expense = item
        },
        contabilized : function(paid){    
            console.log('Envio actualizacion de pago')        
            this.ajax_request = true
            if (paid.paid.bg_mayor){
                paid.paid.bg_mayor = 0
                this.current_expense.legder -= parseFloat(paid.paid.valor)
            }else{
                paid.paid.bg_mayor = 1
                this.current_expense.legder += parseFloat(paid.paid.valor)
            }            
            this.$http.put('{{BASE_URL}}api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {          
                this.ajax_request = false            
                this.updateLedger()
              }, response => {
                alert('Se produjo un error, por favor recargue la página');
              });
        },
        updateLedger: function(){        
            console.log('actualizando mayor')
            var ledger = 0
            for (var x = 0 ; x < (this.order_data.expenses.length);x++){
                var item = this.order_data.expenses[x]
                ledger += parseFloat(item.legder)
            }    

            this.mayor_sgi = 0
            this.mayor_sgi = parseFloat(this.init_ledger) + parseFloat(ledger)
        },
        show_order_invoice_detail : function(){
            this.show_expense = false
            this.show_taxes = false
            this.show_order_invoice = true
            return this.current_order_invoice = this.order_data.order_invoice;
        },
        
        show_origin_expense: function(){
            this.show_expense = false
            this.show_taxes = false
            this.show_order_invoice = false
        },

        show_taxes_detail : function(){
            this.show_expense = false
            this.show_order_invoice = false
            this.show_taxes = true
        },

        get_paid_invoice : function(id_paid){
            this.$http.get('{{BASE_URL}}api/paid-invoice/all/' + id_paid  + '/', {params: {}}).then(response => {          
                this.current_paid = response.data;
              }, response => {
                alert('Se produjo un error, por favor recargue la página');
              });
        }
    },
    mounted() {
            this.$http.get('{{BASE_URL}}pedidos/get_all_data/{{ order.order.nro_pedido }}', {params: {}}).then(response => {          
            this.order_data = response.data.data 
            this.updateLedger()
            this.ajax_request = false 
          }, response => {
            alert('Se produjo un error, por favor recargue la página');
          });
    },
    computed : {
        diff_ledgers : function(){
            return this.mayor_sap - this.mayor_sgi
        },        
    },    
    filters : {
        money(number){
            return(parseFloat(number).toFixed(2))
        },
        int_val(number){
            return(parseInt(number))
        }
    },
  })