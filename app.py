import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from streamlit_option_menu import option_menu
from streamlit_vizzu import VizzuChart, Data, Config, Style
from plotly.subplots import make_subplots

villas_df = pd.read_csv('https://raw.githubusercontent.com/Sulaiman-sfh/Project-3-/master/Clean%20Data/clean_aqqar_villas2.csv')
land_df = pd.read_csv('https://raw.githubusercontent.com/Sulaiman-sfh/Project-3-/master/Clean%20Data/clean_land.csv')
appartment_df = pd.read_csv('https://raw.githubusercontent.com/Sulaiman-sfh/Project-3-/master/Clean%20Data/clean_real_estate.csv')
riy = pd.read_csv("https://raw.githubusercontent.com/Sulaiman-sfh/Project-3-/master/Clean%20Data/clean_quarter_report.csv")

risd_land = pd.read_csv("https://raw.githubusercontent.com/Sulaiman-sfh/Project-3-/master/Clean%20Data/risd_land.csv")
riy_comm1 = pd.read_csv("https://raw.githubusercontent.com/Sulaiman-sfh/Project-3-/master/Clean%20Data/riy_comm1.csv")


with st.sidebar:
    selected = option_menu(
        menu_title = "Aqqar Type",
        options = ["Home page", "Appartments", "Villas", "Lands", "Team members 🏆"],
        icons=["house-fill","building-fill","house-fill","pin-map-fill","award-fill"],
        default_index = 0

    )


