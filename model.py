"""
model.py - Smart Agriculture ML Model
This module handles:
- Loading and preprocessing data
- Training RandomForestClassifier model
- Making crop predictions
- Calculating estimated profit
"""

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report


class CropRecommendationModel:
    """Class to handle model training, prediction, and profit calculation"""
    
    def __init__(self, model_path='crop_model.pkl', encoder_path='label_encoder.pkl'):
        """
        Initialize the model
        
        Args:
            model_path: Path to save/load the trained model
            encoder_path: Path to save/load the label encoder
        """
        self.model_path = model_path
        self.encoder_path = encoder_path
        self.model = None
        self.label_encoder = None
        self.feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        
        # Crop prices per kg (in USD)
        self.crop_prices = {
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
        self.crop_yield = {
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
    
    def load_data(self, data_path):
        """
        Load data from CSV file
        
        Args:
            data_path: Path to the CSV file
            
        Returns:
            DataFrame with loaded data
        """
        try:
            data = pd.read_csv(data_path)
            print(f"✓ Data loaded successfully. Shape: {data.shape}")
            return data
        except FileNotFoundError:
            print(f"✗ Error: File {data_path} not found")
            return None
        except Exception as e:
            print(f"✗ Error loading data: {str(e)}")
            return None
    
    def train_model(self, data_path, test_size=0.2, random_state=42):
        """
        Train the RandomForestClassifier model
        
        Args:
            data_path: Path to the CSV file
            test_size: Proportion of data to use for testing
            random_state: Random seed for reproducibility
            
        Returns:
            Model accuracy
        """
        try:
            # Load data
            data = self.load_data(data_path)
            if data is None:
                return None
            
            # Handle missing values
            data = data.dropna()
            
            # Separate features and target
            X = data[self.feature_names]
            y = data['label']
            
            # Encode target labels
            self.label_encoder = LabelEncoder()
            y_encoded = self.label_encoder.fit_transform(y)
            
            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y_encoded, test_size=test_size, random_state=random_state
            )
            
            print(f"\n📊 Dataset Split:")
            print(f"   Training set: {X_train.shape[0]} samples")
            print(f"   Testing set: {X_test.shape[0]} samples")
            
            # Create and train the RandomForestClassifier
            print("\n🌳 Training RandomForestClassifier...")
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=20,
                min_samples_split=5,
                min_samples_leaf=2,
                random_state=random_state,
                n_jobs=-1
            )
            self.model.fit(X_train, y_train)
            
            # Calculate accuracy
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            print(f"\n✓ Model Training Complete!")
            print(f"   Training Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
            
            # Print classification report
            print("\n📈 Classification Report:")
            try:
                print(classification_report(
                    y_test, y_pred,
                    target_names=self.label_encoder.classes_,
                    zero_division=0
                ))
            except Exception as e:
                print(f"   (Report skipped due to limited test samples)")
                print(f"   Accuracy: {accuracy:.4f}")
            
            # Save model and encoder
            self.save_model()
            
            return accuracy
            
        except Exception as e:
            print(f"✗ Error during model training: {str(e)}")
            return None
    
    def save_model(self):
        """Save trained model and label encoder to files"""
        try:
            with open(self.model_path, 'wb') as f:
                pickle.dump(self.model, f)
            with open(self.encoder_path, 'wb') as f:
                pickle.dump(self.label_encoder, f)
            print(f"\n💾 Model saved successfully!")
            print(f"   Model: {self.model_path}")
            print(f"   Encoder: {self.encoder_path}")
        except Exception as e:
            print(f"✗ Error saving model: {str(e)}")
    
    def load_model(self):
        """Load trained model and label encoder from files"""
        try:
            if os.path.exists(self.model_path) and os.path.exists(self.encoder_path):
                with open(self.model_path, 'rb') as f:
                    self.model = pickle.load(f)
                with open(self.encoder_path, 'rb') as f:
                    self.label_encoder = pickle.load(f)
                print("✓ Model and encoder loaded successfully")
                return True
            else:
                print("✗ Model files not found. Please train the model first.")
                return False
        except Exception as e:
            print(f"✗ Error loading model: {str(e)}")
            return False
    
    def validate_input(self, n, p, k, temperature, humidity, ph, rainfall):
        """
        Validate user input
        
        Args:
            All input parameters
            
        Returns:
            Tuple (is_valid, error_message)
        """
        errors = []
        
        # Validate nitrogen (N)
        if not (0 <= n <= 150):
            errors.append("Nitrogen (N) must be between 0-150")
        
        # Validate phosphorus (P)
        if not (0 <= p <= 150):
            errors.append("Phosphorus (P) must be between 0-150")
        
        # Validate potassium (K)
        if not (0 <= k <= 200):
            errors.append("Potassium (K) must be between 0-200")
        
        # Validate temperature
        if not (10 <= temperature <= 45):
            errors.append("Temperature must be between 10-45°C")
        
        # Validate humidity
        if not (0 <= humidity <= 100):
            errors.append("Humidity must be between 0-100%")
        
        # Validate pH
        if not (3.5 <= ph <= 8.5):
            errors.append("pH must be between 3.5-8.5")
        
        # Validate rainfall
        if not (0 <= rainfall <= 500):
            errors.append("Rainfall must be between 0-500 mm")
        
        if errors:
            return False, "; ".join(errors)
        return True, ""
    
    def predict_crop(self, n, p, k, temperature, humidity, ph, rainfall):
        """
        Predict the most suitable crop based on input parameters
        
        Args:
            All input parameters
            
        Returns:
            Predicted crop name or None if prediction fails
        """
        try:
            # Validate input
            is_valid, error_msg = self.validate_input(
                n, p, k, temperature, humidity, ph, rainfall
            )
            if not is_valid:
                return None, error_msg
            
            # Prepare input data
            input_data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
            
            # Make prediction
            prediction_encoded = self.model.predict(input_data)[0]
            prediction_proba = self.model.predict_proba(input_data)[0]
            
            # Decode prediction
            predicted_crop = self.label_encoder.inverse_transform([prediction_encoded])[0]
            confidence = max(prediction_proba) * 100
            
            return predicted_crop, f"Prediction confident at {confidence:.2f}%"
            
        except Exception as e:
            return None, f"Prediction error: {str(e)}"
    
    def calculate_profit(self, crop, area_in_hectares=1.0):
        """
        Calculate estimated profit for a given crop
        
        Args:
            crop: Crop name
            area_in_hectares: Area of cultivation in hectares (default: 1)
            
        Returns:
            Dictionary with profit details or None if crop not found
        """
        try:
            if crop not in self.crop_prices:
                return None
            
            # Get price and yield
            price_per_kg = self.crop_prices[crop]
            yield_per_hectare = self.crop_yield[crop]
            
            # Calculate total production and revenue
            total_production = yield_per_hectare * area_in_hectares
            revenue = total_production * price_per_kg
            
            # Estimate costs (rough estimation: 40% of revenue)
            estimated_cost = revenue * 0.40
            
            # Calculate profit
            estimated_profit = revenue - estimated_cost
            profit_margin = (estimated_profit / revenue * 100) if revenue > 0 else 0
            
            return {
                'crop': crop,
                'area_hectares': area_in_hectares,
                'yield_kg': total_production,
                'price_per_kg': price_per_kg,
                'revenue': revenue,
                'estimated_cost': estimated_cost,
                'estimated_profit': estimated_profit,
                'profit_margin': profit_margin
            }
            
        except Exception as e:
            print(f"✗ Error calculating profit: {str(e)}")
            return None


# Initialize model instance
model = CropRecommendationModel()


if __name__ == "__main__":
    """Main execution - train model on startup"""
    print("=" * 60)
    print("🌾 Smart Agriculture - Crop Recommendation System")
    print("=" * 60)
    
    # Train model with Crop_recommendation.csv dataset
    accuracy = model.train_model('Crop_recommendation.csv')
    
    if accuracy:
        print("\n" + "=" * 60)
        print("✓ Model is ready for predictions!")
        print("=" * 60)
