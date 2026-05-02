# 🌾 Smart Agriculture Web App

A complete end-to-end AI-powered crop recommendation system built with Python and Streamlit. This application uses machine learning to predict the most suitable crop based on soil and environmental conditions, along with profitability analysis.

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation & Setup](#-installation--setup)
- [Running the Application](#-running-the-application)
- [How to Use](#-how-to-use)
- [System Architecture](#-system-architecture)
- [Dataset Information](#-dataset-information)
- [Model Details](#-model-details)
- [File Descriptions](#-file-descriptions)
- [Troubleshooting](#-troubleshooting)

## ✨ Features

✅ **AI-Powered Crop Prediction**
- Uses RandomForestClassifier for accurate recommendations
- Supports 10 different crop types
- Real-time predictions based on user input

✅ **Comprehensive Input Validation**
- Range checks for all parameters
- User-friendly error messages
- Guided input with help tooltips

✅ **Profitability Analysis**
- Estimates revenue based on crop prices
- Calculates costs and profit margins
- Scalable for different land areas

✅ **Beautiful UI**
- Streamlit-based responsive interface
- Multiple tabs for organization
- Professional styling and layout
- Real-time results display

✅ **Model Information Display**
- Shows model accuracy and details
- Displays supported crops
- Shows input validation ranges
- Displays crop pricing and yields

## 📁 Project Structure

```
JacobAI-assigment/
├── app.py                      # Streamlit frontend application
├── model.py                    # ML model training and prediction logic
├── data.csv                    # Dataset for training
├── crop_model.pkl              # Trained model (auto-generated)
├── label_encoder.pkl           # Label encoder (auto-generated)
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## 📦 Requirements

- Python 3.8 or higher
- pip (Python package manager)

## 🔧 Installation & Setup

### Step 1: Clone or Download the Project

```bash
cd c:\Users\shiva\Desktop\JacobAI-assigment
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

All required packages will be installed:
- `streamlit==1.28.1` - Web app framework
- `pandas==2.0.3` - Data manipulation
- `numpy==1.24.3` - Numerical computing
- `scikit-learn==1.3.0` - Machine learning
- `pickle-mixin==1.1.0` - Model serialization

### Step 4: Verify Installation

```bash
pip list
```

You should see all packages listed.

## ▶️ Running the Application

### Method 1: Using Streamlit (Recommended)

```bash
streamlit run app.py
```

This will:
1. Open your default web browser
2. Navigate to `http://localhost:8501`
3. Load the Smart Agriculture Assistant interface

### Method 2: Manual Model Training (First Time)

The model is automatically trained when `app.py` starts if not already trained. However, you can manually train it:

```bash
python model.py
```

This will:
1. Load the dataset from `data.csv`
2. Train the RandomForestClassifier
3. Display model accuracy and metrics
4. Save `crop_model.pkl` and `label_encoder.pkl`

## 🎯 How to Use

### Step 1: Navigate to the Prediction Tab

Open the application and ensure you're on the **"Predict Crop"** tab.

### Step 2: Enter Parameters

Fill in the following fields with accurate values:

| Parameter | Range | Unit | Description |
|-----------|-------|------|-------------|
| **Nitrogen (N)** | 0-150 | mg/kg | Nitrogen content in soil |
| **Phosphorus (P)** | 0-150 | mg/kg | Phosphorus content in soil |
| **Potassium (K)** | 0-200 | mg/kg | Potassium content in soil |
| **Temperature** | 10-45 | °C | Average temperature |
| **Humidity** | 0-100 | % | Relative humidity |
| **pH Level** | 3.5-8.5 | Scale | Soil pH level |
| **Rainfall** | 0-500 | mm | Annual rainfall |
| **Land Area** | 0.1-1000 | hectares | Area for cultivation |

### Step 3: Click "Predict Crop" Button

The AI model will analyze your inputs and provide:

1. **Recommended Crop** - The most suitable crop with confidence level
2. **Profit Estimation** - Including:
   - Expected yield in kg
   - Price per kg
   - Estimated revenue
   - Estimated cost
   - Estimated profit
   - Profit margin percentage

### Step 4: Review Results

All results are displayed in an easy-to-read format with:
- Color-coded success cards
- Detailed breakdowns
- Input summary table

### Step 5: Explore Other Tabs

- **Model Info Tab** - View model details and supported crops
- **About Tab** - Learn more about the application

## 🏗️ System Architecture

```
┌─────────────────────────────────────────┐
│     Streamlit Frontend (app.py)         │
│  ┌─────────────────────────────────────┐│
│  │   Input Fields & Validation         ││
│  │   Result Display & Visualization    ││
│  │   Model Information & Metrics       ││
│  └─────────────────────────────────────┘│
└─────────────────┬───────────────────────┘
                  │
         ┌────────▼────────┐
         │   Backend Logic │
         │   (model.py)    │
         │                 │
         │ • Prediction    │
         │ • Profit Calc   │
         │ • Validation    │
         └────────┬────────┘
                  │
         ┌────────▼────────────────┐
         │   ML Model Layer        │
         │                         │
         │ RandomForestClassifier  │
         │                         │
         │ crop_model.pkl          │
         │ label_encoder.pkl       │
         └────────┬────────────────┘
                  │
         ┌────────▼──────┐
         │  Data Layer   │
         │                │
         │  data.csv     │
         │  (Training)   │
         └────────────────┘
```

## 📊 Dataset Information

The dataset contains 40+ samples with the following columns:

| Column | Description | Range |
|--------|-------------|-------|
| N | Nitrogen content | 0-120 |
| P | Phosphorus content | 5-76 |
| K | Potassium content | 25-102 |
| temperature | Temperature | 15-27°C |
| humidity | Humidity | 60-99% |
| ph | pH level | 5.75-7.33 |
| rainfall | Rainfall | 48-264 mm |
| label | Crop name | 10 varieties |

### Supported Crops (10 Types)

1. Rice
2. Maize
3. Chickpea
4. Pigeonpea
5. Moth
6. Cotton
7. Sugarcane
8. Wheat
9. Barley
10. Sorghum

## 🤖 Model Details

### Model Type
**RandomForestClassifier** from scikit-learn

### Configuration
- **Number of Trees:** 100
- **Max Depth:** 20
- **Min Samples Split:** 5
- **Min Samples Leaf:** 2
- **Random State:** 42

### Data Split
- **Training Set:** 80% (32+ samples)
- **Testing Set:** 20% (8+ samples)

### Performance
- Model accuracy and detailed metrics are displayed on startup
- Classification report includes precision, recall, and F1-score

### Features (Input)
1. Nitrogen (N)
2. Phosphorus (P)
3. Potassium (K)
4. Temperature
5. Humidity
6. pH Level
7. Rainfall

### Output
- Predicted crop (one of 10 types)
- Confidence level

## 📄 File Descriptions

### `app.py`
The main Streamlit application file that handles:
- User interface and layout
- Input collection and validation
- Result display and visualization
- Model integration
- Multiple tabs for different information

**Key Functions:**
- `initialize_session_state()` - Initializes session variables
- `load_model_once()` - Loads ML model with caching
- `main()` - Main application logic

### `model.py`
Backend ML model and business logic:
- Dataset loading and preprocessing
- Model training and evaluation
- Prediction functionality
- Profit calculation
- Input validation

**Key Classes:**
- `CropRecommendationModel` - Main model class with all methods

**Key Methods:**
- `train_model()` - Trains the RandomForest classifier
- `predict_crop()` - Makes crop predictions
- `calculate_profit()` - Calculates estimated profit
- `validate_input()` - Validates user inputs
- `save_model()` - Saves trained model
- `load_model()` - Loads pre-trained model

### `data.csv`
Training dataset with 40+ samples containing:
- Soil nutrient levels (N, P, K)
- Environmental conditions (temperature, humidity, pH, rainfall)
- Target crop labels

### `requirements.txt`
Python package dependencies for the project

### `crop_model.pkl`
Auto-generated serialized Random Forest model (created after first run)

### `label_encoder.pkl`
Auto-generated label encoder for crop names (created after first run)

## 🔧 Troubleshooting

### Issue: Model not found
**Solution:** Run `python model.py` to train the model first

### Issue: "No module named 'streamlit'"
**Solution:** 
```bash
pip install -r requirements.txt
```

### Issue: Port 8501 already in use
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: Prediction fails
**Solution:**
1. Ensure all inputs are within specified ranges
2. Check that the model files exist
3. Retrain the model by running `python model.py`

### Issue: Application is slow
**Solution:**
- Increase available RAM
- Close other applications
- Try a smaller batch of data

### Issue: Invalid input error
**Solution:**
- Review the input validation ranges in the "Model Info" tab
- Ensure values are within acceptable ranges
- Use realistic soil and climate parameters

## 🚀 Enhancement Ideas

Here are some potential features to add:

1. **Database Integration** - Store historical predictions
2. **API Endpoint** - Expose prediction API for mobile apps
3. **Multi-language Support** - Support multiple languages
4. **Weather Integration** - Auto-fetch weather data
5. **Data Visualization** - Graphs and charts for analysis
6. **Crop Rotation Advice** - Recommend crop rotation schedule
7. **Export Functionality** - Export predictions to PDF/Excel
8. **User Authentication** - Login system for personalization
9. **Real-time Model Updates** - Retrain model with new data
10. **Comparative Analysis** - Compare multiple crops

## 📝 Notes

- The dataset is for demonstration purposes
- Profit calculations are estimates based on average yields and prices
- Always validate recommendations with agricultural experts
- Actual profitability depends on many factors not captured in this model
- Consider local market conditions and regulations

## 👨‍💻 Development Information

**Created:** May 2, 2026  
**Python Version:** 3.8+  
**Framework:** Streamlit 1.28.1  
**ML Library:** scikit-learn 1.3.0

## 📧 Support & Questions

For issues or questions:
1. Check the Troubleshooting section
2. Review the About tab in the application
3. Check the Model Info tab for technical details

## 📜 License

This project is provided as-is for educational and agricultural purposes.

---

**Happy Farming! 🌾 Let AI Guide Your Agricultural Decisions! 🤖**
