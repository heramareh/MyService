from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

logistics_offline_send_response_true = {
        "shipping":{
            "is_success":True
        }
}

logistics_offline_send_response_False = {
        "shipping":{
            "is_success":False
        }
}

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        if request.method == 'POST':
            print "Success, tid:", request.form.get("tid"), ", out_sid:", request.form.get("out_sid"), ", company_code:", request.form.get("company_code")
            return jsonify({'logistics_offline_send_response': logistics_offline_send_response_true})
        else:
            print "False"
            return jsonify({'logistics_offline_send_response': logistics_offline_send_response_False})
    except:
        print "Error"
        return "Error"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name = name)

if __name__ == '__main__':
        app.run(debug=True, host='192.168.0.209', port=500)
