from flask import Flask, render_template, request
from run_ml import predict

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        print(request.form["home-type"])
        hometype = request.form["home-type"]
        hasgarage = request.form["hasgarage"]
        yearbuilt = request.form["yearbuilt"]
        zipcode = request.form["zipcode"]
        lotsizesqft = request.form["lotsizesqft"]
        livingareasqft = request.form["livingareasqft"]
        numofbathrooms = request.form["numofbathrooms"]
        numofbedrooms = request.form["numofbedrooms"]
        numofstories = request.form["numofstories"]
        avgschooldistance = request.form["avgschooldistance"]
  
        prediction = '${0:,.0f}'.format(predict(hometype, hasgarage, yearbuilt, zipcode, lotsizesqft, 
        livingareasqft, numofbathrooms, numofbedrooms, numofstories, avgschooldistance)[0])

        output = prediction[0]

        print(output)
        return render_template("results.html", results=output)

if __name__ == "__main__":
    app.run()