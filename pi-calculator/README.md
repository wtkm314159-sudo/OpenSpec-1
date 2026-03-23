# π Calculator Web Application

A simple yet elegant web application built with Flask to calculate and explore the mathematical constant π (pi).

## Features

- **π Display**: Shows the value of π with up to 15 decimal places
- **Custom Decimal Places**: Calculate π rounded to any number of decimal places (0-15)
- **Circle Calculations**: Given a radius, calculate:
  - Diameter
  - Circumference
  - Area

## Project Structure

```
pi-calculator/
├── app.py                 # Flask application with API endpoints
├── templates/
│   └── index.html        # Web interface
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Navigate to the project directory:
   ```bash
   cd pi-calculator
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. The application will load, displaying π and its properties.

## API Endpoints

### GET `/api/pi`
Returns the value of π and related calculations.

**Response:**
```json
{
  "pi": 3.141592653589793,
  "pi_rounded": 3.1415926536,
  "pi_string": "3.141592653589793",
  "circumference_unit_circle": 6.283185307179586,
  "area_unit_circle": 3.141592653589793
}
```

### GET `/api/pi/<decimals>`
Returns π rounded to a specified number of decimal places.

**Parameters:**
- `decimals` (integer, 0-15): Number of decimal places

**Response:**
```json
{
  "pi": 3.1416,
  "decimals": 4
}
```

### GET `/api/circle/<radius>`
Calculates circle properties for a given radius.

**Parameters:**
- `radius` (float): The radius of the circle

**Response:**
```json
{
  "radius": 5,
  "circumference": 31.41592653589793,
  "area": 78.53981633974483,
  "diameter": 10
}
```

## Usage Examples

### From the Web Interface
1. View π with up to 10 decimal places by default
2. Adjust decimal places and click "Calculate" for custom precision
3. Enter a radius value and click "Calculate" to get circle properties

### From the Command Line (curl)
```bash
# Get π value
curl http://localhost:5000/api/pi

# Get π with 5 decimal places
curl http://localhost:5000/api/pi/5

# Get circle calculations for radius 7
curl http://localhost:5000/api/circle/7
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: RESTful JSON API

## Notes

- π values are calculated using Python's built-in `math.pi` constant
- The application supports decimal precision up to 15 decimal places
- Circle calculations are based on standard geometric formulas

## License

Feel free to use this application for educational and personal purposes.
