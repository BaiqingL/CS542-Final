## CS 542 Team 8 Final Project Porposal

*Baiqing (Andy) Lyu, Shengyao (Jax) Luo, Hanzi (Shirley) Yu, Juncheng (Morgan) Zhang*



For our term project, we will be using the **world happiness report 2021** dataset provided by Kaggle. [World Happiness Report 2021 | Kaggle](https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021)



#### Our goal:

The final hopeful output of this project is that through evaluating the happiness and social data of 149 regions, we can provide a prediction system by giving recommendations on which sector of society to focus on more in order to increase life ladder.



#### Describe the dataset:

Our data set contains the following entries:

1. Country name

2. Year

3. Life ladder (Happiness)

4. GDP

5. Social support

6. Healthy life expectancy

7. Freedom to make choices

8. Generosity

9. Perceptions of corruption

10. Positive affect

We believe that this problem is a **regression** problem as we want to derive a model that can give appropriate weights to different features, allowing us to better understand how much a certain feature matters to overall societal happiness.



### Referenced paper:

* *Network Learning Approaches to study World Happiness*
  
  * https://arxiv.org/abs/2007.09181
  
  * Used two types of computational strategies: predictive modeling and Bayesian networks



### Rough ideas:



We first thought of using `linear regression` to help predicting the life ladder. However, it is important to note that one tradeoff linear regression makes is that it assumes a linear relationship between the features and outputs. This may not be the case as values like GDP has shown increases past certain points does not in fact [grow happiness at the same rate.](https://www.pnas.org/content/107/38/16489)



Therefore, another approach we decided on using was the `random forest regressor` method. We can use multiple decision trees in helping us circumvent the limitations of linear regression, and allow us to create better models at understanding which features contributes more to happiness and how we can better optimize social policies to create for a happier future.



A problem with decision tree is that overfitting can occur easily. Therefore through using a random forest, we can expect lower variance among the multiple decision trees that has in each their own high variance. Through taking a mean output via the decision regression tree outputs, we can also combine the low bias property and better assess the problem.
