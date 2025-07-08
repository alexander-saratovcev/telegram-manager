# Telegram Manager Backend

FastAPI backend for Telegram Manager application.


### Status Badges

```markdown
![Backend CI](https://github.com/alexander-saratovcev/telegram-manager/workflows/Backend%20CI/badge.svg)
![Coverage](https://codecov.io/gh/alexander-saratovcev/telegram-manager/branch/main/graph/badge.svg?flag=backend)
```

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

### Running Tests with Coverage
```bash
make test-cov
```

### Database Initialization
```bash
make init-db
```

## CI/CD Pipeline

This project includes a comprehensive CI/CD pipeline using GitHub Actions that automatically runs on every push to the main branch and pull request.

### Pipeline Features

- **Quality Checks**: Code formatting, linting, and type checking
- **Testing**: Unit tests with coverage reporting
- **Security Scanning**: Vulnerability checks using Safety and Bandit
- **Caching**: Optimized dependency caching for faster builds
- **Path-based Triggers**: Only runs when backend files are modified

### Pipeline Jobs

1. **Quality Checks**
   - Code formatting validation (Black)
   - Linting (Ruff)
   - Type checking (MyPy)

2. **Testing**
   - Unit tests with pytest
   - Coverage reporting
   - Integration with Codecov

3. **Security Checks**
   - Dependency vulnerability scanning (Safety)
   - Code security analysis (Bandit)
   - Security report artifacts

### Local Development

To run the same checks locally that the CI pipeline performs:

```bash
# Install dependencies
make install

# Run all quality checks
make format
make lint
make type-check

# Run tests with coverage
make test-cov
```

## API Documentation

Once the application is running, you can access:

- **Interactive API docs**: http://localhost:8000/docs
- **ReDoc documentation**: http://localhost:8000/redoc
- **OpenAPI schema**: http://localhost:8000/openapi.json
