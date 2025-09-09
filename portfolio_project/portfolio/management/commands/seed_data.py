from django.core.management.base import BaseCommand
from portfolio.models import Service, Project, Article, HeroSection
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seeds the database with initial text data.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        Service.objects.all().delete()
        Project.objects.all().delete()
        Article.objects.all().delete()
        HeroSection.objects.all().delete()

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

        self.stdout.write('Creating new articles...')
        try:
            author = User.objects.get(username='admin')
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Admin user not found. Please create a superuser named "admin" first.'))
            return

        Article.objects.create(
            title='Les Clés d\'une Identité Visuelle Réussie avec l\'IA',
            author=author,
            content='Découvrez comment l\'intelligence artificielle peut transformer votre branding...'
        )
        Article.objects.create(
            title='Django & HTMX : Le Duo Gagnant pour des Sites Modernes',
            author=author,
            content='Pourquoi la combinaison de Django pour le backend et HTMX pour le frontend est si puissante...'
        )
        Article.objects.create(
            title='Mon Top 5 des Outils IA pour la Création de Contenu',
            author=author,
            content='Un aperçu des outils qui ont changé ma façon de travailler...'
        )
        Article.objects.create(
            title='Un Quatrième Article pour Tester la Pagination',
            author=author,
            content='Cet article sert à vérifier que la pagination sur la page du blog fonctionne correctement.'
        )

        self.stdout.write('Creating hero section...')
        HeroSection.objects.create(
            title='Azeez Ridwan – <span class="text-indigo-600 dark:text-indigo-400">Développeur Full-Stack</span> & Créateur de Visuels Publicitaires <span class="text-purple-600 dark:text-purple-400">Hyperréalistes</span>',
            subtitle='Je transforme vos idées en expériences digitales et visuelles uniques.'
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with text content.'))
