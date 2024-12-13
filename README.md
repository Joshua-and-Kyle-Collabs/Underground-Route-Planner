# London Underground Route Planner

## Overview
This project allows users to plan journeys across the London Underground network. It reads station data from an Excel file, creates individual graphs for each line, and provides an interactive interface to plan journeys using Dijkstra's algorithm. Users can input starting and destination stations, and the program will return the best route, including the stations passed and the total journey time.

## Features
- **Data Import**: The script imports data from an Excel file containing the London Underground stations, their connections, and journey times.
- **Graph Creation**: A separate graph is created for each Underground line (Bakerloo, Central, Circle, etc.) using the NetworkX library.
- **Journey Planner**: The program calculates the shortest route between two stations using Dijkstra's algorithm and outputs the stations traveled through and the total journey time.
- **Journey History**: Users can view a history of previous journeys saved in a CSV file.
- **Visualization**: The network can be visualized using Matplotlib to display a map of the Underground network.

## Prerequisites
Make sure to install the required dependencies:

```bash
pip install pandas networkx matplotlib
```

Additionally, ensure you have the Excel file (`London Underground data.xlsx`) formatted correctly with the following columns:
- `Line`: The Underground line.
- `Current Station`: The station where the journey begins.
- `Next Station`: The station connected to the current station.
- `Journey Length`: The travel time between the two stations.

## Installation
1. Clone the repository or download the script file.
2. Install the required libraries using `pip`.
3. Ensure that the `London Underground data.xlsx` file is available in the same directory as the script.
4. Run the script in your Python environment.

## Usage
Once the script is run, the following options will be provided:
1. **Option a**: Plot a new route.
    - Enter the starting station and destination.
    - If valid stations are provided, the program will calculate the best route using Dijkstra's algorithm and show the stations traveled through and the journey duration.
    - The journey details will be saved to a CSV file called `Journeys.csv`.
   
2. **Option b**: View the journey history.
    - The program will display all previously saved journeys from the `Journeys.csv` file.

## Example

### Plot a New Route
```
Would you like to a)Plot a new route? or b)See your journey history? a
Enter Starting station: Baker Street
Enter Destination: Oxford Circus
The stations travelled through are ['Baker Street', 'Bond Street', 'Oxford Circus'], The journey will take 5 minutes
```

### View Journey History
```
Would you like to a)Plot a new route? or b)See your journey history? b
['Baker Street', 'Oxford Circus', ['Baker Street', 'Bond Street', 'Oxford Circus'], 5]
```

## Contribution
Feel free to fork this repository, make improvements, or submit issues if you encounter bugs or have feature requests. Contributions are welcome!

## License
This project is open source and available under the MIT License.
