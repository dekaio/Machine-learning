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
