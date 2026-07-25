<div align="center">

💊 RxGuide AI

Intelligent HCP Targeting & Pharmaceutical Sales-Force Analytics

Python • MySQL • Machine Learning • Power BI

<br>

Turning field-call and prescription data into one clear decision:Which HCP should the sales team prioritize next—and why?

<br>



</div>

🚀 What is RxGuide AI?

Pharmaceutical sales teams regularly visit healthcare professionals, but every HCP does not offer the same opportunity.

A doctor may:

prescribe strongly despite receiving very few visits,

receive frequent calls but generate little prescription growth,

show promising recent momentum,

or be a previously valuable HCP whose activity is now declining.

RxGuide AI identifies these patterns and converts them into practical engagement recommendations.

Instead of stopping at charts, the project produces a prioritized HCP action list for the commercial team.

🎯 The Business Decision

Situation

Recommended action

High prescription value, low field coverage

Increase visit frequency

Strong value, adequate coverage

Maintain engagement

High call activity, weak response

Review call quality or reduce coverage

Valuable HCP with declining prescriptions

Start retention intervention

Strong digital response

Prioritize virtual or hybrid engagement

Low value and low growth potential

Monitor at low priority

✨ What Makes This Project Different?

Most portfolio projects stop here:

Data → Charts → Dashboard

RxGuide AI goes further:

Data
  ↓
Business Analysis
  ↓
HCP Segmentation
  ↓
Prescription-Growth Prediction
  ↓
Opportunity Scoring
  ↓
Recommended Action
  ↓
Power BI Decision Dashboard

The final output is not just what happened.

It also explains:

Which HCP matters

Why the HCP matters

How likely prescription growth is

What the field team should do next

🧠 Intelligence Layer

1. Behaviour-Based HCP Segmentation

K-Means clustering groups HCPs using:

Prescription volume

Recent prescription growth

Field-call frequency

Prescriptions per call

Samples received

Product breadth

Days since last interaction

The resulting clusters are translated into clear business segments:

Segment

Meaning

🟢 Strategic HCPs

High-value and strongly engaged

🔵 High-Potential Under-Covered

Valuable HCPs receiving insufficient attention

🟡 Growth HCPs

Moderate value with improving prescription momentum

🟠 Low-Conversion HCPs

High engagement but weak prescription response

🔴 At-Risk HCPs

Previously valuable HCPs showing decline

2. Prescription-Growth Propensity

Two classification models are compared:

Logistic Regression — interpretable baseline

Random Forest — captures non-linear behaviour

The model estimates the probability that an HCP-product combination will grow in the next month.

A chronological train-test split is used to reduce data leakage.

📊 HCP Opportunity Score

Each HCP receives an explainable priority score:

40%  Predicted Growth Probability
25%  Under-Coverage Score
20%  Current Prescription Potential
15%  Prescriptions-per-Call Efficiency

This score combines machine learning with transparent business logic, making the recommendation easy to explain to both technical and non-technical stakeholders.

🗃️ Dataset at a Glance

<div align="center">

500

50

13.7K+

17.3K+

5

HCPs

Sales Reps

Field Calls

Prescription Records

Products

</div>

The project uses six connected datasets:

Dataset

Purpose

hcps.csv

HCP specialty, segment, territory, and location

sales_reps.csv

Representative, manager, region, and territory

products.csv

Product and therapy-area information

call_activity.csv

HCP calls, channel, duration, and samples

prescriptions.csv

Monthly HCP-product prescription activity

ic_quotas.csv

Quotas, actual performance, attainment, and incentives

Dataset source: rnigam-health/healthcare-analytics

The dataset is synthetic and contains no real patient, physician, or confidential pharmaceutical-company data.

⚙️ End-to-End Architecture

flowchart LR
    A[Raw CSV Files] --> B[Python Cleaning & EDA]
    B --> C[(MySQL Database)]
    C --> D[SQL Business Analysis]
    D --> E[ML Feature Table]
    E --> F[K-Means Segmentation]
    E --> G[Growth Prediction]
    F --> H[Opportunity Score]
    G --> H
    H --> I[Recommended Actions]
    I --> J[Power BI Dashboard]

🔍 SQL Analysis

The SQL layer answers focused commercial questions such as:

Which HCPs generate the highest prescriptions?

Which high-value HCPs are under-covered?

Which representatives produce the best prescriptions-per-call ratio?

Which products are growing month over month?

Which territories show high activity but low output?

Which representatives consistently achieve quota?

How do representatives rank within their territories?

SQL concepts used

JOINs • CTEs • CASE WHEN • LAG • RANK
DENSE_RANK • Conditional Aggregation • Window Functions

📈 Power BI Dashboard

Executive Performance

Total prescriptions

Total field calls

Quota attainment

Product growth

Territory performance

Representative rankings

Prescriptions per call

HCP Intelligence

Behavioural segment distribution

High-potential under-covered HCPs

Growth probability

Opportunity score

Recommended action

HCP-level priority table

Product, specialty, territory, and representative filters

🛠️ Tech Stack

Area

Tools

Data Cleaning & EDA

Python, pandas, NumPy, Matplotlib

Database

MySQL

Business Analysis

SQL, CTEs, joins, window functions

Machine Learning

scikit-learn, K-Means, Logistic Regression, Random Forest

Dashboard

Power BI

Development

Jupyter Notebook, VS Code, Git, GitHub

📁 Repository Structure

rxguide-hcp-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   ├── 02_hcp_segmentation.ipynb
│   └── 03_growth_prediction_and_scoring.ipynb
│
├── sql/
│   ├── 01_schema_and_import.sql
│   ├── 02_business_analysis.sql
│   └── 03_analytical_views.sql
│
├── outputs/
├── powerbi/
│   └── RxGuide_AI_Dashboard.pbix
│
├── requirements.txt
├── README.md
└── LICENSE

💡 Project Value

RxGuide AI demonstrates how to connect:

Business SQL + Machine Learning + Decision Logic + Power BI

The project is designed to move beyond ordinary descriptive analytics and deliver a clear, explainable, HCP-level commercial recommendation.

👤 Author

Anupam Choubey



<div align="center">

Built to turn pharmaceutical data into better field-force decisions.

⭐ Star the repository if you find the project useful.

</div>