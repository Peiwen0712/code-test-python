import pandas as pd
import requests
import json


# Load apply event data into a DataFrame
apply_events = pd.read_csv('apply_events.csv')

# Define a function to get state data based on latitude and longitude
def get_state_data(lat, lon):
    url = f"https://us-state-api.herokuapp.com/?lat={lat}&lon={lon}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data['state']['name']
    else:
        return None

# Add state data to each event row using the US State API
apply_events['state'] = apply_events.apply(lambda row: get_state_data(row['geo'][1], row['geo'][0]), axis=1)

# Create a bar chart showing the distribution of events across states
plt.figure(figsize=(12, 6))
sns.countplot(data=apply_events, x='state')
plt.title('Distribution of Apply Events Across States')
plt.xlabel('State')
plt.ylabel('Number of Events')
plt.show()
