from crypt import methods
from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
from sympy import source


app = Flask(__name__)
model = pickle.load(open('flight_rf.pkl','rb'))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=['Get','Post'])
@cross_origin()
def predict():
    if request.method == "Post":

        # Date of Journey 
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        # print("Departure :", Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_mins = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
        # print("Departure :", Dep_hour, Dep_mins)

        # Arrival 
        date_arr = request.form["Arrival_Time"]
        Arr_hour = int(pd.to_datetime(date_arr, format= "%Y-%m-%dT%H:%M").hour)
        Arr_mins = int(pd.to_datetime(date_arr, format= "%Y-%m-%dT%H:%M").minute)
        # print("Arrival :", Arr_hour, Arr_mins)

        # Duration
        dur_hour = abs(Arr_hour - Dep_hour)
        dur_mins = abs(Arr_mins - Dep_mins)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline = request.form['airline']
        if (airline == 'Jet Airway'):
            Jet_Airways = 1
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline == 'Indigo'):
            Jet_Airways = 0
            Indigo = 1
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0  

        elif (airline == 'Air_India'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 1
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0  

        elif (airline == 'Multiple_Carriers'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 1
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline == 'Spicejet'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0   

        elif (airline == 'Vistara'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0  

        elif (airline == 'GoAir'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline == 'Multiple_carriers_Premium_economy'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0   

        elif (airline == 'Jet_Airways_Business'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Vistara_Premium_economy'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0 

        elif (airline == 'Trujet'):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_Carriers = 0
            Spicejet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0     

        # Source
        # Banglore = 0 (not in column)
        Source = request.form['Source']
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0  

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0 

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1 

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        # Destination     
        Source = request.form['Destination']
        if (Source == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0    

        elif (Source == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0  

        elif (Source == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0                              

        elif (Source == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0  


    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']


        prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_mins,
            Arr_hour,
            Arr_mins,
            dur_hour,
            dur_mins,
            Air_India,
            GoAir,
            Indigo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_Carriers,
            Multiple_carriers_Premium_economy,
            Spicejet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        output = round(prediction[0],2)

        return render_template('home.html', prediction_text="Your Flight Price is ₹ {}".format(output))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug= True)  