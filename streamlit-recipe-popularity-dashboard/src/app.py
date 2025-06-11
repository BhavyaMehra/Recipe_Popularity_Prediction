import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="Recipe Popularity Dashboard", layout="wide")

# --- Project Introduction ---
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 0.3em;'>Recipe Popularity Dashboard</h1>
    <div style='text-align: center; font-size: 1.1em; max-width: 900px; margin: 0 auto 1.5em auto;'>
        <b>What is this project?</b><br>
        Tasty Bytes delivers pre-measured ingredients alongside recipes to customers' doors. We analyzed ~1000 recipes to transform their homepage from random recipe selection to data-driven recommendations.<br><br>
        <b>Why does it matter?</b><br>
        Understanding what makes recipes popular helps us feature the right content, driving more website traffic and connecting more customers with our meal kit service.<br><br>
        <b>What will you see?</b><br>
        In this dashboard, you'll see how we used data science skills to solve a real business problem:
        <div style='text-align: center; margin: 0.5em auto 0 auto; max-width: 700px;'>
            <span style='display: block; margin-bottom: 0.3em;'><b>Skills used:</b> Data cleaning, feature engineering, exploratory data analysis, statistical testing, predictive modeling (<b>Logistic Regression & Random Forest</b>), and model evaluation.</span>
            <span style='display: block;'>You'll follow the journey from raw data to actionable insights and recommendations for the business.</span>
        </div>
    </div>
    <hr style='margin-bottom: 1.5em;'>
    """,
    unsafe_allow_html=True
)

# --- Load Cleaned Data ---
df = pd.read_csv("Data/cleaned_df.csv")

df['high_traffic'] = df['high_traffic'].map({1: 'High', 0: 'Low'})
df['high_traffic'] = pd.Categorical(df['high_traffic'], categories=['High', 'Low'], ordered=True)

# --- Overall Traffic Distribution (FIRST VISUAL) ---

col1, col2 = st.columns(2)
with col1:
    st.header("Overall Recipe Traffic Distribution")
    traffic_counts = df['high_traffic'].value_counts()
    fig_pie = px.pie(
        names=traffic_counts.index,
        values=traffic_counts.values,
        color=traffic_counts.index,
        color_discrete_map={"High": "#636EFA", "Low": "#EF553B"}
    )
    fig_pie.update_traces(textinfo='percent+label')
    fig_pie.update_layout(legend_title_text='Traffic Level', legend=dict(itemsizing='constant'))
    st.plotly_chart(fig_pie, use_container_width=True)
with col2:
    st.header("Data Cleaning & Feature Engineering")
    st.markdown("""
    <ul>
        <li><b>Missing Value Imputation:</b> Filled missing values in <b>calories, carbohydrate, sugar, protein</b> using the median for each recipe category. This approach is robust for right-skewed data and ensures each category's nutritional profile is preserved.</li>
        <li><b>Category Consistency:</b> Fixed typos and merged similar categories (e.g., 'Chicken Breast' into 'Chicken') to ensure only valid, consistent categories are used in analysis and modeling.</li>
        <li><b>Serving Size Standardization:</b> Cleaned the <b>servings</b> column by removing text like 'as a snack' and converting all values to integers, so serving size is a reliable numeric feature.</li>
        <li><b>Target Variable Handling:</b> Replaced missing <b>high_traffic</b> values with 'Low', based on the assumption that missing traffic data likely means low engagement. This prevents bias and allows the model to learn from all recipes.</li>
        <li><b>Data Validation:</b> Checked all columns for correct data types and ensured there are no missing values before analysis. This step is crucial for robust modeling and accurate visualizations.</li>
    </ul>
    """, unsafe_allow_html=True)

# --- EDA: Numeric Features Distribution (all in one visual) ---
st.header("Distribution of Numeric Features")
col3, col4 = st.columns(2)
with col3:
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    numeric_features = ['calories', 'carbohydrate', 'sugar', 'protein']
    for i, feature in enumerate(numeric_features):
        ax = axs[i//2, i%2]
        sns.histplot(df[feature], ax=ax, kde=True, color='skyblue')
        ax.set_title(f"{feature.title()} Distribution")
        ax.set_xlabel(feature.title())
    plt.tight_layout()
    st.pyplot(fig)
with col4:
    fig_box, axs_box = plt.subplots(2, 2, figsize=(12, 8))
    for i, feature in enumerate(numeric_features):
        ax = axs_box[i//2, i%2]
        sns.boxplot(
            x=df['high_traffic'],
            y=df[feature],
            ax=ax
        )
        ax.set_title(f"{feature.title()} by Traffic Level")
        ax.set_xlabel('Traffic Level')
    plt.tight_layout()
    st.pyplot(fig_box)

# --- Category-wise Traffic Analysis and Serving Size by Traffic ---

col5, col6 = st.columns(2)
with col5:
    st.header("Recipe Categories by Traffic Level")
    fig_category = px.histogram(
        df,
        x='category',
        color='high_traffic',
        barmode='group',
        category_orders={"high_traffic": ["High", "Low"]}
    )
    fig_category.update_layout(xaxis_title="Recipe Category", yaxis_title="Count of Recipes", legend_title_text='Traffic Level')
    st.plotly_chart(fig_category, use_container_width=True)
with col6:
    st.header("Serving Size Distribution by Traffic Level")
    fig_servings = px.histogram(
        df,
        x="servings",
        color="high_traffic",
        barmode="group",
        category_orders={"high_traffic": ["High", "Low"]}
    )
    fig_servings.update_layout(xaxis_title="Servings", yaxis_title="Count", legend_title_text='Traffic Level')
    st.plotly_chart(fig_servings, use_container_width=True)
    

# --- Statistical Analysis Table (placeholder, to be filled manually) ---
st.header("Statistical Analysis of Numeric Features")
col7, col8 = st.columns(2)
with col7:
    st.markdown("**Understanding Nutritional Impact on Recipe Popularity**")
    st.markdown("""
    Welch's t-test helps us identify which nutritional features truly affect recipe popularity, especially when comparing uneven groups.

    **Key Findings (p < 0.05):**
    - Calories, carbs, and sugar levels are significantly different in popular recipes
    - Protein content doesn't impact popularity
    
    This guides us to focus on the nutritional factors that actually drive engagement.
    """)
with col8:
    st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)  # Add spacing to align with text
    ttest_results = pd.DataFrame({
        "Feature": ["calories", "carbohydrate", "sugar", "protein"],
        "T-statistic": [2.083, 2.477, -2.172, 1.162],
        "P-value": [0.037, 0.013, 0.030, 0.245],
        "Statistically Significant": [True, True, True, False]
    })
    st.dataframe(ttest_results, hide_index=True, height=200)  # Increased height

# --- Modeling Approach & Metric ---
st.header("Predictive Modeling: How Well Can We Predict Popular Recipes?")
col9, col10 = st.columns(2)
with col9:
    st.markdown("""
    We tested two models on our data:
    <ul>
        <li><b>Logistic Regression</b> (simple, interpretable): Precision = <b>0.90</b></li>
        <li><b>Random Forest</b> (captures complex patterns): Precision = <b>0.79</b></li>
    </ul>
    <br>
    <b>What does this mean?</b> If our model predicts a recipe will be popular, it's right about 9 out of 10 times!
    """, unsafe_allow_html=True)
with col10:
    st.markdown("""
    <b>Why focus on precision?</b><br>
    We want to recommend only the best recipes. Precision tells us: Of all recipes we say are popular, how many really are? High precision means users see only the most engaging content.<br><br>
    <b>Fun fact:</b> If we only cared about recall, we'd recommend everything! But then users would see lots of boring recipes. Precision keeps our recommendations sharp.
    """, unsafe_allow_html=True)

# --- Precision Comparison Visual (leaner bars) ---

col11, col12 = st.columns(2)
with col11:
    st.header("Model Precision Comparison")
    models = ["Logistic Regression", "Random Forest"]
    precisions = [0.90, 0.79]  # Replace with your real values
    fig_prec = go.Figure()
    fig_prec.add_trace(go.Bar(
        x=models,
        y=precisions,
        width=0.3,  # Leaner bars
        text=[f"{p:.2f}" for p in precisions],
        textposition='outside',
    ))
    fig_prec.update_layout(
        yaxis=dict(range=[0, 1]),
        yaxis_title="Precision Score",
        xaxis_title="Model",
        bargap=0.5  # More space between bars
    )
    st.plotly_chart(fig_prec, use_container_width=True)
with col12:
    st.header("Confusion Matrix for Logistic Regression")
    z = [[36, 79], [66, 9]]  # Dummy values, replace with real
    x = ["Predicted Low", "Predicted High"]
    y = ["Actual High", "Actual Low"]
    z_text = [[str(item) for item in row] for row in z]
    fig_cm = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale='Viridis')
    st.plotly_chart(fig_cm, use_container_width=True)

# --- Top Features of Winning Model ---
col13, col14 = st.columns(2)
with col13:
    st.header("Top Features Driving Recipe Popularity")
    features = ["Category Vegetable", "Category Potato", "Category Pork", "Category One Dish Meal", "Category Meat"]
    importance = [3.53, 2.88, 2.55, 1.55, 1.52]
    fig_feat = go.Figure(data=[
        go.Bar(x=features, y=importance,
               text=[f"{v:.2f}" for v in importance], textposition='outside', width=0.5)
    ])
    fig_feat.update_layout(xaxis_title="Feature", yaxis_title="Importance")
    st.plotly_chart(fig_feat, use_container_width=True)
with col14:
    pass

# --- Key Takeaways & Recommendations ---
st.markdown("""
<h1 style='text-align:center; margin-bottom: 0.5em;'>What Did We Learn? Key Takeaways & Next Steps</h1>
<div style='display: flex; justify-content: center;'>
  <div style='text-align:left; font-size:1.1em; min-width: 600px; max-width: 950px;'>
    <ul style='margin: 0 auto;'>
        <li><b>Vegetable, Pork, and Potato recipes are the most likely to be popular.</b> Focusing on these categories can help boost website traffic.</li>
        <li><b>Nutritional factors like calories, carbs, and sugar matter.</b> These features are statistically different in popular recipes, so tracking them can help spot trends.</li>
        <li><b>Precision is the best metric for this task.</b> It ensures we recommend only the most engaging recipes to users.</li>
        <li><b>Logistic Regression is a strong, interpretable model for this problem.</b> It helps us understand which features matter most.</li>
        <li><b>Serving size does not strongly influence popularity.</b> Consider exploring other features like prep time or user ratings in the future.</li>
        <li><b>Next steps:</b> Try more models, tune parameters, and add new features (like user reviews) for even better predictions.</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

# --- GitHub Link ---
st.markdown(
    """
    <div style='text-align: center; font-size: 1.1em; margin-top: 2em;'>
        For more details and the full project, visit the <a href='https://github.com/BhavyaMehra/Recipe_Popularity_Prediction' target='_blank'>GitHub</a>.
    </div>
    """,
    unsafe_allow_html=True
)