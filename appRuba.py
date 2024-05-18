import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import matplotlib as plt
import seaborn as sns
from streamlit_option_menu import option_menu
from streamlit_vizzu import VizzuChart, Data, Config, Style

villas_df = pd.read_csv('Clean Data\clean_aqqar_villas2.csv')
land_df = pd.read_csv('Clean Data\clean_land.csv')
appartment_df = pd.read_csv('Clean Data\clean_real_estate.csv')



with st.sidebar:
    selected = option_menu(
        menu_title = "Menu",
        options = ["Home", "Appartments", "Villas", "Lands"],
        default_index = 0
    )


if selected == "Home":
        st.title(f"Welcome to the Home ")
        st.markdown('## Introduction :')
        st.write("Riyadh, the dynamic capital of Saudi Arabia, presents a wealth of opportunities in its real estate market. From sprawling lands awaiting development to luxurious villas and state-of-the-art apartments, the city caters to every preference and lifestyle. Let’s dive into what makes each of these real estate types a worthy consideration for investors and future residents alike.")
        
        st.markdown('## Data Overview :')
        st.write("to be filled")
        
        """st.markdown('## Discrption :')
        st.write("to be filled")"""

    
if selected == "Appartments":
    
    st.title(f"Welcome to the {selected} page")
    st.markdown('## Introduction :')
    st.write("to be filled")

    
    # comment....
    real_estate_location = appartment_df['location'].value_counts()
    fig = px.pie(real_estate_location, values=real_estate_location.values, names=real_estate_location.index, title='Percentage of appartment in Riyadh Proviance')
    st.plotly_chart(fig)
    st.write("to be filled")

    # comment....
    price_avg = appartment_df[['price', 'location']]
    price_avg =price_avg.groupby('location').mean('price')
    price_avg = price_avg.sort_values(by='price', ascending=False)
    fig = px.bar(price_avg, x=price_avg.index, y='price', title='Average Price per Location', color_discrete_sequence=['#0064ce'])
    st.plotly_chart(fig)
    st.write("to be filled")
    


if selected == "Villas":
    
    st.title(f"Welcome to the {selected} page")
    
    st.markdown('## Introduction :')
    st.write("to be filled")
    ##
    st.header("Chart 1 Title")
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
                    "colorPalette": "#b41204",
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

    ####################
    # comment....
    villas_location = villas_df['location'].value_counts()
    fig = px.pie(villas_location, values=villas_location.values, names=villas_location.index, title='Percentage of Villas in Riyadh Proviance')
    st.plotly_chart(fig)
    st.write("to be filled")
    
    
    # comment ...............
    price_avg = villas_df[['price', 'location']]
    price_avg = price_avg.groupby('location').mean('price')
    price_avg = price_avg.sort_values(by='price', ascending=False)
    fig = px.bar(price_avg, x=price_avg.index, y='price', title='Average Price per Location', color_discrete_sequence=['#0064ce'])
    st.plotly_chart(fig)
    st.write("to be filled")
    
    
    hood_avg = villas_df.groupby('neighbourhood')['square price'].mean().reset_index()
    hood_avg = hood_avg.sort_values(by='square price', ascending=False)
    fig = px.bar(hood_avg[:10], x='neighbourhood', y='square price', title='Sample Bar Chart', color_discrete_sequence=['#0064ce'])
    st.plotly_chart(fig)
    
    fig = px.bar(hood_avg[-10:], x='neighbourhood', y='square price', title='Sample Bar Chart', color_discrete_sequence=['#0064ce'])
    st.plotly_chart(fig)
    

    
    """plt.figure(figsize=(8, 6))
    sns.histplot(villas_df['square price'], kde=True, bins=50)
    plt.xlabel('Price per Square Foot (USD)')
    plt.ylabel('Count')
    plt.title('Distribution of Square Price')
    plt.axvline(villas_df['square price'].median(), color='red', linestyle='--', label='Median')
    plt.text(80, 5000, f"Median price per sq. ft.: {villas_df['square price'].median():.2f} USD")
    st.pyplot(plt)""" 
    st.title("Streamlit Bar Chart with Tags")

    st.header("Filter by Tags")
    unique_tags = set(tag for tag in villas_df['location'])
    selected_tags = st.multiselect("Select tags", options=list(unique_tags), default=list(unique_tags))

    # Filter data based on selected tags
    def filter_by_tags(row, tags):
        return row in tags

    filtered_df = villas_df[villas_df['location'].apply(lambda x: filter_by_tags(x, selected_tags))]

    # Group by 'location' and calculate the mean price
    mean_price_df = filtered_df.groupby('location', as_index=False)['price'].mean()

    # Create bar chart using Plotly
    fig = px.bar(mean_price_df, x='location', y='price', title='Mean Price by Location', labels={'price': 'Mean Price'})

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig)

    

