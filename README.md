RxGuide AI

HCP Targeting and Pharmaceutical Sales-Force Analytics

RxGuide AI is an end-to-end pharmaceutical commercial analytics project built with Python, SQL, machine learning, and Power BI.

It analyzes healthcare-professional engagement, prescription behavior, representative performance, and territory efficiency to answer one practical question:

Which HCPs should the sales team prioritize, and what action should they take next?

Business Problem

Pharmaceutical sales teams interact with many HCPs, but every interaction does not create the same value.

Some HCPs:

Prescribe heavily but receive limited engagement

Receive frequent calls but show weak prescription response

Show strong recent growth

Were previously valuable but are now declining

The goal is to help the commercial team identify these patterns and use field resources more effectively.

What This Project Does

Cleans and validates multi-table pharmaceutical data using Python

Performs business analysis using SQL, CTEs, joins, and window functions

Segments HCPs using K-Means clustering

Predicts next-month prescription growth using classification models

Generates an HCP Opportunity Score

Recommends actions such as increasing visits, maintaining engagement, or reducing low-value calls

Presents the final insights through an interactive Power BI dashboard

Project Workflow

Raw CSV Data
      ↓
Python Cleaning and EDA
      ↓
MySQL Database
      ↓
SQL Business Analysis
      ↓
Machine Learning
      ↓
Opportunity Scoring
      ↓
Power BI Dashboard

Dataset

The project uses a synthetic pharmaceutical commercial dataset containing:

File

Description

hcps.csv

HCP profiles, specialties, segments, and locations

sales_reps.csv

Representative, territory, region, and manager details

products.csv

Pharmaceutical products and therapy areas

call_activity.csv

Rep-HCP calls, channel, duration, and samples

prescriptions.csv

Monthly HCP-product prescription activity

ic_quotas.csv

Quarterly targets, attainment, and incentive outcomes

The dataset contains approximately 31,000 transactional records across calls and prescriptions.

Source: rnigam-health/healthcare-analytics

The data is synthetic and contains no real patient or confidential pharmaceutical-company information.

Machine Learning

1. HCP Segmentation

K-Means clustering groups HCPs using features such as:

Prescription volume

Recent prescription growth

Number of field calls

Prescriptions per call

Samples received

Product breadth

Days since last interaction

The clusters are converted into business-friendly segments such as:

Strategic HCPs

High-Potential Under-Covered HCPs

Growth HCPs

Low-Conversion HCPs

At-Risk HCPs

2. Prescription-Growth Prediction

Two classification models are compared:

Logistic Regression

Random Forest

The model estimates the probability that an HCP-product combination will show prescription growth in the next month.

A time-based train-test split is used to avoid data leakage.

HCP Opportunity Score

The project combines ML predictions and business metrics into an explainable priority score:

40% Growth Probability
25% Under-Coverage Score
20% Prescription Potential
15% Prescriptions-per-Call Efficiency

The score is used to recommend actions such as:

Increase visit frequency

Maintain engagement

Retention intervention

Change engagement channel

Reduce low-value calls

Monitor

SQL Analysis

The SQL layer focuses on high-value business questions:

Top HCPs by prescription volume

High-value but under-covered HCPs

Representative efficiency

Product month-over-month growth

Rep ranking within territories

High-call but low-output territories

Quarterly quota attainment

Techniques used:

JOINs • CTEs • CASE WHEN • LAG • RANK • DENSE_RANK • Window Functions

Power BI Dashboard

Commercial Performance

Total prescriptions

Total field calls

Quota attainment

Product performance

Territory performance

Representative ranking

Prescriptions per call

HCP Intelligence

HCP segment distribution

High-potential under-covered HCPs

Growth probability

Opportunity score

Recommended action

HCP-level priority table

Tech Stack

Python: pandas, NumPy, Matplotlib, scikit-learn

Database: MySQL

SQL: CTEs, joins, aggregations, window functions

Machine Learning: K-Means, Logistic Regression, Random Forest

Visualization: Power BI

Tools: Jupyter Notebook, VS Code, Git, GitHub

Repository Structure

rxguide-hcp-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   ├── 02_hcp_segmentation.ipynb
│   └── 03_growth_prediction_and_scoring.ipynb
├── sql/
│   ├── 01_schema_and_import.sql
│   ├── 02_business_analysis.sql
│   └── 03_analytical_views.sql
├── outputs/
├── powerbi/
│   └── RxGuide_AI_Dashboard.pbix
├── README.md
└── requirements.txt

Key Project Value

This project goes beyond a standard dashboard by combining:

Business SQL + behavioural segmentation + predictive modelling + actionable recommendations + Power BI

The final output is not only a set of charts. It is a prioritized HCP action list that helps a pharmaceutical sales team decide where to focus its effort.

Author

Anupam Choubey

GitHub · Project Repository

License

This project is available under the MIT License.