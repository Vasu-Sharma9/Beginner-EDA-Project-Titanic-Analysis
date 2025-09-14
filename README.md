# Beginner - Exploratory Data Analysis (EDA) Project - Titanic Analysis

This is a practice project where I performed basic **Exploratory Data Analysis (EDA)** on the Titanic dataset using Pandas, Matplotlib, and Seaborn.

## Data Description

The Titanic dataset contains **891 passenger records** with 12 feature columns, including demographics (age, sex), ticket class, fare, number of relatives aboard, and port of embarkation.

Missing values are handled by filling missing ages with the **median age** and imputing the most frequent **embarkation point**.

---

## Exploratory Data Analysis (EDA)

### Key Tasks Performed
- **Data cleaning:** Handle missing values, duplicates  
- **Data aggregation/filtering:** Meaningful subsets (e.g., first-class passengers)  
- **Visualizations:** Survival rates by class, gender, embarkation point  
- **Pattern interpretation:** Fare-survival correlation, age distribution  
- **Summary reporting:** Concise findings report  

### Visualizations and Insights

*1. Survival Rate by Passenger Class*
Bar chart shows survival rates for 1st, 2nd, and 3rd class passengers, highlighting that first-class travelers had the highest survival probability (~62%) compared to about 24% for third-class.

![Survival Rate by Class](images/Screenshot 2025-09-14 145702.png)


*2. Age Distribution Histogram*
Illustrates that the majority of passengers were between **20 and 40 years old**, including children and elderly.

*3. Survival Rate by Gender*
Females had a significantly higher survival rate than males, consistent with the "women and children first" evacuation principle.

*4. Survivors Count by Embarkation Point*
Shows variation in survival numbers based on port of embarkation (Cherbourg, Queenstown, Southampton), possibly reflecting socioeconomic factors.

*5. Fare Distribution by Passenger Class*
Boxplot demonstrates that higher-class passengers paid notably higher fares, positively correlating with survival chances.

> **Screenshots of these plots can be found in the repository.**

---

# Tech Stack

- Python
- Pandas
- Matplotlib
- Seaborn

## Usage

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


