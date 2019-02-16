# Super-Bowl-2019

#### Shen 2019.1.31
Use Seasonal ARIMA with Exogenous Variables to predict the score of super bowl 53. Based on the result of SARIMA, Patriots is going to win!

### Seasonal ARIMA
Game score is also a kind of time series data. And SARIMA is a mature method to analyze time series data. The full name of SARIMA is Seasonal Autoregressive integrated Moving Average. It contains of four parts: Seasonal measure the long period trend, like month, season or years. The Autoregressive indicates that the variable of interest is regressed on its prior values. The "integrated" indicates that model will consider differencing process(the data values have been replaced with the difference between their values and the previous values). The Moving Avg. part indicates that the regression error is actually a linear combination of error terms whose values occurred at various times in the past. The purpose of each of these features is to make the model fit the data as well as possible.

But that’s not enough. Traditionally, time series forecasting only include two parts: time stamp and value at that time. Having a large dataset with rich information, I want to take advantage of that. So I import external variables into the model to improve the performance.

The most difficult and tricky part is to determine the parameters because SARIMA has 6 parameters with different meanings. 

Hopefully, people met this kind of problem before. The auto_arima function can automatically try different combination of parameter within the range that is set in advance and return the best one.  

Then we can see the effect of SARIMA. The model fit so well on the history data. The root mean square error is only 4.9 and 4.3 for two teams. Also score of super bowl is predicated with 80% confidence interval. The result indicates that Patriots will beat Rams with the score of 38 to 35.

### Dataset
The time range of the data is 2013-2018. There are totally 717 observations and 22 independent variables in dataset, which are yards gained by passing/rushing on both offense and defense team. Other variables included Team turnovers lost and turnovers gained, expected points. Weather and stadium type are also considered to see if these two conditions affected performance. Last but not least, Las vegas betting odds was added into dataset, in which Patriots is 2.5 point favorite.

---

#### Shen Update on 2019.2.6
The final score of the super bowl is 13:3, which is the lowest score in the NFL history. 

To be honest, I feel a little bit frustrated beacuse I'm pretty confident before the game since the RMSE for the past five years data is around 4. In addition, the offense of both teams are rank Top in NFL. It's reasonable for them to achieve a high score game. 

But, from the start to end, both teams are focus on defense. I guess this should be the decision of coach, which I have no way to include it in the model.  

Anyway, I learn a lot from this event. I think that is the most valuable part. Prediction can not be perfect all the time. 
