from flask import *
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import json
import pickle

app = Flask(__name__)
app.debug = True
app.secret_key = 'Ranuga D 2008'

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        model = pickle.load(open("./model_random_forrest_regressor.pkl"))
        model_of_car = request.form["M"]
        year_of_car = request.form["Y"]
        transmission_of_car = request.form["T"]
        mileage_of_car = request.form["MI"]
        fuelType_of_car = request.form["F"]
        mpg_of_car = request.form["MPG"]
        engineSize_of_car = request.form["E"]
        info = np.array(
            [
                model_of_car,
                year_of_car,
                transmission_of_car,
                mileage_of_car,
                fuelType_of_car,
                mpg_of_car,
                engineSize_of_car,
            ]
        )
        df = pd.DataFrame(info)
        try:
            result = model.predict(df)
        except:
            result = model.predict(df.T)
        flash(
            f"Price : {result[0]} | Tax : {results[1]} - The results are in pounds (UK)",
            "success",
        )
    else:
        fuelType_json = json.load(open("./fuelType_info_dict.json", "r"))
        model_of_car_info = json.load(open("./model_info_dict.json", "r"))
        transmission_info = json.load(open("./transmission_info_dict.json", "r"))
        return render_template(
            "/index.html",
            transmissions=transmission_info,
            models=model_of_car_info,
            fueltypes=fuelType_json,
            zip=zip
        )


if __name__ == "__main__":
    app.run(host="192.168.1.9", port=2008)
