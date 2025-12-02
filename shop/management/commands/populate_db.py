import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from shop.models import Category, Product

class Command(BaseCommand):
    help = 'Populate the database with sample data in Spanish'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Populating database with Spanish data...')

        categories = [
            'Electrónica',
            'Libros',
            'Ropa',
            'Hogar',
            'Juguetes'
        ]

        for category_name in categories:
            Category.objects.get_or_create(name=category_name, slug=slugify(category_name))

        products = [
            {'name': 'Teléfono Inteligente', 'description': 'Un teléfono inteligente de última generación con una cámara increíble.'},
            {'name': 'Laptop Portátil', 'description': 'Una laptop ligera y potente para trabajar desde cualquier lugar.'},
            {'name': 'Auriculares Inalámbricos', 'description': 'Auriculares con cancelación de ruido para una experiencia de sonido inmersiva.'},
            {'name': 'Televisor 4K', 'description': 'Un televisor con resolución 4K para ver tus películas y series favoritas.'},
            {'name': 'Novela de Ciencia Ficción', 'description': 'Un emocionante viaje a un futuro distópico.'},
            {'name': 'Libro de Cocina', 'description': 'Aprende a preparar deliciosas recetas de todo el mundo.'},
            {'name': 'Camiseta de Algodón', 'description': 'Una camiseta suave y cómoda para el uso diario.'},
            {'name': 'Pantalones Vaqueros', 'description': 'Unos pantalones vaqueros clásicos que nunca pasan de moda.'},
            {'name': 'Zapatillas Deportivas', 'description': 'Unas zapatillas cómodas y con estilo para hacer deporte o para el día a día.'},
            {'name': 'Sofá de Tres Plazas', 'description': 'Un sofá espacioso y confortable para toda la familia.'},
            {'name': 'Mesa de Centro', 'description': 'Una mesa de centro elegante y funcional para tu salón.'},
            {'name': 'Juego de Sábanas', 'description': 'Un juego de sábanas de algodón suave para un descanso perfecto.'},
            {'name': 'Juego de Construcción', 'description': 'Un juego de construcción para que los niños desarrollen su creatividad.'},
            {'name': 'Muñeca Articulada', 'description': 'Una muñeca con múltiples articulaciones para que los niños puedan jugar sin límites.'},
            {'name': 'Coche de Carreras a Escala', 'description': 'Una réplica a escala de un famoso coche de carreras.'},
            {'name': 'Cámara de Fotos Réflex', 'description': 'Captura momentos inolvidables con esta cámara de alta calidad.'},
            {'name': 'Tableta Gráfica', 'description': 'Ideal para diseñadores y artistas digitales.'},
            {'name': 'El Gran Gatsby', 'description': 'Un clásico de la literatura estadounidense.'},
            {'name': 'Chaqueta de Cuero', 'description': 'Una chaqueta de cuero atemporal para un look rebelde.'},
            {'name': 'Lámpara de Escritorio', 'description': 'Ilumina tu espacio de trabajo con esta moderna lámpara.'},
        ]

        for i, product_data in enumerate(products):
            category = Category.objects.order_by('?').first()
            product_name = product_data['name']
            product_slug = slugify(product_name)
            product_description = product_data['description']
            product_price = round(random.uniform(10, 500), 2)
            
            # Check if slug is unique, if not, append a number
            original_slug = product_slug
            counter = 1
            while Product.objects.filter(slug=product_slug).exists():
                product_slug = f'{original_slug}-{counter}'
                counter += 1

            Product.objects.create(
                category=category,
                name=product_name,
                slug=product_slug,
                description=product_description,
                price=product_price,
            )

        self.stdout.write(self.style.SUCCESS('¡La base de datos se ha poblado con éxito!'))