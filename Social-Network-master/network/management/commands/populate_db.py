import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from network.models import User, Electif, Stage, Poste, Mobilite

class Command(BaseCommand):
    help = 'Populate the database with fake users and related data'

    def handle(self, *args, **kwargs):
        first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Jack", "Karen", "Louis", "Mona", "Nina", "Oscar", "Paul", "Quinn", "Rachel", "Steve", "Tom",
                       "Aymar", "Alain", "Harouna", "Salma", "Mohammed"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
                      "OUEDRAOGO", "Barry", "EL AMOURY", "EL HILALI", "KISSOU", "KINDO"]

        nationalities = ['Français', 'Marocain', 'Chinois', 'Ivoirien', 'Burkinabé']
        majors = ['Aide à la Décision', 'Énergie', 'Matériau', 'Industrie']
        options = ['Génie Industriel', 'Data Science et Digitalisation', 'Énergie']
        filieres = ['Industrie 4.0', 'Ingénierie des Systèmes Complexes', 'Entreprendre en Afrique']
        electives = {
            'concevoir_rechercher': [
                'Applications de la physique statistique aux SHS', 'Introduction à la cyber Sécurité', 'Physique théorique', 'Gestion des risques', 'Traitement d\'images et multimédias', 'Processus Stochastiques'
            ],
            'developper_innover': [
                'Logiciel industriel ABAQUS', 'Durabilité environnementale et justice sociale', 'Réseaux Telecoms', 'La ville de demain : initiation à une démarche responsable et durable', 'Nouvelles technologies pour la mobilité terrestre', 'Facteurs Humains'
            ],
            'produire_promouvoir_vendre': [
                'Marketing', 'Fondamentaux de la Finance du Marché', 'Finance d\'entreprise', 'Stratégie d\'entreprise', 'Entreprenariat social et défis socio-économiques en Afrique : stratégies pour un développement durable', 'Introduction à l\'analyse politique du monde contemporain'
            ]
        }
        stages_data = [
            ('Ingénieur en Robotique', 'Automatisation industrielle', 'ABB'),
            ('Chef de Projet Éolien', 'Énergie renouvelable', 'EDF Renouvelables'),
            ('Data Scientist', 'Analyse de données', 'BNP Paribas'),
            ('Ingénieur en Intelligence Artificielle', 'Technologie de l\'information', 'Google'),
            ('Consultant en Stratégie', 'Conseil en gestion', 'McKinsey & Company'),
            ('Responsable de la Sécurité des Systèmes d\'Information (CISO)', 'Sécurité informatique', 'Airbus'),
            ('Ingénieur en Nanotechnologie', 'Recherche et développement', 'IBM Research'),
            ('Responsable de la Chaîne Logistique', 'Logistique et distribution', 'Amazon'),
            ('Ingénieur Calcul en Aérospatial', 'Aérospatiale', 'Safran'),
            ('Directeur de la Production', 'Industrie manufacturière', 'L\'Oréal'),
            ('Architecte Logiciel', 'Technologies de l\'information', 'Microsoft'),
            ('Responsable de la Maintenance Industrielle', 'Automobile', 'Renault'),
            ('Ingénieur en Énergie Solaire', 'Énergie renouvelable', 'TotalEnergies'),
            ('Ingénieur en Biotechnologie', 'Sciences de la vie', 'Sanofi'),
            ('Expert en FinTech', 'Technologie financière', 'Revolut')
        ]

        mobilites_data = [
            ('École Centrale Casablanca', 'Ingénierie Mécanique et Énergétique'),
            ('École Centrale Supelec', 'Génie Électrique et Électronique'),
            ('École Centrale Lyon', 'Génie Civil et Environnement'),
            ('École Centrale Nantes', 'Ingénierie des Matériaux'),
            ('École Centrale Lille', 'Informatique et Systèmes d\'Information'),
            ('École Centrale Marseille', 'Aérospatial et Mécanique des Fluides'),
            ('École Centrale Beijing', 'Biotechnologies et Santé'),
            ('École Centrale India', 'Énergies Renouvelables'),
            ('École Centrale Afrique', 'Management et Innovation Technologique'),
            ('École Centrale Canada', 'Ingénierie Financière et Actuariat')
        ]

        users_to_create = [
            (10, True, True, True),  # 10 users with mentoring_1A, mentoring_2A, mentoring_3A
            (5, False, False, True),  # 5 users with mentoring_3A only
            (8, True, True, True),  # 8 users with mentoring_1A, mentoring_2A, mentoring_3A
            (3, True, False, False)  # 3 users with mentoring_1A only
        ]

        for count, mentoring_1A, mentoring_2A, mentoring_3A in users_to_create:
            for _ in range(count):
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)
                username = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 1000)}"
                email = f"{username}@example.com"
                nationality = 'Marocain' if random.random() < 0.4 else random.choice(nationalities)
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
                    major=random.choice(majors),
                    option=random.choice(options),
                    filiere=random.choice(filieres),
                    linkedin=f"https://linkedin.com/in/{username}",
                    other_links=f"https://github.com/{username}",
                    mentoring_1A=mentoring_1A,
                    mentoring_2A=mentoring_2A,
                    mentoring_3A=mentoring_3A
                )

                for stage_type in ['PFE', 'Operateur', 'Academique']:
                    if stage_type == 'PFE' and random.random() < 0.6:
                        Stage.objects.create(
                            user=user,
                            domaine='Analyse de données',
                            entreprise='Google',
                            theme='Data Scientist',
                            annee=random.randint(2015, 2023),
                            type_stage=stage_type
                        )
                    else:
                        stage = random.choice(stages_data)
                        Stage.objects.create(
                            user=user,
                            domaine=stage[1],
                            entreprise=stage[2],
                            theme=stage[0],
                            annee=random.randint(2015, 2023),
                            type_stage=stage_type
                        )

                # Assign 'Cesure' stage to some users
                if random.random() < 0.24:
                    stage = random.choice(stages_data)
                    Stage.objects.create(
                        user=user,
                        domaine=stage[1],
                        entreprise=stage[2],
                        theme=stage[0],
                        annee=random.randint(2015, 2023),
                        type_stage='Cesure'
                    )

                for _ in range(3):
                    poste = random.choice(stages_data)
                    Poste.objects.create(
                        user=user,
                        entreprise=poste[2],
                        domaine=poste[1],
                        poste_occupe=poste[0]
                    )

                mobilite = random.choice(mobilites_data)
                Mobilite.objects.create(
                    user=user,
                    ecole=mobilite[0],
                    filiere=mobilite[1]
                )

                electif_type = random.choice(list(electives.keys()))
                competence = random.choice(electives[electif_type])
                Electif.objects.create(
                    user=user,
                    type=electif_type,
                    competence=competence
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake users and related data'))