if selected == "Lands":
    
    st.title(f"Welcome to the {selected} page")
    st.markdown('## Introduction :')
    st.write("to be filled")
    
    # Average Square Price per Square Meter by City 
    avg_price_per_sq_meter = land_df.groupby('المدينة')['سعر المتر'].mean().reset_index()
    avg_price_per_sq_meter = avg_price_per_sq_meter.sort_values(by='سعر المتر', ascending=False)
    fig = px.bar(avg_price_per_sq_meter, x='المدينة', y='سعر المتر',
                    title='Average Square Price per Square Meter by City')
    st.plotly_chart(fig)
    st.write("to be filled")


    # The 10 most expensive neighborhoods in Riyadh 
    land_riyadh = land_df[land_df['المدينة'] == 'الرياض']
    avg_price_per_sq_meter = land_riyadh.groupby('الحي')['سعر المتر'].mean().reset_index()
    avg_price_per_sq_meter = avg_price_per_sq_meter.sort_values(by='سعر المتر', ascending=False)
    fig = px.bar(avg_price_per_sq_meter[:10], x='الحي', y='سعر المتر',
                    title='The 10 most expensive neighborhoods in Riyadh')    
    st.plotly_chart(fig)
    st.write("to be filled")
    
    
    # The 10 cheapest neighborhoods in Riyadh 
    fig = px.bar(avg_price_per_sq_meter[:10], x='الحي', y='سعر المتر',
                    title='The 10 cheapest neighborhoods in Riyadh')
    st.plotly_chart(fig)
    st.write("to be filled")
    
    
    # 
    avg_price_per_perpuse = land_df.groupby('الغرض')['سعر المتر'].mean().reset_index()
    avg_price_per_perpuse = avg_price_per_perpuse.sort_values(by='سعر المتر', ascending=False)
    fig = px.bar(avg_price_per_perpuse, x='الغرض', y='سعر المتر',
                    title='Average Square Meter Price by Purpose')
    st.plotly_chart(fig)
    st.write("to be filled")

########################################################################################################################################  
st.title("Villas price")

# Create a slider to select a range of prices
price_range = st.slider(
    "Select price range:",
    min_value=int(villas_df['price'].min()), 
    max_value=int(villas_df['price'].max()),
    value=[int(villas_df['price'].min()), int(villas_df['price'].max())],
    step=10000
)

# Filter the DataFrame based on the selected price range
filtered_df = villas_df[(villas_df['price'] >= price_range[0]) & (villas_df['price'] <= price_range[1])]

# Display an info box with the minimum selected price
st.info(f"Minimum selected price: {price_range[0]}")
st.info(f"Maximum selected price: {price_range[1]}")

# Display the selected price range
st.write(f"Selected price range: {price_range[0]} to {price_range[1]}")

max_display_rows = 100  # Set a limit for the number of rows to display
if len(filtered_df) > max_display_rows:
    st.write(f"Displaying the first {max_display_rows} rows out of {len(filtered_df)} total filtered rows.")
    filtered_df = filtered_df.head(max_display_rows)
else:
    st.write(f"Displaying all {len(filtered_df)} filtered rows.")

# Display the filtered DataFrame with additional styling
st.markdown("### Filtered Villas Data")
st.dataframe(filtered_df)

 
##########################################333



