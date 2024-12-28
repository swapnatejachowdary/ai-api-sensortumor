import pickle
from flask import Flask,request 
api=Flask(__name__)
with open('ai.pkl','rb') as f:
    ai=pickle.load(f)
@api.route('/')
def home():
    return "API Server Running"
@api.route('/predict',methods=['GET'])
def predict():
    T=request.args.get('T')
    T=float(T)
    P=request.args.get('P')
    P=float(P)
    ECG=request.args.get('ECG')
    ECG=float(ECG)
    
    data=[[T,P,ECG]]
    response=ai.predict(data)[0]
    return response
if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=2000
    )