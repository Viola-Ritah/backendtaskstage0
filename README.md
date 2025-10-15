# Backend Task Stage 0

## Description

This is a simple FastAPI backend application for HNG13 Stage 0. It provides a REST API endpoint that returns user profile information along with a random cat fact fetched from an external API.

## Features

- User profile endpoint with personal details
- Integration with cat fact API for fun facts
- UTC timestamp generation
- Error handling for external API calls

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd backendtaskstage0
   ```

2. Install dependencies:
   ```
   pip install -r requiremnts.txt
   ```

3. Run the application:
   ```
   uvicorn main:app --reload
   ```

The application will start on `http://127.0.0.1:8000`.

## API Endpoints

### GET /me

Returns user profile data in JSON format.

## Dependencies

- FastAPI: Web framework for building APIs
- Pydantic: Data validation and serialization
- Requests: HTTP library for API calls
- Uvicorn: ASGI server for running FastAPI

## Project Structure

- `main.py`: Main application file with FastAPI routes
- `requiremnts.txt`: Python dependencies
- `README.md`: Project documentation

