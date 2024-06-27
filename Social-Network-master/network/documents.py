from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from .models import User, Electif, Stage, Poste, Mobilite, FAQ

# Définir l'index Elasticsearch pour les utilisateurs
user_index = Index('users')

@user_index.doc_type
class UserDocument(Document):
    class Django:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'bio',
            'nationality',
            'promotion',
            'graduation_date',
            'phone_number',
            'major',
            'option',
            'filiere',
            'email',
            'linkedin',
            'other_links',
        ]

# Définir des documents pour les autres modèles de manière similaire
electif_index = Index('electifs')

@electif_index.doc_type
class ElectifDocument(Document):
    class Django:
        model = Electif
        fields = [
            'type',
            'competence',
        ]

stage_index = Index('stages')

@stage_index.doc_type
class StageDocument(Document):
    class Django:
        model = Stage
        fields = [
            'domaine',
            'entreprise',
            'theme',
            'annee',
            'type_stage',
        ]

poste_index = Index('postes')

@poste_index.doc_type
class PosteDocument(Document):
    class Django:
        model = Poste
        fields = [
            'entreprise',
            'domaine',
            'poste_occupe',
        ]

mobilite_index = Index('mobilites')

@mobilite_index.doc_type
class MobiliteDocument(Document):
    class Django:
        model = Mobilite
        fields = [
            'ecole',
            'filiere',
        ]

faq_index = Index('faqs')

@faq_index.doc_type
class FAQDocument(Document):
    class Django:
        model = FAQ
        fields = [
            'question',
            'answer',
        ]
