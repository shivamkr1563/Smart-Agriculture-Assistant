# Configuration File for Smart Agriculture Web App
# Modify these settings to customize the application

# ==================== CROP CONFIGURATION ====================

# Crop prices per kg (in USD)
CROP_PRICES = {
    'rice': 0.40,
    'maize': 0.35,
    'chickpea': 0.80,
    'pigeonpeas': 0.90,
    'mothbeans': 0.75,
    'cotton': 4.50,
    'sugarcane': 0.15,
    'wheat': 0.45,
    'barley': 0.40,
    'sorghum': 0.35,
    'apple': 2.50,
    'banana': 1.00,
    'blackgram': 0.75,
    'coconut': 3.00,
    'coffee': 5.00,
    'grapes': 2.00,
    'jute': 1.50,
    'kidneybeans': 1.20,
    'lentil': 1.10,
    'mango': 1.80,
    'mungbean': 0.95,
    'muskmelon': 1.50,
    'orange': 0.80,
    'papaya': 1.20,
    'pomegranate': 2.50,
    'watermelon': 0.50
}

# Average yield in kg per hectare for each crop
CROP_YIELD = {
    'rice': 2500,
    'maize': 4000,
    'chickpea': 1200,
    'pigeonpeas': 1500,
    'mothbeans': 1000,
    'cotton': 2500,
    'sugarcane': 60000,
    'wheat': 2500,
    'barley': 2000,
    'sorghum': 1800,
    'apple': 15000,
    'banana': 40000,
    'blackgram': 1000,
    'coconut': 10000,
    'coffee': 2000,
    'grapes': 20000,
    'jute': 2500,
    'kidneybeans': 1500,
    'lentil': 1200,
    'mango': 8000,
    'mungbean': 1000,
    'muskmelon': 20000,
    'orange': 15000,
    'papaya': 25000,
    'pomegranate': 8000,
    'watermelon': 30000
}

# ==================== MODEL CONFIGURATION ====================

# Random Forest Model Parameters
MODEL_PARAMS = {
    'n_estimators': 100,          # Number of trees
    'max_depth': 20,              # Maximum tree depth
    'min_samples_split': 5,       # Minimum samples to split
    'min_samples_leaf': 2,        # Minimum samples in leaf
    'random_state': 42,           # For reproducibility
    'n_jobs': -1                  # Use all processors
}

# Data split configuration
DATA_CONFIG = {
    'test_size': 0.2,             # Test set percentage
    'random_state': 42,           # Random seed
    'random_state': 42
}

# ==================== INPUT VALIDATION RANGES ====================

INPUT_RANGES = {
    'N': {'min': 0, 'max': 150, 'unit': 'mg/kg'},
    'P': {'min': 0, 'max': 150, 'unit': 'mg/kg'},
    'K': {'min': 0, 'max': 200, 'unit': 'mg/kg'},
    'temperature': {'min': 10, 'max': 45, 'unit': '°C'},
    'humidity': {'min': 0, 'max': 100, 'unit': '%'},
    'ph': {'min': 3.5, 'max': 8.5, 'unit': 'scale'},
    'rainfall': {'min': 0, 'max': 500, 'unit': 'mm'}
}

# ==================== PROFIT CALCULATION ====================

# Cost estimation as percentage of revenue (0-100)
COST_PERCENTAGE = 40  # 40% of revenue

# ==================== FILE PATHS ====================

DATA_FILE = 'data.csv'
MODEL_FILE = 'crop_model.pkl'
ENCODER_FILE = 'label_encoder.pkl'

# ==================== STREAMLIT UI CONFIGURATION ====================

STREAMLIT_CONFIG = {
    'page_title': '🌾 Smart Agriculture Assistant',
    'page_icon': '🌾',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded'
}

# ==================== FEATURE NAMES ====================

FEATURE_NAMES = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# ==================== NOTES ====================

"""
HOW TO USE THIS FILE:

1. To change crop prices:
   - Modify the CROP_PRICES dictionary
   - Example: 'rice': 0.50  (changed from 0.40)

2. To adjust crop yields:
   - Modify the CROP_YIELD dictionary
   - Example: 'wheat': 3000  (changed from 2500)

3. To tune ML model:
   - Modify MODEL_PARAMS
   - Increase n_estimators for better accuracy (slower)
   - Decrease max_depth to prevent overfitting
   - Retrain model after changes: python model.py

4. To change cost percentage:
   - Modify COST_PERCENTAGE
   - Example: COST_PERCENTAGE = 35  (35% cost)

5. To add new crop:
   - Add to CROP_PRICES: 'newcrop': price
   - Add to CROP_YIELD: 'newcrop': yield
   - Add sample data to data.csv
   - Retrain model: python model.py

6. To modify input ranges:
   - Edit INPUT_RANGES dictionary
   - Example: 'N': {'min': 0, 'max': 200, ...}
   - Update validation in model.py validate_input()

7. After any configuration changes:
   - Delete model files: crop_model.pkl, label_encoder.pkl
   - Retrain model: python model.py
   - Restart app: streamlit run app.py
"""