if selected == "Home page":
    st.title("Exploring Riyadh's Real Estate Market opportunities")
    st.image("https://www.jacksonvillemag.com/wp-content/uploads/2020/05/Screen-Shot-2020-05-11-at-5.25.58-PM-1.png")

    st.markdown("Riyadh, the dynamic capital of Saudi Arabia, presents a wealth of opportunities in its real estate market. From sprawling lands awaiting development to luxurious villas and state-of-the-art apartments, the city caters to every preference and lifestyle. Let’s dive into what makes each of these real estate types a worthy consideration for investors and future residents alike.")
    
    st.header('Data Overview')
    st.markdown("Based on the huge market of real estate and Aqqar we decided to collect different datasets each with different real estate type (Appartments, Villas and Lands), and another one from Real Estate General Authority to compare prices.")
    

    

    meanss = riy.pivot_table(values='Meter_Price_W_Avg_IQR', index='district_ar', columns='yearnumber', aggfunc='mean').reset_index()
    # Adjust the file path and format accordingly

    st.header("Historical analysis for Riyadh Real Estate")

    loc = riy['location'].unique()
    loc = loc[loc != 'Unknown']
    loc = np.insert(loc, 0, 'الكل')

    option = st.selectbox(
    "Choose the proviance you want",loc)
    if option == 'الكل':
         filtered_riy = riy.copy()
    else:
        filtered_riy = riy[riy['location'] == option]

    district = filtered_riy['district_ar'].unique()

    selected_tags = st.multiselect("Select tags", options=list(district), default=list(district))
    # Creating the Plotly figure
    fig = go.Figure()

    for district in selected_tags:
        district_data = meanss[meanss['district_ar'] == district]
        if not district_data.empty:
            fig.add_trace(go.Scatter(x=district_data.columns[1:], y=district_data.values[0][1:], mode='lines+markers', name=district))

    # Update layout
    fig.update_layout(
        title='Meter Price Change Over the Years for Different Districts',
        xaxis_title='Year',
        yaxis_title='Meter Price',
        legend_title='District',
        width=800,
        height=600
    )

    # Show the figure
    st.plotly_chart(fig)


    #second plotly graph
    risd_mean = risd_land.pivot_table(values='Meter_Price_W_Avg_IQR', index='district_ar', columns='yearnumber', aggfunc='mean').reset_index()
    comm_mean = riy_comm1.pivot_table(values='Meter_Price_W_Avg_IQR', index='district_ar', columns='yearnumber', aggfunc='mean').reset_index()

    loc2 = riy['location'].unique()
    loc2 = loc2[loc2 != 'Unknown']
    loc2 = np.insert(loc2, 0, 'الكل')

    # Add unique key to st.selectbox
    option2 = st.selectbox("Choose the proviance you want:", loc2, key='selectbox_province')
    if option2 == 'الكل':
        filtered_riy = riy.copy()
    else:
        filtered_riy = riy[riy['location'] == option2]

    district = filtered_riy['district_ar'].unique()

    # Add unique key to st.multiselect
    selected_tags2 = st.multiselect("Select tags", options=list(district), default=list(district), key='multiselect_tags')

    fig = go.Figure()
    for district in selected_tags2:
        district_data = risd_mean[risd_mean['district_ar'] == district]
        if not district_data.empty:
            fig.add_trace(go.Scatter(x=district_data.columns[1:], y=district_data.values[0][1:], mode='lines+markers', name=district))

    fig.update_layout(
        title='Residual Estates Changes for Different Districts',
        xaxis_title='Year',
        yaxis_title='Meter Price',
        legend_title='District',
        width=800,
        height=600
    )

    st.plotly_chart(fig)



    #third plotly graph
    fig = go.Figure()
    for district in selected_tags2:
        district_data = comm_mean[comm_mean['district_ar'] == district]
        if not district_data.empty:
            fig.add_trace(go.Scatter(x=district_data.columns[1:], y=district_data.values[0][1:], mode='lines+markers', name=district))

    fig.update_layout(
        title='Commercial Estates Changes for Different Districts ',
        xaxis_title='Year',
        yaxis_title='Meter Price',
        legend_title='District',
        width=800,
        height=600
    )
    st.plotly_chart(fig)
    st.subheader("Top Districts in Riyadh and Their Meter Price Changes from 2018 to 2023")
    st.markdown("""
                - North Region: Alnakheel, 2018: 3173, 2023: 6886, Change: Increased by 117%.

                - South Region: Almarouh, 2018: 1153, 2023: 1681, Change: Increased by 46%.

                - West Region: Labn, 2018: 996, 2023: 2531, Change: Increased by 154%.

                - East Region: Qortuba, 2018: 2197, 2023: 4450, Change: Increased by 103%.

                - Central Region: Alhada, 2018: 3000, 2023: 5300, Change: Increased by 77%.""")

    st.title("Conclusion")
    st.markdown("""In conclusion, the analysis highlights significant price variations across Riyadh, offering critical insights for potential buyers and investors.
                 By leveraging detailed visualizations, users can easily compare prices and identify trends, making it a valuable tool for buyers, investors,
                 and real estate professionals. The clear presentation of data helps to understand the market dynamics, highlighting areas with the highest and lowest average prices.""")
    st.markdown("""
                - We saw that the northern of riyadh is the most expensive.
                - Found the best real estate that fits your needs.
                - Most people prefer new real estates over the old ones.
                """ )
    # st.markdown("""Additionally, the app showcases the collaborative effort of the data science team, emphasizing their roles and contributions to the project.""")


    
