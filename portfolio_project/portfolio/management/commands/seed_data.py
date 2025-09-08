from django.core.management.base import BaseCommand
from portfolio.models import Service, Project

class Command(BaseCommand):
    help = 'Seeds the database with initial text data for services and projects. Images can be added manually via the admin panel.'

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

        self.stdout.write('Creating new projects (without images)...')
        Project.objects.create(
            title='Portfolio V1',
            description='Mon premier site portfolio personnel construit avec Django et HTMX. Une vitrine de mes compétences en développement web et en design.',
            category=Project.Category.WEB_DEVELOPMENT,
            technologies_used='Django, HTMX, TailwindCSS',
        )
        Project.objects.create(
            title='Campagne Publicitaire "Future"',
            description='Une série de visuels futuristes générés par IA pour une marque de technologie innovante, mettant en avant des concepts de produits.',
            category=Project.Category.AI_VISUALS,
            technologies_used='Midjourney, Photoshop',
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with text content.'))
