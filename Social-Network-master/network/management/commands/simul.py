import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from network.models import User, Electif, Stage, Poste, Mobilite

class Command(BaseCommand):
    help = 'Add specific users BELEM Moussa and DALLO Alidou'

    def handle(self, *args, **kwargs):
        # Specific users to add
        specific_users = [
            {
                "first_name": "BELEM",
                "last_name": "Moussa",
                "username": "belem.moussa",
                "email": "belem.moussa@example.com",
                "nationality": "Burkinabé",
                "promotion": "2022",
                "graduation_date": timezone.now().replace(year=2022, month=6, day=15).date(),
                "phone_number": "+22670000000",
                "major": "Intelligence Artificielle",
                "option": "Data Science et Digitalisation",
                "filiere": "Industrie 4.0",
                "linkedin": "https://linkedin.com/in/belem.moussa",
                "other_links": "https://github.com/belem.moussa",
                "mentoring_1A": True,
                "mentoring_2A": True,
                "mentoring_3A": True
            },
            {
                "first_name": "DALLO",
                "last_name": "Alidou",
                "username": "dallo.alidou",
                "email": "dallo.alidou@example.com",
                "nationality": "Burkinabé",
                "promotion": "2022",
                "graduation_date": timezone.now().replace(year=2022, month=6, day=15).date(),
                "phone_number": "+22670000001",
                "major": "Intelligence Artificielle",
                "option": "Data Science et Digitalisation",
                "filiere": "Industrie 4.0",
                "linkedin": "https://linkedin.com/in/dallo.alidou",
                "other_links": "https://github.com/dallo.alidou",
                "mentoring_1A": True,
                "mentoring_2A": True,
                "mentoring_3A": True
            }
        ]

        for user_data in specific_users:
            user = User.objects.create_user(
                username=user_data["username"],
                password="12",
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                user_group="Alumni",
                nationality=user_data["nationality"],
                promotion=user_data["promotion"],
                graduation_date=user_data["graduation_date"],
                phone_number=user_data["phone_number"],
                major=user_data["major"],
                option=user_data["option"],
                filiere=user_data["filiere"],
                linkedin=user_data["linkedin"],
                other_links=user_data["other_links"],
                mentoring_1A=user_data["mentoring_1A"],
                mentoring_2A=user_data["mentoring_2A"],
                mentoring_3A=user_data["mentoring_3A"]
            )

            Poste.objects.create(
                user=user,
                entreprise='Onea',
                domaine='Intelligence Artificielle',
                poste_occupe='Ingénieur en Intelligence Artificielle'
            )

            Mobilite.objects.create(
                user=user,
                ecole='École Centrale',
                filiere='Industrie 4.0'
            )

            Electif.objects.create(
                user=user,
                type='concevoir_rechercher',
                competence='Introduction à la cyber Sécurité'
            )

        self.stdout.write(self.style.SUCCESS('Successfully added BELEM Moussa and DALLO Alidou'))
