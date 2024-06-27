from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import User

from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import User, Stage, Poste, Mobilite



from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from django.contrib import messages





from django.contrib.auth.decorators import login_required, permission_required

from .models import *






from django.contrib.admin.views.decorators import staff_member_required




from django.contrib.auth import authenticate


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('indexx')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.groups.filter(name='Alumni').exists():
                messages.success(request, 'Vous êtes connecté en tant que membre du groupe Alumni.')
            elif user.groups.filter(name='Eleve').exists():
                messages.success(request, 'Vous êtes connecté en tant que membre du groupe Élève.')
            else:
                messages.success(request, 'Vous êtes connecté, mais vous n\'appartenez à aucun groupe spécifique.')
            return redirect('indexx')
        else:
            messages.error(request, 'Nom d\'utilisateur et/ou mot de passe incorrect(s). Veuillez réessayer.')
    
    return render(request, 'network/login.html')




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))




from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from .models import User  # Importez le modèle User personnalisé depuis votre fichier models.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from .models import User

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_group = request.POST.get('user_group')  # Ajout du champ user_group

        # Validation des entrées
        if not username or not email or not password or not first_name or not last_name or not user_group:
            messages.error(request, "Tous les champs sont requis")
            return redirect('register')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Email invalide")
            return redirect('register')

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, "Un utilisateur avec ce nom d'utilisateur existe déjà")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Un utilisateur avec cet email existe déjà")
            return redirect('register')

        # Hachage du mot de passe
        hashed_password = make_password(password)

        # Création de l'utilisateur
        user = User(username=username, email=email, password=hashed_password, 
                    first_name=first_name, last_name=last_name, user_group=user_group)
        user.save()

        messages.success(request, "Inscription réussie. Vous pouvez maintenant vous connecter.")
        return redirect('users_list')

    return render(request, 'network/add.html')





from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import User
from .forms import EditUserForm

def admin_required(user):
    return user.is_superuser

@user_passes_test(admin_required)
def edit_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informations de l\'utilisateur mises à jour avec succès!')
            return redirect('users_list')  # Redirection vers la vue users_list après mise à jour
    else:
        form = EditUserForm(instance=user)
    
    return render(request, 'network/edit_user.html', {'form': form, 'profile_user': user})





    
    
    
    
    
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required








from django.shortcuts import get_object_or_404


from django.http import Http404
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    ('-date_created')

    page_number = request.GET.get('page', 1)
    

    context = {
        "username": user,
        
        
        "page": "profile",
    }

    return render(request, 'network/profile.html', context)

@staff_member_required
def goto_admin(request):
    return redirect('/admin/')



def indexx(request):
    return render(request, 'network/indexx.html')





from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('indexx')










from django.db.models import Q

from django.contrib.auth import get_user_model

User = get_user_model()

from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import User, Electif, Stage, Poste, Mobilite

