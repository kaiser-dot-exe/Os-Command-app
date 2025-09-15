import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    output = ""
    if request.method == 'POST':
        ip_address = request.form.get('ip_address')
        if ip_address:
            # Zafiyet burada! Kullanıcı girdisi doğrudan komuta ekleniyor.
            command = f"ping -c 4 {ip_address}"
            try:
                output = os.popen(command).read()
            except Exception as e:
                output = str(e)

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)