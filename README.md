# Machine-learning
Machine learning learners code
## Simple Linear Regression
### Assumptions of linear Regression   
1. Linearity
2. Homoscedasticity
3. Multivariate normality
4. Independence of errors
5. Lack of multicollinearity 
## Multiple Linear Regression   
In multiple linear regression, there is no need for feature scaling, since the coefficients will compensate the feature value.   
### Statistical significance(alpha), Pvalue and Null Hypothesis   
### Building a model   
1. All-in- If there is prior knowledge or you have to or preparing for backward elimination 
2. Backward Elimination(Fastest one)   
Step 1. Select a significance level to stay in the model (eg SL = 0.05)   
Step 2. Fit the full model with all possible predictors.   
Step 3. Cosider the predictor with the highest P-value. If P> SL, go to Step 4, otherwise go to 5   
Step 4. Remove the predictor.    
Step 5. Fit the model without this variable.   
3. Forward Selection
Step 1: Select a significance level to enter the model(e.g. SL=0.05)   
Step 2: Fit all simple regression models y-x. Select the one with the lowest P-Value.   
Step 3. Keep this variable and fit all possible models with one extra predictor added to the one you already have.   
Step 4. Consider the predictor with the lowest p-Value. If P<SL, go to Step 3, otherwise ignore it and keep the previous model.   
4. Bidirectional Elimination   
Step 1: Select a significance level to enter and to stay in the model.(eg. SLenter=0.05, SLStay=0.05)   
Step 2: Perform the next step of forward selection(new variables must have P<SLenter to enter)   
Step 3: Perform all steps of backward elimination(old variables must have P<slstay to stay)   
Step 4. No new variables can enter and no old variables can exit.   
5. Score Comparison   

Backward elimination is irrelevant in python because the sklearn library automatically takes care of selecting the statistically significant features while training the model to make accurate predictions.

## Polynomial Linear Regression
y = b0 +b1x1 + b2x1^2+ ...+ bnx1^n   
Why is it called as linear?   
Linearity depends upon the coefficients. 
## Support Vector Regression
### When to apply feature scaling?
  If the output values are much higher than the features.   
  If the features are in binary, then no need to apply feature scaling.   
  No need to apply feature scaling for variables for which one hot encoding was done.   
## Decision tree regression
  CERT (Classification and Regression Trees)   
## Random forest regression
* Random forest is an example of ensemble learning
Step 1: Pick at random K data points from the Training set.   
Step 2: Build the decision tree associated to these K data points.   
Step 3: Choose the number Ntree of trees you want to build and repeat Steps 1 and 2.   
Step 4: For a new data point, make each one of our Ntree trees predict the value of Y to for the data point in question and assign the new data point the average across all of the predicted Y values.

## Clustering
### Hierarchical clustering
Two types - Agglomerative(Bottom up) and Hierarchial(Top down)

## Reinforcement Learning
### Upper Confidence Bound(UCB) Intuition
  Step 1: At each round n, we consider two numbers for each ad i;
  * Ni(n) - the number of times the ad i was selected up to round n
  * Ri(n) - the sum of rewards of the ad i up to round n
  Step 2: From these two numbers we compute
  * the average reward of ad i up to round n
  * the confidence interval at round n
  Step 3: We select the ad i that has the maximum UCB
  ![RCB algorithm](https://github.com/dekaio/Machine-learning/blob/master/images/UCBalgorithm.PNG)