if selected == "Appartments":
    
    st.title(f"{selected}")
    st.markdown("""The apartment options in Riyadh are diverse, meeting a wide range of needs and budgets.
                 For the middle market, there are many newly developed residential complexes designed for comfortable living with a focus on community and convenience.
                 This segment caters primarily to young families and middle-income earners seeking a harmonious balance between affordability and access to essential facilities and services.
                 Additionally, there are also more basic apartment options available that provide essential amenities ,
                 suitable for those with more modest budgets or individuals looking for simplicity and functionality in their living spaces.
                 These apartments often prioritize affordability and practicality while still offering a comfortable living environment.""")


    # #a map showing the number of appartments in each province 
    # real_estate_location = appartment_df['location'].value_counts().reset_index()
    # real_estate_location.columns = ['location', 'count']

    # #Map coordinates
    # location_coordinates = {
    #     'شمال-الرياض': {'lat': 24.774265, 'lon': 46.738586},
    #     'جنوب-الرياض': {'lat': 24.607009, 'lon': 46.675295},
    #     'شرق-الرياض': {'lat': 24.633611, 'lon': 46.851111},
    #     'غرب-الرياض': {'lat': 24.666667, 'lon': 46.516667},
    #     'وسط-الرياض': {'lat': 24.713552, 'lon': 46.675296}
    # }

    # # Map the coordinates to the location data
    # real_estate_location['lat'] = real_estate_location['location'].map(lambda loc: location_coordinates[loc]['lat'])
    # real_estate_location['lon'] = real_estate_location['location'].map(lambda loc: location_coordinates[loc]['lon'])

    # #create the map
    # fig = px.scatter_mapbox(
    #     real_estate_location,
    #     lat='lat',
    #     lon='lon',
    #     size='count',
    #     color='location',
    #     size_max=150,
    #     zoom=10,
    #     mapbox_style='carto-positron',
    #     title='Apartment Locations in Riyadh'
    # )

    # st.plotly_chart(fig)



    #Pie chart of the number of appartments for each location
    real_estate_location = appartment_df['location'].value_counts()
    fig = px.pie(real_estate_location, values=real_estate_location.values, names=real_estate_location.index, title='Percentage of appartment in Riyadh Proviance')
    st.plotly_chart(fig)
    st.write("The pie chart illustrates the distribution of apartments across different regions in Riyadh Province. The northern region dominates the market, accounting for 53.9% of the apartments, which suggests a high concentration of residential properties in this area. The eastern region follows with 34.6%, indicating significant residential activity. The western region has 8.01% of the apartments, showing a smaller yet notable presence. The central and southern regions have the least number of apartments, with 1.91% and 1.53%, respectively. This distribution highlights the regional disparities in residential property availability within Riyadh Province.")
    
    
    #Scatter chart of area
    fig_area = px.scatter(appartment_df, x='area', y='price', 
                        title='Relationship Between Apartment Area and Price',
                        labels={'area': 'Area (sq meters)', 'price': 'Price (SAR)'}, 
                        trendline='ols')
    st.plotly_chart(fig_area)
    st.write("The scatter plot shows a moderate positive correlation between the area of the apartment and its price. Larger apartments tend to be more expensive, emphasizing the value of additional space.")
    #Scatter chart of age
    fig_age = px.scatter(appartment_df, x='age', y='price', 
                        title='Relationship Between Apartment Age and Price',
                        labels={'age': 'Age (years)', 'price': 'Price (SAR)'}, 
                        trendline='ols')
    st.plotly_chart(fig_age)
    st.write("The scatter plot shows a negative correlation between the age of the apartment and its price. Newer apartments tend to have higher prices, indicating a preference for newer properties.")


    loc = appartment_df['location'].unique()
    loc = np.insert(loc, 0, 'الكل')

    # Create a selectbox for location selection
    option = st.selectbox("Choose the location you want", loc)

    # Filter the DataFrame based on the selected option
    if option == 'الكل':
        filtered_apprts = appartment_df.copy()
    else:
        filtered_apprts = appartment_df[appartment_df['location'] == option]

    # Create and display the scatter plot for Price vs. Area
    fig_area = px.scatter(filtered_apprts, x='area', y='price', 
                        title=f'Price vs. Area for Location: {option}',
                        labels={'area': 'Area (sq meters)', 'price': 'Price (SAR)'}, 
                        trendline='ols')

    st.plotly_chart(fig_area)
    st.write("The scatter plot shows a moderate positive correlation between the area of the apartment and its price for the selected location. Larger apartments tend to be more expensive, emphasizing the value of additional space.")

    # # Show the bar chart
    # st.plotly_chart(fig)

    price_avg = appartment_df[['price', 'location']]
    price_avg =price_avg.groupby('location').mean('price')
    price_avg = price_avg.sort_values(by='price', ascending=False)
    fig = px.bar(price_avg, x=price_avg.index, y='price', title='Average Appartments Price per Location', color_discrete_sequence=['#83c9ff'])
    st.plotly_chart(fig)
    st.write("The bar chart illustrates the average apartment prices in different regions of Riyadh. The northern region has the highest average prices, exceeding 50,000 SAR, likely due to its desirable neighborhoods and amenities. The southern region shows the lowest average prices, while the eastern and western regions have similar, moderate prices. The central region maintains an average price reflecting its mixed residential and commercial nature. This chart highlights the significant price variations across Riyadh, offering valuable insights for buyers and investors.")

    #highest and lowest 
    loc = appartment_df['location'].unique()
    loc = np.insert(loc, 0, 'الكل')
    option = st.selectbox("Choose the province you want", loc)
    if option == 'الكل':
        filtered_apprts = appartment_df.copy()
    else:
        filtered_apprts = appartment_df[appartment_df['location'] == option]
    hood_avg = filtered_apprts.groupby('district')['price'].mean().reset_index()
    hood_avg = hood_avg.sort_values(by='price', ascending=False)
    # Create a subplot with 1 row and 2 columns
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Top 10 Districts with Highest Average Prices", "Lowest Average Prices for Apartments"))
    fig.add_trace(
        go.Bar(x=hood_avg['district'][:10], y=hood_avg['price'][:10], name='Top 10 Expensive Districts', marker_color='#83c9ff'),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(x=hood_avg['district'][-10:], y=hood_avg['price'][-10:], name='10 Cheapest Districts', marker_color='#0064ce'),
        row=1, col=2
    )
    fig.update_layout(height=600, width=800, title_text="Average Prices of Apartments by District")
    st.plotly_chart(fig)

    st.write("""
    The first bar chart shows the top 10 districts with the highest average prices for apartments. These districts represent areas where apartment prices are significantly higher, possibly due to various factors such as location, amenities, and demand.
    The second bar chart displays the 10 districts with the lowest average prices for apartments, highlighting areas where apartments are more affordable.
    By comparing these two charts, stakeholders can gain insights into the price distribution across different districts, which can aid in decision-making related to real estate investments and development.
    """)




    #selecting the best apartments for you
    #Create a slider to select a range of prices
    st.header("Find your perfect appartment match")
    price_range = st.slider(
        "Select price range:",
        min_value=int(appartment_df['price'].min()), 
        max_value=int(appartment_df['price'].max()),
        value=[int(appartment_df['price'].min()), int(appartment_df['price'].max())],
        step=1000
    )
    #Price range
    filtered_df = appartment_df[(appartment_df['price'] >= price_range[0]) & (appartment_df['price'] <= price_range[1])]
    #Number of beds
    beds_num = [ 1,  2, 3, 4, 5, 6, 7]
    bed_option = st.selectbox(
    "Choose the number of bedrooms you want",beds_num)
    filtered_df = filtered_df[filtered_df['beds'] == bed_option]

    #number of livings
    livings_num = [ 0.,  1.,  2.,  3.,  4., 5.]
    livings_option = st.selectbox(
    "Choose the number of living rooms you want",livings_num)
    filtered_df = filtered_df[filtered_df['livings'] == livings_option]

    #number of WC
    wc_num = [ 1, 2, 3, 4, 5]
    wc_option = st.selectbox(
    "Choose the number of bathrooms you want",wc_num)
    filtered_df = filtered_df[filtered_df['wc'] == wc_option]

    #Furnished or not
    Furnished_num = [ "Yes", "NO"]
    Furnished_option = st.selectbox(
    "Do you want it to be Furnished?",Furnished_num)
    if Furnished_option == 'Yes':
        filtered_df = filtered_df[filtered_df['furnished'] == 1]
    else:
        filtered_df = filtered_df[filtered_df['furnished'] == 0]

    district_counts = filtered_df['district'].value_counts().reset_index()
    district_counts.columns = ['district', 'count']

    fig = px.bar(district_counts, x='district', y='count', title='Frequency of District Names', color_discrete_sequence=['#83c9ff'])

    # Show the bar chart
    st.plotly_chart(fig)





