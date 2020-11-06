import os
from datetime import datetime
from flask import Flask, request, jsonify

from data_study import DataStudy
from data_getter import DataGetter
from plot_manager import PlotManager
from data_preprocess import DataPreprocess
from analysis_manager import AnalysisManager

app = Flask(__name__)

# http://127.0.0.1:5000/?country_code=israel&start_date_month=8&start_date_day=1&end_date_month=10&end_date_day=1&predict_date_month=10&predict_date_day=15


@app.route('/')
def main():
    try:
        ### GET API PARAMETERS ###
        country_code = request.args.get('country_code')
        start_date_month = int(request.args.get('start_date_month'))
        start_date_day = int(request.args.get('start_date_day'))
        end_date_month = int(request.args.get('end_date_month'))
        end_date_day = int(request.args.get('end_date_day'))
        predict_date_month = int(request.args.get('predict_date_month'))
        predict_date_day = int(request.args.get('predict_date_day'))

        # TODO: make sure the arguments are legit

        from_date = datetime(year=2020, month=start_date_month, day=start_date_day)
        to_date = datetime(year=2020, month=end_date_month, day=end_date_day)
        predict_date = datetime(year=2020, month=predict_date_month, day=predict_date_day)

        ### CALCULATION ###
        # get data
        data = DataGetter.get_country_data(country_code=country_code,
                                           from_date=from_date,
                                           to_date=to_date)
        # data cleaning and formatting
        data = DataPreprocess.fix_country_data(data=data)
        # investigation our questions
        model = AnalysisManager.build_linear_model(data=data)

        ### RETURN JSON ###
        return jsonify({"country": country_code,
                        "predict_data": predict_date,
                        "predicted_confirmed_cases": model.predict(predict_date=predict_date)})
    except Exception as error:
        return jsonify({"error_message": error})


if __name__ == '__main__':
    app.run(debug=True)
