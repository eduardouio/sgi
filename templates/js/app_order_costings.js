var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
      order_data: {},
      comentarios : '',
      liquidated_order : false,
      current_expense : null,
      current_order_invoice : {},
      current_taxes: {},
      current_paid : null,
      init_ledger : parseFloat('{{ data.init_ledger }}'.replace(',','.')),      
      diferecia_mayores : 0.0,
      nro_order : '{{ data.order }}',
      ajax_request : true,
      show_costings : false,
      show_expense : false,
      show_order_invoice : false,
      show_taxes : false,
      show_form_liquidated : false,
      systems_ledger : "{{ data.ledger if data.ledger else  'false' }}",
      current_ledger : {
        'tipo' : 'inicial',
        'nro_pedido' : '{{ data.order.nro_pedido }}',
        'id_parcial' : 0,
        'costo_producto' : parseFloat('{{ data.order_invoice.order_invoice.valor_tasa_trimestral }}'),
        'facturas_sgi' : parseFloat('{{ data.total_invoiced }}'.replace(',','.')),
        'mayor_sap' : 0,
        'mayor_sgi' : 0,
        'precio_entrega' : parseFloat('{{ data.costs.sums.indirectos }}'.replace(',','.')),
        'provisiones_sap' : 0,
        'provisiones_sgi' : parseFloat('{{ data.total_provisions }}'.replace(',','.')),
        'reliquidacion_ice' : parseFloat('{{ data.costs.sums.ice_advalorem_reliquidado }}'.replace(',','.')),
      },
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
            if (paid.paid.bg_mayor){
                paid.paid.bg_mayor = 0
                this.current_expense.legder -= parseFloat(paid.paid.valor)
            }else{
                paid.paid.bg_mayor = 1
                this.current_expense.legder += parseFloat(paid.paid.valor)
            }            
            this.$http.put(host + host+'api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
                this.updateLedger()
              }, response => {
                alert('Se produjo un error, por favor recargue la página');
              });
        },

        updateLedger: function(){
            console.log('actualizando mayor')
            if (typeof(this.order_data.expenses) != 'object'){                
                console.log('[Debug] El pedido no tiene gastos')
                return false
            }
            var ledger = 0
            for (var x = 0 ; x < (this.order_data.expenses.length);x++){
                var item = this.order_data.expenses[x]
                ledger += parseFloat(item.legder)
            }    
            this.current_ledger.mayor_sgi = 0
            this.current_ledger.mayor_sgi = Math.round((parseFloat(this.init_ledger) + parseFloat(ledger))*100)/100
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
            this.$http.get(host+'api/paid-invoice/all/' + id_paid  + '/', {params: {}}).then(response => {          
                this.current_paid = response.data;
              }, response => {
                alert('Se produjo un error, por favor recargue la página');
              });
        },

        liquidate_order : function(){
            var ledger_is_registered = false
            var order_is_registered = false
            this.liquidated_order = true
            this.show_form_liquidated = false
            console.log('Registrando Mayor...')
            this.$http.post(host+'api/ledger/create/', this.current_ledger, {headers: {"X-CSRFToken":this.csrftoken}} ).then(response => {                     
                console.log('Mayor registrado correctamente en base de datos')
                ledger_is_registered = true
            }, response => {
              alert('Se produjo un error, por favor recargue la página');
            });

            this.order_data.order.observaciones +=  this.comentarios
            this.order_data.order.bg_isclosed = 1
            console.log('Actualizando Pedido...')
            this.$http.put(host + 'api/order/update/{{ data.order.nro_pedido}}/', this.order_data.order, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
                console.log('Pedido Actualizado correntamente, iniciando redireccionamiento')
                alert('Que belleza!')
                order_is_registered = true         
              }, response => {
                alert('Se produjo un error, por favor recargue la página');
              });                       
        },
    },
    mounted() {
            this.$http.get( 'http://localhost:8000/api/order/all-data/{{ data.order.nro_pedido }}/', {params: {}}).then(response => {          
            this.order_data = response.body 
            this.ajax_request = false
            this.updateLedger()
          }, response => {
            alert('Se produjo un error, por favor recargue la página');
          });
    },
    computed : {
        diff_ledgers : function(){
            return Math.round((this.current_ledger.mayor_sap - this.current_ledger.mayor_sgi) *100)/100
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