if selected == "Villas":
    
    st.title(f"{selected}")
    st.markdown("""Villa prices in Riyadh vary significantly based on location, size, and amenities, reflecting the city's rapid development and increasing demand for luxury housing. 
                Key areas such as the North of Riyadh, and East of Riyadh,  are among the most sought-after, commanding higher prices due to their prime locations and high-quality infrastructure.""")

    #Graph of avg price of each province 
    data = Data()
    data.add_df(villas_df)

    chart1 = VizzuChart(key="vizzu1")
   
    chart1.feature("tooltip", True)
    chart1.animate(data)

    bubble = st.checkbox("Bubble graph")
    if not bubble:
        chart1.animate(
        Data.filter(None),
        Config(
        {
            "coordSystem": "cartesian",
            "geometry": "area",
            "x": "location",
            "y": {"set": "mean(square price)", "range": {"min": "auto", "max": "110%"}},
            "color": None,
            "lightness": None,
            "size": "mean(square price)",
            "noop": None,
            "split": False,
            "align": "none",
            "orientation": "horizontal",
            "label": "mean(square price)",
            "sort": "none",
        }
        ),
        Style(
        {
            "plot": {
                "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                "marker": {
                    "label": {
                        "numberFormat": "prefixed",
                        "maxFractionDigits": "1",
                        "numberScale": "shortScaleSymbolUS",
                    },
                    "rectangleSpacing": None,
                    "circleMinRadius": 0.005,
                    "borderOpacity": 1,
                    "colorPalette": "#83c9ff",
                },
            }
        }
        ),
        )
    else:
        chart1.animate(
        Data.filter(None),
        Config(
        {
        "coordSystem": "cartesian",
        "geometry": "circle",
        "x": None,
        "y": {"set": None, "range": {"min": "auto", "max": "auto"}},
        "color": "location",
        "lightness": None,
        "size": "mean(price)",
        "noop": None,
        "split": False,
        "align": "none",
        "orientation": "horizontal",
        "label": None,
        "sort": "byValue",
        }
        ),
        Style(
        {
        "plot": {
        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
        "marker": {
            "label": {
                "numberFormat": "prefixed",
                "maxFractionDigits": "1",
                "numberScale": "shortScaleSymbolUS",
            },
            "rectangleSpacing": None,
            "circleMinRadius": 0.005,
            "borderOpacity": 1,
            "colorPalette": "#03ae71 #f4941b #f4c204 #d49664 #f25456 #9e67ab #bca604 #846e1c #fc763c #b462ac #f492fc #bc4a94 #9c7ef4 #9c52b4 #6ca2fc #5c6ebc #7c868c #ac968c #4c7450 #ac7a4c #7cae54 #4c7450 #9c1a6c #ac3e94 #b41204",
        },
        }
        }
        ),
        )
    chart1.show()
    st.markdown("""In North Riyadh, areas such as Al Malqa and Al Nakhil feature villas priced around 4 million SAR and square price 10k SAR,
                 highlighting the premium attached to newer constructions and added amenities.
                 In contrast, East Riyadh offers more affordable options, with villas in areas like Al Munsiyah and Al Rimal priced between 2 million SAR and square price 5.9k SAR.""")
    
    # Pie chart
    villas_location = villas_df['location'].value_counts()
    fig = px.pie(villas_location, values=villas_location.values, names=villas_location.index, title='Percentage of Villas in Riyadh Proviance')
    st.plotly_chart(fig)
    st.write("""The distribution of villas across various locations in Riyadh Province.
              The west of Riyadh has a notable availability of villas,
                consistent with other locations like the east and north, indicating a balanced residential landscape across the province.""")
    
    

    #Scatter plot graph    
    x_data = villas_df['propertyAge']
    y_data = villas_df['price']
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='markers', name='Scatter Plot'))

    fig.update_layout(
        title='The relation between the property age and price',
        xaxis_title='Property Age',
        yaxis_title='Price'
    )

    st.plotly_chart(fig)
    st.markdown("When examining how the age of a property influences villa prices in Riyadh, it becomes clear that there's a relationship between the property age and the price. The relationship between villa age and price in Riyadh shows that newer properties command higher prices due to their modern features and lower maintenance costs.on other hand some buyers looking for older properties are likely motivated by lower prices and the potential for negotiating further reductions to account for renovation costs. Understanding this trend is crucial for investors and buyers in making informed decisions in Riyadh's real estate market.")
    
    
    st.markdown("Riyadh, the capital city of Saudi Arabia, is a sprawling metropolis that features a diverse range of residential properties, catering to both opulent lifestyles and more modest budgets. Here's an insightful look into the neighborhoods that host the top 10 most expensive villas based on the locations, contrasted with those offering more affordable options.")
    #the 10 most and least expensive niebourhoods in riyadh for villas
    loc = villas_df['location'].unique()
    loc = np.insert(loc, 0, 'الكل')
    option = st.selectbox(
    "Choose the proviance you want",loc)
    if option == 'الكل':
         filtered_villas = villas_df.copy()
    else:
        filtered_villas = villas_df[villas_df['location'] == option]
    
    hood_avg = filtered_villas.groupby('neighbourhood')['square price'].mean().reset_index()
    hood_avg = hood_avg.sort_values(by='square price', ascending=False)
    fig = px.bar(hood_avg[:10], x='neighbourhood', y='square price', title='The 10 most expensive neighborhoods in Riyadh')
    st.plotly_chart(fig)
    
    fig = px.bar(hood_avg[-10:], x='neighbourhood', y='square price', title='The 10 cheapest neighborhoods in Riyadh')
    st.plotly_chart(fig)

    st.markdown("These neighborhoods illustrate the diversity of Riyadh’s residential areas, from the most luxurious to more budget-friendly options, reflecting the city's growing demand for varied housing solutions. Whether seeking opulence or affordability, Riyadh's diverse neighborhoods provide something for everyone")
    

    

    

