import pandas
import os



def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")

#if csv file is in directory
# csv_filepath = "gradebook2.csv"

csv_filepath = os.path.join(os.path.dirname(__file__), "data", "gradebook.csv")
print("Filepath:", os.path.abspath(csv_filepath))


grades = pandas.read_csv(csv_filepath)
print ("Grades:", type(grades))
print(dir(grades))
print(grades.tail())

#find av grade

grades_col = grades["final_grade"]

avg_grade = grades_col.mean()
print("AVG Grade:", avg_grade)

for index, row in grades.iterrows():
    print (index)
    print(row["final_grade"])
    #my_grades.append(row["final_grade"])

grades_list = grades.to_dict("records")
