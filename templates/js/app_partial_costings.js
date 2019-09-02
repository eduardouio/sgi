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
      liquidated_partial : Boolean(parseInt('{{ data.current_partial.partial.bg_isclosed }}')),
      show_costings : false,
      current_paid : null,
      comentarios : '',
      current_selected_partial : null,
      show_order_invoice : false,
      show_origin_expense : false,
      show_liquidate_btn : true,
      show_liquidate_confirm_btn : false,
      diff_ledgers : 0,
      show_taxes : false,
      show_info_invoice : false,
      current_ledger : {
        'tipo' : 'parcial',
        'nro_pedido' : '{{ data.complete_order_info.order.nro_pedido }}',
        'id_parcial' : parseInt('{{ data.current_partial.partial.id_parcial }}'),
        'costo_inicial_producto' : parseFloat('{{ data.complete_order_info.order_invoice.totals.value_tct | round(3) }}'),
        'costo_producto' : parseFloat('{{ data.current_partial.info_invoice.totals.value_tct | round(3) }}'),
        'facturas_sgi' : parseFloat('{{ data.facturas_sgi | round(3) }}'),
        'provisiones_sgi' : parseFloat('{{ data.provisiones_sgi | round(3) }}'),
        'reliquidacion_ice' : parseFloat('{{ data.reliquidacion_ice | round(2)}}'),
        'saldo_producto' : parseFloat('{{ data.saldo_producto | round(3) }}'),
        'mayor_sap' : 0,
        'mayor_sgi' : 0,
        'precio_entrega' : parseFloat('{{ data.costings.sums.prorrateos_total | round(3) }}'),
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
              legder_value -= parseFloat(k.ledger.costo_producto)
              legder_value -= parseFloat(k.ledger.precio_entrega)
              
              //Verificamos si existe reliquidacion de ICE
            var ice_pagado = (
              parseFloat(k.partial.ice_advalorem_pagado )
              + parseFloat(k.partial.ice_especifico_pagado)
              )

              var ice_reliquidado = 0

              k.info_invoice.info_invoice_detail.forEach((idx,val) => {
                ice_reliquidado += parseFloat(idx.ice_advalorem)
                ice_reliquidado += parseFloat(idx.ice_especifico)
              })
              console.log('Calculanfo diferencia de ice ')
              console.log(ice_reliquidado - ice_pagado)
              legder_value += (ice_reliquidado - ice_pagado)
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
        var current_partial = null
        this.all_partials.forEach((key,val)=>{
          if(key.partial.ordinal_parcial === (id +1 )){
            current_partial = key
          }
        })
        this.current_selected_partial = current_partial
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
    liquidatePartial : function(){
      console.log('Llamamos a liquidar el parcial')
      var partial = {
        id_parcial : this.current_partial.partial.id_parcial,
        observaciones : this.current_partial.partial.observaciones += this.comentarios,
        bg_isclosed : 1,
        id_user_cierre : parseInt('{{ data.request.user.id }}'),
        nro_pedido : this.complete_order_info.order.nro_pedido,
      }
      this.show_liquidate_confirm_btn = false
      this.show_liquidate_btn = false
      this.liquidated_partial = true
      
      this.$http.post(host + 'api/ledger/create/', this.current_ledger, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {
        this.$http.put(host + 'api/partial/update/' + partial.id_parcial + '/', partial, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {
          this.partial_close = true
          window.print()
                  }, response => {
          alert(response)
        });
      }, response => {
        console.log('No es posible crear el parcial')
          this.deleteExistingLedger(this.current_ledger)
      });
      
      },
      deleteExistingLedger: function (current_ledger){
        console.log('eliminando mayor existente')
        this.$http.get(host + 'api/ledger/delete-existing/' + current_ledger.nro_pedido + '/' + current_ledger.id_parcial + '/' , { headers: { "X-CSRFToken":this.csrftoken}}).then(response => {
          console.log('Mayor eliminado correctamennte')
          this.liquidatePartial()
        }, response => {
          console.log('No se puede elimiar un mayor que no existe')
          alert('Error interno consulte con soporte, [msg] -> El mayor que intenta eliminar no existe')
        })
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