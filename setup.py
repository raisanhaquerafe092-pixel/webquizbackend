#!/usr/bin/env python3
"""
Django Backend Setup Script
Run this to set up the Django project with migrations and initial data
"""

import os
import sys
import subprocess
import django
from pathlib import Path

# Add the project directory to Python path
PROJECT_ROOT = Path(__file__).resolve().parent / "quizappbackend"
sys.path.append(str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizappbackend.settings')

def run_command(command):
    """Run a shell command and return the result"""
    print(f"Running: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True, cwd=PROJECT_ROOT)
        print("✓ Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {e.stderr}")
        return False

def setup_django():
    """Set up Django project"""
    print("🚀 Setting up Django Quiz Backend...\n")
    
    # Check if virtual environment exists
    venv_path = Path(__file__).parent / ".venv"
    if not venv_path.exists():
        print("Creating virtual environment...")
        run_command("python -m venv .venv")
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    if not run_command("pip install django==5.2.6 djangorestframework==3.16.1 django-cors-headers==4.9.0"):
        print("Failed to install dependencies. Please run: pip install -r requirements.txt")
        return False
    
    # Make migrations
    print("\n🗃️  Creating migrations...")
    if not run_command("python manage.py makemigrations"):
        print("Failed to create migrations")
        return False
    
    # Apply migrations
    print("\n🗄️  Applying migrations...")
    if not run_command("python manage.py migrate"):
        print("Failed to apply migrations")
        return False
    
    # Create superuser (optional)
    print("\n👤 Creating superuser...")
    run_command('python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username=\'admin\').exists() or User.objects.create_superuser(\'admin\', \'admin@example.com\', \'admin123\')"')
    
    print("\n✅ Django setup complete!")
    print("\nTo start the development server:")
    print("cd webquizbackend/quizappbackend")
    print("python manage.py runserver")
    print("\nAdmin login:")
    print("Username: admin")
    print("Password: admin123")
    print("URL: http://localhost:8000/admin/")
    
    return True

if __name__ == "__main__":
    setup_django()