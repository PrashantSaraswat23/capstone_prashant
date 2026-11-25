
from flask import Blueprint, render_template

from app.services.crime_analysis import (
    get_dashboard_summary,
    get_yearly_crime_counts,
    get_top_crime_categories,
    get_monthly_crime_counts,
    get_weekday_month_heatmap,
    get_top_community_areas,
    get_hourly_crime_distribution,
    get_community_statistical_analysis,
    get_crime_correlation
)

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/dashboard")
def dashboard():

    # UC2: Dashboard Analysis
    summary = get_dashboard_summary()
    yearly_crimes = get_yearly_crime_counts()
    top_categories = get_top_crime_categories()
    monthly_crimes = get_monthly_crime_counts()
    heatmap_data = get_weekday_month_heatmap()
    community_areas = get_top_community_areas()

    # UC3: Statistical Analysis
    hourly_crimes = get_hourly_crime_distribution()
    community_stats = get_community_statistical_analysis()
    correlation_data = get_crime_correlation()

    return render_template(
        "dashboard.html",

        # UC2 data
        summary=summary,
        yearly_crimes=yearly_crimes.to_dict(orient="records"),
        top_categories=top_categories.to_dict(orient="records"),
        monthly_crimes=monthly_crimes.to_dict(orient="records"),
        heatmap_data=heatmap_data.to_dict(orient="index"),
        heatmap_columns=heatmap_data.columns.tolist(),
        community_areas=community_areas.to_dict(orient="records"),

        # UC3 data
        hourly_crimes=hourly_crimes.to_dict(orient="records"),
        community_stats=community_stats,
        correlation_data=correlation_data
    )
