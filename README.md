# Chamados 911

Projeto baseado nas especificações e requisitos do do projeto 911 Calls do curso "Python for Data Science and Machine Learning Bootcamp".
Abaixo segue as especificações do projeto educacional:

For this capstone project we will be analyzing some 911 call data from Kaggle.
- Data and Setup
-- Import data visualization libraries
-- Show data frame info
- Basic Questions
-- What are the top 5 zipcodes for 911 calls?
-- What are the top 5 townships (twp) for 911 calls?
-- Take a look at the 'title' column, how many unique title codes are there?
- Creating new features
In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.
-- What is the most common Reason for a 911 call based off of this new column?
-- Now use seaborn to create a countplot of 911 calls by Reason.
-- What is the data type of the objects in the timeStamp column?
-- Use pd.to_datetime to convert the column 'timeStamp' from strings to DateTime objects.
-- Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week
-- Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week
-- Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.
-- Now do the same for Month:
-- Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame.
-- Now create a simple plot off of the dataframe indicating the count of calls per month.
-- Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. 
-- Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. 
-- Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call
-- Now let's move on to creating heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week.
-- Now create a HeatMap using this new DataFrame.
-- Now create a clustermap using this DataFrame.
-- Now repeat these same plots and operations, for a DataFrame that shows the Month as the column.
