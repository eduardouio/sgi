var app = new Vue({
  el: "#app",
  delimiters: ["${", "}"],
  data: {
    order_data: data,
    current_product: null,
    current_lables: [],
    new_range: {
      id_factura_detalle: null,
      initial_range: null,
      end_range: null,
      quantity: null,
      parcial: null,
      notas: null,
    },
    batch_number: null,
    response_range: null,
    total_labels: parseInt("{{data.order_data.units | round(0)}}"),
    is_direct_order: false,
    csrftoken: Cookies.get("csrftoken"),
    error_message: "",
    is_completed: false,
    is_closed: true,
    is_loading: false,
    show_error_message: false,
    show_detail_range: false,
    show_response_message: false,
    show_add_range_button:false,
    show_warning_simbol:false,
  },
  methods: {
    selectProduct: function (id) {
      console.log("obteneinedo etiquetas de los productos seleccionados" + id);
      details = this.order_data["oder_invoice_details"];
      current_product = null;
      details.forEach(function (item) {
        console.log(id === item.cod_contable);
        if (item.cod_contable === id) {
          current_product = item;
        }
      });
      this.current_product = current_product;
      this.new_range.cod_contable = current_product.cod_contable;
      this.new_range.unities = 0;
      this.new_range.id_factura_detalle =
        current_product.detalle_pedido_factura;
      this.getRangesLabels(current_product.detalle_pedido_factura);
    },
    validFormRangeData: function (form_data) {
      this.show_error_message = false;
      this.error_message = "";
      this.show_add_range_button = false;
      let is_valid = true;
      const checkArray = Object.entries(form_data).map(([key, value]) => {
        if (key != "notas") {
          if (value === null || value === "") {
            console.log(key);
            is_valid = false;
          }
        }
      });

      if (!is_valid) {
        this.show_error_message = true;
        this.error_message =
          "Todos los campos son obligatorios, complete la información e intente nuevamente";
      }
      return is_valid;
    },
    validateRange: function () {
      console.log("realizamos la validacion de los rangos");
      let = valid_form_data = this.validFormRangeData(this.new_range);
      if (!valid_form_data) {
        return false;
      }
      this.is_loading = true;
      let url =
        host.trim() +
        `api/labels/validate-range/${this.new_range.initial_range}/${this.new_range.end_range}/${this.new_range.quantity}/`;
      this.$http.get(url).then(
        (response) => {
          this.show_response_message = true;
          this.is_loading = false;
          this.show_add_range_button = true;

          this.response_range = response.body;
          this.new_range.initial_range = this.response_range.first_tag;
          this.new_range.end_range = this.response_range.last_tag;
          this.show_warning_simbol = response.body.concordance;
          if (response.body.difference > 10) {
            this.show_error_message = true;
            this.error_message = 'La diferencia entre los rangos es muy grande, por favor verifique la información';
            this.show_add_range_button = false;
          }
        },
        (error) => {
          alert("Error en Servidor");
          console.dir(error);
          this.is_loading = false;
        }
      );
    },
    validateBatch: function () {
      this.is_loading = true;
      console.log('Validamos el Lote');
      if ((this.batch_number == null || this.batch_number == '')
      &&
      ( this.new_range.parcial == null || this.new_range.parcial == '')) {
        this.show_error_message = true;
        this.error_message = 'El número de lote y parcial son obligatorios';
        return false;
      }
      let url = host.trim() + `api/labels/validate-batch/${this.batch_number}/`;
      this.$http.get(url).then(response => {
        this.show_response_message = false;
        this.is_loading = false;
        if (response.body.status =! 500){
          this.new_range.initial_range = response.body.first_tag;
          this.new_range.end_range = response.body.last_tag;
          this.new_range.quantity = response.body.quantity;
          this.response_range.first_tag = response.body.first_tag;
          this.response_range.last_tag = response.body.last_tag;
          this.response_range.quantity = response.body.quantity;
          this.response_range.difference = 0;
          this.response_range.concordance = true;
          this.show_response_message = true;
          this.show_add_range_button = true;
        }else{
          this.show_error_message = true;
          this.error_message = 'Servicio no disponible, intente usar rangos';
          this.is_loading = false;
          this.show_add_range_button = false;
        }
      },(error) => {
        alert("Error en Servidor");
        this.is_loading = false;
        this.show_add_range_button = false;
        console.dir(error);
      });
    },
    getRangesLabels: function (id_factura_detalle) {
      this.current_lables = [];
      labels = null;
      let url =
        host.trim() + "api/labels/from-id-invoice/" + id_factura_detalle + "/";
      this.$http.get(url, { params: {} }).then(
        (response) => {
          labels = response.body;
          this.current_lables = labels;
        },
        (error) => {
          alert("Error al obtener las etiquetas");
          console.dir(error);
        }
      );
    },
    checkOrderLabels: function () {
      console.log("revisamos el estado de las etiquetas ");
    },
    checkOrderType: function () {
      console.log("Verificamos el tipo de pedido");
      if (this.order_data.order.regimen === "10") {
        this.new_range.parcial = 0;
        this.is_direct_order = true;
      }
    },
    deleteRange: function(id_range){
      let result = confirm('¿Desea eliminar el rango?');
      
      if (!result){
        return false;
      }

      let url = host.trim() + `api/labels/delete/${id_range}/`;
      this.$http.delete(
        url,
        {headers: { "X-CSRFToken": this.csrftoken }}
        ).then(response => {
        this.getRangesLabels(this.current_product.detalle_pedido_factura);
      },error => {
        alert("Error en Servidor");
        this.is_loading = false;
      });
    },
    addRange: function () {
      console.log("agregando un nuevo rango");
      url = host.trim() + "api/labels/create/";
      this.$http
        .post(url, this.new_range, {
          headers: { "X-CSRFToken": this.csrftoken },
        })
        .then(
          (response) => {
            console.log("respuesta de la peticion");
            console.dir(response);
            const altBtn = document.getElementById("altCloseButton");
            this.is_completed = false;
            this.is_closed = true;
            this.is_loading = false;
            this.show_error_message = false;
            this.show_detail_range = false;
            this.show_response_message = false;
            this.show_add_range_button = false;
            this.show_warning_simbol = false;
            this.batch_number = null;
            let new_range = {
              id_factura_detalle: null,
              initial_range: null,
              end_range: null,
              quantity: null,
              parcial: null,
              notas: null,
            };
            this.new_range = new_range;
            altBtn.click();
            this.getRangesLabels(this.current_product.detalle_pedido_factura);
            location.reload();
          },
          (response) => {
            console.log("error de la peticion");
            alert("Error al ingresar las etiquetas Uno de los rangos ya se eccuentra registrado");
            console.dir(response);
          }
        );
    },
  },
  mounted() {
    console.log("Iniciamos aplicacion de etiquetado");
    this.checkOrderType();
    this.checkOrderLabels();
  },
  computed: {
    assigned() {
      if(this.current_lables.length == 0){
        return 0;
      }
      let total = 0;
      this.current_lables.forEach(element => {
        total += element.quantity;
      });
      return total;
    },
    pending() {
      return(this.total - this.assigned);
    },
    total(){
      return parseInt(this.current_product.unidades);
    }
  },
  filters: {
    number(val) {
      let = new_val = parseFloat(val);
      return parseInt(new_val * 100) / 100;
    },
    int(val) {
      return parseInt(val);
    },
  },
});
