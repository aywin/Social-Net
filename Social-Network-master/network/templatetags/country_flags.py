# network/templatetags/extra_filters.py
from django import template

register = template.Library()

COUNTRY_FLAGS = {
    "Burkina Faso": "🇧🇫",
    "Maroc": "🇲🇦",
    "Chine": "🇨🇳",
    "France": "🇫🇷",
    "Côte d'Ivoire": "🇨🇮",
    "Bénin": "🇧🇯",
    "Tunisie": "🇹🇳",
    # Ajoutez d'autres pays et drapeaux ici si nécessaire
}

@register.filter(name='country_flag')
def country_flag(nationality):
    return COUNTRY_FLAGS.get(nationality, "")

