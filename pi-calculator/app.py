from flask import Flask, render_template, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pi')
def get_pi():
    """Return π value and related calculations"""
    pi_value = math.pi
    return jsonify({
        'pi': pi_value,
        'pi_rounded': round(pi_value, 10),
        'pi_string': str(pi_value),
        'circumference_unit_circle': 2 * pi_value,
        'area_unit_circle': pi_value,
    })

@app.route('/api/pi/<int:decimals>')
def get_pi_decimals(decimals):
    """Return π rounded to specified decimal places"""
    if decimals < 0 or decimals > 15:
        return jsonify({'error': 'Decimals must be between 0 and 15'}), 400
    
    pi_value = math.pi
    return jsonify({
        'pi': round(pi_value, decimals),
        'decimals': decimals
    })

@app.route('/api/circle/<float:radius>')
def circle_calculations(radius):
    """Calculate circle properties for a given radius"""
    if radius < 0:
        return jsonify({'error': 'Radius must be positive'}), 400
    
    pi_value = math.pi
    return jsonify({
        'radius': radius,
        'circumference': 2 * pi_value * radius,
        'area': pi_value * radius ** 2,
        'diameter': 2 * radius
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
