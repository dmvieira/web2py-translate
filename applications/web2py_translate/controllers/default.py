# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    """
    Put your code and select translate language to use bing translator to
    translate
    """

    response.flash = T("Welcome to Web2py Translate!")
    args = {
            'client_id': '8ah98sa9d98asdh89ahd9h38hd38dhja9ds',#your client id here
            'client_secret': '6D4ZdXe5edg0bo9JDMSD+wCl8np2w88QIbfYKmKfDUc=',#your azure secret here
            'scope': 'http://api.microsofttranslator.com',
            'grant_type': 'client_credentials'
        }

    form = SQLFORM.factory(Field('file', 'text'))
    if form.process().accepted:
        try:
            session.file = eval(form.vars.file)
            redirect(URL('translate'))
        except:
            response.flash = T("Wrong file format... Try again")
    return dict(form=form)

def translate():

    import base64

    if request.args(0):
        _automatic_translate(...)

    fields = list()
    for key, value in session.file:
        fields.append(Field(base64.b64encode(key), default=value, label=key))

    form = SQLFORM.factory(*fields)
    if form.process().accepted:
        for enc_translates in form.vars:
            dec_translates = base64.b64decode(enc_translates)
            if session.file.get(dec_translates):
                session.file[dec_translates] = form.vars.enc_translates


    return dict(form=form)

def _automatic_translate(_text, _from, _to):
    import json
    import requests
    import urllib
    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    oauth_junk = json.loads(requests.post(oauth_url, data=urllib.urlencode(args)).content)
    translation_args = {
            'text': _text,
            'to': _to,
            'from': _from
            }
    headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
    translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
    translation_result = requests.get(translation_url+urllib.urlencode(translation_args), headers=headers)
    return translation_result.content