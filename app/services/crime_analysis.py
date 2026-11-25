
import pandas as pd
import numpy as np

from app.database import get_db_connection


def load_crime_data():
    """Load crime records from SQLite."""
    conn = get_db_connection()

    try:
        df = pd.read_sql_query("SELECT * FROM crime", conn)
    finally:
        conn.close()

    return df


# ---------------- UC2: EXISTING DASHBOARD ANALYSIS ----------------

def get_dashboard_summary():
    df = load_crime_data()

    total_crimes = len(df)
    total_arrests = int(df["arrest"].fillna(0).sum())

    arrest_rate = (
        round(total_arrests / total_crimes * 100, 2)
        if total_crimes else 0
    )

    return {
        "total_crimes": total_crimes,
        "total_arrests": total_arrests,
        "arrest_rate": arrest_rate,
        "crime_categories": int(df["primary_type"].nunique())
    }


def get_yearly_crime_counts():
    df = load_crime_data()

    return (
        df.groupby("year")
        .size()
        .reset_index(name="crime_count")
        .sort_values("year")
    )


def get_top_crime_categories():
    df = load_crime_data()

    result = (
        df["primary_type"]
        .dropna()
        .value_counts()
        .head(10)
        .reset_index()
    )

    result.columns = ["primary_type", "crime_count"]

    result["percentage"] = (
        result["crime_count"] / len(df) * 100
    ).round(2)

    return result

def get_monthly_crime_counts():
    df = load_crime_data()

    return (
        df.groupby("Month")
        .size()
        .reset_index(name="crime_count")
        .sort_values("Month")
    )


def get_weekday_month_heatmap():
    df = load_crime_data()

    return pd.crosstab(df["Month"], df["DayOfWeek"])


def get_top_community_areas():
    df = load_crime_data()

    result = (
        df["community_code"]
        .dropna()
        .value_counts()
        .head(10)
        .reset_index()
    )

    result.columns = ["community_code", "crime_count"]

    return result


# ---------------- UC3: STATISTICAL INSIGHTS ----------------

# 1. Crime Intensity by Time

def get_hourly_crime_distribution():
    df = load_crime_data()

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    df = df.dropna(subset=["date"])

    df["hour"] = df["date"].dt.hour

    result = (
        df.groupby("hour")
        .size()
        .reindex(range(24), fill_value=0)
        .reset_index(name="crime_count")
    )

    return result



# 2. Community Area Mean and IQR Outlier Analysis

def get_community_statistical_analysis():
    df = load_crime_data()

    community_counts = (
        df.dropna(subset=["community_code"])
        .groupby("community_code")
        .size()
        .reset_index(name="total_crimes")
        .sort_values("total_crimes", ascending=False)
    )

    crime_counts = community_counts["total_crimes"].to_numpy()

    mean_crimes = float(np.mean(crime_counts))

    q1 = float(np.percentile(crime_counts, 25))
    q3 = float(np.percentile(crime_counts, 75))

    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    outliers = community_counts[
        (community_counts["total_crimes"] < lower_bound) |
        (community_counts["total_crimes"] > upper_bound)
    ]

    return {
        "community_counts": community_counts.to_dict(orient="records"),
        "crime_count_values": crime_counts.tolist(),
        "mean_crimes": round(mean_crimes, 2),
        "q1": round(q1, 2),
        "q3": round(q3, 2),
        "iqr": round(iqr, 2),
        "lower_bound": round(lower_bound, 2),
        "upper_bound": round(upper_bound, 2),
        "outliers": outliers.to_dict(orient="records"),
        "total_community_areas": len(community_counts)
    }


# 3. Crime Cross-Correlation

def get_crime_correlation():
    df = load_crime_data()

    numeric_columns = [
        "year",
        "Month",
        "arrest",
        "domestic",
        "beat_num",
        "district_code",
        "ward_no",
        "community_code"
    ]

    available_columns = [
        col for col in numeric_columns
        if col in df.columns
    ]

    numeric_df = df[available_columns].apply(
        pd.to_numeric,
        errors="coerce"
    )

    correlation_matrix = numeric_df.corr()

    return {
        "columns": correlation_matrix.columns.tolist(),
        "matrix": correlation_matrix.round(2).values.tolist()
    }
