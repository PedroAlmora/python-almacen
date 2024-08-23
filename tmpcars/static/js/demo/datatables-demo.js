// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
	 language: {
                "lengthMenu": "Mostar _MENU_ registros",
                "zeroRecords":"No se encontraron resultados",
                "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                "infoEmpty": "Mostrando 0 registros",
                "infoFiltered": "(filtrando de un total de _MAX_ registros)",
                "sSearch": "Buscar:",
                "oPaginate":{
                  "sFirst": "Primero",
                  "sLast": "Ultimo",
                  "sNext": "Siguiente",
                  "sPrevious": "Anterior"
                },
                "sProcessing": "Procesando....",
            },
   responsive: "true",
   dom: "Bfrtilp",
   buttons:[
       {
           extend: 'excelHtml5',
           text:   '<i class="fas fa-file-excel"></i>',
           titleAttr:  'Exportar a Excel',
           className: 'btn btn-success'
       },
       {
           extend: 'pdfHtml5',
           text:   '<i class="fas fa-file-pdf"></i>',
           titleAttr:  'Exportar a PDF',
           className: 'btn btn-danger'
       },
       {
           extend: 'print',
           text:   '<i class="fa fa-print"></i>',
           titleAttr:  'Imprimir',
           className: 'btn btn-info'
       },
   ]
  });
});
