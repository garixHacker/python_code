import requests
from flask import  jsonify
import urllib.parse


network_url = "https://8b44-2c0f-ef58-1202-c900-f668-4741-2b8a-6d94.ngrok-free.app"

instance_value = "instance46258"

token_value = "70zd1sbbcbybqmth"







def sendPaiement(data):

    print(data, "DEBUG FOR PAYEMENT ON ARTICLE")

    formatPaiement = {
        "numc": "d25b8915-6886-4a47-a275-0ed60b889ddf",
        "montant": data['montant'],
        "numPaid": data['momo'],
        "typeVersement": "Commande Beauty",
        "name": data['name']
    }

    response = requests.post('https://wortispay.com/api/paiement/json', json=formatPaiement)
    return response.json()







# ETAPE 1  (ATTENTE)


def send_notif_noki_restaurant(num, articles, key_command ,name_resto="Restaurant"):

    name_logo = "Noki"
    
    message = f"""
Cher *{name_resto}*,

Une nouvelle commande a été passée :

Numéro de commande : *{key_command}*
Articles commandés :
"""


    for article in articles:
        message += f"*{article['quantite']} x {article['article']}*\n"

    message += """
Merci pour votre collaboration et votre service.

"""


    url = "https://api.ultramsg.com/instance46258/messages/image"

    # Encode le message en UTF-8 et utilise URL encode
    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to={num}&image={network_url}/download_img/{name_logo}&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)


    if response.status_code == 200:
        print("Notification envoyée avec succès au lounge")
        return "ok_success"
    else:
        print("Échec de l'envoi de la notification au lounge")
        return "ok_failed"







def send_notif_noki_agent(num,client,adresse,keys_command,articles):

    name_logo = "Noki"


    message = f"""
    
Cher Agent du Service Noki Noki,

Une nouvelle commande a été passée :

Numéro de commande : *{keys_command}*
Client : *{client}*
Adresse de livraison : *{adresse}*
Articles commandés :
"""


    for article in articles:
        message += f"*{article['quantite']} x {article['article']}*\n"



    url = "https://api.ultramsg.com/instance46258/messages/image"

    # Encode le message en UTF-8 et utilise URL encode
    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to={num}&image={network_url}/download_img/{name_logo}&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)



    if response.status_code == 200:
        
        print("Notification envoyée avec succès au dash")
        
        return "ok_success"
        
    else:

        print("Échec de l'envoi de la notification au dash")
        
        return "ok_failed"





# ETAPE 2 (CONFIRMER)


def send_notif_restaurant_livreur(num,client,adresse,keys_command,articles):

    name_logo = "Noki"

    message = f"""
Cher Livreur Noki Noki,

Une nouvelle commande *{keys_command}* est en cours de traitements :

Client : *{client}*
Adresse de livraison : *{adresse}*
Articles commandés :
"""


    for article in articles:
        message += f"*{article['quantite']} x {article['article']}*\n"



    url = "https://api.ultramsg.com/instance46258/messages/image"

    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to={num}&image={network_url}/download_img/{name_logo}&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)


    if response.status_code == 200:
        
        print("Notification envoyée avec succès au driver")
        
        return "ok_success"
        
    else:

        print("Échec de l'envoi de la notification au driver")
        
        return "ok_failed"







def send_notif_restaurant_client(num,resto,key_command,articles):

    if resto =="":

        resto="Paul"


    message = f"""

Cher client,

Votre commande au restaurant *{resto}* est en cours de traitements :

Numéro de commande : *{key_command}*
Articles commandés :
"""


    for article in articles:
        message += f"*{article['quantite']} x {article['article']}*\n"

    message +=f"""

Payer par mobile money en cliquant sur ce lien:
💳 - {network_url}/send_payement
    """


    url = "https://api.ultramsg.com/instance46258/messages/image"

    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to={num}&image={network_url}/download_img/{resto}&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)


    if response.status_code == 200:
        
        print("Notification envoyée avec succès au client confirm")
        
        return "ok_success"
        
    else:

        print("Échec de l'envoi de la notification au client confirm")
        
        return "ok_failed"







