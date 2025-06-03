# Recipe Popularity Prediction

## Background  
Tasty Bytes, an online recipe startup, features new recipes daily on their homepage. Popular recipes can boost site traffic by up to 40%, but predicting which recipes will become popular beforehand is challenging. Recipes are labeled popular based on a high engagement score.

## Overview  
This project is part of Data Scientist Certification @ DataCamp. It aims to predict recipe popularity using machine learning, focusing on identifying unpopular recipes with at least 75% accuracy to help the startup optimize featured content. The approach includes data cleaning, exploratory analysis, feature engineering, and comparing models to maximize precision.

## Metric Choice  
We predict if a recipe will be popular (high traffic) or not.  
- A **false positive** means recommending a recipe as popular when it’s actually unpopular, which wastes homepage space and lowers engagement.  
- A **false negative** means missing a truly popular recipe, which is less harmful here.  

Because avoiding false positives is more important, we chose **precision** as our key metric to reduce wrong recommendations.

## Key Highlights  
- **Data Processing**: Addressed missing values and encoded categorical variables.  
- **EDA**: Analyzed trends and variable relationships.  
- **Feature Engineering**: Created relevant features to boost model performance.  
- **Modeling**: Evaluated two models for Precision:  
  - Logistic Regression: **0.8977**  
  - Random Forest: **0.7925**  

## Skills Demonstrated  
- Data wrangling  
- Exploratory data analysis  
- Feature engineering  
- Model development  
- Performance evaluation

## Final Summary & Recommendations

- **Top Recipe Categories:** Vegetable, Pork, and Potato drive most traffic. Focus promotions here.  
- **Nutritional Insights:** Calories, Carbs, and Sugar differ by popularity; track these to align with preferences.  
- **Model Performance:** Logistic Regression hit 89.77% precision; next, tune and try other models.  
- **Servings Feature:** No clear impact; consider replacing with prep time, ingredient count, or user reviews.

### Next Steps  
Promote top categories, monitor nutrition trends, refine models, and collect more user engagement data.
