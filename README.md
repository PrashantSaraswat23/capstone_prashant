
# Chicago Crime Data Analysis & Flask Dashboard

An end-to-end data analytics project focused on analyzing Chicago crime records, identifying crime patterns, and presenting insights through an interactive Flask dashboard.

## Project Overview

This project uses Python, Pandas, NumPy, SQL, and data visualization techniques to explore crime trends, geographical distributions, arrest patterns, and statistical insights.

## Objectives

- Clean and preprocess crime datasets.
- Perform Exploratory Data Analysis (EDA).
- Analyze crime categories, yearly and monthly trends.
- Examine community areas and district-wise crime patterns.
- Perform statistical analysis and identify outliers.
- Analyze correlations between numerical variables.
- Store and query data using SQLite.
- Build an interactive Flask dashboard.

## Technology Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Database:** SQLite, SQL
- **Web Framework:** Flask
- **Frontend:** HTML, CSS
- **Environment:** Jupyter Notebook
- **Version Control:** Git, GitHub

## Project Structure

```text
Chicago-Crime-Capstone/
├── app.py
├── app/
│   ├── services/
│   ├── templates/
│   └── static/
├── data/
│   └── Chicago Datasets/
├── notebooks/
│   └── Chicago_Crime_Capstone.ipynb
├── reports/
│   ├── analysis_results/
│   ├── chicago_crime.db
│   └── chicago_crime_cleaned.csv
├── requirements.txt
└── README.md
```

## Key Analysis

1. **Crime Category Analysis** – Identify frequently reported crime types.
2. **Temporal Analysis** – Examine yearly, monthly, and weekday crime trends.
3. **Geographical Analysis** – Analyze community areas, districts, and crime hotspots.
4. **Arrest Analysis** – Examine arrest patterns and percentages.
5. **Statistical Analysis** – Calculate mean, quartiles, IQR, outliers, and correlations.

## Flask Dashboard

The Flask application presents:
- Crime analysis summaries.
- Yearly and monthly crime trends.
- Top crime categories.
- Community area analysis.
- Statistical insights and correlation results.

## Installation & Execution

**1. Clone the repository**

```bash
git clone https://github.com/PrashantSaraswat23/capstone_prashant.git
cd capstone_prashant
```

**2. Create and activate virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python app.py
```

Open in browser: `http://127.0.0.1:5000/`

## Dataset Note

The available dataset contains 498 records, predominantly from 2016 and May. It is a limited sample and should not be considered representative of all Chicago crime records. The date field does not contain actual time-of-day information, so reliable hourly analysis is not possible.

## Author

**Prashant Saraswat**

- GitHub: [PrashantSaraswat23](https://github.com/PrashantSaraswat23)
- Repository: [Chicago Crime Capstone](https://github.com/PrashantSaraswat23/capstone_prashant)