# ETAPE 4 (PRET POUR LA LIVRAISON)


def send_notif_restaurant_livreur_ready(num,resto,client,key_command,adresse,articles):

    message = f"""
Cher Livreur Noki Noki,

La commande *{key_command}* est prête pour la livraison.

Nom du client: *{client}*
Adresse de livraison: *{adresse}*
Téléphone: *{num}*
Articles commandés :
"""
    

    for article in articles:
        message += f"*{article['quantite']} x {article['article']}*\n"


    message += """
Merci pour votre efficacité et votre ponctualité.
"""



    url = "https://api.ultramsg.com/instance46258/messages/image"

    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to={num}&image={network_url}/download_img/{resto}&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)


    if response.status_code == 200:
        
        print("Notification envoyée avec succès au drive confirm")
        
        return "ok_success"
        
    else:

        print("Échec de l'envoi de la notification au drive confirm")
        
        return "ok_failed"






def send_notif_restaurant_client_ready(num,resto,adresse):

    message = f"""

Cher client votre commande est en cours de livraison. Veuillez patienter, notre livreur est en route pour vous apporter vos articles à l'adresse *{adresse}*.

Nous vous remercions pour votre patience.


"""


    url = "https://api.ultramsg.com/instance46258/messages/image"

    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to={num}&image={network_url}/download_img/{resto}&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)


    if response.status_code == 200:
        
        print("Notification envoyée avec succès au drive confirm")
        
        return "ok_success"
        
    else:

        print("Échec de l'envoi de la notification au drive confirm")
        
        return "ok_failed"






# ETAPE 6 (LIVREE)




def send_notif_livreur_restaurant_success(num,resto,key_command):

    
    message = f"""

Cher Restaurant *{resto}*,

Nous tenons à vous informer que la commande *{key_command}* a été livrée avec succès.
Nous vous remercions pour votre collaboration. N'hésitez pas à nous contacter si vous avez des questions ou des préoccupations.

"""


    url = "https://api.ultramsg.com/instance46258/messages/image"

    # Encode le message en UTF-8 et utilise URL encode
    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to={num}&image={network_url}/download_img/{resto}&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)


    if response.status_code == 200:
        print("Notification envoyée avec succès au lounge")
        return "ok_success"
    else:
        print("Échec de l'envoi de la notification au lounge")
        return "ok_failed"






def send_notif_livreur_agent_success(num,resto,key_command,articles):
    
    message = f"""
Nous tenons à vous informer que la commande *{key_command}* a été livrée avec succès:

Restaurant : *{resto}*
Articles commandés :
"""


    for article in articles:
        message += f"*{article['quantite']} x {article['article']}*\n"


    url = "https://api.ultramsg.com/instance46258/messages/image"

    # Encode le message en UTF-8 et utilise URL encode
    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to={num}&image={network_url}/download_img/{resto}&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)


    if response.status_code == 200:
        print("Notification envoyée avec succès au dash")
        return "ok_success"
    else:
        print("Échec de l'envoi de la notification au dash")
        return "ok_failed"









def send_notif_sms(num):

    message = """

Hello my friend ! 

"""


    url = "https://api.ultramsg.com/instance46258/messages/chat"

    payload = {
        "token": "70zd1sbbcbybqmth",
        "to": f"+242{num}",
        "body": message.encode('utf-8')  # Encodez le message en UTF-8
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        
        print("Notification envoyée avec succès au drive confirm")
        
        return "ok_success"
        
    else:

        print("Échec de l'envoi de la notification au drive confirm")
        
        return "ok_failed"





def send_notif_img(num):


    message = """

Hello my friend ! 

"""

    url = "https://api.ultramsg.com/instance46258/messages/image"

    # Encode le message en UTF-8 et utilise URL encode
    encoded_message = urllib.parse.quote(message.encode('utf-8'))

    payload = f"token=70zd1sbbcbybqmth&to=+242057695232&image={network_url}/download_img/&caption={encoded_message}"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    if response.status_code == 200:
        print("Notification envoyée avec succès")
        return "ok_success"
    else:
        print("Échec de l'envoi de la notification ")
        return "ok_failed"


