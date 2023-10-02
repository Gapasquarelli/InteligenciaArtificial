import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
import math



#Simulações
simulations = []

regr2_sim1 = MLPRegressor(hidden_layer_sizes=(70,40),max_iter=18000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=600)
simulations.append(regr2_sim1)
#media:  0.059728857195775274
#desvio:  0.0008117665640323996

regr2_sim2 = MLPRegressor(hidden_layer_sizes=(50,40),max_iter=18000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=600)
simulations.append(regr2_sim2)
#media:  0.06000919212219362
#desvio:  0.0008652748094478276

regr2_sim3 = MLPRegressor(hidden_layer_sizes=(60,30),max_iter=18000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=600)
simulations.append(regr2_sim3)
#media:  0.06022084145511443
#desvio:  0.00047134491250183717

regr3_sim1 = MLPRegressor(hidden_layer_sizes=(50,40,20),max_iter=30000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=800)
simulations.append(regr3_sim1)
#media:  0.28333590412559123
#desvio:  0.006460540189092581

regr3_sim2 = MLPRegressor(hidden_layer_sizes=(80,70),max_iter=30000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=800)
simulations.append(regr3_sim2)
#media:  0.2874081087528498
#desvio:  0.004330039296021476

regr3_sim3 = MLPRegressor(hidden_layer_sizes=(60,50),max_iter=30000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=800)
simulations.append(regr3_sim3)
#media:  0.28482324834953426
#desvio:  0.00608660851722576

regr4_sim1 = MLPRegressor(hidden_layer_sizes=(100,70,50),max_iter=18000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=1000)
simulations.append(regr4_sim1)
#media:  5.217450075926991
#desvio:  0.0655467994512969

regr4_sim2 = MLPRegressor(hidden_layer_sizes=(120,60),max_iter=18000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=1000)
simulations.append(regr4_sim2)
#media:  5.751197316490248
#desvio:  0.2797006923104905

regr4_sim3 = MLPRegressor(hidden_layer_sizes=(60,30),max_iter=18000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=1000)
simulations.append(regr4_sim3)
#media:  17.92303050355803
#desvio:  36.25030486484493

regr5_sim1 = MLPRegressor(hidden_layer_sizes=(70,40),max_iter=10000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=700)
simulations.append(regr5_sim1)
#media:  4271.189907357826
#desvio:  219.44642016767932

regr5_sim2 = MLPRegressor(hidden_layer_sizes=(70,40),max_iter=10000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=700)
simulations.append(regr5_sim2)
#media:  4400.418540802745
#desvio:  274.8146478227021

regr5_sim3 = MLPRegressor(hidden_layer_sizes=(70,40),max_iter=10000,activation='relu',solver='adam',learning_rate='adaptive',n_iter_no_change=700)
simulations.append(regr5_sim3)
#media:  4350.819302325114
#desvio:  211.2906064686795

simulation_paths = {
    regr2_sim1: './imagens/teste2/sim1',
    regr2_sim2: './imagens/teste2/sim2',
    regr2_sim3: './imagens/teste2/sim3',
    regr3_sim1: './imagens/teste3/sim1',
    regr3_sim2: './imagens/teste3/sim2',
    regr3_sim3: './imagens/teste3/sim3',
    regr4_sim1: './imagens/teste4/sim1',
    regr4_sim2: './imagens/teste4/sim2',
    regr4_sim3: './imagens/teste4/sim3',
    regr5_sim1: './imagens/teste5/sim1',
    regr5_sim2: './imagens/teste5/sim2',
    regr5_sim3: './imagens/teste5/sim3'
}

test_files = {
    regr2_sim1: 'teste2.npy',
    regr2_sim2: 'teste2.npy',
    regr2_sim3: 'teste2.npy',
    regr3_sim1: 'teste3.npy',
    regr3_sim2: 'teste3.npy',
    regr3_sim3: 'teste3.npy',
    regr4_sim1: 'teste4.npy',
    regr4_sim2: 'teste4.npy',
    regr4_sim3: 'teste4.npy',
    regr5_sim1: 'teste5.npy',
    regr5_sim2: 'teste5.npy',
    regr5_sim3: 'teste5.npy'
}

for i in simulations:
    media = 0
    erros = []
    regr = i
    print('Carregando Arquivo de teste')
    arquivo = np.load(test_files[regr])
    x = arquivo[0]
    y = np.ravel(arquivo[1])
    for j in range(10):
        print('Treinando RNA')        
        regr = regr.fit(x,y)
        
        erros.append(regr.best_loss_)
        media += regr.best_loss_

        y_est = regr.predict(x)

        plt.figure(figsize=[14,7])

        #plot curso original
        plt.subplot(1,3,1)
        plt.plot(x,y)

        #plot aprendizagem
        plt.subplot(1,3,2)
        plt.plot(regr.loss_curve_)

        #plot regressor
        plt.subplot(1,3,3)
        plt.plot(x,y,linewidth=1,color='yellow')
        plt.plot(x,y_est,linewidth=2)

        #plt.savefig(f'{simulation_paths[regr]}/E{j}.png')

    media = media / 10

    variancia = 0

    for i in erros:
        variancia += math.pow(i-media, 2)

    desvio = math.sqrt(variancia/10)
    
    print("Simulação: ", simulation_paths[regr])
    print("media: ", end=" ")
    print(media)
    print("desvio: ", end=" ")
    print(desvio)