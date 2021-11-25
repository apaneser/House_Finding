from flask import Flask, render_template, request
from run_ml import predict
from run_ml import getJsonData

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def prediction():
    # Get the data from the POST request.
    if request.method == "POST":
        print('valuecheck: ' + request.form["home-type"])
        hometype = int(request.form["home-type"])
        hasgarage = int(request.form["hasgarage"])
        yearbuilt = int(request.form["yearbuilt"])
        zipcode = int(request.form["zipcode"])
        lotsizesqft = request.form["lotsizesqft"]
        livingareasqft = int(request.form["livingareasqft"])
        numofbathrooms = float(request.form["numofbathrooms"])
        numofbedrooms = int(request.form["numofbedrooms"])
        numofstories = int(request.form["numofstories"])
        avgschooldistance = int(request.form["avgschooldistance"])

        prediction = '${0:,.0f}'.format(predict(hometype, hasgarage, yearbuilt, zipcode, lotsizesqft, 
        livingareasqft, numofbathrooms, numofbedrooms, numofstories, avgschooldistance)[0])

        print(prediction)
        return render_template("results.html", results=prediction)

@app.route('/map')
def map():
    getJsonData()
    return render_template("map.html")

@app.route('/stats')
def stats():
    return render_template("stats.html")
    

if __name__ == "__main__":
    app.run(debug=True)