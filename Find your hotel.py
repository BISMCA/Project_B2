import pandas as pd
import streamlit as st
from PIL import Image
import urllib.request

#url = "https://raw.githubusercontent.com/BISMCA/Files/main/rev_sort.csv"
#rev_sort = pd.read_csv(r'C:\Users\ASUS\Desktop\BISMCA\Project B\Draft\rev_sort.csv')

url = "https://raw.githubusercontent.com/BISMCA/Files/main/rev_sorted_short.csv"
rev_sort = pd.read_csv(url)

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Files/blob/e33c2ce8dbbf2e400cee59437aa8e5c15831fe6e/sort.jpg?raw=true',
   "sort.png")
img = Image.open("sort.png")
st.image(img, caption = 'Lets Travel')


from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.title("Find your hotels")
st.write(
    """This app filters out and finds the hotels based on your requirement of stay in your hotel such as food, accommodation, commute,family friendliness, resort etc
    """)  


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    modify = st.checkbox("Add filters", value =True)

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    return df


#df = pd.read_csv(data_url)
dummy = filter_dataframe(rev_sort)
#st.dataframe(dummy)

col1,col2,col3 = st.columns(3)

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Hotel_Photos/blob/main/hotel%201.png?raw=true',
   "img1.png")

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Hotel_Photos/blob/main/hotel%202.png?raw=true',
   "img2.png")

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Hotel_Photos/blob/main/hotel%203.png?raw=true',
   "img3.png")

urllib.request.urlretrieve(
  'https://github.com/BISMCA/Hotel_Photos/blob/main/hotel%204.png?raw=true',
   "img4.png")


image1 = Image.open("img1.png")
image2 = Image.open("img2.png")
image3 = Image.open("img3.png")
image4 = Image.open("img4.png")
#Loading Hotels
with col1:
    m=0
    star_rating = dummy.iloc[m,2]
    topic = dummy.iloc[m,3]
    hotel = dummy.iloc[m,0]
    
    st.image(image1, caption= hotel, width = 100, use_column_width=100)
    st.write(hotel)
    st.write('rating:',star_rating)
    st.write('best known for:', topic)

with col3:
    m=1
    star_rating = dummy.iloc[m,2]
    topic = dummy.iloc[m,3]
    hotel2 = dummy.iloc[m,0]
    
    st.image(image2, caption= hotel2, width = 100, use_column_width=100)
    st.write(hotel2)
    st.write('rating:',star_rating)
    st.write('best known for:', topic)
    
with col1:
    m=2
    star_rating = dummy.iloc[m,2]
    topic = dummy.iloc[m,3]
    hotel3 = dummy.iloc[m,0]
    
    st.image(image3, caption= hotel3, width = 100, use_column_width=100)
    st.write(hotel3)
    st.write('rating:',star_rating)
    st.write('best known for:', topic)
    
with col3:
    m=3
    star_rating = dummy.iloc[m,2]
    topic = dummy.iloc[m,3]
    hotel4 = dummy.iloc[m,0]
    
    st.image(image4, caption= hotel4, width = 100, use_column_width=100)
    st.write(hotel4)
    st.write('rating:',star_rating)
    st.write('best known for:', topic)


