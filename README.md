# Real Estate Data Analysis Project
This project contains scripts and data for analyzing real estate information. The project is structured to include data cleaning, analysis, and visualization processes.
## Streamlit
The streamlit app will show the best real estate for you, and view data analysis<a href="https://rand-team.streamlit.app/" target="_blank">HERE</a>


## Project Structure

- `clean_aqqar_villas2.csv`: Cleaned data of Aqqar Villas.
- `clean_land.csv`: Cleaned data of land properties.
- `clean_quarter_report.csv`: Cleaned quarterly report data.
- `clean_real_estate.csv`: Cleaned real estate data including various property types.
- `app.py`: Python script for running the main application.
- `My work Project3.ipynb`: Jupyter Notebook containing the data analysis and visualization.

## Data Overview

The dataset comprises four main files, each representing different types of real estate properties and market reports:

### clean_aqqar_villas2.csv

- **Description**: Contains detailed information about Aqqar Villas.
- **Attributes**:
  - **Villa ID**: Unique identifier for each villa.
  - **Location**: Geographic location of the villa.
  - **Size (sq ft)**: Total area of the villa in square feet.
  - **Price**: Market price of the villa.
  - **Number of Bedrooms**: Total number of bedrooms in the villa.
  - **Number of Bathrooms**: Total number of bathrooms in the villa.
  - **Amenities**: List of amenities available in the villa (e.g., swimming pool, garden, garage).
  - **Year Built**: The year the villa was constructed.

### clean_land.csv

- **Description**: Provides data on land properties.
- **Attributes**:
  - **Land ID**: Unique identifier for each land property.
  - **Location**: Geographic location of the land.
  - **Size (acres)**: Total area of the land in acres.
  - **Price**: Market price of the land.
  - **Zoning Type**: Zoning classification of the land (e.g., residential, commercial, agricultural).
  - **Availability Status**: Current availability status of the land (e.g., available, sold, under contract).

### clean_quarter_report.csv

- **Description**: Includes quarterly reports of the real estate market.
- **Attributes**:
  - **Report ID**: Unique identifier for each report.
  - **Quarter**: The specific quarter of the year the report covers (e.g., Q1, Q2, Q3, Q4).
  - **Year**: The year the report was generated.
  - **Total Sales**: Total sales volume in the real estate market for the quarter.
  - **Average Price**: Average property price in the market for the quarter.
  - **Market Trends**: Analysis of market trends observed during the quarter.
  - **Region**: Geographic region covered by the report.

### clean_real_estate.csv

- **Description**: Contains various real estate properties, including apartments, houses, and commercial properties.
- **Attributes**:
  - **Property ID**: Unique identifier for each property.
  - **Type (Apartment, House, Commercial)**: Type of the property (e.g., apartment, house, commercial).
  - **Location**: Geographic location of the property.
  - **Size (sq ft)**: Total area of the property in square feet.
  - **Price**: Market price of the property.
  - **Number of Bedrooms**: Total number of bedrooms in the property (if applicable).
  - **Number of Bathrooms**: Total number of bathrooms in the property (if applicable).
  - **Year Built**: The year the property was constructed.
  - **Amenities**: List of amenities available in the property (e.g., parking, gym, security).


