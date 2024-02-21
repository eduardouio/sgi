var app = new Vue({
    el: '#app',
    data: {
        ajaxRequest: true,
        file : {
            url:null,
            tipo:null,
            pedido:null,
            parcial:null,
        }
    },
    methods: {
        submitForm: function () {
            alert('Hola Eguardo');
        }
    }
})