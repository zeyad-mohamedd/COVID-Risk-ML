import joblib

joblib.dump(model, 'models/model.pkl')

model = joblib.load('models/model.pkl')
