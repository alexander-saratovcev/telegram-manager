# Telegram Manager Backend

FastAPI backend for Telegram Manager application.

## Features

- FastAPI web framework with async support
- SQLAlchemy ORM with async PostgreSQL
- Pydantic settings management
- AWS S3 integration
- ARQ job queue with Redis
- Comprehensive testing setup
- Code formatting and linting
- Type checking with MyPy

## Requirements

- Python 3.13+
- Poetry (dependency management)
- PostgreSQL 12+
- Redis (for job queue)

## Installation

1. Install dependencies using Poetry:
```bash
make install
```

2. Copy the environment file and configure your settings:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Initialize PostgreSQL databases:
```bash
make init-db
```

4. Activate the virtual environment:
```bash
poetry shell
```

## Environment Variables

Copy the `.env.example` file to `.env` and configure your environment variables:

```bash
cp .env.example .env
```

The `.env.example` file already contains all the required variables with default values. Edit the `.env` file to set your specific configuration values.

## Running the Application

### Development Mode
```bash
make dev
```

### Production Mode
```bash
make run
```

## Development Tools

### Code Formatting
```bash
make format
```

### Linting
```bash
make lint
```

### Type Checking
```bash
make type-check
```

### Running Tests
```bash
make test
```

### Database Initialization
```bash
make init-db
```

## API Documentation

Once the application is running, you can access:

- **Interactive API docs**: http://localhost:8000/docs
- **ReDoc documentation**: http://localhost:8000/redoc
- **OpenAPI schema**: http://localhost:8000/openapi.json
