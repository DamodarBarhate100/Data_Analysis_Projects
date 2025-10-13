import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

netflix_df = pd.read_csv('datasets/netflix_titles.csv')

# _________ DATA CLEANING ___________
# Handling duplicate values
print('No of duplicates before handling:',netflix_df.duplicated(subset=['show_id']).sum())
netflix_df.drop_duplicates(subset=['show_id'],inplace=True)
print('No of duplicates after handling:',netflix_df.duplicated(subset=['show_id']).sum())

#  Converting data types
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'],errors='coerce')
netflix_df['type'] = netflix_df['type'].astype('category')
netflix_df['rating'] = netflix_df['rating'].astype('category')

# Handling missing values
print('No. of missing values in each column:\n',netflix_df.isna().sum())
netflix_df.dropna(subset=['show_id','title','duration','date_added','rating'],inplace=True)
netflix_df.fillna({'director':'other','cast':'other','country':'other'},inplace=True)
# Verifying
print('No. of missing values in each column:\n',netflix_df.isna().sum().sum())
print('No. of duplicate values in each column:\n',netflix_df.duplicated().sum())

# (End of data cleaning)


# ___________EXPLORATORY DATA ANALYSIS (EDA)______________

# Number of titles released per year
title_released = (netflix_df.groupby(by=['release_year'])
                  .agg(No_of_title_released=('title','count'))
                  .reset_index())
print('\n Number of title released per year:\n',title_released.head())

# Visualization
sns.lineplot(data=title_released,x='release_year',y='No_of_title_released',color='red')
plt.title('Number of title released per year',fontweight='bold')
plt.xlabel('Release Year',fontweight='bold')
plt.ylabel('Number of title',fontweight='bold')
plt.grid(True,linestyle='dashed',alpha=0.5)
plt.tight_layout()
plt.savefig('visual_reports/01_number_of_titles_per_year.png')
plt.close()


#  Top 10 countries by the most amount of content released
countries = []
def count_countries(x):
        seperator = ','
        if seperator not in x:
                countries.append(x)
        else:
                l = x.split(',')
                countries.extend(l)
        return countries

netflix_df['country'].apply(count_countries)
countries_df = pd.DataFrame(countries,columns=['country'])
countries_df['country'] = countries_df['country'].str.strip().str.title()
countries_df['country'] = countries_df[countries_df['country']!='Other']
top_10_countries = countries_df['country'].value_counts().nlargest(10).reset_index()
print("\n Top 10 countries by content:\n",top_10_countries)

# Visualtization
sns.barplot(data=top_10_countries,x='country',y='count',color='lightgreen')
plt.title("Top 10 countries by content",fontweight='bold')
plt.xlabel("Country",fontweight='bold')
plt.ylabel("No. of content released",fontweight='bold')
plt.grid(True,linestyle='dashed',alpha=0.5)
plt.tight_layout()
# plt.show()
plt.savefig('visual_reports/02_top_10_countries_by_content')
plt.close()

# Comparing Number of Movies Vs Number of TV shows using pie chart
movies_tv_shows = netflix_df['type'].value_counts()
print("\n Number of Movies and TV shows:\n",movies_tv_shows)

# Plotting Pie Chart
plt.pie(x=movies_tv_shows,
        autopct='%1.1f%%',
        colors=['#1F77B4','#FF7F0E'],
        labels=['Movies','TV-shows']
        )
plt.title('Distribution of Movies Vs Tv-Shows (1925-2021)',fontweight='bold')
plt.legend()
plt.tight_layout()
plt.savefig('visual_reports/03_Distribution_of_movies_vs_tv_shows.png')
plt.close()


# Analyzing the trend of average movies duration over the year
movie_durations_df = netflix_df[netflix_df['type']=='Movie']
movie_durations_df = movie_durations_df[['show_id','type','release_year','duration']]

movie_durations_df['duration'] = movie_durations_df['duration'].apply(lambda x: x.replace('min',''))
movie_durations_df['duration'] = pd.to_numeric(movie_durations_df['duration'])
durations_over_years = movie_durations_df.groupby(by=['release_year'])['duration'].mean().reset_index()
durations_over_years['duration'] = durations_over_years['duration'].round(2)
print("\n Average movie duration over the years:\n",durations_over_years.head())

# Visualization - Trend of average movie duration over  years
sns.lineplot(data=durations_over_years,
                x='release_year',
                y='duration',
                color='salmon',
                marker='o',
                markeredgewidth=2,
                markerfacecolor ='darkred')
plt.title('Trend of average movie duration over years',fontweight='bold',)
plt.xlabel('Release Year',fontweight='bold')
plt.ylabel('Duration',fontweight='bold')
plt.grid(True,linestyle='dashed',alpha=0.5)
plt.tight_layout()
plt.savefig('visual_reports/04_avg_movie_duration_over_years')
plt.close()
