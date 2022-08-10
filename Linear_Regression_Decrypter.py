from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np 
import pickle
import create_dataset as c_d
import os

def train_model(data_path):
    print('Train Model')
    data=np.load(data_path)
    X=data['encrypted_txt']
    Y=data['origina_txt']
    reg_model=LinearRegression()
    reg_model.fit(X,Y)
    y_pred=reg_model.predict(X)
    print(f'MSE: {mean_squared_error(Y,y_pred)}')
    with open('model.pickle','wb') as f:
        pickle.dump(reg_model,f)

def load_model(model_name):
    with open(model_name,'rb') as f:
        reg_model=pickle.load(f)
    print(f'Model Loeaded from {model_name}')
    return reg_model

if __name__=='__main__':
    if 'model.pickle' in os.listdir(os.getcwd()):
        continue_train=input('Model Found Do you want to still train the model(Y/N) ')
        if continue_train=='Y' or continue_train=='y': 
            train_model('mydata.npz')
    else: 
        train_model('mydata.npz')
    
    final_model=load_model('model.pickle')
    encrypted_text=input('Enter Encrypted Text to Decrypt using our model: ')
    data=c_d.get_corpus_to_csv(encrypted_text,1)
    op=final_model.predict(data)
    c_d.convert_numpy_array_to_op_string(op)