# Netflix Titles Data Analysis

##  Project Overview
This project explores the **Netflix Titles dataset** to analyze how Netflix’s content library has evolved over time.  
Through **data cleaning**, **exploratory data analysis (EDA)**, and **visualization**, the project uncovers insights into:
- How many titles Netflix releases each year  
- Which countries contribute the most content  
- The balance between Movies and TV Shows  
- How movie durations have changed over time  

The project demonstrates a complete end-to-end data analytics workflow — from raw data to actionable insights — using Python.


##  Data Cleaning & Preprocessing
Steps performed to ensure data quality:
1. **Removed duplicates** using `show_id`
2. **Handled missing values**
   - Dropped rows missing key fields like `title`, `duration`, `rating`
   - Filled missing categorical values (`director`, `cast`, `country`) with `"other"`
3. **Converted data types**
   - `date_added` → `datetime`
   - `type` and `rating` → `category`
4. Verified dataset integrity after cleaning



##  Exploratory Data Analysis (EDA)

###  Number of Titles Released per Year
Analyzed the growth of Netflix’s content library year by year.  
**Visualization:** Line chart showing titles released per year.  
 `visual_reports/01_number_of_titles_per_year.png`



### Top 10 Countries by Content Released
Extracted and counted country occurrences to find the top contributors to Netflix’s library.  
**Visualization:** Bar chart showing top 10 countries.  
 `visual_reports/02_top_10_countries_by_content.png`



### Movies vs TV Shows Distribution
Compared the proportion of Movies and TV Shows in the Netflix dataset.  
**Visualization:** Pie chart showing content type distribution.  
 `visual_reports/03_Distribution_of_movies_vs_tv_shows.png`



### 4 Trend of Average Movie Duration Over Years
Calculated the average duration of movies released each year to identify trends.  
**Visualization:** Line chart of average movie duration by release year.  
 `visual_reports/04_avg_movie_duration_over_years.png`


##  Key Insights
-  Netflix has shown **consistent growth** in the number of titles released each year.  
-  The **USA**, **India**, and **UK** lead in producing the most Netflix content.  
-  Movies make up the **majority** of Netflix’s catalog, though TV Shows have increased in recent years.  
-  The **average duration of movies** fluctuates over time, reflecting evolving viewer preferences.


## Key Learnings & Outcomes
- Mastered **data cleaning and preprocessing** for real-world datasets.  
- Strengthened my understanding of **EDA and data visualization** techniques.  
- Learned to translate raw data into **clear, insightful business conclusions**.  
- Improved ability to tell stories through data and create professional visual reports.  

