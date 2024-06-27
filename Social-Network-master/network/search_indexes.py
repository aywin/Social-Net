from haystack import indexes
from .models import User, Electif, Stage, Poste, Mobilite

class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr='username')
    bio = indexes.CharField(model_attr='bio', null=True)
    email = indexes.CharField(model_attr='email', null=True)
    nationality = indexes.CharField(model_attr='nationality', null=True)
    promotion = indexes.CharField(model_attr='promotion', null=True)
    phone_number = indexes.CharField(model_attr='phone_number', null=True)
    major = indexes.CharField(model_attr='major', null=True)
    option = indexes.CharField(model_attr='option', null=True)
    filiere = indexes.CharField(model_attr='filiere', null=True)
    linkedin = indexes.CharField(model_attr='linkedin', null=True)
    other_links = indexes.CharField(model_attr='other_links', null=True)

    def get_model(self):
        return User

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ElectifIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    type = indexes.CharField(model_attr='type')
    competence = indexes.CharField(model_attr='competence')

    def get_model(self):
        return Electif

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class StageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    domaine = indexes.CharField(model_attr='domaine')
    entreprise = indexes.CharField(model_attr='entreprise')
    theme = indexes.CharField(model_attr='theme')
    annee = indexes.IntegerField(model_attr='annee')
    type_stage = indexes.CharField(model_attr='type_stage')

    def get_model(self):
        return Stage

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class PosteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    domaine = indexes.CharField(model_attr='domaine')
    entreprise = indexes.CharField(model_attr='entreprise')
    poste_occupe = indexes.CharField(model_attr='poste_occupe')

    def get_model(self):
        return Poste

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class MobiliteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    ecole = indexes.CharField(model_attr='ecole')
    filiere = indexes.CharField(model_attr='filiere')

    def get_model(self):
        return Mobilite

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
