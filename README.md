# DJANGO REST FRAMEWORK ASSIGNMENT

This project is built with Django REST framework and implements a RESTful API for a hotel reservation system. The API supports the following main functionalities:

- **GET /api/hotels/**: Retrieve a list of all hotels in the database.
- **POST /api/hotels/**: Create a new hotel record by sending JSON data.

## Prerequisites

- Python 3.8 or higher
- Django
- Django REST framework
- MySQL

## Quick Start

### 1. Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/A00488698/restassignment.git
cd restassignment
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **Linux/macOS:**

  ```bash
  source venv/bin/activate
  ```

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

### 4. Install Dependencies

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Database Configuration

To configure MySQL, create a `.env` file in the project root and add the following information:

```bash
DB_NAME=hotel_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

Then, log in to your local MySQL instance and create the database:

```sql
CREATE DATABASE hotel_db;
```

## Database Migration

Run the following command to apply the migrations and create the necessary database tables:

```bash
python manage.py migrate
```

## Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

## Testing the API with Postman

- Open Postman and navigate to the URL: `http://127.0.0.1:8000/api/hotels/`.

### POST Request Examples

Use the following JSON payloads as test examples when sending a POST request:

**Example 1:**

```json
{
  "name": "Hotel California",
  "location": "Los Angeles, California",
  "pricePerNight": "200"
}

{
  "name": "Grand Hyatt",
  "location": "New York City, New York",
  "pricePerNight": "350"
}

{
  "name": "The Ritz",
  "location": "Paris, France",
  "pricePerNight": "500"
}
```

**Screenshot:** 
![GET Response Screenshot](/screenshot1.jpg)

### GET Request

Send a GET request to `http://127.0.0.1:8000/api/hotels/` to retrieve the list of hotels.  
**Screenshot:**  
![GET Response Screenshot](/screenshot.jpg)

## API Endpoints Implementation Explanation

The API endpoint is implemented using Django REST framework's class-based view `ListCreateAPIView`. This view handles both GET and POST requests in a single class.

### Implementation Code

```python
from rest_framework import generics
from .models import Hotel
from .serializers import HotelSerializer

class HotelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
```

- **GET Request:**  
  Retrieves and serializes all hotel records.

- **POST Request:**  
  Validates and creates a new hotel record using the provided JSON data.

This unified approach simplifies the code while ensuring the API is easy to maintain and extend.

