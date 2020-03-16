/**
 * Modulo de muestra de costos de parcial 
 * 
 * Eduardo Villota (2019) <eduardouio7@gmail.com> 
 */
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
      liquidated_partial : Boolean(parseInt('{{ data.current_partial.partial.bg_isclosed }}')),
      current_selected_partial : null,
      current_paid : null,
      comentarios : '',
      have_ice_reliquidated : Boolean(parseInt('{{ data.have_ice_reliquidated}}')),
      ice_reliquidado : {
          expense : 'ICE ADVALOREM RELIQUIDADO',
          provision : parseFloat('{{ data.ice_reliquidado.provision }}'),
          invoiced_value : 0,
          legder : 0,
      },
      show_expense : false,
      show_costings : false,
      show_order_invoice : false,
      show_origin_expense : false,
      show_ice_reliquidated : false,
      show_ice_reliquidated_mayor : false,
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
        'reliquidacion_ice': parseFloat('{{ data.costings.ice_reliquidado  | round(2) }}'),
        'saldo_producto' : parseFloat('{{ data.saldo_producto | round(3) }}'),
        'mayor_sap' : parseFloat('{{ data.current_partial.partial.saldo_mayor }}'),
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
        this.$http.put('{{ data.host }}api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', 
        paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {
            this.updateLedger()
          }, response => {
            console.dir(response)
            alert('Se produjo un error, por favor recargue la página');
          });
    },

    updateLedger: function(){
          console.log('actualizando mayor')
        if (typeof(this.complete_order_info.expenses) != 'object'){                
          return false
      }
      //Cargamos los costos iniciales
      var legder_value = (this.complete_order_info.init_ledger + this.complete_order_info.origin_expenses_tct)
      console.log('Saldos Productos mas GO -> ' + legder_value )
      /** sumamos los gastos iniciales */
      this.complete_order_info.expenses.forEach((k,v)=>{
          console.log(k.expense.concepto + ' Mayor -> ' + k.ledger + ' Facturado-> ' + k.invoiced_value)
          legder_value += k.legder
      })
      console.log('saldo Gastos iniciales ->' + legder_value)
      // Sumamos los gastos de cada parcial
      this.all_partials.forEach((k,v)=>{
        legder_value += k.taxes.total_pagado
        k.expenses.forEach((key,val)=>{
          console.log(key.expense.concepto + ' Mayor -> ' + key.ledger + ' Facturado -> ' + k.invoiced_value)
          legder_value += key.legder
        })
      })
      console.log('Sumamos reliquidaciones del ICE agreagadas a los mayores')
      $.each(this.all_partials, function(k,v){
          console.log('Sumamos los ices reliquidados de los anteriores parciales')
          if (v.ledger){
            if (v.ledger.bg_mayor){
              legder_value += parseFloat(v.ledger.reliquidacion_ice)
            }
          }else{
            console.error('Parcial no sumado en mayor')
            console.dir(v)
          }
      })

      if (this.current_partial.partial.bg_isclosed === 1){
        if(this.current_partial.ledger.bg_mayor){
          legder_value += parseFloat(this.current_partial.ledger.reliquidacion_ice)
        }
      }
            
      console.log('Saldos Gastos Parcial ->' + legder_value)
      // restamos las descargas de productos
      if (parseInt('{{ data.current_partial_pos }}') > 0){
          console.log('inciando descarga de gastos')
          this.all_partials.forEach((k,v)=>{
            if(k.partial.bg_isclosed === 1){
              legder_value -= parseFloat(k.ledger.costo_producto)
              legder_value -= parseFloat(k.ledger.precio_entrega)
            }})}

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
        console.log('Cambiando de parcial, parcial ' + id + ' activo')
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
        this.show_ice_reliquidated = false
        this.show_ice_reliquidated_mayor = false
      },
      updatePartial: function(){
        //Actualiza el valor del mayor en el parcial
        console.log('Arcualizando parcial')
        var partial = {
          id_parcial : this.current_partial.partial.id_parcial,
          saldo_mayor : this.current_ledger.mayor_sap,
          nro_pedido : this.complete_order_info.order.nro_pedido,
        }

        this.$http.put('{{ data.host }}api/partial/update/' + partial.id_parcial + '/', partial,{
          headers : {"X-CSRFToken":this.csrftoken}}).then(response=>{
              console.log('Salfo del Mayor actualizado')
              console.log(response)
          },err=>{
              console.log('Error actualizando el saldo del mayor')
              console.dir(err)
              alert('Hubo un error actualizando el saldo del Mayor')
          })
      },
      showOrderInvoice : function(){
        console.log('mostrando factura del pedido')
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = true
        this.show_info_invoice = false
        this.show_ice_reliquidated = false
        this.show_ice_reliquidated_mayor = false
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
        this.show_ice_reliquidated_mayor = false
        this.show_ice_reliquidated = false
      },

      showInfoInvoice : function(id_partial){
        console.log('Estamos mostrando una factura informativa')
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_info_invoice = true
        this.show_ice_reliquidated_mayor = false
        this.show_ice_reliquidated = false
        this.current_info_invoice = this.all_partials[id_partial].info_invoice
      },
      showReliquidacionICE : function(){
        console.log('se muestra el gasto de reliquidacion ice')
        this.show_ice_reliquidated = true
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_ice_reliquidated_mayor = false
        this.show_info_invoice = false
      },
      showReliquidacionICEMayor : function(){
        console.log('se muestra el gasto de reliquidacion ice tomada del mayor')
        this.show_ice_reliquidated = false
        this.show_expense = false
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_ice_reliquidated_mayor = true
        this.show_info_invoice = false

      },
      selectExpense : function(item){
        console.log('Seleccionando Gasto', item)
        this.show_expense = true
        this.show_taxes = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_info_invoice = false
        this.show_ice_reliquidated = false
        this.show_ice_reliquidated_mayor = false
        this.current_expense = item
      },
      showTaxes : function(){
        console.log('Mostrando los impuestos del parcial')
        this.show_expense = false
        this.show_origin_expense = false
        this.show_order_invoice = false
        this.show_ice_reliquidated = false
        this.show_ice_reliquidated_mayor = false
        this.show_info_invoice = false
        this.show_taxes = true
      },
      contabilized : function(paid = null, ice_mayor = false){
        if(ice_mayor){
          if (this.current_selected_partial.ledger.bg_mayor){
            this.current_selected_partial.ledger.bg_mayor = 0
          }else{
            this.current_selected_partial.ledger.bg_mayor = 1
          }
          console.log('Contabilizando ice del mayor, de un parcial anterior')
          this.$http.put('{{ data.host }}api/ledger/update/' + this.current_selected_partial.ledger.id_mayor + '/' ,
              {
                id_mayor : this.current_selected_partial.ledger.id_mayor,
                bg_mayor : this.current_selected_partial.ledger.bg_mayor,
                nro_pedido : this.current_selected_partial.ledger.nro_pedido,
                id_parcial : this.current_selected_partial.ledger.id_parcial,
                tipo : this.current_selected_partial.ledger.tipo,
              }, {headers: {"X-CSRFToken":this.csrftoken }}).then(response=>{
                console.log('Se actualiza ledger base de datos')
                console.dir(response)
                this.updateLedger()
              }, response => {
                console.log('Hubo un error actualizando el valor del mayor')
                console.dir(response)
              })
        }else{
          console.log('Envio actualizacion de pago')
        if (paid.paid.bg_mayor){
            paid.paid.bg_mayor = 0
            this.current_expense.legder -= parseFloat(paid.paid.valor)
        }else{
            paid.paid.bg_mayor = 1
            this.current_expense.legder += parseFloat(paid.paid.valor)
        }            
        this.$http.put('{{ data.host }}api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', 
              paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
            this.updateLedger()
          }, response => {
            alert('Se produjo un error, por favor recargue la página');
          });
        }
    },
    get_paid_invoice : function(id_paid){
      this.$http.get('{{data.host }}api/paid-invoice/all/' + id_paid  + '/', {params: {}}).then(response => {          
          this.current_paid = response.data;
        }, response => {
          alert('Se produjo un error, por favor recargue la página');
        });
  },
    liquidatePartial : function(){
      console.log('Liquidando parcial')

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

      this.$http.post('{{ data.host }}api/ledger/create/', this.current_ledger, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {
        this.$http.put('{{ data.host }}api/partial/update/' + partial.id_parcial + '/', partial, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {
          this.partial_close = true
          this.$http.get('{{data.host}}api/order/close/{{data.nro_order}}/',{ headers: { "X-CSRFToken":this.csrftoken}}).then(response=>{
            console.log('Intenando cerrar pedido')
            console.dir(response)
          },response=>{
            alert('No es posible cerrar el pedido')
            console.dir(response)
          });
          window.print()
                  }, response => {
          console.log('Mayor registrado correctamente')
          console.dir(response)
        });
      }, response => {
        console.log('No es posible crear el mayor del parcial')
        console.dir(response)
        alery('No es posible crear el parcial')
      });
      },
      deleteExistingLedger: function (){
        console.log('Intentado eliminar el mayor existente ')
        this.$http.get('{{ data.host }}api/ledger/ledger-exist/' + this.current_ledger.nro_pedido + '/' + this.current_ledger.id_parcial + '/' , { headers: { "X-CSRFToken":this.csrftoken}}).then(response => {
          console.log('resultado de busqueda de parcial')
          console.dir(response)
          if (response.data['exist'] === 1){
              this.$http.delete('{{ data.host }}api/ledger/delete/' + response.data['id_mayor'], { headers: { "X-CSRFToken":this.csrftoken}}).then(response => {
                console.log('Mayor del parcial Eliminado')
                this.liquidatePartial()
              })
          }else{
            console.log('El parcial no tiene registrado un mayor')
            this.liquidatePartial()
          }
        }, response => {
          console.log('Error en comunicaicon http')
          console.dir(response)
          alert('No es posible comunicarse con el servidor')
        })

        return 0;
    },
    },
    mounted() {
      this.$http.get('{{ data.host }}api/order/all-data/{{ data.complete_order_info.order.nro_pedido }}', { params: {}}).then(response => {
      console.log('inicio de proceso recuperar parcial')
      console.dir(response)
      this.complete_order_info = response.body 
      var x = 0
      this.all_partials = []
      response.body.partials.forEach(el => {        
        if (x < parseInt('{{ data.ordinal_partial }}')) {
          this.$http.get('{{ data.host }}api/partial/all-data/' + el.id_parcial + '/',{ params: {}}).then(resp => {
            console.log('obteniendo informacion completa del parcial orinal nro' + x )
            console.dir(resp)
            this.all_partials.unshift(resp.body)
            this.selectPartial()
            this.updateLedger()
            }, err=>{
              console.log('No se puede obtener informacion del parcial ordinal ' + x)
              console.dir(err)
            })
            x=x+1
      }
        })
    }, error => {
      alert('Ocurrio un error al cargar la aplicacion, por recargue la pagina')
      console.log('Error al iniciar la aplicaicon')
      console.dir(error)
    })
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