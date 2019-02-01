import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error
from math import sqrt
import os

# Importing data
os.chdir('/Users/yangshen/PycharmProjects/playground/Superbowl2019')

# Train and Test
data = pd.read_csv('NFL2018csv4.0.csv')
RamsPatriotsAvgLast2Game = pd.read_csv('RamsPatriotsAvgLast2Game.csv')

# Patriots
data_patriots = data[data['Team'] == 'New England Patriots']
data_patriots.index = range(0, 113)
# train_patriots = pd.Series.to_frame(data_patriots['Tm'][0:98])
# test_patriots = pd.Series.to_frame(data_patriots['Tm'][97:])
exogenous_patriots = pd.DataFrame()
exogenous_patriots['obs'] = range(113)
exogenous_patriots = pd.concat(
    [exogenous_patriots, data_patriots.iloc[:, [8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21]]], axis=1)

# Rams
data_Rams = data[data['Team'] == 'Los Angeles Rams']
data_Rams.index = range(0, 99)
exogenous_Rams = pd.DataFrame()
exogenous_Rams['obs'] = range(99)
exogenous_Rams = pd.concat([exogenous_Rams, data_Rams.iloc[:, [8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21]]], axis=1)
exogenous_Rams.index = range(14, 113)
data_Rams.index = range(14, 113)

# Test seasonal

# sm.tsa.seasonal_decompose(df['Team_Score']).plot()
# result = sm.tsa.stattools.adfuller(train_patriots)
# plt.show()

# All to train and predict

fit3 = auto_arima(data_patriots['Score_Tm'],
                  exogenous=exogenous_patriots,
                  start_p=0, start_q=0,
                  max_p=15, max_q=15,
                  start_P=0, start_Q=0,
                  # d=1, D=1,
                  max_d=10, max_D=10,
                  m=7, seasonal=True,
                  trace=True,
                  error_action='ignore',
                  suppress_warnings=True,
                  stepwise=True)

pred_patriots = fit3.predict(n_periods=2, exogenous=RamsPatriotsAvgLast2Game.iloc[[2, 3], :], return_conf_int=True,
                             alpha=0.2)
fi3_pred = fit3.predict_in_sample(exogenous=exogenous_patriots)
print(sqrt(mean_squared_error(data_patriots['Score_Tm'], fi3_pred)))

fit4 = auto_arima(data_Rams['Score_Tm'],
                  exogenous=exogenous_Rams,
                  start_p=0, start_q=0,
                  max_p=15, max_q=15,
                  start_P=0, start_Q=0,
                  # d=1, D=1,
                  max_d=10, max_D=10,
                  m=1, seasonal=True,
                  trace=True,
                  error_action='ignore',
                  suppress_warnings=True,
                  stepwise=True)

pred_rams = fit4.predict(n_periods=2, exogenous=RamsPatriotsAvgLast2Game.iloc[[0, 1], :], return_conf_int=True,
                         alpha=0.2)
fit4_pred = fit4.predict_in_sample(exogenous=exogenous_Rams)
print(sqrt(mean_squared_error(data_Rams['Score_Tm'], fit4_pred)))

#Patriots
plt.figure(figsize=(16, 4))
plt.xlabel('2013-2018 Season Game ID')
plt.ylabel('Team Score')
plt.plot(data_patriots['Score_Tm'], label='Train_Patriots', alpha=0.3)
plt.plot(fi3_pred, label='Test_Patriots', alpha=0.6, color='green')
plt.plot([112, 115], [33.50830406, 37.5], '--', color='green', label='Prediction_Patriots', alpha=0.8)
plt.errorbar(len(data_patriots['Score_Tm']) + 3, 38, yerr=5.6, markersize=4, capsize=4, ecolor='green', alpha=0.5,
             label='80% Confident Interval')
plt.scatter(len(data_patriots['Score_Tm']) + 3, 38, color='green', marker="d", s=100)
plt.text(len(data_patriots['Score_Tm']) + 3.8, 42, 'Patriots:38', fontsize=20,color='green')
plt.text(len(data_patriots['Score_Tm']) - 4.5, -1, 'RMSE:4.3715', fontsize=12, color='black')
# plot opp predict
plt.errorbar(len(data_patriots['Score_Tm']) + 2, 35, yerr=6.2, markersize=4, capsize=4, ecolor='r', alpha=0.5)
plt.scatter(len(data_patriots['Score_Tm']) + 2, 35, color='r', marker="d", s=100, alpha=0.8)
plt.text(len(data_patriots['Score_Tm']) + 3.1, 27, 'Rams:35', fontsize=20, color='r')
plt.legend(loc='upper left')

#Rams
plt.figure(figsize=(16, 4))
#plt.xlabel('2013-2018 Season Game ID')
plt.ylabel('Team Score')
plt.plot(data_Rams['Score_Tm'], label='Train_Rams', alpha=0.3)
plt.plot(range(14, 113), fit4_pred, label='Test_Rams', alpha=0.6, color='r')
plt.plot([112, 115], [25.77049696, 35], '--', color='r', label='Prediction_Rams', alpha=0.8)
plt.errorbar(len(data_patriots['Score_Tm']) + 2, 35, yerr=6.2, markersize=4, capsize=4, ecolor='r', alpha=0.5,
             label = '80% Confident Interval')
plt.scatter(len(data_patriots['Score_Tm']) + 2, 35, color='r', marker="d", s=100)
plt.text(len(data_patriots['Score_Tm']) + 3.1, 27, 'Rams:35', fontsize=20, color='r')
plt.text(len(data_patriots['Score_Tm']) - 2.5, -8.5, 'RMSE:4.905', fontsize=12, color='black')
# plot opp predict
plt.errorbar(len(data_patriots['Score_Tm']) + 3, 38, yerr=5.6, markersize=4, capsize=4, ecolor='green', alpha=0.5)
plt.scatter(len(data_patriots['Score_Tm']) + 3, 38, color='green', marker="d", s=100, alpha=0.8)
plt.text(len(data_patriots['Score_Tm']) + 3.8, 42, 'Patriots:38', fontsize=20, color='green')
plt.legend(loc='upper left')
plt.xticks([])
