Summary:
The analysis uses the data from CBS Statline dataset - 84918ENG (Vermeden verbruik fossiele energie en emissie CO2) - to analyze and understand how much of the share of Dutch CO2 emissions is avoided by producing electricity from renewables and which sources are driving the change. Between 2010 and 2024, the total renewable energy share increased from 3.9% to 22.2% of national emissions avoided, with solar PV contributing the most to this increase. The analysis uses relative metrics for policy relevance and accessibility to a non-technical audience.  

Environment setup: 
The assignment was done using Anaconda and Spyder IDE 
1) Download and install Anaconda from https://www.anaconda.com/
2) Create an environment - Open Anaconda prompt and run
   conda create -n cbs_env python=3.10
   conda activate cbs_env
3) Install dependencies - pip install pandas matplotlib cbsodata

Instructions to run:
1) Open Spyder - Open Anaconda prompt and run
   spyder
2) Open the main script - main.py
3) Run the script
4) #Output: image.png

Data source: 
1) CBS Statline - dataset 84918ENG. Accessed via https://opendata.cbs.nl/#/CBS/nl/navigatieScherm/thema --> Energie --> Hernieuwbare energie --> Totaalbeeld --> Vermeden verbruik fossiele energie en emissie CO2
2) The main script accesses the data live via cbsodata.get_data('84918ENG'). All the data is publicly available. 

