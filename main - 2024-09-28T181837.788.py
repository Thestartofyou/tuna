import csv
import matplotlib.pyplot as plt
import datetime

# Define the file where data will be stored
DATA_FILE = 'tuna_population_data.csv'

# Function to add sighting or tagging data
def add_data(date, location, tuna_count, water_temp, notes=''):
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, location, tuna_count, water_temp, notes])
    print(f"Data added: {date}, {location}, {tuna_count} tuna, {water_temp}°C")

# Function to load data from the file
def load_data():
    data = []
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Function to visualize population trends over time
def visualize_population_trend():
    data = load_data()
    dates = []
    tuna_counts = []

    for row in data:
        date = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        tuna_count = int(row[2])
        dates.append(date)
        tuna_counts.append(tuna_count)
    
    # Plotting the data
    plt.figure(figsize=(10, 5))
    plt.plot(dates, tuna_counts, marker='o', linestyle='-', color='b')
    plt.title('Bluefin Tuna Sightings/Taggings Over Time')
    plt.xlabel('Date')
    plt.ylabel('Tuna Count')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Sample Usage
if __name__ == "__main__":
    # Uncomment below to add data entries:
    # add_data('2024-09-28', 'Gulf of Maine', 15, 19.5, 'Sighted near fishing boats')
    # add_data('2024-09-29', 'Outer Banks', 10, 22.1, 'Tagged 5 Bluefin Tuna')

    # Visualize population trends
    visualize_population_trend()
