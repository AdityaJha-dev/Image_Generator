import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI # <-- Modern import

# --- Setup ---
load_dotenv()
# Initialize OpenAI client
try:
    client = OpenAI()
except openai.APIKeyNotFoundError:
    print("ERROR: OPENAI_API_KEY not found in .env file.")
    exit()

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Generate images based on a prompt
@app.route('/generateimages/<prompt>')
def generate(prompt):
    print("prompt:", prompt)
    try:
        # Use the modern client to generate images
        response = client.images.generate(
        model="dall-e-3", # Use the best model
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="hd", # For DALL-E 3, you can choose "standard" or "hd"
        style="vivid" # For DALL-E 3, you can choose "natural" or "vivid"
      )
        # To return the image URLs, you need to format the response
        image_urls = [image.url for image in response.data]
        return jsonify(image_urls)

    except openai.BadRequestError as e:
        # This will catch the safety system error and return a friendly message
        print(f"OpenAI API Error: {e}")
        error_message = "Your prompt was rejected by the safety system. Please try a different prompt."
        return jsonify({"error": error_message}), 400
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)