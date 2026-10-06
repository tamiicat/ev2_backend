from django.shortcuts import render
from django.urls import reverse_lazy

def inicio(request):
    lista_inicio = [
        {
            'imagen': 'images/invierno.jpg',
            'nombre': 'Destinos Invierno',
            'url': reverse_lazy('temas:tema1'),   
            'texto_boton': 'Visitar',
            'clase_boton': 'btn-visitar',
        },
        {
            'imagen': 'images/verano.jpg',
            'nombre': 'Destinos Verano',
            'url': reverse_lazy('temas:tema2'),    
            'texto_boton': 'Visitar',
            'clase_boton': 'btn-visitar',
        },
    ]

    contexto_inicio = {
            'lista_inicio': lista_inicio, 
        }

    return render(request, 'inicio/inicio.html', contexto_inicio)

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
        'titulo': 'Lugares que Deberías Visitar en Invierno',
        'lista_destinos': lista_destinos_invierno, 
    }
    
    return render(request, 'inicio/tema1.html', contexto_invierno)

def tema2(request):
    lista_destinos_verano = [
            {
                'id': 2,
                'nombre': 'San Pedro de Atacama',
                'texto_boton': 'Comprar viaje',
                'descripcion':'Un destino sorprendente en medio del desierto más árido del mundo. Puedes conocer el Valle de la Luna, géiseres, lagunas altiplánicas y disfrutar de algunos de los cielos más despejados del planeta, ideales para observar las estrellas. Perfecto para quienes buscan aventura, cultura y paisajes diferentes.',
                'precio': 78.156,
                'imagen': 'images/san_pedro_atacama.jpg',
                'clase_boton': 'btn-outline-success',
            },
            {
                'id': 3,
                'nombre': 'Rapa Nui',
                'texto_boton': 'Comprar viaje',
                'descripcion':'Una isla llena de historia, cultura y misterio, famosa por sus enormes moáis. Sus volcanes, playas, cuevas y paisajes naturales se combinan con la fascinante cultura del pueblo Rapa Nui. Es un destino ideal para quienes quieren vivir una experiencia diferente y descubrir una de las culturas más singulares de Chile.',
                'precio': 399.933,
                        'imagen': 'images/rapa_nui.jpg',
                'clase_boton': 'btn-outline-secondary',
            },
    ]
    
    contexto = {
        'titulo': 'Lugares que Deberías Visitar en Verano',
        'lista_elementos': lista_destinos_verano,
    }
    
    return render(request, 'inicio/tema2.html', contexto)
