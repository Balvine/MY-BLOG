

import urllib.request,json
from .models import Quote

# Quote = quote.Quote

base_url= None
def configure_request(app):
# Getting QUOTE_API_BASE_URL
   global base_url
   base_url = app.config['QUOTE_BASE_URL']





def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    
   
    with urllib.request.urlopen(base_url) as url:
        get_quote_data=url.read()
        get_quote_response=json.loads(get_quote_data)

        quote_object= None

        if get_quote_response:
            id=get_quote_response.get('id')
            author=get_quote_response.get('author')
            quote=get_quote_response.get('quote')
            quote_object=Quote(id,author,quote)
        
    return quote_object