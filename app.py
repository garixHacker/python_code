from flask import Flask, jsonify, request , send_from_directory, send_file
from flask_cors import CORS
import notif_whatsapp

app = Flask(__name__)
CORS(app)




# ETAPE 1  (ATTENTE)



@app.route('/api/restaurant', methods=['POST'])
def send_notif_noki_restaurant_route():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')

    print(data_user)

    number_phone = data_user["num"]
    name_resto = data_user["resto"]
    article_number = data_user["articles"]
    key_command = data_user["key"]


    notif_whatsapp.send_notif_noki_restaurant(number_phone,article_number,key_command,name_resto)

    return jsonify({"status": "ok"}), 200









@app.route('/api/agent', methods=['POST'])
def send_notif_noki_agent_route():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')

    sms = """ 
        Welcome noki food service notification !
    """

    print(data_user)

    number_phone = data_user["num"]
    name_client = data_user["client"]
    article_number = data_user["articles"]
    key_command = data_user["key"]
    adresse = data_user["adresse"]


    notif_whatsapp.send_notif_noki_agent(number_phone,name_client,adresse,key_command,article_number)

    return jsonify({"status": "ok"}), 200






# ETAPE 2 (CONFIRMER)



@app.route('/api/livreur', methods=['POST'])
def send_notif_restaurant_livreur_route():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')


    print(data_user)


    number_phone = data_user["num"]
    name_client = data_user["client"]
    article_number = data_user["articles"]
    key_command = data_user["key"]
    adresse = data_user["adresse"]


    notif_whatsapp.send_notif_restaurant_livreur(number_phone,name_client,adresse,key_command,article_number)

    return jsonify({"status": "ok"}), 200





@app.route('/api/client_confirm', methods=['POST'])
def send_notif_restaurant_client_route():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')


    print(data_user)

    number_phone = data_user["num"]
    name_resto = data_user["resto"]
    article_number = data_user["articles"]
    key_command = data_user["key"]


    notif_whatsapp.send_notif_restaurant_client(number_phone,name_resto,key_command,article_number)

    return jsonify({"status": "ok"}), 200




# ETAPE 4 (PRET POUR LA LIVRAISON)



@app.route('/api/livreur_ready', methods=['POST'])
def send_notif_restaurant_livreur_ready_route():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')


    print(data_user)

    number_phone = data_user["num"]
    name_resto = data_user["resto"]
    article_number = data_user["articles"]
    key_command = data_user["key"]
    name_client = data_user["client"]
    adresse = data_user["adresse"]


    notif_whatsapp.send_notif_restaurant_livreur_ready(number_phone,name_resto,name_client,key_command,adresse,article_number)

    return jsonify({"status": "ok"}), 200





@app.route('/api/client_ready', methods=['POST'])
def send_notif_restaurant_client_ready_route():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')


    print(data_user)

    number_phone = data_user["num"]
    name_resto = data_user["resto"]
    adresse = data_user["adresse"]

    notif_whatsapp.send_notif_restaurant_client_ready(number_phone,name_resto,adresse)

    return jsonify({"status": "ok"}), 200







# ETAPE 6 (LIVREE)

@app.route('/api/livreur_resto_success', methods=['POST'])
def send_notif_livreur_restaurant_success_route():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')


    print(data_user)

    number_phone = data_user["num"]
    name_resto = data_user["resto"]
    key_command = data_user["key"]


    notif_whatsapp.send_notif_livreur_restaurant_success(number_phone,name_resto,key_command)

    return jsonify({"status": "ok"}), 200




@app.route('/api/livreur_agent_success', methods=['POST'])
def send_notif_livreur_agent_success_route():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')


    print(data_user)

    
    number_phone = data_user["num"]
    name_resto = data_user["resto"]
    key_command = data_user["key"]
    article_number = data_user["articles"]


    notif_whatsapp.send_notif_livreur_agent_success(number_phone,name_resto,key_command,article_number)

    return jsonify({"status": "ok"}), 200






@app.route('/api/img', methods=['POST'])
def send_notif_img():
    if request.is_json:
        # Si les données sont JSON

        print(" -- JSON DATA --")
        
        data_user = request.json

    elif request.form:
        # Si les données sont envoyées via un formulaire

        print(" -- FORMULAR DATA -- ")
        
        data_user = request.form
        
    else:
        # Si les données sont envoyées comme du texte brut

        print("-- TEXT DATA --")

        data_user = request.data.decode('utf-8')


    print(data_user)

    number_phone = data_user["num"]

    notif_whatsapp.send_notif_img(number_phone)

    return jsonify({"status": "ok"}), 200





@app.route('/download_img/<string:name>', methods=['GET'])
def send_any_file_from_directory(name):


    print("--Image select--",name)

    directory_path = "desc"

    if name == "Paul":

        file_name = "Paul.png"


    elif name == "Noki":

        file_name = "Noki.png"


    elif name == "Cigusta":

        file_name = "Cigusta.png"


    try:

        return send_from_directory(directory_path, file_name)


    except Exception as e:

        return str(e), 500  # Utilisez le code d'erreur approprié, par exemple, 500 pour une erreur interne du serveur






@app.route('/send_payement', methods=['GET'])
def send_payement():


    data = {

        'montant': 100, 
        'momo': '057695232', 
        'name': 'Test'
    }


    try:

        notif_whatsapp.sendPaiement(data)

        return {"status":"200"},200

    except Exception as e:

        return str(e), 500  








if __name__ == '__main__':
    app.run(debug=True,port=3000)