def search(request):
    query = request.GET.get('q', '')
    page_number = request.GET.get('page', 1)
    results = []

    if query:
        user_results = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(bio__icontains=query) |
            Q(nationality__icontains=query) |
            Q(promotion__icontains=query) |
            Q(major__icontains=query) |
            Q(option__icontains=query) |
            Q(filiere__icontains=query) |
            Q(email__icontains=query) |
            Q(linkedin__icontains=query) |
            Q(other_links__icontains=query) |
            Q(user_group__icontains=query)
        ).distinct().prefetch_related('postes')

        electif_results = Electif.objects.filter(
            Q(competence__icontains=query) |
            Q(type__icontains=query)
        ).distinct().select_related('user')

        stage_results = Stage.objects.filter(
            Q(domaine__icontains=query) |
            Q(entreprise__icontains=query) |
            Q(theme__icontains=query) |
            Q(type_stage__icontains=query)
        ).distinct().select_related('user')

        poste_results = Poste.objects.filter(
            Q(entreprise__icontains=query) |
            Q(domaine__icontains=query) |
            Q(poste_occupe__icontains=query)
        ).distinct().select_related('user')

        mobilite_results = Mobilite.objects.filter(
            Q(ecole__icontains=query) |
            Q(filiere__icontains=query)
        ).distinct().select_related('user')

        results = list(set(user_results) |
                       set(e.user for e in electif_results) |
                       set(s.user for s in stage_results) |
                       set(p.user for p in poste_results) |
                       set(m.user for m in mobilite_results))

    paginator = Paginator(results, 10)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        users_data = []
        for user in page_obj:
            latest_post = user.postes.last()
            users_data.append({
                'username': user.username,
                'profile_pic': user.profile_pic.url if user.profile_pic else '',
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_group': user.user_group,
                'nationality': user.nationality,
                'promotion': user.promotion,
                'bio': user.bio,
                'latest_post': {
                    'domaine': latest_post.domaine if latest_post else '',
                    'entreprise': latest_post.entreprise if latest_post else ''
                } if latest_post else {}
            })

        return JsonResponse({
            'results': users_data,
            'current_page': page_obj.number,
            'num_pages': paginator.num_pages,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next(),
        })

    return render(request, 'network/search_results.html', {'page_obj': page_obj, 'query': query})


from django.shortcuts import render
from django.db.models import Q
from .models import User

def mentoring(request):
    mentors = User.objects.filter(
        Q(mentoring_1A=True) | Q(mentoring_2A=True) | Q(mentoring_3A=True)
    ).distinct()

    return render(request, 'network/mentor.html', {'mentors': mentors})


from django.shortcuts import render, get_object_or_404
from .models import User, Stage, Poste, Mobilite





from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import User, Electif, Stage, Poste, Mobilite

