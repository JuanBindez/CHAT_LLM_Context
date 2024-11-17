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

![image](https://github.com/user-attachments/assets/9d93c464-d5e0-45c7-b279-bd22e347fcf2)

![Captura de tela de 2024-11-17 18-35-57](https://github.com/user-attachments/assets/692749a8-d785-478e-9020-b7d985f4d32d)

## Deployment

### The CHAT is already set up with Docker for deployment. Run the following commands:

#### To Test
    docker-compose up --build

#### To Deploy
    docker-compose up -d

#### To Stop
    docker-compose down

