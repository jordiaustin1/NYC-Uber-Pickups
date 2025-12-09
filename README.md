NYC Uber Pickups — Data Engineering & Data Analysis Project
Author: Jordi
Tools Used: Python, MySQL, Tableau, VS Code
Dataset: Uber Pickups in NYC (FiveThirtyEight)

Project Overview

This project demonstrates a complete Data Engineering + Data Analysis workflow, taking raw Uber pickups data and transforming it into a fully visualized dashboard hosted on Tableau Public.

You will find:

✔ ETL pipeline (Python → MySQL)
✔ Cleaned dataset
✔ Tableau visualizations
✔ Final dashboard
✔ Project documentation


ETL Pipeline (Python → MySQL)

Raw CSV loaded using this script:
scripts/etl_uber.py

The script:
- Reads raw CSV
- Cleans date column
- Creates MySQL table
- Inserts data row by row


Visualizations (Tableau)
The following charts were created:

1. Trips per Day
Shows demand trends across January–February.

2. Active Vehicles Over Time
Indicates driver availability patterns.

3. Trips by Base Number
Highlights the most active Uber bases.

4. Combined Dashboard
All insights assembled into one interactive dashboard.

You can view the public dashboard here:
https://public.tableau.com/app/profile/jordi.austin/viz/NYCUberPickups-MiniProject/NYCUberPickups?publish=yes


Key Insights:

- Uber demand shows strong day-to-day fluctuations.
- Weekdays generally see more activity than weekends.
- Certain bases dominate the trip volume in NYC.
- Active vehicle count correlates strongly with total trips.


How to Reproduce
1. Clone this repo:
git clone https://github.com/YOUR-USERNAME/nyc-uber-pickups.git

2. Run ETL
python scripts/etl_uber.py

3. Open Tableau Workbook
Load tableau/uber_dashboard.twbx.


Conclusion
This mini-project showcases:
- Data engineering skills (ETL, pipelines, MySQL)
- Data analytics skills (cleaning, modeling, visualization)
- Dashboard creation using Tableau Public
- Professional documentation for portfolio use
