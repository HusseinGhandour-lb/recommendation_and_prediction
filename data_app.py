from flask import Flask, render_template, request, redirect, url_for, session
import data_ml
import pandas as pd
import pickle

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

# extract the training the data to use in the recomendation project
with open('needed_files/model_laptop.pkl', 'rb') as f:
    pickle_file = pickle.load(f)

#creating the route and the function
@app.route('/', methods=['GET', 'POST'])
def pred():
    
    #cheacking if the user apply post function and press submit
    if request.method == 'POST':
        if 'submit' in request.form:
            
            #get the user input to use it
            name = request.form.get('brand').lower()
            ram = request.form.get('ram')
            storage = request.form.get('storage')
            
            user_pd = pd.DataFrame({'ram': [ram], 'storage': [storage],'brand_name': data_ml.encod([name])})
            pred = data_ml.pred_model(pickle_file['train'], user_pd)
            
            #use the data_ml functions with the training and apply prediction
            recomendation1 = data_ml.recommend(pickle_file['df'], pickle_file['train'], user_pd)
            session['pred_value'] = round(pred[0], 2)
            session['recomendation'] = recomendation1
            return redirect(url_for('pred'))
        
    #return the values and load them with the frontend     
    pred_value = session.get('pred_value')
    recomendation = session.get('recomendation')
    return render_template('index.html', pred_value=pred_value, recomendation=recomendation)

if __name__ == '__main__':
    app.run(debug=True)