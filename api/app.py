from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

# Ensure static directories exist (good practice to keep)
# os.makedirs('static/images/gallery', exist_ok=True)
# os.makedirs('static/images', exist_ok=True)

# Define your gallery images list
GALLERY_IMAGES = [
    {
        'filename': '1.jpg',
        'title': 'Luxury Sedan - Before',
        'description': 'Full exterior detail transformation'
    },
    {
        'filename': '2.jpg',
        'title': 'Luxury Sedan - After',
        'description': 'Complete paint correction and ceramic coating'
    },
    {
        'filename': '3.jpg',
        'title': 'SUV Interior Detail',
        'description': 'Deep cleaning and leather conditioning'
    },
    {
        'filename': '4.jpg',
        'title': 'Sports Car Paint Correction',
        'description': 'Swirl marks and scratches removed'
    },
    {
        'filename': '5.jpg',
        'title': 'Truck Full Detail',
        'description': 'Complete interior and exterior service'
    },
    {
        'filename': '6.jpg',
        'title': 'Classic Car Restoration',
        'description': 'Vintage vehicle brought back to life'
    }
]

# The single route for your homepage
@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    # Render the base.html template, passing all necessary data
    return render_template('api/index.html', 
                           current_year=current_year,
                           gallery_images=GALLERY_IMAGES)

if __name__ == '__main__':
    app.run(debug=True)