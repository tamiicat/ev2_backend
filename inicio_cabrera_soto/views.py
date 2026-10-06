from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio/inicio.html')

def tema1(request):
    lista_destinos_invierno = [
        {
            'id': 1,
            'nombre': 'Parque Nacional Congüillío',
            'texto_boton': 'Comprar viaje',
            'descripcion': 'Un destino ideal para quienes buscan naturaleza, bosques y paisajes volcánicos. Destaca por el volcán Llaima, sus lagos, araucarias milenarias y senderos rodeados de impresionantes paisajes. Es perfecto para hacer trekking, fotografía y disfrutar de la tranquilidad de la naturaleza.',
            'precio': 24.999,
            'imagen': 'images/parque_conguillio.jpeg',
            'clase_boton': 'btn-outline-primary',
        },
        {
            'id': 2,
            'nombre': 'Torres del Paine',
            'texto_boton': 'Comprar viaje',
            'descripcion': 'Uno de los lugares más emblemáticos de Chile y un imperdible para los amantes de la aventura. Sus enormes montañas, glaciares, lagos de aguas turquesas y las famosas Torres del Paine ofrecen paisajes únicos y experiencias inolvidables. Ideal para trekking y conexión con la naturaleza.',
            'precio': 129.048,
            'imagen': 'images/torres_del_paine.jpg',
            'clase_boton': 'btn-outline-success',
        },
    ]

    contexto_invierno = {
        'titulo': 'Lugares que Deberías Visitar en Invierno - Chile',
        'lista_destinos': lista_destinos_invierno, 
    }
    
    return render(request, 'inicio/tema1.html', contexto_invierno)

