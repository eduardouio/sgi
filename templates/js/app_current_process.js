/**
 * aplicaicion de para procesos activos
 * revision y aprobacion de facturas
 */
var app = new Vue({
  el: "#app_current_process",
  delimiters: ["${", "}"],
  data: { },
  methods: {
    updateDateProcess: function(column, id, nro_order){
        console.log(`Actualizando pedido ${id} ${column}`);
        let item_update = document.getElementById(column + '_' +id);
        let date = this.get_date(column);

        if (date === false){
            alert('Seleccione una fecha de la entrada de la cabecera');
            item_update.checked = false;
            return false;
        }

        if (item_update.checked){
            // actualiza la fecha en el server
            console.log(column + "__" + id);
            let resp = this.updateServer(column, date, id, nro_order);
            let cell = document.getElementById(column + '__' + id);
            let date_pos = date.split('-');
            cell.innerHTML = `${date_pos[2]}/${date_pos[1]}/${date_pos[0]}`;
            cell.classList.add('bg-success');
        }
    },
    get_date: function(column){
        console.log('Obtenemos la fecha de la cabecera');
        let date = document.getElementById("date_update");
        if (!date.value){
            return false;
        }
        return date.value
    },
    updateServer: function(column, date, id, nro_order){
        console.log('Enviando actualizacion al server');

        let url = "{{request.enterprise.url_app }}api/order/update/" + id +'/';
        let name_column = 'nro_pedido';

        if(id.search('-') === -1){
            url = "{{request.enterprise.url_app }}api/partial/update/" + id +'/';
            name_column = 'id_parcial';
        }

        let data = {};
        data[name_column] = id;
        data[column] = date;
        data['nro_pedido'] = nro_order;


        this.$http.put(url,
          data,
          { headers: {"X-CSRFToken": '{{ csrf_token}}'}}).then(resp => {
                console.log('Actualizado Correctamente');
                console.dir(resp);
          }, error => {
              console.dir(error);
              alert('Error al procesar la solicitud');
          });
    },
  },
  filters: {
    money: function (val) {
      return parseFloat(val).toFixed(2);
    },
    int: function (val) {
      return parseInt(val);
    },
  },
});