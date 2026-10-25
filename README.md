# DevOps CI/CD Pipeline – Health Check API

A simple Python health-check service with automated tests, Docker packaging, and a GitHub Actions CI pipeline.

The application exposes a single `/health` endpoint that returns HTTP 200 and a JSON status payload. The repository includes unit tests, a Dockerfile, and a CI workflow that runs the tests and builds the Docker image on every push and pull request.

## Features

- Flask health-check endpoint (`GET /health`)
- Unit tests with Python `unittest`
- Docker containerisation
- GitHub Actions CI pipeline

## Technologies

- Python 3.13 + Flask
- Python `unittest`
- Docker
- GitHub Actions
- YAML

## Project Structure

\\\
devops-cicd-pipeline/
├── .github/workflows/ci.yml
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
\\\

## Local Setup (Windows + PowerShell)

### Prerequisites
- Python 3.13+
- Git
- Docker Desktop (running)

### Steps

\\\powershell
git clone https://github.com/JamesDonaghy/devops-cicd-pipeline.git
cd devops-cicd-pipeline

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
\\\

If you receive an execution-policy error when activating the virtual environment:

\\\powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
\\\

Then run the activation command again.

## Running the Application

\\\powershell
python app.py
\\\

In a second terminal:

\\\powershell
Invoke-WebRequest -Uri http://127.0.0.1:5000/health -UseBasicParsing
\\\

Expected response: HTTP 200 and `{"status":"healthy"}`.

## Running the Tests

\\\powershell
python -m unittest test_app.py -v
\\\

## Docker

\\\powershell
# Build
docker build -t healthcheck-api .

# Run
docker run -d -p 5000:5000 --name healthcheck-container healthcheck-api

# Test
Invoke-WebRequest -Uri http://127.0.0.1:5000/health -UseBasicParsing

# Clean up
docker stop healthcheck-container
docker rm healthcheck-container
\\\

## CI Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push and pull request to `master`. It:

1. Checks out the code
2. Sets up Python 3.13
3. Installs dependencies
4. Runs the unit tests
5. Builds the Docker image (only if tests pass)

## Architecture

\\\
Developer
    │
    │ git push
    ▼
GitHub Repository
    │
    │ on push / PR
    ▼
GitHub Actions (Ubuntu runner)
    ├── Install dependencies
    ├── Run unit tests
    └── Build Docker image
\\\

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `Activate.ps1` cannot be loaded | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` |
| Port 5000 already in use | Stop the conflicting process or change the port |
| Docker commands fail | Ensure Docker Desktop is running |

## Limitations

- No cloud deployment
- No Kubernetes or orchestration
- No authentication
- Uses the Flask development server
- Single-job CI pipeline

## Skills Demonstrated

- Git & GitHub
- Python + Flask
- Unit testing
- Docker
- GitHub Actions (YAML)
- Technical documentation

## Licence

MIT
