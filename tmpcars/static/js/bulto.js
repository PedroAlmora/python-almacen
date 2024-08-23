$(document).ready(function() {
    var productos = [];
    
    // Agregar producto al arreglo
    $('#agregar-producto').click(function() {
        var codigoBarras = $('#codigo-barras').val();
        var productoEncontrado = false;
        $('#tabla-producto tr').each(function() {
            var codigoBarrasProducto = $(this).find('td:eq(1)').text();
            if (codigoBarrasProducto === codigoBarras) {
                var nombreProducto = $(this).find('td:eq(0)').text();
                var cantidad = 1;
                for (var i = 0; i < productos.length; i++) {
                    if (productos[i].nombre === nombreProducto) {
                        productos[i].cantidad++;
                        productoEncontrado = true;
                        break;
                    }
                }
                if (!productoEncontrado) {
                    productos.push({
                        'nombre': nombreProducto,
                        'cantidad': cantidad
                    });
                }
                actualizarTabla();
            }
        });
        $('#codigo-barras').val('');
    });
    
    function actualizarTabla() {
        var html = '';
        $.each(productos, function(index, producto) {
            html += '<tr><td>' + producto.nombre + '</td><td>' + producto.cantidad + '</td></tr>';
        });
        $('#tabla-productos tbody').html(html);
    }
});