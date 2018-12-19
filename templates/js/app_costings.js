var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
      order_data: {},
      ajaxRequest : true,
      current_expense : {},
      product_value : parseFloat('{{ order.init_ledger }}'.replace(',','.')),
      mayor_sgi : 0.0,
      mayor_sap : 0.0,
      diferecia_mayores : 0.0,
    },
    methods : {
        get_data: function(){
        axios      
        .get('{{BASE_URL}}pedidos/get_all_data/{{ order.order.nro_pedido }}')
        .then(response => (
            this.order_data = response.data.data
            ))        
        .catch(error=>(allert('Error en peticion')))

        setTimeout(() => {
            this.ajaxRequest = false
        }, 1000);
        },
        select_expense : function(item){
            if (typeof(item) == 'object'){
                return this.current_expense = item
            }
            var order_data = this.order_data
            if (item === 'invoice'){
                var expense = {
                    "sale": 0,
                    "legder":0,
                    "parcial":this.order_data.order_invoice.parcial,
                    "complete":this.order_data.order_invoice.complete,
                    "provision":this.order_data.order_invoice.provision,
                    "paids":[],
                    "invoiced_value": this.order_data.order_invoice.order_invoice_detail_sums.value,
                    "expense":
                    {
                        "id_gastos_nacionalizacion":0,
                        "id_parcial":0,
                        "concepto":"FACTURA PROVEEDOR",
                        "tipo":"PRODUCTO",
                        "valor_provisionado":this.order_data.order_invoice.order_invoice.valor,
                        "fecha": this.order_data.order_invoice.order_invoice.id_factura_proveedor,
                        "nro_pedido":"{{ order.order.nro_pedido }}",
                        "identificacion_proveedor":"0"
                    }                    
                }
                

                this.order_data.order_invoice.order_invoice_detail.forEach(function(el){
                    expense.paids.push({
                        "paid":
                        {
                            "id_detalle_documento_pago":0,
                            "valor": (el.nro_cajas * el.costo_caja) ,
                            "bg_mayor":1,
                            "id_documento_pago":0
                        },
                        "supplier":
                        {
                            "identificacion_proveedor":"0000000000",
                            "nombre": el.product,
                            "categoria":"TRIBUTOS",
                        },
                        "invoice":
                        {
                            "id_documento_pago":0,
                            "nro_factura": order_data.order_invoice.order_invoice.id_factura_proveedor,
                            "fecha_emision": order_data.order_invoice.order_invoice.fecha_emision,                            
                        }
                    }
                )
                })
            return this.current_expense = expense
            }
        
        if (this.order_data.order.regimen === '70'){
            console.log('super Error')
            return {}
        }
        
        var expense = {
            "sale":  0,
            "legder":0  ,
            "parcial":!order_data.taxes.complete,
            "complete":order_data.taxes.complete,
            "provision":false,
            "paids":[
                {
                    "paid":
                    {
                        "id_detalle_documento_pago":0,
                        "valor": order_data.taxes.arancel_advalorem,
                        "bg_mayor":1,
                        "id_documento_pago":0
                    },
                    "supplier":
                    {
                        "identificacion_proveedor":"0000000000",
                        "nombre": 'ARANCEL ADVALOREM',
                        "categoria":"TRIBUTOS",
                    },
                    "invoice":
                    {
                        "id_documento_pago":0,
                        "nro_factura": order_data.taxes.nro_liquidacion,
                        "fecha_emision": order_data.taxes.fecha_liquidacion,                        
                    }
                },
                {
                    "paid":
                    {
                        "id_detalle_documento_pago":0,
                        "valor": order_data.taxes.arancel_especifico ,
                        "bg_mayor":1,
                        "id_documento_pago":0
                    },
                    "supplier":
                    {
                        "identificacion_proveedor":"0000000000",
                        "nombre": 'ARANCEL ESPECIFICO',
                        "categoria":"TRIBUTOS",
                    },
                    "invoice":
                    {
                        "id_documento_pago":0,
                        "nro_factura": order_data.taxes.nro_liquidacion,
                        "fecha_emision": order_data.taxes.fecha_liquidacion,                        
                    }
                },
                {
                    "paid":
                    {
                        "id_detalle_documento_pago":0,
                        "valor": order_data.taxes.fondinfa ,
                        "bg_mayor":1,
                        "id_documento_pago":0
                    },
                    "supplier":
                    {
                        "identificacion_proveedor":"0000000000",
                        "nombre": 'FONDINFA',
                        "categoria":"TRIBUTOS",
                    },
                    "invoice":
                    {
                        "id_documento_pago":0,
                        "nro_factura": order_data.taxes.nro_liquidacion,
                        "fecha_emision": order_data.taxes.fecha_liquidacion,                        
                    }
                },
                {
                    "paid":
                    {
                        "id_detalle_documento_pago":0,
                        "valor": order_data.taxes.ice_advalorem ,
                        "bg_mayor":1,
                        "id_documento_pago":0
                    },
                    "supplier":
                    {
                        "identificacion_proveedor":"0000000000",
                        "nombre": 'ICE ADVALOREM',
                        "categoria":"TRIBUTOS",
                    },
                    "invoice":
                    {
                        "id_documento_pago":0,
                        "nro_factura": order_data.taxes.nro_liquidacion,
                        "fecha_emision": order_data.taxes.fecha_liquidacion,                        
                    }
                },
                {
                    "paid":
                    {
                        "id_detalle_documento_pago":0,
                        "valor": order_data.taxes.ice_especifico ,
                        "bg_mayor":1,
                        "id_documento_pago":0
                    },
                    "supplier":
                    {
                        "identificacion_proveedor":"0000000000",
                        "nombre": 'ICE ESPECIFICO',
                        "categoria":"TRIBUTOS",
                    },
                    "invoice":
                    {
                        "id_documento_pago":0,
                        "nro_factura": order_data.taxes.nro_liquidacion,
                        "fecha_emision": order_data.taxes.fecha_liquidacion,                        
                    }
                },
            ],
            "invoiced_value": order_data.taxes.total_pagado,
            "expense":
            {
                "id_gastos_nacionalizacion":0,
                "id_parcial":0,
                "concepto":"TRIBUTOS SENAE",
                "tipo":"IMPUESTOS",
                "valor_provisionado":order_data.taxes.total_provisionado,
                "fecha": order_data.taxes.fecha_liquidacion,
                "nro_pedido":"{{ order.order.nro_pedido }}",
                "identificacion_proveedor":"0"
            }                    
        }
        return this.current_expense = expense
        },
    contabilized : function(paid){
        console.log('envia a actualizar pago')
        if (paid.paid.bg_mayor){
            paid.paid.bg_mayor = 0
            this.mayor_sgi -= parseFloat(paid.paid.valor)
            this.current_expense.legder -= parseFloat(paid.paid.valor)
        }else{
            paid.paid.bg_mayor = 1
            this.mayor_sgi += parseFloat(paid.paid.valor)
            this.current_expense.legder += parseFloat(paid.paid.valor)
        }
    },    
    },
    created: function() {
        this.get_data()
    },
    computed : {
        diff_ledgers : function(){
            return this.mayor_sap - this.mayor_sgi
        }
    },    
    filters : {
        money(number){
            return(parseFloat(number).toFixed(2))
        }
    },
  })