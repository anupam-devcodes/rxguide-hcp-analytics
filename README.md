<img
src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:2563EB,100:06B6D4&height=230&section=header&text=RxGuide%20AI&fontSize=58&fontColor=FFFFFF&animation=fadeIn&fontAlignY=35&desc=HCP%20Targeting%20%E2%80%A2%20Growth%20Propensity%20%E2%80%A2%20Sales-Force%20Intelligence&descSize=18&descAlignY=58"
width="100%"
/>

<div align="center">

Turning pharmaceutical commercial data into clear HCP engagement decisions

<br>



<br>

Which healthcare professionals should the pharmaceutical sales team prioritize next—and what action should it take?

</div>

🧭 Overview

RxGuide AI is an end-to-end pharmaceutical commercial analytics project that combines Python, MySQL, machine learning, and Power BI to improve HCP targeting and sales-force effectiveness.

It analyzes prescription behaviour, field-call activity, product performance, representative productivity, territory efficiency, and quota attainment to identify:

high-value HCPs receiving insufficient attention,

HCPs showing strong prescription-growth potential,

over-covered HCPs with weak prescription response,

previously valuable HCPs whose activity is declining,

and representatives or territories using field resources inefficiently.

The final output is an HCP-level priority list containing a behavioural segment, growth probability, opportunity score, priority tier, and recommended engagement action.

🎯 Business Decision

HCP pattern

Recommended action

High prescriptions with limited field coverage

Increase visit frequency

Strong value with adequate coverage

Maintain engagement

High call activity with weak response

Review call quality or reduce coverage

Valuable HCP with declining prescriptions

Launch retention intervention

Strong response to virtual engagement

Prioritize virtual or hybrid calls

Low value and low growth potential

Monitor at low priority

✨ Why This Project Is Different

Most analytics projects stop at:

Raw Data → Analysis → Charts → Dashboard

RxGuide AI continues until the analysis becomes a decision:

Raw Data
   ↓
Python Data Validation and EDA
   ↓
MySQL Business Analysis
   ↓
HCP Behavioural Segmentation
   ↓
Prescription-Growth Prediction
   ↓
HCP Opportunity Scoring
   ↓
Recommended Commercial Action
   ↓
Power BI Decision Dashboard

The project answers four levels of business questions:

Level

Question

Descriptive

What happened?

Diagnostic

Why did it happen?

Predictive

Which HCP-product relationships may grow next?

Prescriptive

What should the sales team do?

🧠 Intelligence Layer

1️⃣ Behaviour-Based HCP Segmentation

K-Means clustering groups HCPs using their actual prescription and engagement behaviour.

Core features

Prescription Volume
Recent Prescription Growth
Field-Call Frequency
Prescriptions per Call
Average Call Duration
Samples Received
Product Breadth
Days Since Last Interaction

The numeric clusters are converted into commercial segments:

Segment

Business interpretation

🟢 Strategic HCPs

High prescription value and strong engagement

🔵 High-Potential Under-Covered

Strong opportunity with insufficient field coverage

🟡 Growth HCPs

Moderate current value with improving momentum

🟠 Low-Conversion HCPs

Frequent calls but weak prescription response

🔴 At-Risk HCPs

Previously valuable HCPs showing recent decline

2️⃣ Prescription-Growth Propensity

The supervised-learning model estimates whether an HCP-product relationship is likely to show prescription growth in the following month.

Two models are compared:

Logistic Regression — interpretable baseline

Random Forest — captures non-linear behavioural relationships

A chronological split is used instead of a random split:

Earlier Months → Training
Later Month    → Validation
Final Month    → Testing

The final model produces:

growth_probability

The project treats this output as predictive propensity—not proof that a field call caused prescription growth.

🎯 HCP Opportunity Score

Machine-learning predictions are combined with transparent commercial indicators:

Opportunity Score
│
├── 40%  Predicted Growth Probability
├── 25%  Under-Coverage Score
├── 20%  Current Prescription Potential
└── 15%  Prescriptions-per-Call Efficiency

The final decision table contains:

Field

Purpose

hcp_id

Unique HCP identifier

product_id

Product linked to the opportunity

behaviour_segment

ML-generated HCP segment

growth_probability

Estimated next-month growth probability

opportunity_score

Combined commercial priority score

priority_tier

High, medium, or low priority

