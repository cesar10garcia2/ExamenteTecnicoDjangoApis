# ExamenteTecnicoDjangoApis
Apis de una tienda online, para registrar pedidos y consultar cosas

#APIS

/pedidos/api/obtener_productos

/pedidos/api/obtener_categorias

/pedidos/api/obtener_productos/{producto_id}

# JSOM PARA REGISTRAR LOS PEDIDOS
/pedidos/api/guardar_pedido
# ESTRUCTURA PARA ENVIAR A LA API


    {
    
        "cliente": {
            "nombre" : "Cesar",
            "celular" : "898989",
            "direccion":"sullana"
        },
        
        "detalle": [
            {
                "producto": 1,
                "cantidad" : "2",
                "precio_unitario" : "2",
                "sub_total":"4"
            },
            {
                "producto": 2,
                "cantidad" : "2",
                "precio_unitario" : "2",
                "sub_total":"4"
            }
        ]
    }