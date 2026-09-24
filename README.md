SpaceX Falcon 9 First-Stage Landing Prediction

End-to-end data science project predicting whether a SpaceX Falcon 9 first stage will land successfully. Landing success matters commercially because a reusable first stage is what makes a launch cheaper. Completed as the capstone of the IBM Data Science Professional Certificate (2023).

Pipeline
Step	Notebook	What it does
1. Data collection (API)	Lab1_Ans_jupyter-labs-spacex-data-collection-api.ipynb	Pulls launch, rocket, launchpad and core data from the SpaceX REST API
2. Data collection (web scraping)	Lab_2_Ans_jupyter-labs-webscraping.ipynb	Scrapes Falcon 9 launch records from Wikipedia with BeautifulSoup
3. Data wrangling	Lab_3_Ans_labs-jupyter-spacex-Data wrangling (1).ipynb	Cleans the data and creates the Class label (1 = landed, 0 = did not land)
4. EDA with SQL	Lab_4_Ans_jupyter-labs-eda-sql-coursera_sqllite.ipynb	SQL queries in SQLite on launch sites, payloads and outcomes
5. EDA with visualisation	Lab_5_Ans_jupyter-labs-eda-dataviz.ipynb.jupyterlite.ipynb	Charts of success vs. flight number, payload, orbit and launch site
6. Launch-site analysis	Lab_6_Ans_lab_jupyter_launch_site_location.jupyterlite.ipynb	Interactive Folium maps of launch sites, outcomes and proximities
7. Interactive dashboard	spacex_dash_app.py	Plotly Dash app: site dropdown, success pie chart, payload slider, payload vs. outcome scatter
8. Machine learning	Lab_7_Ans_SpaceX_Machine_Learning_Prediction_Part_5.jupyterlite.ipynb	Standardises features, tunes and compares four classifiers

The final presentation is in Devendra_DS-capstone_SpaceX_21Oct2023.pptx.

Results

Four classifiers were tuned with GridSearchCV (10-fold cross-validation) on an 80/20 train/test split (random_state=2).

Model	Cross-validation accuracy	Test accuracy
Logistic Regression	84.6%	83.3%
Support Vector Machine	84.8%	83.3%
Decision Tree	88.6%	94.4%
K-Nearest Neighbours	84.8%	83.3%

Best model: Decision Tree (entropy criterion, max depth 4).

Limitation: the dataset is small (90 launches), so the test set has only 18 rows. One extra correct or incorrect prediction moves test accuracy by about 5.6 points. Treat the differences between models as indicative, not conclusive. A larger dataset, repeated cross-validation and metrics such as F1 or ROC-AUC would give a more reliable comparison.

Run the dashboard
bash
pip install -r requirements.txt
python spacex_dash_app.py

Open http://127.0.0.1:8050 in your browser.

Data
SpaceX REST API: https://api.spacexdata.com/v4
Wikipedia: List of Falcon 9 and Falcon Heavy launches
spacex_launch_dash.csv (56 launches, used by the dashboard) is derived from spacex_launch_geo.csv in this repo: launch site, payload mass, outcome class and booster version.
Notes
The lab notebooks follow the IBM Skills Network capstone structure; author credits are kept in the notebooks.
Some cells that used IBM's hosted environment were re-run locally, so a few outputs may differ slightly.
Tech stack

Python, Pandas, NumPy, Scikit-learn, SQL (SQLite), Plotly, Dash, Folium, Matplotlib, Seaborn, BeautifulSoup, Requests
