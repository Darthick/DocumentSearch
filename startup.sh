#!/bash
set -e

# Navigate to the correct directory
cd /home/site/wwwroot  # Use the actual path where your application is located

# Install dependencies
pip install -r requirements.txt

# Start the application
gunicorn -b 0.0.0.0:$PORT chat:app
