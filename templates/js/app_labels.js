var app = new Vue({
  el: "#app",
  delimiters: ["${", "}"],
  data: {
    order_data: data,
    current_product: null,
    current_lables: [],
    is_completed: false,
    is_closed: true,
    show_detail_range: false,
    new_range: {
      id_factura_detalle: null,
      initial_range: null,
      end_range: null,
      quantity: null,
      parcial: null,
      notas: null,
    },
    csrftoken: Cookies.get("csrftoken"),
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
    validateRange: function () {
      console.log("realizamos la validacion de los rangos");
      console.dir(this.new_range);
    },
    getRangesLabels: function (id_factura_detalle){
      this.current_lables = [];
      labels = null

      url = host.trim() + "api/labels/from-id-invoice/" + id_factura_detalle + "/";
      this.$http.get(url, {params:{}}).then(
        response => {
        labels = response.body;
        this.current_lables = labels;
      },reponse=>{
        alert('Error al obtener las etiquetas');
      });
      
    },
    checkOrderLabels: function () {
      console.log("revisamos el estado de las etiquetas " + id);
    },
    addRange: function () {
      console.log("agregando un nuevo rango");
      url = host.trim() + "api/labels/create/";
      console.log(url);
      this.$http
        .post(url, this.new_range, {
          headers: { "X-CSRFToken": this.csrftoken },
        })
        .then(
          (response) => {
            console.log("respuesta de la peticion");
            console.dir(response);
            location.reload();
          },
          (response) => {
            console.log("error de la peticion");
            alert("Error al ingresar las etiquetas" + response);
            console.dir(response);
          }
        );
    },
    mounted() {
      console.log("Iniciamos aplicacion de etiquetado");
      this.checkOrderLabels();
    },
  },
  properties: {
    csrftoken: Cookies.get("csrftoken"),
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
