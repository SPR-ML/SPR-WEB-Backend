import datetime

importance = {
    'absences': 172,
    'studytime_ratio': 123,
    'health': 116,
    'age': 110,
    'goout': 92,
    'Dalc_per_week': 73,
    'reason': 73,
    'Mjob': 65,
    'class': 64,
    'Medu': 61,
    'freetime': 60,
    'Fedu': 59,
    'PairEdu': 58,
    'All_alc': 56,
    'activities': 51,
    'Walc': 42,
    'famsup': 41,
    'famrel': 41,
    'Fjob': 41,
    'guardian': 34,
    'failures': 30,
    'traveltime': 30,
    'schoolsup': 25,
    'famsize': 24,
    'school': 23,
    'higher': 22,
    'nursery': 21,
    'romantic': 17,
    'address': 17,
    'paid': 16,
    'more_high': 16,
    'internet': 13,
    'Pstatus': 9,
    'All_sup': 3
}

appearance = {
    'RandomForest': 2.5136288034360588,
    'CatBoost': 2.5201534580726337,
    'XGRFBoost': 2.577467060911487,
    'LightGBM': 2.600404101246184,
    'Support Vector Machine': 2.606449937079663,
    'XGBoost': 2.655595771443991,
    'SGD': 2.6793871215014433,
    'ElasticNet': 2.86670253809402,
    'DecisionTree': 3.496992828203838
}

modelStat = {
    'v1': {
        'version': 'v1',
        'date': datetime.date(2020, 9, 7),
        'r2_score': {'G': 0.3026819923371647, 'M': 0.5402298850574713},
        'auc': 0
    },
    'v2': {
        'version': 'v2',
        'date': datetime.date(2020, 9, 7),
        'r2_score': {"G": 0.7624521072796935,"M": 0.7126436781609196},
        'auc': 0
    },
    'v3': {
        'version': 'v3',
        'date': datetime.date(2020, 9, 8),
        'r2_score': 0.3084157932510938,
        'rsme': 2.328060360826329
    },
    'v4': {
        'version': 'v4',
        'date': datetime.date(2020, 9, 9),
        'r2_score': 0.3123073836119675,
        'rsme': 2.321501045083196
    }
}
