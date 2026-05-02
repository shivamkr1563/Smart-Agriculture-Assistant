"""
verify_setup.py - Verification Script
This script checks if the Smart Agriculture Web App is properly configured
Run this before starting the application to ensure everything works
"""

import sys
import os
from pathlib import Path

def print_header(title):
    """Print a formatted section header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def check_python_version():
    """Check if Python version is compatible"""
    print_header("1. Python Version Check")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    print(f"   Current Version: Python {version_str}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Status: Compatible")
        return True
    else:
        print("   ❌ Status: Not Compatible (Requires Python 3.8+)")
        return False

def check_packages():
    """Check if all required packages are installed"""
    print_header("2. Package Installation Check")
    
    packages = {
        'streamlit': '1.28.1',
        'pandas': '2.0.3',
        'numpy': '1.24.3',
        'sklearn': '1.3.0',
    }
    
    all_installed = True
    
    for package, version in packages.items():
        try:
            __import__(package if package != 'sklearn' else 'sklearn')
            print(f"   ✅ {package:<15} - Installed")
        except ImportError:
            print(f"   ❌ {package:<15} - NOT installed")
            all_installed = False
    
    if not all_installed:
        print("\n   📝 Install missing packages:")
        print("   pip install -r requirements.txt")
    
    return all_installed

def check_files():
    """Check if all required files exist"""
    print_header("3. File Structure Check")
    
    required_files = {
        'app.py': 'Streamlit UI',
        'model.py': 'ML Model',
        'data.csv': 'Training Data',
        'requirements.txt': 'Dependencies',
        'README.md': 'Documentation',
        'crop_model.pkl': 'Trained Model',
        'label_encoder.pkl': 'Label Encoder'
    }
    
    all_exist = True
    
    for filename, description in required_files.items():
        exists = os.path.exists(filename)
        status = "✅" if exists else "❌"
        print(f"   {status} {filename:<25} - {description}")
        if not exists:
            all_exist = False
    
    return all_exist

def check_model_quality():
    """Check model files and integrity"""
    print_header("4. Model Files Check")
    
    model_ok = True
    
    # Check model file
    if os.path.exists('crop_model.pkl'):
        size = os.path.getsize('crop_model.pkl')
        if size > 0:
            print(f"   ✅ crop_model.pkl - {size:,} bytes")
        else:
            print("   ❌ crop_model.pkl - File is empty")
            model_ok = False
    else:
        print("   ❌ crop_model.pkl - File not found")
        print("      Run: python model.py")
        model_ok = False
    
    # Check encoder file
    if os.path.exists('label_encoder.pkl'):
        size = os.path.getsize('label_encoder.pkl')
        if size > 0:
            print(f"   ✅ label_encoder.pkl - {size:,} bytes")
        else:
            print("   ❌ label_encoder.pkl - File is empty")
            model_ok = False
    else:
        print("   ❌ label_encoder.pkl - File not found")
        print("      Run: python model.py")
        model_ok = False
    
    return model_ok

def check_data_file():
    """Check dataset integrity"""
    print_header("5. Dataset Check")
    
    try:
        import pandas as pd
        
        data = pd.read_csv('data.csv')
        print(f"   ✅ data.csv loaded successfully")
        print(f"   📊 Samples: {len(data)}")
        print(f"   📋 Columns: {len(data.columns)}")
        print(f"   🌾 Crops: {data['label'].nunique() if 'label' in data.columns else 'Unknown'}")
        
        # Check required columns
        required_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'label']
        missing_cols = [col for col in required_cols if col not in data.columns]
        
        if missing_cols:
            print(f"   ⚠️  Missing columns: {missing_cols}")
            return False
        else:
            print(f"   ✅ All required columns present")
            return True
    except Exception as e:
        print(f"   ❌ Error reading data.csv: {str(e)}")
        return False

def check_code_syntax():
    """Check if Python files have valid syntax"""
    print_header("6. Code Syntax Check")
    
    files_to_check = ['app.py', 'model.py']
    all_valid = True
    
    for filename in files_to_check:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                compile(f.read(), filename, 'exec')
            print(f"   ✅ {filename} - Syntax valid")
        except SyntaxError as e:
            print(f"   ❌ {filename} - Syntax error: {str(e)}")
            all_valid = False
    
    return all_valid

def check_dependencies():
    """Check specific imports"""
    print_header("7. Import Dependencies Check")
    
    dependencies = [
        ('streamlit', 'Streamlit UI Framework'),
        ('pandas', 'Data Processing'),
        ('numpy', 'Numerical Computing'),
        ('sklearn.ensemble', 'Machine Learning'),
        ('sklearn.preprocessing', 'Data Preprocessing'),
        ('pickle', 'Model Serialization')
    ]
    
    all_ok = True
    
    for module, description in dependencies:
        try:
            __import__(module)
            print(f"   ✅ {module:<30} - {description}")
        except ImportError as e:
            print(f"   ❌ {module:<30} - {description}")
            print(f"      Error: {str(e)}")
            all_ok = False
    
    return all_ok

def run_prediction_test():
    """Test a sample prediction"""
    print_header("8. Prediction Test")
    
    try:
        from model import model
        
        print("   🧪 Running test prediction...")
        
        # Load model first
        if not model.load_model():
            print("   ⚠️  Model files not loaded, attempting to train...")
            return True
        
        # Test prediction
        crop, confidence = model.predict_crop(
            n=90, p=42, k=43,
            temperature=21, humidity=80,
            ph=6.5, rainfall=200
        )
        
        if crop:
            print(f"   ✅ Prediction successful: {crop.upper()}")
            print(f"   📊 {confidence}")
            
            # Test profit calculation
            profit = model.calculate_profit(crop)
            if profit:
                print(f"   💰 Estimated profit: ${profit['estimated_profit']:,.2f}")
                return True
            else:
                print(f"   ⚠️  Could not calculate profit")
                return True
        else:
            print(f"   ❌ Prediction failed: {confidence}")
            return False
    except Exception as e:
        print(f"   ❌ Test failed: {str(e)}")
        return False

def generate_report(results):
    """Generate final verification report"""
    print_header("Verification Report")
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    
    percentage = (passed / total * 100) if total > 0 else 0
    
    print(f"\n   Checks Passed: {passed}/{total} ({percentage:.0f}%)")
    
    status = "🟢 READY" if percentage == 100 else "🟡 PARTIAL" if percentage >= 80 else "🔴 NOT READY"
    print(f"   Status: {status}")
    
    if percentage == 100:
        print("\n   ✅ All checks passed! Ready to run:")
        print("   streamlit run app.py")
    elif percentage >= 80:
        print("\n   ⚠️  Most checks passed. Review warnings above.")
        print("   Common fixes:")
        print("   - pip install -r requirements.txt")
        print("   - python model.py")
    else:
        print("\n   ❌ Multiple issues found. Please fix above errors.")
        print("   Recommended steps:")
        print("   1. pip install -r requirements.txt")
        print("   2. python model.py")
        print("   3. python verify_setup.py")
    
    return percentage == 100

def main():
    """Run all verification checks"""
    print("\n")
    print("╔════════════════════════════════════════════════════╗")
    print("║   🌾 Smart Agriculture Web App - Setup Verifier   ║")
    print("╚════════════════════════════════════════════════════╝")
    
    results = {
        'Python Version': check_python_version(),
        'Packages': check_packages(),
        'Files': check_files(),
        'Model Files': check_model_quality(),
        'Dataset': check_data_file(),
        'Code Syntax': check_code_syntax(),
        'Dependencies': check_dependencies(),
        'Prediction': run_prediction_test()
    }
    
    ready = generate_report(results)
    
    print("\n" + "="*60)
    print("  Verification Complete!")
    print("="*60 + "\n")
    
    return 0 if ready else 1

if __name__ == "__main__":
    sys.exit(main())
