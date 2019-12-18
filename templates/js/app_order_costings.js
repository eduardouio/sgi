/**
 * Modulo de liquidacion de pedido 
 * 
 * Eduardo Villota (2019) <eduardouio7@gmail.com>
 */
var app = new Vue({
  el: '#app',
  delimiters: ['${', '}'],
  data: {
    ajax_request : true,
    complete_order_info: {},  
    nro_order : '{{ data.complete_order_info.order }}',
    current_order_invoice : {},
    csrftoken : Cookies.get('csrftoken'),
    liquidated_order : Boolean(parseInt('{{ data.complete_order_info.order.bg_isclosed }}')),
    show_form_liquidated : false,
    show_ice_reliquidated : false,
    show_ice_reliquidated_mayor : false,
    current_expense : null,
    show_expense : false,
    show_costings : false,
    current_paid : null,
    comentarios : '',
    show_order_invoice : false,
    show_origin_expense : false,
    show_liquidate_btn : false,
    show_liquidate_confirm_btn : false,
    diff_ledgers : 0,
    ice_reliquidado : {
      expense : 'ICE ADVALOREM RELIQUIDADO',
      provision : parseFloat('{{ data.ice_reliquidado.provision }}'),
      invoiced_value : 0,
      legder : 0,
    },
    show_taxes : false,
    current_ledger : {
      'tipo' : 'pedido',
      'nro_pedido' : '{{ data.complete_order_info.order.nro_pedido }}',
      'id_parcial' : 0,
      'costo_inicial_producto' : parseFloat('{{ data.complete_order_info.order_invoice.totals.value_tct | round(3) }}'),
      'costo_producto' : parseFloat('{{ data.complete_order_info.order_invoice.totals.value_tct | round(3) }}'),
      'facturas_sgi' : parseFloat('{{ data.facturas_sgi | round(3) }}'),
      'provisiones_sgi' : parseFloat('{{ data.provisiones_sgi | round(3) }}'),
      'reliquidacion_ice' : parseFloat('{{ data.reliquidacion_ice | round(2)}}'),
      'saldo_producto' : parseFloat('{{ data.saldo_producto | round(3) }}'),
      'mayor_sap' : parseFloat('{{ data.complete_order_info.order.saldo_mayor }}'),
      'mayor_sgi' : 0,
      'precio_entrega' : parseFloat('{{ data.costings.sums.prorrateos_total | round(3) }}'),
    },
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
      this.$http.put('{{ data.host }}api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
          this.updateLedger()
        }, response => {
          console.dir(response)
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
    var legder_value = (this.complete_order_info.init_ledger + this.complete_order_info.origin_expenses_tct)
    /** sumamos los gastos iniciales */
    this.complete_order_info.expenses.forEach((k,v)=>{
        legder_value += k.legder
    })
    console.log('sumamos la reliquidacion del ice')
    console.log('pendiente')
    this.diff_ledgers = Math.abs((this.current_ledger.mayor_sap - legder_value).toFixed(3))
    return this.current_ledger.mayor_sgi = legder_value.toFixed(3)
  },
    showOrderInvoice : function(){
      console.log('mostrando factura del pedido')
      this.show_order_invoice = true
      this.show_expense = false
      this.show_taxes = false
      this.show_origin_expense = false
      this.current_order_invoice = this.complete_order_info.order_invoice
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
    showTaxes : function(){
      console.log('Mostrando los impuestos del parcial')
      this.show_expense = false
      this.show_origin_expense = false
      this.show_order_invoice = false
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
      this.$http.put('{{ data.host }}api/paid-invoice-detail/update/' + paid.paid.id_detalle_documento_pago + '/', 
            paid.paid, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {
            console.log('pago actualizado')
            console.dir(response)
          this.updateLedger()
        }, response => {
          alert('Se produjo un error, por favor recargue la página');
          console.dir(response)
        });
  },
  get_paid_invoice : function(id_paid){
    this.$http.get('{{ data.host }}api/paid-invoice/all/' + id_paid  + '/', {params: {}}).then(response => {          
        this.current_paid = response.data;
      }, response => {
        alert('Se produjo un error, por favor recargue la página');
        console.dir(response)
      });
},
  updateOrder : function(){
    console.log('Actualizamos el pedido para retistrar el valor del mayor')
    var my_order = {
      nro_pedido : '{{ data.nro_order }}',
      flete_aduana : '{{ data.complete_order_info.order.flete_aduana }}',
      incoterm : '{{ data.complete_order_info.order.incoterm }}',
      seguro_aduana : '{{ data.complete_order_info.order.seguro_aduana }}',
      saldo_mayor : this.current_ledger.mayor_sap,
    }
    this.$http.put('{{ data.host }}api/order/update/{{ data.nro_order }}/', my_order, { 
      headers : {"X-CSRFToken":this.csrftoken}}).then(response=>{
        console.log('saldo de mayor actualizado')
        console.dir(response)
      },response=>{
        console.log('No fue posible actualizar el pedido')
        console.dir(response)
        alert('Hubo un error actualizando el saldo del Mayor')
      })
  },
  liquidateOrder : function(){
    console.log('Iniciamos la liquidacion del pedido')
    this.show_liquidate_confirm_btn = false
    this.show_liquidate_btn = false
    this.liquidated_partial = true
    this.complete_order_info.order.bg_isclosed = 1 
    this.complete_order_info.order.notas_cierre += this.comentarios 
    console.dir(this.complete_order_info)
    this.$http.post('{{ data.host }}api/ledger/create/', this.current_ledger, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {
      console.log('Mayor Registrado correctamente')
      this.$http.put('{{ data.host }}api/order/update/{{data.complete_order_info.order}}/', this.complete_order_info.order, {headers: {"X-CSRFToken":this.csrftoken }} ).then(response => {                     
        alert('pedido {{ data.nro_order }} se liquido Correctamente 😄 [Status:Cerrado]')
        console.log('[debug] pedido cerrado correctamente')
        this.order_close = true
        this.show_form_liquidated = false
        window.print()
      }, response => {
        console.log('Error en la solicitud')
        console.dir(response)
        alert('No es posible conectarse al servidor');
      });
    }, response => {
      console.dir(response)
      alert('Se produjo un error, por favor recargue la página');
    });
    },
  },
  mounted() {
    this.$http.get('{{ data.host }}api/order/all-data/{{ data.complete_order_info.order.nro_pedido }}', { params: {}}).then(response => {
    this.complete_order_info = response.body
    this.ajax_request = false    
    this.updateLedger()
  }, response => {
    alert('Ocurrio un error al cargar la aplicacion, por recargue la pagina')
    console.dir(response)
  });
},
filters : {
  money : function(number){
    return parseFloat(number).toFixed(2)
  },
  int_val : function(number){
    return parseInt(number)
  }}
})