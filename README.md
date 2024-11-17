# CHAT LLM Context

### To Test It

#### Install requirements
    pip install -r requirements.txt

#### Create an API Key from Groq:

* link: https://console.groq.com/keys


#### Add this API key to an environment variable in a .env file:
    GROQ_API_KEY="Key"

#### Run the App
    python3 main.py


## Deployment

### The CHAT is already set up with Docker for deployment. Run the following commands:

#### To Test
    docker-compose up --build

#### To Deploy
    docker-compose up -d

#### To Stop
    docker-compose down

