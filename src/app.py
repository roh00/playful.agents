from fastapi import FastAPI
from first_agent_astro import web_agent

app = FastAPI()


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello world"}

# GET all items
@app.get("/ping")
def get_items():
    return "pong"

# GET a single item by ID
@app.get("/chart/{birth_date}")
def get_chart(birth_date):
    raw_response = web_agent.run(
        prompt=("I want to know my sun sign and some predictions based on my DOB "+birth_date),
    )

    # Clean the response by stripping unnecessary parts
    # cleaned_response = raw_response.split("\n\n")[-1].strip()

    # Return the cleaned response as JSON
    # return {"response": raw_response}
    return web_agent.run("I want to know my sun sign and some predictions based on my DOB "+birth_date)
