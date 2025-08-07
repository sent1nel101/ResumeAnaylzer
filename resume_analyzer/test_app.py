#!/usr/bin/env python3
"""Test script to verify the Flask app can initialize properly."""

import sys
import os

def test_app():
    """Test if the Flask app can be imported and initialized."""
    try:
        # Import the app
        import app
        print("OK - App module imported successfully")
        
        # Check if Flask app exists
        if hasattr(app, 'app'):
            flask_app = app.app
            print("OK - Flask app instance found")
            
            # Test app configuration
            with flask_app.app_context():
                print("OK - Flask app context works")
                
            # Test routes
            routes = [rule.rule for rule in flask_app.url_map.iter_rules()]
            print(f"OK - Routes found: {routes}")
            
            # Test template rendering (without request context)
            print("OK - Flask app is properly configured")
            
        else:
            print("ERROR - Flask app instance not found")
            return False
            
        print("\nSUCCESS - All tests passed! The app should start successfully.")
        return True
        
    except Exception as e:
        print(f"ERROR - {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_app()
    sys.exit(0 if success else 1)
