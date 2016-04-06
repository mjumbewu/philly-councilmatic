# These are all the settings that are specific to a jurisdiction

###############################
# These settings are required #
###############################

OCD_CITY_COUNCIL_ID = 'ocd-organization/b27c56d4-7a09-40a8-8051-63b2d363dfa0'
CITY_COUNCIL_NAME = 'Philadelphia City Council'
OCD_JURISDICTION_ID = 'ocd-jurisdiction/country:us/state:pa/place:philadelphia/government'
LEGISLATIVE_SESSIONS = ['2011'] # the last one in this list should be the current legislative session
CITY_NAME = 'Philadelphia'
CITY_NAME_SHORT = 'Philly'

# VOCAB SETTINGS FOR FRONT-END DISPLAY
CITY_VOCAB = {
    'MUNICIPAL_DISTRICT': 'Ward',         # e.g. 'District'
    'SOURCE': 'City of Philadelphia',
    'COUNCIL_MEMBER': 'Council Member',   # e.g. 'Council Member'
    'COUNCIL_MEMBERS': 'Council Members', # e.g. 'Council Members'
    'EVENTS': 'Meetings',                 # label for the events listing, e.g. 'Events'
}

#########################
# The rest are optional #
#########################

# this is for populating meta tags
SITE_META = {
    'site_name' : 'Philadelphia Councilmatic',       # e.g. 'Chicago Councilmatc'
    'site_desc' : 'City Council, demystified. Keep tabs on Philadelphia legislation, council members, & meetings.',       # e.g. 'City Council, demystified. Keep tabs on Chicago legislation, aldermen, & meetings.'
    'site_author' : '',     # e.g. 'DataMade'
    'site_url' : '',        # e.g. 'https://chicago.councilmatic.org'
    'twitter_site': '',     # e.g. '@DataMadeCo'
    'twitter_creator': '',  # e.g. '@DataMadeCo'
}

LEGISTAR_URL = ''           # e.g. 'https://chicago.legistar.com/Legislation.aspx'


# this is for the boundaries of municipal districts, to add
# shapes to posts & ultimately display a map with the council
# member listing. the boundary set should be the relevant
# slug from the ocd api's boundary service
# available boundary sets here: http://ocd.datamade.us/boundary-sets/
BOUNDARY_SET = ''           # e.g. 'chicago-wards-2015'

# this is for configuring a map of council districts using data from the posts
# set MAP_CONFIG = None to hide map
MAP_CONFIG = {
    'center': [39.952642, -75.163382],
    'zoom': 10,
    'color': "#54afe8",
    'highlight_color': "#C00000",
}


FOOTER_CREDITS = [
    {
        'name':     '', # e.g. 'DataMade'
        'url':      '', # e.g. 'http://datamade.us'
        'image':    '', # e.g. 'datamade-logo.png'
    },
]

# this is the default text in search bars
SEARCH_PLACEHOLDER_TEXT = 'Search' # e.g. 'police, zoning, O2015-7825, etc.'



# these should live in CITY_APP/static/
IMAGES = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/LibertyBell.svg',
    # TODO; make logo-lg.png configurable
}

# THE FOLLOWING ARE VOCAB SETTINGS RELEVANT TO DATA MODELS, LOGIC
# (this is diff from VOCAB above, which is all for the front end)

# this is the name of the meetings where the entire city council meets
# as stored in legistar
CITY_COUNCIL_MEETING_NAME = 'City Council'

# this is the name of the role of committee chairs, e.g. 'CHAIRPERSON' or 'Chair'
# as stored in legistar
# if this is set, committees will display chairs
COMMITTEE_CHAIR_TITLE = 'Chairperson'

# this is the anme of the role of committee members,
# as stored in legistar
COMMITTEE_MEMBER_TITLE = 'Member'




# this is for convenience, & used to populate a table
# describing legislation types on the default about page template
LEGISLATION_TYPE_DESCRIPTIONS = [
    {
        'name': 'Ordinance',
        'search_term': 'Ordinance',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': '',
    },
    {
        'name': 'Claim',
        'search_term': 'Claim',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': '',
    },
]

# these keys should match committee slugs
COMMITTEE_DESCRIPTIONS = {
    # e.g. "committee-on-aviation" : "The Committee on Aviation has jurisdiction over matters relating to aviation and airports.",
}

# these blurbs populate the wells on the committees, events, & council members pages
ABOUT_BLURBS = {
    "COMMITTEES" :      "",
    "EVENTS":           "",
    "COUNCIL_MEMBERS":  "",
}

# these override the headshots that are automatically populated
# the keys should match a person's slug
MANUAL_HEADSHOTS = {
    # e.g. 'emanuel-rahm': {'source': 'cityofchicago.org', 'image': 'manual-headshots/emanuel-rahm.jpg' },
}

# notable positions that aren't district representatives, e.g. mayor & city clerk
# keys should match person slugs
EXTRA_TITLES = {
    # e.g. 'emanuel-rahm': 'Mayor',
}
