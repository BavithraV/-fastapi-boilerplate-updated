DM Reporter Rating AI

A production-style FastAPI boilerplate that evaluates training efficiency between a District Manager (DM) and a Reporter using an AI model.

The system receives ratings from both the DM and the Reporter, sends them to an LLM (Large Language Model), and returns an efficiency score along with feedback describing the effectiveness of the training interaction.

⸻

Overview

In many organizations, District Managers train reporters or junior employees.
This system helps evaluate:
	•	How effectively the DM teaches
	•	How efficiently the Reporter learns
	•	Overall training efficiency score

The evaluation is performed using an AI model that analyzes the provided ratings and generates feedback.

⸻

Architecture

The project follows a layered architecture commonly used in production FastAPI applications.

Client
↓
API Layer (Routes)
↓
Service Layer (Business Logic)
↓
LLM + Repository Layer
↓
Response

Each layer has a specific responsibility, making the system modular, maintainable, and scalable.

⸻

Project Structure

dm_reporter_rating_ai
│
├── app
│   ├── api
│   │   └── v1
│   │       └── rating_routes.py
│   │
│   ├── config
│   │   └── settings.py
│   │
│   ├── core
│   │   ├── logger.py
│   │   └── exceptions.py
│   │
│   ├── llm
│   │   ├── llm_client.py
│   │   ├── prompt_builder.py
│   │   └── output_parser.py
│   │
│   ├── models
│   │   └── rating_model.py
│   │
│   ├── repositories
│   │   └── rating_repository.py
│   │
│   ├── schemas
│   │   └── rating_schema.py
│   │
│   ├── services
│   │   └── rating_service.py
│   │
│   ├── utils
│   │
│   └── main.py
│
├── tests
│   ├── test_rating_api.py
│   └── test_rating_service.py
│
├── requirements.txt
├── pytest.ini
├── .env
└── README.md

⸻

Folder Explanation

app/

Contains the entire application source code.

⸻

api/

Defines the FastAPI routes and endpoints.

Example:
rating_routes.py receives requests from the user and sends them to the service layer.

⸻

config/

Stores configuration related to the application.

Example:
	•	environment variables
	•	API keys
	•	model settings

⸻

core/

Contains shared infrastructure components.

Examples:
	•	logging setup
	•	global exception handlers

⸻

llm/

Handles all AI-related operations.

Responsibilities:
	•	Build prompts
	•	Send requests to the LLM
	•	Parse AI responses

Files:
	•	prompt_builder.py → creates prompts sent to the AI model
	•	llm_client.py → communicates with the LLM API
	•	output_parser.py → converts AI responses into structured data

⸻

models/

Defines application data models.

These represent entities used within the system.

⸻

repositories/

Handles data persistence and database interactions.

Responsibilities:
	•	Save rating results
	•	Retrieve historical ratings

Separating repository logic from services helps keep business logic clean.

⸻

schemas/

Defines request and response models using Pydantic.

Responsibilities:
	•	Validate API input
	•	Structure API responses
	•	Ensure type safety

Example:
	•	RatingRequest
	•	RatingResponse

⸻

services/

Contains the core business logic of the application.

Responsibilities:
	•	Generate prompts
	•	Call the LLM
	•	Process responses
	•	Return evaluation results

Example:
rating_service.py calculates the AI-based training efficiency score.

⸻

utils/

Utility functions and helper methods used across the application.

⸻

tests/

Contains unit tests and API tests.

Tests ensure:
	•	service logic works correctly
	•	API endpoints behave as expected
	•	LLM responses are mocked for consistent testing

⸻

main.py

Application entry point.

Responsibilities:
	•	Initialize FastAPI
	•	Register API routers
	•	Start the application server

⸻

Running the Application

Install dependencies

pip install -r requirements.txt

Run the FastAPI server

uvicorn app.main:app –reload

Open API documentation

http://127.0.0.1:8000/docs

⸻

Running Tests

pytest

This will run all unit tests and API tests.

⸻

Technologies Used
	•	FastAPI
	•	Python
	•	Pydantic
	•	Pytest
	•	OpenAI API
	•	AI Prompt Engineering
