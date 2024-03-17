import flask
import pandas as pd
import pickle

with open(f"iris.pkl","rb") as f:
    model = pickle.load(f)
labels = {0: "setosa", 1: "versicolor", 2: "virginica"}
app = flask.Flask(__name__, template_folder = "templates")

@app.route("/",methods = ["GET","POST"])

def main():
    if flask.request.method == "GET":
        return flask.render_template("main.html")
    if flask.request.method == "POST":
        SepalLengthCm = float(flask.request.form["SepalLengthCm"])
        SepalWidthCm = float (flask.request.form["SepalWidthCm"])
        PetalLengthCm =  float(flask.request.form["PetalLengthCm"])
        PetalWidthCm = float(flask.request.form["PetalWidthCm"])
        
        input_values = pd.DataFrame([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]],
                                    columns = ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"],
                                    index = ["input"])
        prediction = model.predict(input_values)[0]
        predicted_label = labels[prediction] 
        return flask.render_template("main.html",original_input = {"SepalLengthCm":SepalLengthCm,
                                                                        "SepalWidthCm":SepalWidthCm,
                                                                        "PetalLengthCm":PetalLengthCm,
                                                                        "PetalWidthCm":PetalWidthCm,},result = predicted_label)
if __name__ =="__main__":
    app.run(host = "0.0.0.0", port = 8080)