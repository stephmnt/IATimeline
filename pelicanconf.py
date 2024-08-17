AUTHOR = 'Stéphane Manet'
AUTHOR = 'Stéphane Manet'
SITENAME = "Une histoire de l'intelligence artificielle"
SITEURL = "https://stephmnt.github.io/IATimeline/"
METADESCRIPTION = "Découvrez une chronologie détaillée qui explore le développement et l'évolution de l'intelligence artificielle, ainsi que la perception et les réactions des sphères culturelles et intellectuelles."
PATH = "content"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['timeline_js']
THEME = 'themes/dimension'

SITEDESCRIPTION = '<p>Ce site a été réalisé à l\'aide de la library <a href="http://timeline.knightlab.com" target="_blank">TimelineJS</a> et du moteur de template <a href="https://getpelican.com" target="_blank">Pelican</a> (en Python). Le thème s\'appuie sur "Dimension" par <a href="https://html5up.net" target="_blank">html5up</a>.</p> <p>Vous pouvez consulter le code source du projet sur sa page <a href="https://github.com/stephmnt/IATimeline">Github</a>.</p>'

# Social widgets
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/stephanemanet'),
          ('github', 'https://github.com/stephmnt'),
         )

# Afficher le menu
DISPLAY_PAGES_ON_MENU = True

# Configuration pour la timeline
TIMELINE_MEDIA_URL = 'images/une-histoire-de-lintelligence-artificielle.webp'
TIMELINE_CAPTION = 'Certaines images sont générées par intelligence artificielle'
TIMELINE_CREDIT = 'Prompt : un ordinateur à l\'époque des années 50 avec de vieux transistors.'
TIMELINE_HEADLINE = 'Une histoire de l\'intelligence artificielle'
TIMELINE_TEXT = '<p>par <a href="https://linkedin.com/in/stephanemanet" rel="me" target="_blank">Stéphane Manet</p>'
DEFAULT_DATE = 'fs'