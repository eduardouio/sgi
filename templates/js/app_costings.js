var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
      order_data: {},
      current_expense : {},
      current_order_invoice : {},
      current_taxes: {},
      product_value : parseFloat('{{ order.init_ledger }}'.replace(',','.')),
      mayor_sgi : 0.0,
      mayor_sap : 0.0,
      diferecia_mayores : 0.0,
      ajax_request : true,
      show_expense : false,
      show_order_invoice : false,
      show_taxes : false,
    },
    methods : {    
        select_expense : function(item){
            this.show_expense = true
            this.show_order_invoice  = false
            this.show_taxes = false
            return this.current_expense = item
        },
        contabilized : function(paid){
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
        show_order_invoice_detail : function(){
            this.show_expense = false
            this.show_taxes = false
            this.show_order_invoice = true
            return this.current_order_invoice = this.order_data.order_invoice;
        },
        show_taxes_detail : function(){
            this.show_expense = false
            this.show_order_invoice = false
            this.show_taxes = true
        }
    },
    mounted() {
            this.$http.get('{{BASE_URL}}pedidos/get_all_data/{{ order.order.nro_pedido }}', {params: {}}).then(response => {          
            this.order_data = response.data.data; 
            this.ajax_request = false            
          }, response => {
            alert('Se produjo un error, por favor recargue la página');
          });
    },
    computed : {
        diff_ledgers : function(){
            return this.mayor_sap - this.mayor_sgi
        },
        total_value : function(){
            return 0.00
        },
        total_invoiced : function(){
            return 0.00
        },
        total_sale : function(){
            return 0.00
        },
        total_ledgers : function(){
            return 0
        }
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