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
      current_info_invoice : {},
      csrftoken : Cookies.get('csrftoken'),
      current_expense : null,
      show_expense : false,
      show_costings : false,
      current_paid : null,
      current_selected_partial : null,
      show_order_invoice : false,
      show_origin_expense : false,
      diff_ledgers : 0,
      show_taxes : false,
      show_info_invoice : false,
      current_ledger : {
        'tipo' : 'parcial',
        'nro_pedido' : '{{ data.complete_order_info.order.nro_pedido }}',
        'id_parcial' : parseInt('{{ data.current_partial.partial.id_parcial }}'),
        'costo_inicial_producto' : parseFloat('{{ data.complete_order_info.order_invoice.totals.value_tct }}'),
        'costo_producto' : parseFloat('{{ data.current_partial.info_invoice.totals.value_tct }}'),
        'saldo_producto' : 0,
        'facturas_sgi' : 0,
        'provisiones_sgi' : 0,
        'mayor_sap' : 0,
        'mayor_sgi' : 0,
        'precio_entrega' : 0,
        'provisiones_sap' : 0,
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
        this.$http.put(host + 'api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
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
      //Cargamos los costos iniciales
      var descargas = 0
      var legder_value = (this.complete_order_info.init_ledger + this.complete_order_info.origin_expenses_tct)
      /** sumamos los gastos iniciales */
      this.complete_order_info.expenses.forEach((k,v)=>{
          legder_value += k.legder
      })
      
      // Sumamos los gastos de cada parcial
      this.all_partials.forEach((k,v)=>{
        legder_value += k.taxes.total_pagado
        k.expenses.forEach((key,val)=>{
          legder_value += key.legder
        })
      })      

      // restamos las descargas de productos
      if (parseInt('{{ data.current_partial_pos }}') > 0){
          console.log('inciando descarga de gastos')
          this.all_partials.forEach((k,v)=>{
            if(k.partial.bg_isclosed === 1){
                alert('Implementar esta seccion en el segundo parcial')
            }
          })
      }
      this.diff_ledgers = Math.abs((this.current_ledger.mayor_sap - legder_value).toFixed(3))
      return this.current_ledger.mayor_sgi = legder_value.toFixed(3)
    },
      selectPartial : function(){
        console.log('Marcando Parcial {{data.current_partial_pos + 1 }} como activo')
        if ((this.current_partial === null) && (this.all_partials.length === parseInt('{{ data.ordinal_partial }}'))){
          this.current_partial = this.all_partials[parseInt('{{ data.current_partial_pos }}')]
          this.ajax_request = false
        }
      },
      changePartial : function(id){
        this.current_selected_partial = this.all_partials[id]
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_info_invoice = false

      },
      showOrderInvoice : function(){
        console.log('mostrando factura del pedido')
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = true
        this.show_info_invoice = false
        this.current_order_invoice = this.complete_order_info.order_invoice
        return true
      },

      showOriginExpense : function(){
        console.log('Mostrando Gastos en Origen')
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = true
        this.show_order_invoice = false
        this.show_info_invoice = false
      },

      showInfoInvoice : function(id_partial){
        console.log('Estamos mostrando una factura informativa')
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_info_invoice = true
        this.current_info_invoice = this.all_partials[id_partial].info_invoice
      },

      selectExpense : function(item){
        console.log('Seleccionando Gasto', item)
        this.show_expense = true
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_info_invoice = false
        this.current_expense = item
      },
      showTaxes : function(){
        console.log('Mostrando los impuestos del parcial')
        this.show_expense = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_info_invoice = false
        this.show_taxes = true
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
        this.$http.put(host + 'api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
            this.updateLedger()
          }, response => {
            alert('Se produjo un error, por favor recargue la página');
          });
    },
    get_paid_invoice : function(id_paid){
      this.$http.get(host + 'api/paid-invoice/all/' + id_paid  + '/', {params: {}}).then(response => {          
          this.current_paid = response.data;
        }, response => {
          alert('Se produjo un error, por favor recargue la página');
        });
  },
    },
    mounted() {
      this.$http.get(host + 'api/order/all-data/{{ data.complete_order_info.order.nro_pedido }}', { params: {}}).then(response => {
      this.complete_order_info = response.body 
      var x = 0
      response.body.partials.forEach(el => {        
        if (x < parseInt('{{ data.ordinal_partial }}')) {
          this.$http.get(host + 'api/partial/all-data/' + el.id_parcial + '/',{ params: {}}).then(resp => {
          this.all_partials.unshift(resp.body)
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