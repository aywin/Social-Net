from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    bio = models.TextField(max_length=160, blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    user_group = models.CharField(max_length=10,blank=True, null=True)  # Alumni ou Eleve

    # Champs supplémentaires
    nationality = models.CharField(max_length=100, blank=True, null=True)
    promotion = models.CharField(max_length=10, blank=True, null=True)
    graduation_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Majeurs, options, filières
    major = models.CharField(max_length=50, choices=[
        ('Aide à la Décision', 'Aide à la Décision'),
        ('Énergie', 'Énergie'),
        ('Matériau', 'Matériau'),
        ('Industrie', 'Industrie')
    ], blank=True, null=True)
    
    option = models.CharField(max_length=50, choices=[
        ('Génie Industriel', 'Génie Industriel'),
        ('Data Science et Digitalisation', 'Data Science et Digitalisation'),
        ('Énergie', 'Énergie')
    ], blank=True, null=True)
    
    filiere = models.CharField(max_length=100, choices=[
        ('Industrie 4.0', 'Industrie 4.0'),
        ('Ingénierie des Systèmes Complexes', 'Ingénierie des Systèmes Complexes'),
        ('Entreprendre en Afrique', 'Entreprendre en Afrique')
    ], blank=True, null=True)
    
    email = models.EmailField(blank=True, null=True)
    mentoring_1A = models.BooleanField(default=False)
    mentoring_2A = models.BooleanField(default=False)
    mentoring_3A = models.BooleanField(default=False)
    linkedin = models.URLField(blank=True, null=True)
    other_links = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'profile_pic': self.profile_pic.url if self.profile_pic else '',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'user_group': self.user_group,
            'nationality': self.nationality,
            'promotion': self.promotion,
            'graduation_date': self.graduation_date,
            'phone_number': self.phone_number,
            'major': self.major,
            'option': self.option,
            'filiere': self.filiere,
            'email': self.email,
            'mentoring_1A': self.mentoring_1A,
            'mentoring_2A': self.mentoring_2A,
            'mentoring_3A': self.mentoring_3A,
            'linkedin': self.linkedin,
            'other_links': self.other_links,
            'electifs': [electif.serialize() for electif in self.electifs.all()],
        }

class Electif(models.Model):
    CONCEVOIR_RECHERCHER_MODULES = [
        ('Applications de la physique statistique aux SHS', 'Applications de la physique statistique aux SHS'),
        ('Introduction à la cyber Sécurité', 'Introduction à la cyber Sécurité'),
        ('Physique théorique', 'Physique théorique'),
        ('Gestion des risques', 'Gestion des risques'),
        ('Traitement d\'images et multimédias', 'Traitement d\'images et multimédias'),
        ('Processus Stochastiques', 'Processus Stochastiques'),
    ]
    
    DEVELOPPER_INNOVER_MODULES = [
        ('Logiciel industriel ABAQUS', 'Logiciel industriel ABAQUS'),
        ('Durabilité environnementale et justice sociale', 'Durabilité environnementale et justice sociale'),
        ('Réseaux Telecoms', 'Réseaux Telecoms'),
        ('La ville de demain : initiation à une démarche responsable et durable', 'La ville de demain : initiation à une démarche responsable et durable'),
        ('Nouvelles technologies pour la mobilité terrestre', 'Nouvelles technologies pour la mobilité terrestre'),
        ('Facteurs Humains', 'Facteurs Humains'),
    ]
    
    PRODUIRE_PROMOUVOIR_VENDRE_MODULES = [
        ('Marketing', 'Marketing'),
        ('Fondamentaux de la Finance du Marché', 'Fondamentaux de la Finance du Marché'),
        ('Finance d\'entreprise', 'Finance d\'entreprise'),
        ('Stratégie d\'entreprise', 'Stratégie d\'entreprise'),
        ('Entreprenariat social et défis socio-économiques en Afrique : stratégies pour un développement durable', 'Entreprenariat social et défis socio-économiques en Afrique : stratégies pour un développement durable'),
        ('Introduction à l\'analyse politique du monde contemporain', 'Introduction à l\'analyse politique du monde contemporain'),
    ]
    
    ELECTIF_TYPES = [
        ('concevoir_rechercher', 'Concevoir et Rechercher'),
        ('developper_innover', 'Développer et Innover'),
        ('produire_promouvoir_vendre', 'Produire, Promouvoir et Vendre')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='electifs')
    type = models.CharField(max_length=50, choices=ELECTIF_TYPES)
    competence = models.CharField(max_length=150)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.type == 'concevoir_rechercher' and self.competence not in dict(self.CONCEVOIR_RECHERCHER_MODULES):
            raise ValidationError(f"{self.competence} n'est pas valide pour Convevoir et Rechercher")
        if self.type == 'developper_innover' and self.competence not in dict(self.DEVELOPPER_INNOVER_MODULES):
            raise ValidationError(f"{self.competence} n'est pas valide pour Développer et Innover")
        if self.type == 'produire_promouvoir_vendre' and self.competence not in dict(self.PRODUIRE_PROMOUVOIR_VENDRE_MODULES):
            raise ValidationError(f"{self.competence} n'est pas valide pour Produire, Promouvoir et Vendre")

    def __str__(self):
        return f"{self.get_type_display()} - {self.competence}"

    def serialize(self):
        return {
            'type': self.get_type_display(),
            'competence': self.competence,
        }

class Stage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stages', default=1)
    domaine = models.CharField(max_length=100, default='Inconnu')
    entreprise = models.CharField(max_length=100, default='Inconnu')
    theme = models.CharField(max_length=200, default='Inconnu')
    annee = models.PositiveIntegerField(default=2024)
    type_stage = models.CharField(max_length=50, choices=[
        ('PFE', 'PFE'),
        ('Cesure', 'Césure'),
        ('Operateur', 'Opérateur'),
        ('Academique', 'Académique')
    ], default='PFE')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.domaine} - {self.entreprise}"

   
class Poste(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postes', default=1)
    entreprise = models.CharField(max_length=100, default='Inconnu')
    domaine = models.CharField(max_length=100, default='Inconnu')
    poste_occupe = models.CharField(max_length=100, default='Inconnu')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.domaine} - {self.entreprise}"

class Mobilite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mobilites', default=1)
    ecole = models.CharField(max_length=100, default='Inconnu')
    filiere = models.CharField(max_length=100, default='Inconnu')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.ecole} - {self.filiere}"

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question