if selected == "Lands":
    
    st.title(f"{selected}")
    st.markdown("""Land holds immense value and potential within the bustling real estate market in Riyadh.
              From vast expanses awaiting development to prime parcels in strategic locations, land is a cornerstone of the city's growth and prosperity.
                Let's explore the significance of land in Riyadh's real estate landscape and the opportunities it presents for investors and developers alike.""")
    
    #Percentage of Lands in Riyadh (Top 10 Neighborhoods)
    lands_location = land_df['الحي'].value_counts()
    top_10 = lands_location.head(10)
    other_count = lands_location.sum() - top_10.sum()
    top_10['Other'] = other_count

    fig = px.pie(
        names=top_10.index, 
        values=top_10.values, 
        title='Percentage of Lands in Riyadh (Top 10 Neighborhoods)',
    )
    st.plotly_chart(fig)
    st.markdown("""This chart provides a detailed visual comparison of land availability across Riyadh's neighborhoods. 
                It serves as a valuable tool for investors, developers, and city planners, enabling them to identify key areas with significant development potential and make informed decisions about where to focus their efforts in the real estate market.""")

    # Average Square Price per Square Meter by City 
    avg_price_per_sq_meter = land_df.groupby('المدينة')['سعر المتر'].mean().reset_index()
    avg_price_per_sq_meter = avg_price_per_sq_meter.sort_values(by='سعر المتر', ascending=False)
    fig = px.bar(avg_price_per_sq_meter, x='المدينة', y='سعر المتر',
                    title='Average Square Meter Price by Region')
    st.plotly_chart(fig)
    st.write("""This chart provides a clear depiction of the variations in real estate costs across different regions. 
             Investors can utilize this data to make well-informed decisions regarding their investments and living arrangements based on the relative affordability or expense of properties in these areas. 
             Notably, Jubailah stands out with the highest average price per square meter among all the Riyadh regions, primarily due to its strategic location near the northern part of the Riyadh province.""")

    ####show the most and the least expensive lands 
    land_riyadh = land_df[land_df['المدينة'] == 'الرياض']

    avg_price_per_sq_meter = land_riyadh.groupby('الحي')['سعر المتر'].mean().reset_index()
    avg_price_per_sq_meter = avg_price_per_sq_meter.sort_values(by='سعر المتر', ascending=False)
    #Create a subplot with 1 row and 2 columns
    fig = make_subplots(rows=1, cols=2, subplot_titles=("The 10 most expensive neighborhoods in Riyadh", "The 10 cheapest neighborhoods in Riyadh"))
    #Add the bar chart for the 10 most expensive neighborhoods to the first column
    fig.add_trace(
        go.Bar(x=avg_price_per_sq_meter['الحي'][:10], y=avg_price_per_sq_meter['سعر المتر'][:10], name='Expensive Neighborhoods'),
        row=1, col=1
    )
    #Add the bar chart for the 10 cheapest neighborhoods to the second column
    fig.add_trace(
        go.Bar(x=avg_price_per_sq_meter['الحي'][-10:], y=avg_price_per_sq_meter['سعر المتر'][-10:], name='Cheapest Neighborhoods'),
        row=1, col=2
    )

    fig.update_layout(height=600, width=800, title_text="Neighborhood Prices in Riyadh")
    st.plotly_chart(fig)

    st.markdown("""These charts compare real estate prices in Riyadh's most and least expensive neighborhoods.
                 The most expensive neighborhoods have prices ranging from 6,000 to 8,000 SAR per square meter, while the cheapest range from 700 to 1,400 SAR per square meter.
                 This data helps investors make informed decisions and assists residents in choosing neighborhoods based on affordability.""")
    
  

    
    avg_price_per_perpuse = land_df.groupby('الغرض')['سعر المتر'].mean().reset_index()
    avg_price_per_perpuse = avg_price_per_perpuse.sort_values(by='سعر المتر', ascending=False)
    fig = px.bar(avg_price_per_perpuse, x='الغرض', y='سعر المتر',
                    title='Average Square Meter Price by Type')
    st.plotly_chart(fig)
    st.markdown("""This chart offers a clear visual comparison of real estate prices categorized by their different types (commercial, residential, both).
                 The particularly elevated prices of commercial properties emphasize their premium status in the market,
                 highlighting them as substantial investment prospects despite their higher price tags.""")
    

    #Select the best land for you
    st.header("Find the best land for you")
    st.markdown("Here you can find the best land depending on your selections (land Type, square meter price) to get the best neighborhoods that has the most fitting lands.")
    
    land_price_range = st.slider(
        "Select price per meter range:",
        min_value=int(land_df['سعر المتر'].min()), 
        max_value=int(land_df['سعر المتر'].max()),
        value=[int(land_df['سعر المتر'].min()), int(land_df['سعر المتر'].max())],
        step=1000
    )
    filtered_land = land_df[(land_df['سعر المتر'] >= land_price_range[0]) & (land_df['سعر المتر'] <= land_price_range[1])]

    land_type = land_df['الغرض'].unique()
    land_type = land_type[land_type != 'Unknown']

    land_type_option = st.selectbox(
    "Choose land type:",land_type)

    filtered_land = filtered_land[filtered_land['الغرض'] == land_type_option]


    lands_counts = filtered_land['الحي'].value_counts().reset_index()
    lands_counts.columns = ['الحي', 'count']

    fig = px.bar(lands_counts, x='الحي', y='count', title='Frequency of District Names', color_discrete_sequence=['#83c9ff'])

    # Show the bar chart
    st.plotly_chart(fig)





