import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from network.models import User, Electif, Stage, Poste, Mobilite

class Command(BaseCommand):
    help = 'Populate the database with fake users and related data'

    def handle(self, *args, **kwargs):
        new_first_names = ["Lucas", "Sophie", "Emma", "Noah", "Liam", "Mia", "Ethan", "Oliver", "Charlotte", "Amelia", "James", "Benjamin", "Elijah", "Harper", "Avery", "Abigail", "Mason", "Logan", "Ella", "Scarlett",
                           "Nathan", "Adeline", "Zara", "Hugo", "Leo"]
        new_last_names = ["Robinson", "Walker", "Lewis", "Hill", "Scott", "Green", "Adams", "Baker", "Carter", "Evans", "Turner", "Parker", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook",
                          "Howard", "Ward", "Peterson", "Gray", "James"]

        nationalities = ['Français', 'Marocain', 'Burkinabé']
        major = 'Aide à la Décision'
        filiere = 'Industrie 4.0'
        electives = [
            'Gestion des risques', 'Facteurs Humains', 'Finance d\'entreprise'
        ]
        stages_data = [
            ('Ingénieur en Robotique', 'Automatisation industrielle', 'ABB'),
            ('Chef de Projet Éolien', 'Énergie renouvelable', 'EDF Renouvelables'),
            ('Data Scientist', 'Analyse de données', 'BNP Paribas'),
            ('Responsable de la Chaîne Logistique', 'Logistique et distribution', 'Amazon'),
            ('Ingénieur en Intelligence Artificielle', 'Technologie de l\'information', 'Google'),
            ('Directeur de la Production', 'Industrie manufacturière', 'L\'Oréal'),
        ]

        mobilites_data = [
            ('École Centrale Supelec', 'Génie Électrique et Électronique'),
            ('École Centrale Lyon', 'statistiques des financaes')
        ]

        specific_users_count = 24
        specific_nationalities = ['Français', 'Marocain', 'Burkinabé']

        for i in range(specific_users_count):
            first_name = new_first_names[i % len(new_first_names)]
            last_name = new_last_names[i % len(new_last_names)]
            username = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 1000)}"
            email = f"{username}@example.com"
            nationality = specific_nationalities[i % len(specific_nationalities)]
            promotion = str(random.randint(2015, 2021))
            graduation_year = random.randint(2018, 2024)
            graduation_date = timezone.now().replace(year=graduation_year, month=6, day=15).date()  # Graduation date set to June 15th of the graduation year

            user = User.objects.create_user(
                username=username,
                password="12",
                first_name=first_name,
                last_name=last_name,
                email=email,
                user_group="Alumni",
                nationality=nationality,
                promotion=promotion,
                graduation_date=graduation_date,
                phone_number=f"+{random.randint(1000000000, 9999999999)}",
                major=major,
                option=random.choice(['Génie Industriel', 'Data Science et Digitalisation', 'Énergie']),
                filiere=filiere,
                linkedin=f"https://linkedin.com/in/{username}",
                other_links=f"https://github.com/{username}",
                mentoring_1A=True,
                mentoring_2A=True,
                mentoring_3A=True
            )

            # Create all stages for the user
            for stage in stages_data:
                for stage_type in ['PFE', 'Operateur', 'Academique']:
                    Stage.objects.create(
                        user=user,
                        domaine=stage[1],
                        entreprise=stage[2],
                        theme=stage[0],
                        annee=random.randint(2015, 2023),
                        type_stage=stage_type
                    )

            # Assign 'Cesure' stage to the user
            Stage.objects.create(
                user=user,
                domaine=stages_data[0][1],
                entreprise=stages_data[0][2],
                theme=stages_data[0][0],
                annee=random.randint(2015, 2023),
                type_stage='Cesure'
            )

            # Create all postes for the user
            for poste in stages_data:
                Poste.objects.create(
                    user=user,
                    entreprise=poste[2],
                    domaine=poste[1],
                    poste_occupe=poste[0]
                )

            # Create mobilites for the user
            for mobilite in mobilites_data:
                Mobilite.objects.create(
                    user=user,
                    ecole=mobilite[0],
                    filiere=mobilite[1]
                )

            # Create electives for the user
            for elective in electives:
                Electif.objects.create(
                    user=user,
                    type='developper_innover',  # Assuming type is 'developper_innover' for all electives
                    competence=elective
                )

        self.stdout.write(self.style.SUCCESS('Successfully added 24 specific users with all stages, postes, mobilities, electives, and major'))
