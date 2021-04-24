# %%
import numpy as np
import pandas as pd
import streamlit as st


st.title('Python Project NYPD statistics')
st.write("This is simple project with Python using NYPD data about incidents in New York city. Dataset is about gun involving accidents in period 2006-2019. https://www1.nyc.gov/site/nypd/stats/crime-statistics/crime-statistics-landing.page")
a = pd.read_csv('NYPD_Shooting_Incident_Data__Historic_.csv',
                sep=';', header=0)
st.write('Amount of attackers by race in New York city total by years')
# FIRST CHART WITH AMOUNT OF ATTACKS WITH GUNS TOTAL OVER YEARS
suspects = pd.DataFrame({'lab': ['BLACK', 'ASIAN', 'WHITE HISPANIC', 'ASIAN / PACIFIC ISLANDER', 'BLACK HISPANIC', 'UNKNOWN'], 'Amount people attacks per race total:': [a.PERP_RACE.str.count("BLACK").sum(), a.PERP_RACE.str.count(
    "ASIAN").sum(), a.PERP_RACE.str.count("WHITE HISPANIC").sum(), a.PERP_RACE.str.count("ASIAN / PACIFIC ISLANDER").sum(), a.PERP_RACE.str.count("BLACK HISPANIC").sum(), a.PERP_RACE.str.count("UNKNOWN").sum(), ]})
st.bar_chart(suspects.set_index('lab'))


# SECOND CHART WITH AMOUNT OF VICTIMS TOTOL OVER YEARS

victims = pd.DataFrame({'lab': ['BLACK', 'ASIAN', 'WHITE HISPANIC', 'ASIAN / PACIFIC ISLANDER', 'BLACK HISPANIC', 'UNKNOWN'], 'Peole race which was attacked per race total:': [a.VIC_RACE.str.count("BLACK").sum(), a.VIC_RACE.str.count(
    "ASIAN").sum(), a.VIC_RACE.str.count("WHITE HISPANIC").sum(), a.VIC_RACE.str.count("ASIAN / PACIFIC ISLANDER").sum(), a.VIC_RACE.str.count("BLACK HISPANIC").sum(), a.VIC_RACE.str.count("UNKNOWN").sum(), ]})
st.write('Amount of victims by race in New York city total by years')
st.bar_chart(victims.set_index('lab'))


# MAP DATA,
st.write("Map of areas where acts took place")
data = pd.DataFrame({
    'lat': a.Latitude,
    'lon': a.Longitude
})


# Adding code so we can have map default to the center of the data
midpoint = (np.average(data['lat']), np.average(data['lon']))

st.map(data)

st.write('Areas with amount of attack happened trougth years')
# AREA CHART WITH AREAS WHERE IT TOOK PLACE
area = pd.DataFrame({'lab': ['QUEENS', 'BRONX', 'MANHATTAN', 'STATEN ISLAND', 'BROOKLYN'], 'AREAS': ['QUEENS', 'BRONX', 'MANHATTAN', 'STATEN ISLAND', 'BROOKLYN'], 'Areas': [
                    a.BORO.str.count("QUEENS").sum(), a.BORO.str.count("BRONX").sum(), a.BORO.str.count("MANHATTAN").sum(), a.BORO.str.count("STATEN ISLAND").sum(), a.BORO.str.count("BROOKLYN").sum()]})

st.bar_chart(area.set_index('lab'))

# GENDER COPARISON
gender = pd.DataFrame({'lab': ['MALE', 'FEMALE'], 'Gender which done the attack:': [a.PERP_SEX.str.count("M").sum(), a.PERP_SEX.str.count(
    "F").sum()]})
st.area_chart(gender.set_index('lab'))

# LINE CHART WITH ATTACKS AND TIME OF ATTACK
st.write('Number of attacks trougth years in Ney York city')
a['OCCUR_DATE'] = pd.to_datetime(a['OCCUR_DATE'], dayfirst=True)

df1 = a['OCCUR_DATE'].dt.date.value_counts()
df1.columns = ['OCCUR_DATE', 'Count']
dates = pd.date_range('2006', periods=160, freq='M')

df = pd.DataFrame(df1, index=dates)

st.area_chart(df)
st.dataframe(df1)
# CHECKBOX WITH DATAFRAME
if st.checkbox('Show dataframe'):
    st.dataframe(a)


# %%