if selected == "Team members 🏆":
    card_css = """
    <style>
    .card-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: space-between;
    }

    .card {
        background-color: #83c9ff;
        border-radius: 10px;
        padding: 20px;
        color: white;
        text-align: center;
        width: 48%; /* Adjust to fit two cards per row */
        box-sizing: border-box;
    }

    .card .icon {
        font-size: 50px;
    }

    .card .name {
        font-size: 24px;
        font-weight: bold;
        margin-top: 10px;
    }

    .card .role {
        font-size: 18px;
        margin-top: 5px;
    }
    </style>
    """

    st.markdown(card_css, unsafe_allow_html=True)

    # Create the cards HTML
    card_html1 = """
    <div class="card">
        <div class="icon">👩‍🎓</div>
        <div class="name">Rand</div>
        <div class="role">Data scientist</div>
    </div>
    """
    card_html2 = """
    <div class="card">
        <div class="icon">👨‍🎓</div>
        <div class="name">Sulaiman</div>
        <div class="role">Data scientist</div>
    </div>
    """
    card_html3 = """
    <div class="card">
        <div class="icon">👩‍🎓</div>
        <div class="name">Ruba</div>
        <div class="role">Data scientist</div>
    </div>
    """

    card_html4 = """
    <div class="card">
        <div class="icon">👨‍🎓</div>
        <div class="name">Tariq</div>
        <div class="role">Data scientist</div>
    </div>
    """
    card_html5 = """
    <div class="card">
        <div class="icon">👨‍🎓</div>
        <div class="name">Rayan</div>
        <div class="role">Data scientist</div>
    </div>
    """
    # Create a container for the cards
    card_container_html = f"""
    <div class="card-container">
        {card_html1}
        {card_html2}
        {card_html3}
        {card_html4}
        {card_html5}
    </div>
    """

    # Display the card container in the Streamlit app
    st.markdown(card_container_html, unsafe_allow_html=True)