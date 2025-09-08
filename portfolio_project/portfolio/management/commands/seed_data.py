import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from portfolio.models import Service, Project
from django.conf import settings

class Command(BaseCommand):
    help = 'Seeds the database with initial data for services and projects.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        Service.objects.all().delete()
        Project.objects.all().delete()

        self.stdout.write('Creating new services...')
        Service.objects.create(
            title='Développement Web Full-Stack',
            description='Création d\'applications web sur mesure, de la conception à la mise en production, avec Django, React et Next.js.'
        )
        Service.objects.create(
            title='Création Visuelle par IA',
            description='Génération d\'images hyperréalistes et de vidéos publicitaires uniques grâce à des outils d\'IA avancés.'
        )
        Service.objects.create(
            title='Community Management',
            description='Gestion et animation de vos réseaux sociaux pour bâtir et engager votre communauté.'
        )

        self.stdout.write('Creating new projects...')

        # Create a dummy image file in the media directory
        dummy_image_name = 'dummy_project_image.jpg'
        dummy_image_path = os.path.join(settings.MEDIA_ROOT, dummy_image_name)

        # Ensure media directory exists
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        with open(dummy_image_path, 'w') as f:
            f.write('dummy content')

        project1 = Project(
            title='Portfolio V1',
            description='Mon premier site portfolio personnel construit avec Django et HTMX. Une vitrine de mes compétences en développement web et en design.',
            category=Project.Category.WEB_DEVELOPMENT,
            technologies_used='Django, HTMX, TailwindCSS'
        )
        with open(dummy_image_path, 'rb') as f:
            project1.image.save(dummy_image_name, ContentFile(f.read()))

        project2 = Project(
            title='Campagne Publicitaire "Future"',
            description='Une série de visuels futuristes générés par IA pour une marque de technologie innovante, mettant en avant des concepts de produits.',
            category=Project.Category.AI_VISUALS,
            technologies_used='Midjourney, Photoshop'
        )
        with open(dummy_image_path, 'rb') as f:
            project2.image.save(dummy_image_name, ContentFile(f.read()))

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))

        # Clean up dummy file
        os.remove(dummy_image_path)
