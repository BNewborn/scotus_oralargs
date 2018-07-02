
# coding: utf-8

# ###### Calls to API
#
# Courtesy of Ben Musch - [Git](https://github.com/BenMusch/oyez-api-python/blob/master/oyez_api/__init__.py)

# In[6]:


import requests

BASE_URL = 'https://www.oyez.org/'
BASE_API_URL = 'https://api.oyez.org/'

def cases(term):
    '''
    Grab cases by term.
    Input: term
    Output: JSON
    '''
    url = BASE_API_URL + "cases?filter=term:" + str(term) + "&per_page=100"
    print(f"Cases: {url}")
    return requests.get(url).json()

def case(term, docket_num):
    '''
    Grab case by term, docket_num.
    Input: term,docket_num
    Output: JSON
    '''
    url = 'https://api.oyez.org/' + "cases/" + str(term) + "/" + docket_num
    return requests.get(url).json()

def transcript_data(term, docket_num):
    '''
    Grab transcript_data by term, docket_num.
    Input: term,docket_num
    Output: JSON
    '''
    case_data = case(term, docket_num)
    return [ requests.get(data["href"]).json() for data in case_data["oral_argument_audio"] ]

def get_oral_href(case_inp):
    '''
    Input: 1 Case
    Returns: JSON Page of Oral Argument - Down to "Sections"
    User should then loop through sections to get each speaking bit

    This function will take an individual case,
    likely fed in via a loop of oyez_api.cases(year).
    It will then, for a given case, get the oral_arguments_href
    and call for that link via request.
    '''
    href = case_inp['href']
    full_case = requests.get(href).json()
    oral_page = full_case["oral_argument_audio"][0]['href']
    full_transcript = requests.get(oral_page).json()

    return full_transcript['transcript']['sections']

def grab_speaking_text_print(section):
    '''
    Input: turns section of Oral Argument Page
    Output: Speaker, Text

    This function needs a double for loop to get within the sections>
    turns area of the JSON. Then, it can isolate the text and speaker

    '''
    print(f"Speaker: {section['speaker']['name']}")
    print(f"Text: {section['text_blocks'][0]['text']}")
    print("***********************************")

def voting_decisions(case_inp):
    '''
    This function takes in a SCOTUS case and returns 3 lists: Majority voting justices, 
    minority voting justices and other (i.e. any other outcomes like recusal). I will then use
    this as part of our input for the MongoDB, maybe it will come in handy with visualizations
    or some other metric
    
    Input: 1 Case
    Output: 3 Lists - Majority, Minority, Other
    '''
    majority=[]
    minority=[]
    other=[]
    href = case_inp['href']
    full_case = requests.get(href).json()
    decisions_href = full_case["decisions"][0]['href']
    decisions_page = requests.get(decisions_href).json()
    for member in decisions_page['votes']:
        if member['vote'] == "majority":
            majority.append(member['member']['name'])
        elif member['vote'] == "minority":
            minority.append(member['member']['name'])
        else:
            other.append(member['name'])
    return majority, minority, other

def justice_voting(majority,minority,other,justice):
    if justice in majority:
        return "majority"
    elif justice in minority:
        return "minority"
    elif justice in other:
        return "other"
    else:
        return "N/A"
