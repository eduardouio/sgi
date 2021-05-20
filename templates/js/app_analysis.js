var app = new Vue({
    el : '#app',
    delimiters : ['${','}'],
    data:{
        all_data : data,
        select_row : null,
        current_item: null,
        selected_item: false,
    }, methods: {
        // Selecciona la informacion de un registro para mostrarlo
        selectItem(id){
            console.log(`Se selecciona el item ${id}`);
            this.selected_item = true;
            this.current_item = this.all_data[id];
        }
    },
    filters:{
        number(val) {
            let = new_val = parseFloat(val);
            return (parseInt(new_val * 100) / 100);
        }, 
        int(val){
            return parseInt(val);
        }
    }
});