
import streamlit as st
import pandas as pd
import plotly.express as px
# Load datasets
df1 = pd.read_csv('co2.csv')  # CO2 data
df2 = pd.read_csv('n20.csv')  # N2O data
df3 = pd.DataFrame({
    'Year': [1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860,
             1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870,
             1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880,
             1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890,
             1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900,
             1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910,
             1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920,
             1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930,
             1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940,
             1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950,
             1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960,
             1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970,
             1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
             1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,
             1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
             2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
             2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030,
             2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040,
             2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050],
    'Mixing_Ratio_Observed': [801.0, 802.0, 804.0, 805.0, 807.0, 808.0, 809.0, 811.0, 812.0, 814.0,
                              815.0, 817.0, 818.0, 820.0, 821.0, 823.0, 825.0, 826.0, 828.0, 829.0,
                              831.0, 833.0, 834.0, 836.0, 837.0, 839.0, 841.0, 842.0, 844.0, 845.0,
                              847.0, 849.0, 851.0, 853.0, 855.0, 856.0, 859.0, 861.0, 863.0, 865.0,
                              867.0, 869.0, 872.0, 874.0, 876.0, 878.0, 881.0, 883.0, 885.0, 888.0,
                              890.0, 894.0, 898.0, 902.0, 907.0, 911.0, 916.0, 920.0, 925.0, 930.0,
                              935.0, 940.0, 945.0, 950.0, 956.0, 961.0, 967.0, 972.0, 978.0, 984.0,
                              990.0, 995.0, 1001.0, 1007.0, 1013.0, 1020.0, 1026.0, 1032.0, 1038.0,
                              1044.0, 1049.0, 1055.0, 1060.0, 1066.0, 1071.0, 1076.0, 1081.0, 1086.0,
                              1091.0, 1096.0, 1102.0, 1108.0, 1113.0, 1118.0, 1123.0, 1129.0, 1134.0,
                              1141.0, 1147.0, 1154.0, 1161.0, 1169.0, 1177.0, 1188.0, 1197.0, 1207.0,
                              1217.0, 1228.0, 1239.0, 1250.0, 1263.0, 1275.0, 1288.0, 1301.0, 1314.0,
                              1328.0, 1342.0, 1357.0, 1372.0, 1387.0, 1403.0, 1418.0, 1435.0, 1451.0,
                              1467.0, 1483.0, 1499.0, 1516.0, 1533.0, 1549.0, 1566.0, 1586.0, 1606.0,
                              1626.0, 1644.68, 1658.21, 1670.6, 1682.88, 1693.24, 1704.27, 1713.9,
                              1724.42, 1735.22, 1736.51, 1741.84, 1748.8, 1751.15, 1754.32, 1765.33,
                              1772.62, 1773.48, 1771.59, 1773.19, 1777.49, 1777.53, 1774.71, 1775.16,
                              1781.81, 1787.39, 1793.87, 1799.14, 1802.9, 1717.8326884441376,
                              1724.660579493744, 1731.4884705433506, 1738.316361592957,
                              1745.1442526425617, 1751.9721436921682, 1758.8000347417747,
                              1765.6279257913811, 1772.4558168409876, 1779.283707890594,
                              1786.1115989401987, 1792.9394899898052, 1799.7673810394117,
                              1806.5952720890182, 1813.4231631386247, 1820.251054188231,
                              1827.0789452378376, 1833.9068362874441, 1840.734727337051,
                              1847.5626183866577, 1854.390509436264, 1861.2184004858714,
                              1868.0462915354789, 1874.8741825850854, 1881.7020736346918,
                              1888.5299646842983, 1895.357855733905, 1902.1857467835115,
                              1909.013637833118, 1915.841528882725, 1922.6694199323315,
                              1929.497310981938, 1936.325202031544, 1943.1530930811513,
                              1950.2201953213733, 1957.028340922205, 1963.936487524748,
                              1970.4646572795664, 1977.2925483291729]
})

import datetime
import streamlit as st
import plotly.express as px

# Assuming df1, df2, df3 are your dataframes for CO2, N2O, CH4 respectively.

# Get the current year
current_year = datetime.datetime.now().year

