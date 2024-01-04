import PySimpleGUI as sg
import joblib
import numpy as np

def create_layout():
    sg.theme('LightGrey1')

    layout = [
        [sg.Text('UF:'), sg.Input(key='UF')],
        [sg.Text('IDADE:'), sg.Input(key='IDADE')],
        # Adicione mais campos para outras variáveis
        [sg.Button('Predict Credit Score'), sg.Button('Exit')],
    ]

    return layout

def predict_credit_score(values):
    # Obter valores dos campos de entrada
    uf = int(values['UF'])
    idade = int(values['IDADE'])
    # Obtenha valores para outras variáveis

    # Carregar modelo treinado
    model = joblib.load('modelo_random_forest.pkl')

    # Realizar a predição
    new_data = np.array([uf, idade])  # Adicione outros valores para a nova entrada
    predicted_score = model.predict(new_data.reshape(1, -1))

    # Exibir resultado
    sg.popup(f'The predicted credit score is: {predicted_score[0]:.2f}', title='Credit Score Prediction')

def main():
    window = sg.Window('Credit Score Predictor', create_layout())

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Predict Credit Score':
            predict_credit_score(values)

    window.close()

if __name__ == '__main__':
    main()
