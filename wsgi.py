import os
from app import app

if __name__ == "__main__":
    # Production server for Render
    port = int(os.environ.get('PORT', 8000))
    
    try:
        # Try Gunicorn first (Linux/production)
        from gunicorn.app.base import BaseApplication
        
        class StandaloneApplication(BaseApplication):
            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super().__init__()

            def load_config(self):
                for key, value in self.options.items():
                    if key in self.cfg.settings and value is not None:
                        self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        options = {
            'bind': f'0.0.0.0:{port}',
            'workers': 4,
            'timeout': 120,
        }
        StandaloneApplication(app, options).run()
        
    except ImportError:
        # Fallback to Waitress (Windows/development)
        from waitress import serve
        print(f"Starting Waitress server on http://0.0.0.0:{port}")
        serve(app, host='0.0.0.0', port=port, threads=6)