def search_profiles(request):
    query = request.GET.get('q', '')
    user_group = request.GET.get('user_group')
    nationality = request.GET.get('nationality')
    electif = request.GET.get('electif')
    major = request.GET.get('major')
    option = request.GET.get('option')
    filiere = request.GET.get('filiere')
    stage_type = request.GET.get('stage_type')
    stage_domaine = request.GET.get('stage_domaine')
    poste_occupe = request.GET.get('poste_occupe')
    mobilite_filiere = request.GET.get('mobilite_filiere')
    mobilite_ecole = request.GET.get('mobilite_ecole')

    # Initial query set
    users = User.objects.all()
    print("Initial user count:", users.count())

    if user_group:
        users = users.filter(user_group__iexact=user_group)
        print(f"After filtering by user_group={user_group}:", users.count())
    if nationality:
        users = users.filter(nationality__iexact=nationality)
        print(f"After filtering by nationality={nationality}:", users.count())
    if electif:
        users = users.filter(electifs__competence__iexact=electif)
        print(f"After filtering by electif={electif}:", users.count())
    if major:
        users = users.filter(major__iexact=major)
        print(f"After filtering by major={major}:", users.count())
    if option:
        users = users.filter(option__iexact=option)
        print(f"After filtering by option={option}:", users.count())
    if filiere:
        users = users.filter(filiere__iexact=filiere)
        print(f"After filtering by filiere={filiere}:", users.count())
    if stage_type:
        users = users.filter(stages__type_stage__iexact=stage_type)
        print(f"After filtering by stage_type={stage_type}:", users.count())
    if stage_domaine:
        users = users.filter(stages__domaine__iexact=stage_domaine)
        print(f"After filtering by stage_domaine={stage_domaine}:", users.count())
    if poste_occupe:
        users = users.filter(postes__poste_occupe__iexact=poste_occupe)
        print(f"After filtering by poste_occupe={poste_occupe}:", users.count())
    if mobilite_filiere:
        users = users.filter(mobilites__filiere__iexact=mobilite_filiere)
        print(f"After filtering by mobilite_filiere={mobilite_filiere}:", users.count())
    if mobilite_ecole:
        users = users.filter(mobilites__ecole__iexact=mobilite_ecole)
        print(f"After filtering by mobilite_ecole={mobilite_ecole}:", users.count())

    # Avoid duplicates by using distinct
    users = users.distinct()

    context = {
        'page_obj': users,
        'query': query,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('network/search_results.html', context)
        return JsonResponse({'html': html})

    return render(request, 'network/search_results.html', context)




# views.py
from django.http import JsonResponse
from .models import Stage, Poste

def autocomplete(request):
    query = request.GET.get('q', '').strip().lower()
    suggestions = set()

    if query:
        # Rechercher dans les domaines des stages
        stage_domains = Stage.objects.filter(
            domaine__icontains=query
        ).values_list('domaine', flat=True).distinct()
        
        # Rechercher dans les domaines des postes
        poste_domains = Poste.objects.filter(
            domaine__icontains=query
        ).values_list('domaine', flat=True).distinct()

        # Ajouter les résultats à l'ensemble des suggestions
        suggestions.update(stage_domains)
        suggestions.update(poste_domains)

    return JsonResponse(list(suggestions), safe=False)

from django.shortcuts import render
from .models import Poste, Stage

def domaines_utilisateurs(request):
    # Récupérer tous les domaines des postes et stages des utilisateurs
    postes_domaines = Poste.objects.values_list('domaine', flat=True).distinct()
    stages_domaines = Stage.objects.values_list('domaine', flat=True).distinct()
    
    # Combiner les domaines uniques des postes et des stages
    domaines_utilisateurs = set(list(postes_domaines) + list(stages_domaines))
    
    context = {
        'domaines_utilisateurs': domaines_utilisateurs
    }
    
    return render(request, 'network/postes.html', context)



from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def user_profile_ajax(request, username):
    try:
        user = User.objects.get(username=username)
        html = render_to_string('network/full_profile.html', {'profile_user': user}, request=request)
        return JsonResponse({'html': html})
    except User.DoesNotExist:
        return JsonResponse({'error': 'Utilisateur non trouvé.'})










from django.shortcuts import render, get_object_or_404, redirect


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.bio = request.POST.get('bio')
        user.user_group = request.POST.get('user_group')

        if 'profile_pic' in request.FILES:
            user.profile_pic = request.FILES['profile_pic']
        if 'cover' in request.FILES:
            user.cover = request.FILES['cover']
        
        user.save()
        messages.success(request, "Les modifications du profil ont été enregistrées avec succès.")  # Message flash de succès
        return redirect('profile', username=user.username)

    profile_pic_url = profile_user.profile_pic.url if profile_user.profile_pic and hasattr(profile_user.profile_pic, 'url') else None

    context = {
        "profile_user": profile_user,
        "profile_pic_url": profile_pic_url,
    }
    
    return render(request, 'network/profile.html', context)





from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Electif, Stage, Poste, Mobilite

@login_required
def full_profile(request, username):
    user = get_object_or_404(User, username=username)
    stages = Stage.objects.filter(user=user)
    postes = Poste.objects.filter(user=user)
    mobilites = Mobilite.objects.filter(user=user)
    electifs = Electif.objects.filter(user=user)
    
    context = {
        'profile_user': user,
        'stages': stages,
        'postes': postes,
        'mobilites': mobilites,
        'electifs': electifs,
    }
    
    return render(request, 'network/full_profile.html', context)



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Stage, Poste, Mobilite
from .forms import ProfileForm




@login_required
def add_stage(request):
    if request.method == 'POST':
        domaine = request.POST['domaine']
        entreprise = request.POST['entreprise']
        theme = request.POST['theme']
        annee = request.POST['annee']
        type_stage = request.POST['type_stage']
        Stage.objects.create(user=request.user, domaine=domaine, entreprise=entreprise, theme=theme, annee=annee, type_stage=type_stage)
        messages.success(request, 'Stage ajouté avec succès!')
        return redirect('profile')
    return render(request, 'network/add_stage.html')


@login_required
def update_stage(request, stage_id):
    stage = get_object_or_404(Stage, id=stage_id, user=request.user)
    if request.method == 'POST':
        stage.domaine = request.POST['domaine']
        stage.entreprise = request.POST['entreprise']
        stage.theme = request.POST['theme']
        stage.annee = request.POST['annee']
        stage.type_stage = request.POST['type_stage']
        stage.save()
        messages.success(request, 'Stage mis à jour avec succès!')
        return redirect('profile')
    return render(request, 'network/update_stage.html', {'stage': stage})


@login_required
def delete_stage(request, stage_id):
    stage = get_object_or_404(Stage, id=stage_id, user=request.user)
    if request.method == 'POST':
        stage.delete()
        messages.success(request, 'Stage supprimé avec succès!')
        return redirect('profile')
    return render(request, 'network/delete_stage.html', {'stage': stage})


@login_required
def add_poste(request):
    if request.method == 'POST':
        domaine = request.POST['domaine']
        entreprise = request.POST['entreprise']
        Poste.objects.create(user=request.user, domaine=domaine, entreprise=entreprise)
        messages.success(request, 'Poste ajouté avec succès!')
        return redirect('profile')
    return render(request, 'network/add_poste.html')


@login_required
def update_poste(request, poste_id):
    poste = get_object_or_404(Poste, id=poste_id, user=request.user)
    if request.method == 'POST':
        poste.domaine = request.POST['domaine']
        poste.entreprise = request.POST['entreprise']
        poste.save()
        messages.success(request, 'Poste mis à jour avec succès!')
        return redirect('profile')
    return render(request, 'network/update_poste.html', {'poste': poste})


@login_required
def delete_poste(request, poste_id):
    poste = get_object_or_404(Poste, id=poste_id, user=request.user)
    if request.method == 'POST':
        poste.delete()
        messages.success(request, 'Poste supprimé avec succès!')
        return redirect('profile')
    return render(request, 'network/delete_poste.html', {'poste': poste})


@login_required
def add_mobilite(request):
    if request.method == 'POST':
        ecole = request.POST['ecole']
        filiere = request.POST['filiere']
        Mobilite.objects.create(user=request.user, ecole=ecole, filiere=filiere)
        messages.success(request, 'Mobilité ajoutée avec succès!')
        return redirect('profile')
    return render(request, 'network/add_mobilite.html')


@login_required
def update_mobilite(request, mobilite_id):
    mobilite = get_object_or_404(Mobilite, id=mobilite_id, user=request.user)
    if request.method == 'POST':
        mobilite.ecole = request.POST['ecole']
        mobilite.filiere = request.POST['filiere']
        mobilite.save()
        messages.success(request, 'Mobilité mise à jour avec succès!')
        return redirect('profile')
    return render(request, 'network/update_mobilite.html', {'mobilite': mobilite})


@login_required
def delete_mobilite(request, mobilite_id):
    mobilite = get_object_or_404(Mobilite, id=mobilite_id, user=request.user)
    if request.method == 'POST':
        mobilite.delete()
        messages.success(request, 'Mobilité supprimée avec succès!')
        return redirect('profile')
    return render(request, 'network/delete_mobilite.html', {'mobilite': mobilite})


from django.shortcuts import render
from django.http import JsonResponse

def load_blog_content(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'network/blog_content.html')
    return JsonResponse({'error': 'network/Invalid request'}, status=400)

from django.http import JsonResponse
from django.template.loader import render_to_string

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import User

def load_profile(request, username):
    user = get_object_or_404(User, user__username=username)
    html = render_to_string('network/profile_partial.html', {'user': user}, request=request)
    data = {
        'html': html
    }
    return JsonResponse(data)


@login_required
 # Ensure that only staff members can access this view
def users_list(request):
    users = User.objects.all()
    return render(request, 'network/users.html', {'users': users})
from django.shortcuts import render
from .models import Stage, Poste, Mobilite

def overview(request):
    stages = Stage.objects.all()
    postes = Poste.objects.all()
    mobilites = Mobilite.objects.all()
    
    context = {
        'stages': stages,
        'postes': postes,
        'mobilites': mobilites,
    }
    
    return render(request, 'network/overview.html', context)







from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
@staff_member_required
def delete_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Utilisateur supprimé avec succès.')
        return redirect('users_list')
    else:
        return render(request, 'network/delete.html', {'user': user})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Electif


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Electif, Stage, Poste, Mobilite

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Electif, Stage, Poste, Mobilite

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Sauvegarder les électifs
            Electif.objects.filter(user=user).delete()
            if form.cleaned_data['competence_concevoir_rechercher']:
                Electif.objects.create(user=user, type='concevoir_rechercher', competence=form.cleaned_data['competence_concevoir_rechercher'])
            if form.cleaned_data['competence_developper_innover']:
                Electif.objects.create(user=user, type='developper_innover', competence=form.cleaned_data['competence_developper_innover'])
            if form.cleaned_data['competence_produire_promouvoir_vendre']:
                Electif.objects.create(user=user, type='produire_promouvoir_vendre', competence=form.cleaned_data['competence_produire_promouvoir_vendre'])
            
            messages.success(request, 'Votre profil a été mis à jour avec succès!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
        # Pré-remplir les champs des électifs
        user_electifs = Electif.objects.filter(user=user)
        initial_data = {}
        for electif in user_electifs:
            if electif.type == 'concevoir_rechercher':
                initial_data['competence_concevoir_rechercher'] = electif.competence
            elif electif.type == 'developper_innover':
                initial_data['competence_developper_innover'] = electif.competence
            elif electif.type == 'produire_promouvoir_vendre':
                initial_data['competence_produire_promouvoir_vendre'] = electif.competence
        form.initial.update(initial_data)

    # Récupérer les objets de Stage, Poste et Mobilite
    stages = Stage.objects.filter(user=user)
    postes = Poste.objects.filter(user=user)
    mobilites = Mobilite.objects.filter(user=user)

    return render(request, 'network/profiles.html', {
        'form': form,
        'stages': stages,
        'postes': postes,
        'mobilites': mobilites,
    })



@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        # Simuler une réponse simple du chatbot
        response_message = f"Vous avez dit : {user_message}"

        return JsonResponse({'response': response_message})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FAQ, User
import logging

logger = logging.getLogger(__name__)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FAQ, User
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get('message', '').strip().lower()

        # Log the received message
        logger.debug(f"Received message: {user_message}")

        response = "Je suis désolé, je n'ai pas de réponse à cette question pour le moment."

        if "affiche moi tous les eleves" in user_message:
            users = User.objects.filter(user_group='Eleve')
            user_type = "élèves"
        elif "affiche moi tous les alumni" in user_message:
            users = User.objects.filter(user_group='Alumni')
            user_type = "alumni"
        else:
            # Chercher une réponse dans la FAQ
            faq = FAQ.objects.filter(question__icontains=user_message).first()
            if faq:
                response = faq.answer
            else:
                response = "Je suis désolé, je n'ai pas de réponse à cette question pour le moment."

        if users.exists():
            user_count = users.count()
            user_list = "\n".join([f"{user.username} ({user.first_name} {user.last_name})" for user in users])
            response = f"L'École Centrale Casablanca a actuellement {user_count} {user_type} inscrits sur la plateforme. Vous pouvez parcourir cette liste et retrouver les profils qui vous correspondent :\n{user_list}"
        else:
            response = f"L'École Centrale Casablanca n'a actuellement aucun {user_type} inscrit sur la plateforme."

        # Log the response
        logger.debug(f"Response: {response}")

        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)