# Define functions for each dashboard
def dashboard1():
    st.title("CO2 Mixing Ratio Dashboard")
    
    # Convert the Year column to integer if not already
    df1['Year'] = df1['Year'].astype(int)

    min_year = int(df1['Year'].min())
    max_year = int(df1['Year'].max())  # Ensure this is an integer
    
    selected_years = st.slider(
        "Select year range:",
        min_value=min_year,
        max_value=max_year,  # Ensure this is an integer
        value=(min_year, max_year),
        step=1
    )
    
    filtered_df = df1[(df1['Year'] >= selected_years[0]) & (df1['Year'] <= selected_years[1])]
    
    fig = px.line(filtered_df, x='Year', y='PPM', title=f'CO2 Mixing Ratio from {selected_years[0]} to {selected_years[1]}')
    fig.update_xaxes(showgrid=False)  # Hide x-axis grid
    fig.update_yaxes(showgrid=False)  # Hide y-axis grid
    st.plotly_chart(fig)
    
    avg_mixing_ratio = filtered_df['PPM'].mean()
    st.subheader("Statistics")
    st.write(f"Average Mixing Ratio: {avg_mixing_ratio:.2f}")

    # Display current year PPM
    current_ppm = df1[df1['Year'] == current_year]['PPM'].values
    if current_ppm.size > 0:
        st.write(f"Current Year PPM ({current_year}): {current_ppm[0]:.2f}")
    else:
        st.write(f"No data available for the current year ({current_year}).")

def dashboard2():
    st.title("N2O Mixing Ratio Dashboard")

    # Print the column names for debugging
    st.write("Columns in df2:", df2.columns)

    # Strip whitespace from column names
    df2.columns = df2.columns.str.strip()  # Remove leading/trailing whitespace from column names

    # Ensure Year is integer type
    df2['Year'] = df2['Year'].astype(int)

    # Get min and max years
    min_year = int(df2['Year'].min())
    max_year = int(df2['Year'].max())
    
    selected_years = st.slider(
        "Select year range:",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        step=1
    )
    
    filtered_df = df2[(df2['Year'] >= selected_years[0]) & (df2['Year'] <= selected_years[1])]
    
    # Ensure the column name matches (use the correct column name)
    fig = px.line(filtered_df, x='Year', y='Mixing_Ratio_Observed', title=f'N2O Mixing Ratio from {selected_years[0]} to {selected_years[1]}')

    # Hide x and y axis grids
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    st.plotly_chart(fig)
    
    # Calculate average mixing ratio
    avg_mixing_ratio = filtered_df['Mixing_Ratio_Observed'].mean()
    st.subheader("Statistics")
    st.write(f"Average Mixing Ratio: {avg_mixing_ratio:.2f}")

    # Display current year Mixing Ratio
    current_mixing_ratio = df2[df2['Year'] == current_year]['Mixing_Ratio_Observed'].values
    if current_mixing_ratio.size > 0:
        st.write(f"Current Year Mixing Ratio ({current_year}): {current_mixing_ratio[0]:.2f}")
    else:
        st.write




def dashboard3():
    st.title("CH4 Mixing Ratio Dashboard")
    
    # Convert the Year column to integer if not already
    df3['Year'] = df3['Year'].astype(int)

    min_year = int(df3['Year'].min())
    max_year = int(df3['Year'].max())  # Ensure this is an integer
    
    selected_years = st.slider(
        "Select year range:",
        min_value=min_year,
        max_value=max_year,  # Ensure this is an integer
        value=(min_year, max_year),
        step=1
    )
    
    filtered_df = df3[(df3['Year'] >= selected_years[0]) & (df3['Year'] <= selected_years[1])]
    
    fig = px.line(filtered_df, x='Year', y='Mixing_Ratio_Observed', title=f'CH4 Mixing Ratio from {selected_years[0]} to {selected_years[1]}')
    
    # Remove grid lines
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    st.plotly_chart(fig)
    
    avg_mixing_ratio = filtered_df['Mixing_Ratio_Observed'].mean()
    st.subheader("Statistics")
    st.write(f"Average Mixing Ratio: {avg_mixing_ratio:.2f}")

    # Display current year Mixing Ratio
    current_mixing_ratio = df3[df3['Year'] == current_year]['Mixing_Ratio_Observed'].values
    if current_mixing_ratio.size > 0:
        st.write(f"Current Year Mixing Ratio ({current_year}): {current_mixing_ratio[0]:.2f}")
    else:
        st.write(f"No data available for the current year ({current_year}).")

# Create a Streamlit app
st.title('Greenhouse Gases Dashboard')

# Sidebar content: Add an image and a quote
try:
    st.sidebar.image('earth.png', use_column_width=True)
except FileNotFoundError:
    st.sidebar.error('Image not found. Please check the file path.')

st.sidebar.markdown("The Earth does not belong to us. We belong to the Earth.")
st.sidebar.markdown(
"-Marlee Matlin")
st.sidebar.markdown(
"")



# Create a sidebar with options
option = st.sidebar.selectbox('Select Dataset', ['CO2', 'N2O', 'CH4'])

# Display the appropriate dashboard based on the selection
if option == 'CO2':
    dashboard1()
elif option == 'N2O':
    dashboard2()
elif option == 'CH4':
    dashboard3()
