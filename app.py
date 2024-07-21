from flask import Flask, render_template, request
from churches import ephesus, smyrna, pergamos, thyatira, sardis, philadelphia, laodicea

app = Flask(__name__)

churches = [ephesus, smyrna, pergamos, thyatira, sardis, philadelphia, laodicea]

@app.route('/')
def index():
    return render_template('index.html', churches=churches)

@app.route('/compare')
def compare():
    church1 = request.args.get('church1')
    church2 = request.args.get('church2')
    church1_obj = next((church for church in churches if church.name.lower() == church1.lower()), None)
    church2_obj = next((church for church in churches if church.name.lower() == church2.lower()), None)
    if church1_obj and church2_obj:
        return render_template('compare.html', church1=church1_obj, church2=church2_obj)
    else:
        return "One or both churches not found", 404

if __name__ == '__main__':
    app.run(debug=True)