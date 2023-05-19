import openai
from flask import Flask, request, jsonify

# Set up Flask application
app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'API_KEY'  

# Define API endpoint
@app.route('/course_plan', methods=['POST'])
def generate_course_plan():
    # Retrieve subject from the request
    subject = request.json['subject']

    # Generate course plan using GPT-3.5 API
    prompt = f"What are the main topics and materials for a course on {subject}?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0
    )

    # Extract the generated course plan from the API response
    course_plan = response.choices[0].text.strip()

    # Return the course plan as a JSON response
    return jsonify({'course_plan': course_plan})

# Run the Flask application
if __name__ == '__main__':
    app.run()
