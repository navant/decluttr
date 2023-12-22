# Decluttr App
Decluttr: Revolutionize Managing Your Personal items  
Decluttr is an AI powered platform redefining the way you manage your belongings, prioritizing environmental sustainability and convenience.  

THE VISION:  

![image](https://github.com/navant/decluttr/assets/12711084/96e6bd8a-82cc-4666-8ffb-2d8241c064a8)

  
In its most basic version, it uses Google Gemini Pro Vision to recognize and describe objects, it allow user to update and store description in their inventory.

![image](https://github.com/navant/decluttr/assets/12711084/a6d58170-59ad-4e9f-bdfd-11f9b5d1d502)
![image](https://github.com/navant/decluttr/assets/12711084/6ec3d895-319f-4588-8783-c8146a5a35b1)

# Tech Stack  
  
React front-end  
FastAPI Python backend  (https://fastapi.tiangolo.com/)  
Llamaindex for LLM interactions in python  (https://docs.llamaindex.ai/en/stable/)  
TruLens for LLMOps (https://www.trulens.org/)   
  
# Availability

The app is currently only available for local deployment

## How to install locally

(0) Install docker desktop (https://docs.docker.com/desktop/install/windows-install/)

(1) clone the repository
```git clone https://github.com/navant/decluttr```

(2) If you use Vscode and have docker installed on your machine, install the dev containers extension (https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 
Open the repo folder then select operation "Dev Containers: Re-open in dev container" (access commands using CTRL-Shift P)
This will download the required container image and install dependencies.

(3) Start the backend:  
  
create an .env file with your secrets (/workspaces/decluttr/decluttr-app/backend/.env)  
  
```
GOOGLE_API_KEY = "..."  
OPENAI_API_KEY = '...'    
SUPABASE_URL = '...'  
SUPABASE_KEY = '...'
```
  
follow isntructions in decluttr-app/backend/README.md  
  
```cd ./decluttr-app/backend```  
```poetry install``` to install all required python libraries  
```python main.py```  
  
It works if you can access http://127.0.0.1:8000/docs  
  
  
(3) Start the front-end:    
  
following isntructions in decluttr-app/backend/README.md  
  
```cd ./decluttr-app/frontend```  
```npm install``` to install all required python libraries  
```npm start```  

Check your app on http://localhost:3000/ !  






