# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql(
    """SELECT employee_id, last_name FROM employees""", conn
)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql(
    """SELECT last_name, employee_id FROM employees""", conn
)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql(
    """SELECT last_name, employee_id AS ID FROM employees""", conn
)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql(
    """
    SELECT *, 
    CASE 
        WHEN job_title = 'President' OR job_title = 'VP Sales' OR job_title = 'VP Marketing' THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
    FROM employees
""",
    conn,
)

# STEP 6
# Replace None with your code
df_name_length = None

# STEP 7
# Replace None with your code
df_short_title = None

# STEP 8
# Replace None with your code
sum_total_price = None

# STEP 9
# Replace None with your code
df_day_month_year = None