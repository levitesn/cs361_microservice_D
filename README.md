# Travel Tips FastAPI Service

## Overview

This FastAPI microservice provides two endpoints: one for retrieving a random travel tip and another for retrieving a travel tip from a specific category. The tips are hardcoded and categorized for easy access.

## Features

- Get a random travel tip.
- Get a travel tip from a specified category.

## Endpoints

### Random Travel Tip

- **Endpoint**: `/random_tip`
- **Method**: `GET`
- **Response**:
  - `200 OK`: Returns a random travel tip.
  ```json
  {
    "tip": "string"
  }
  ```

### Category Travel Tip

- **Endpoint**: `/categorytip/{category}`
- **Method**: `GET`
- **Path Parameters**:
  - `category`: The category from which to retrieve a travel tip.
- **Response**:
  - `200 OK`: Returns a random travel tip from the specified category.
  ```json
  {
    "tip": "string"
  }
  ```
  - `404 Not Found`: If the specified category does not exist.
  ```json
  {
    "detail": "Category not found"
  }
  ```

## Running the Service

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

### Running the Server

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The service will be accessible at `http://127.0.0.1:8000`.

## Example Requests

### Random Travel Tip

To get a random travel tip, send a `GET` request to `/random_tip`:

```bash
curl -X GET "http://127.0.0.1:8000/random_tip"
```

### Category Travel Tip

To get a travel tip from a specific category, send a `GET` request to `/categorytip/{category}` where `{category}` is the category of tips you want (e.g., `packing`, `safety`, `budget`):

```bash
curl -X GET "http://127.0.0.1:8000/categorytip/packing"
```

## Project Structure

```
.
├── app.py        # The main FastAPI application
├── tests.py  # Integration tests
└── README.md      # This README file
```

## Integration Tests

To run the integration tests, ensure you have `pytest` and `httpx` installed:

```bash
pip install pytest httpx
```

Run the tests with the following command:

```bash
pytest tests.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [levitesn@oregonstate.edu].
