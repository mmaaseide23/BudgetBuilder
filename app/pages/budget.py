import pymysql
import pandas as pd
import altair as alt

# conn = pymysql.connect(host='your-rds-endpoint', user='admin', password='password', db='your-db')
# df = pd.read_sql(\"SELECT * FROM transactions\", conn)
# conn.close()

# Plotting example
# chart = alt.Chart(df).mark_bar().encode(
#     x='gender',
#     y='amount_spent',
#     color='sector:N'
# )
# st.altair_chart(chart)