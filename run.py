from app import create_app

# Create an instance of the Flask application
app = create_app()

if __name__ == "__main__":
    # Run the app locally with debug mode enabled
    app.run(debug=True, host="0.0.0.0", port=5000)