recommended_action

Suggested engagement strategy

🗃️ Dataset Snapshot

<div align="center">

👨‍⚕️ HCPs

🧑‍💼 Sales Reps

📞 Field Calls

💊 Prescription Records

🧪 Products

500

50

13.7K+

17.3K+

5

</div>

Dataset

Description

hcps.csv

HCP specialty, segment, location, and territory

sales_reps.csv

Representative, manager, region, and territory

products.csv

Pharmaceutical product and therapy-area details

call_activity.csv

HCP interactions, channel, duration, and samples

prescriptions.csv

Monthly HCP-product prescription activity

ic_quotas.csv

Quarterly targets, actual performance, and incentives

📌 Dataset source: rnigam-health/healthcare-analytics

The dataset is synthetic and contains no real patient, physician, or confidential pharmaceutical-company information.

🔄 End-to-End Architecture

flowchart LR
    A["Raw CSV Data"] --> B["Python Cleaning & EDA"]
    B --> C[("MySQL Database")]
    C --> D["SQL Business Analysis"]
    D --> E["HCP-Product-Month Feature Table"]
    E --> F["K-Means Segmentation"]
    E --> G["Growth Classification"]
    F --> H["Opportunity Scoring"]
    G --> H
    H --> I["Recommended Actions"]
    I --> J["Power BI Dashboard"]

📊 Power BI Experience

Executive Performance

Total prescriptions

Total field calls

Prescriptions per call

Quota attainment

Monthly prescription trend

Product performance

Territory performance

Representative ranking

HCP Intelligence

Behavioural segment distribution

High-potential under-covered HCPs

Prescription-growth probability

Opportunity-score distribution

Priority-tier breakdown

Recommended-action breakdown

Calls-versus-prescriptions analysis

HCP-level targeting table

Interactive filters

Region • Territory • Representative • Specialty • Product • Segment

🛠️ Technology Stack

Layer

Technologies

Data preparation

Python, pandas, NumPy

Exploratory analysis

Matplotlib, Jupyter Notebook

Database

MySQL

Business analytics

SQL, CTEs, joins, window functions

Machine learning

scikit-learn, K-Means, Logistic Regression, Random Forest

Business intelligence

Power BI

Development

VS Code, Git, GitHub

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
│   ├── hcp_segments.csv
│   ├── growth_predictions.csv
│   ├── hcp_recommendations.csv
│   └── model_evaluation.csv
│
├── powerbi/
│   └── RxGuide_AI_Dashboard.pbix
│
├── requirements.txt
├── README.md
└── LICENSE

<details>
<summary><strong>🐍 Python: Data Validation, Cleaning and EDA</strong></summary>

<br>

Python is used to prepare reliable data before it enters SQL or machine learning.

Data-quality checks

Datatype validation

Date conversion

Missing-value analysis

Duplicate detection

Primary-key uniqueness

Foreign-key validation

Invalid category detection

Numeric range checks

Outlier inspection

Focused exploratory analysis

Monthly prescription trend

Product contribution

Specialty-wise prescribing behaviour

Territory performance

Calls versus prescription volume

Face-to-face versus virtual engagement

Samples versus prescription response

Representative productivity

Prescription-growth distribution

The project avoids unnecessary charts and keeps EDA focused on decisions that support HCP targeting.

</details>

<details>
<summary><strong>🗄️ SQL: Business Analysis and Analytical Views</strong></summary>

<br>

SQL performs the main commercial analysis rather than being used only to extract data.

Business questions

Which HCPs generate the highest prescription volume?

Which high-value HCPs receive too few calls?

Which representatives achieve the best prescriptions-per-call ratio?

Which products show the strongest month-over-month growth?

Which territories have high call activity but low output?

Which representatives consistently achieve quota?

How do representatives rank within their territories?

SQL concepts demonstrated

Multi-Table JOINs
Common Table Expressions
Conditional Aggregation
CASE WHEN
LAG()
RANK()
DENSE_RANK()
Rolling Metrics
Window Functions

Core analytical views

vw_hcp_monthly_features
vw_rep_performance
vw_territory_performance
vw_product_monthly_trends

Important modelling rule

Calls and prescriptions are independently aggregated to the same grain before joining:

HCP + Product + Month

This prevents many-to-many joins from multiplying rows and inflating prescription or call metrics.

</details>

