# Recipe Popularity Dashboard

This project is a Streamlit application designed to analyze and visualize the factors influencing recipe popularity on a website. The dashboard provides insights into recipe traffic, nutritional information, and actionable recommendations to enhance user engagement.

## Project Structure

```
streamlit-recipe-popularity-dashboard
├── src
│   └── app.py                # Main entry point for the Streamlit dashboard
├── Data
│   └── cleaned_df.csv        # Cleaned dataset containing recipe information
├── requirements.txt           # List of dependencies for the project
└── README.md                  # Documentation for the project
```

## Features

- **Data Cleaning & Preprocessing**: The dashboard performs necessary data cleaning steps, including handling missing values and correcting categorical inconsistencies.
- **Exploratory Data Analysis**: Visualizations of key nutritional features, recipe categories, and their relationship with traffic levels.
- **Predictive Modeling Insights**: Displays insights from predictive models to understand what drives recipe popularity.
- **Actionable Recommendations**: Provides recommendations based on the analysis to improve recipe engagement and traffic.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/streamlit-recipe-popularity-dashboard.git
   cd streamlit-recipe-popularity-dashboard
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Dashboard

To run the Streamlit dashboard, execute the following command in your terminal:
```
streamlit run src/app.py
```

This will start the Streamlit server, and you can view the dashboard in your web browser at `http://localhost:8501`.

## Acknowledgments

- This project utilizes data science techniques to analyze recipe popularity and enhance user engagement on recipe websites.
- Special thanks to the contributors and the community for their support and resources.