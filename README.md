# Image Generator Using OpenAI DALL·E

A Flask-based web application that generates images from text prompts using OpenAI’s DALL·E 3 API. The project demonstrates integrating OpenAI’s image generation models into a backend service with a simple web interface.

## Overview
This application allows users to enter a text prompt and generate a high-quality image using OpenAI’s DALL·E 3 model. The backend exposes an API endpoint that processes the prompt, calls the OpenAI image generation API, and returns image URLs to the frontend for display.

The project focuses on practical API integration, error handling, and clean separation between frontend and backend logic.

## Features
- Text-to-image generation using DALL·E 3
- Flask-based backend API
- Simple web interface built with Bootstrap
- JSON-based image URL responses
- Graceful handling of OpenAI safety and API errors

## Tech Stack
- Python
- Langchain
- Gen AI
- Flask
- OpenAI API (DALL·E 3)
- HTML / Bootstrap

## Project Structure

    ├── app.py                   # Flask application and image generation logic
    ├── requirements.txt         # Python dependencies
    ├── templates/
    │   └── index.html           # Frontend UI
    ├── LICENSE
    └── README.md

## How It Works
1. User enters a text prompt in the web interface.
2. The frontend sends the prompt to the Flask backend.
3. The backend calls OpenAI’s DALL·E 3 image generation API.
4. Generated image URLs are returned as a JSON response.
5. The frontend displays the generated image(s) to the user.

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/<your-username>/Image_Generator.git  
cd Image_Generator  

### 2. Create and activate a virtual environment
python -m venv venv  
source venv/bin/activate  

### 3. Install dependencies
pip install -r requirements.txt  

### 4. Configure environment variables
Create a `.env` file in the root directory and add:
OPENAI_API_KEY=your_openai_api_key  

### 5. Run the application
python app.py  

The application will be available at:
http://localhost:8080  

## Usage
- Open the web interface in a browser
- Enter a descriptive text prompt
- Submit the prompt to generate an image
- View the generated image returned by the API

## Notes
- The application uses the DALL·E 3 model with HD quality and vivid style.
- OpenAI safety rejections are handled and returned as user-friendly errors.
- Image URLs are returned directly from OpenAI and are not stored locally.

## Future Improvements
- Prompt history and saved generations
- Multiple image generation per request
- Download and caching support
- Authentication and usage limits

## License
This project is licensed under the MIT License.