<details>
<summary><strong>🤖 Machine-Learning Methodology</strong></summary>

<br>

HCP segmentation workflow

Build one aggregated row per HCP

Select behavioural features

Handle missing values

Cap extreme outliers

Standardize numerical features

Test multiple values of k

Compare elbow and silhouette results

Visualize cluster separation using PCA

Profile clusters and assign commercial names

Growth-prediction features

Previous-Month Prescriptions
Three-Month Rolling Average
Recent Growth Rate
Current-Month Calls
Face-to-Face Call Ratio
Samples Distributed
Average Call Duration
HCP Specialty
Product
Territory
Behavioural Segment

Model evaluation

Precision

Recall

F1-score

ROC-AUC

Confusion matrix

Feature importance

The final model is selected using both predictive quality and business interpretability.

</details>

<details>
<summary><strong>🚀 Installation and Execution</strong></summary>

<br>

1. Clone the repository

git clone https://github.com/anupam-devcodes/rxguide-hcp-analytics.git
cd rxguide-hcp-analytics

2. Create a virtual environment

Windows PowerShell

python -m venv venv
venv\Scripts\Activate

macOS/Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

4. Create the MySQL database

CREATE DATABASE rxguide_analytics;
USE rxguide_analytics;

5. Run SQL files in order

sql/01_schema_and_import.sql
sql/02_business_analysis.sql
sql/03_analytical_views.sql

6. Run notebooks in order

1. notebooks/01_data_cleaning_and_eda.ipynb
2. notebooks/02_hcp_segmentation.ipynb
3. notebooks/03_growth_prediction_and_scoring.ipynb

7. Open Power BI

powerbi/RxGuide_AI_Dashboard.pbix

Update the local MySQL credentials and refresh the data model.

</details>

<details>
<summary><strong>🛡️ Analytical Safeguards</strong></summary>

<br>

The project follows several safeguards that prevent common portfolio-project mistakes:

Calls and prescriptions are aggregated before being joined

Chronological validation is used for prediction

Future information is excluded from training features

Numerical features are scaled before K-Means

Clusters are profiled before receiving business labels

Logistic Regression is retained as an interpretable baseline

Predictive association is not presented as causation

Opportunity-score weights remain transparent

No fabricated accuracy or business-impact figures are reported

</details>

<details>
<summary><strong>⚠️ Limitations</strong></summary>

<br>

The dataset is synthetic and does not represent one specific pharmaceutical company.

Prescription growth is affected by external factors not available in the dataset.

Field calls and prescriptions may be associated without proving causation.

The small product catalogue limits product-level generalization.

Opportunity-score weights require stakeholder validation before production use.

The solution is designed as an analytics portfolio project, not a regulated production system.

</details>

<details>
<summary><strong>🔮 Future Enhancements</strong></summary>

<br>

SHAP-based model explanations

Probability calibration

Model monitoring over rolling periods

Territory-capacity constraints

Next-best-channel recommendations

Automated data-quality tests

HCP drill-through dashboard

Causal or incremental-impact analysis

</details>

🏆 Project Highlights

<div align="center">

Business Analytics

Machine Learning

Decision Intelligence

Multi-table SQL analysis

HCP behavioural clustering

HCP Opportunity Score

Sales-force effectiveness

Growth-propensity prediction

Recommended actions

Product and territory trends

Time-based validation

Power BI priority dashboard

</div>

💡 Core Project Value

RxGuide AI transforms disconnected pharmaceutical data into an explainable HCP-level engagement strategy.

It demonstrates the complete analytics lifecycle:

Data Quality
   +
Business SQL
   +
Feature Engineering
   +
Machine Learning
   +
Decision Logic
   +
Power BI Storytelling

👨‍💻 Author

<div align="center">

Anupam Choubey





</div>

🙏 Acknowledgements

Synthetic dataset source: rnigam-health/healthcare-analytics

Python analytics ecosystem: pandas, NumPy, Matplotlib, and scikit-learn

Business-intelligence platform: Microsoft Power BI

The original dataset remains subject to any terms specified by its creator.

📄 License

This repository is available under the MIT License.

<div align="center">

💊 From prescription data to smarter field-force decisions

⭐ Star the repository if you find the project useful

</div>

<img
src="https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,55:2563EB,100:0F172A&height=120&section=footer"
width="100%"
/>