# Super-Bowl-2019
#### Shen 2019.1.31
Use SARIMA and several models to predict the score of super bowl 53. SARIMA model prediction is 38:35, Patriots win!

### Workflow
First, we collect different kinds of information to extend our dataset as much as possible. Next, we use the dataset as the input of our five models. First two to predict the winner and last three to predict the score. All of our models are written in R or Python cos we think this can give us highest freedom to control the model. Then the Avg. data of previous two games of Patriots and Rams, which are Division and Conference Championship, is used to predict the final result. This is because last two are most competitive playoff games, which we think can best represent the resent team performance. Finally, we use weight avg. to calculate the consensus score.

### SARIMA
Game score is also a kind of time series data. And SARIMA is a mature method to analyze time series data. The full name of SARIMA is Seasonal Autoregressive integrated Moving Average. It contains of four parts: Seasonal measure the long period trend, like month, season or years. The Autoregressive indicates that the variable of interest is regressed on its prior values. The "integrated" indicates that model will consider differencing process(the data values have been replaced with the difference between their values and the previous values). The Moving Avg. part indicates that the regression error is actually a linear combination of error terms whose values occurred at various times in the past. The purpose of each of these features is to make the model fit the data as well as possible.

But that’s not enough. Traditionally, time series forecasting only include two parts: time stamp and value at that time. Since we have a large dataset with rich information, we want to take advantage of that. So we import external variables into our model to improve the performance.

The most difficult and tricky part is to determine the parameters cos SARIMA has 6 parameters with different meanings. 

Hopefully, people met this kind of problem before. We can use the auto_arima function to automatically try different combination of parameter within the range you set in advance and return the best one.  

Then we can see the effect of SARIMA. The x axis is the game ID since 2013 in time order. The light blue line behind is the actual score. The red line and green line is the prediction score of Rams and Patriots. We can see that the model fit so well on the history data. The root mean square error is only 4.9 and 4.3 for two teams. Also score of super bowl is predicated with 80% confidence interval. The result indicates that Patriots will beat Rams with the score of 38 to 35.

### Dataset
The time range of our data is 2013-2018. There are two dependent variables, one is win or lose, another one is points scored. There are totally 717 observations and 22 independent variables in our dataset, which are yards gained by passing/rushing on both offense and defense team. Other variables included Team turnovers lost and turnovers gained, expected points. We also considered weather and stadium type to see if these two conditions affected performance. Last but not least, we added las vegas betting odds into our model. We used the latest points spread in our model, in which case Patriots is 2.5- point favorite.
