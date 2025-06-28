# Django Developer Practical Test

## Setup

## 🚀 Running Without Docker

If you prefer running **without Docker**, you need to have:

✅ **PostgreSQL** running locally with the credentials you set in `.env`.
✅ **Redis** running locally on the default port (`6379`).
✅ A **Celery worker** running to handle background tasks.

### 1️⃣ Setup **pyenv** (optional, for local Python isolation)

1. Follow instructions for your OS from the official repository: [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file)
2. Install Python:

   ```bash
   pyenv install 3.11.8
   ```
3. Set the local Python version:

   ```bash
   pyenv local 3.11.8
   ```

---

### 2️⃣ Setup **poetry**

1. Install Poetry:

   ```bash
   pip install poetry
   ```
2. Install dependencies:

   ```bash
   poetry install
   ```

---

### 3️⃣ Environment Variables

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```
2. Open `.env` and specify:

   * **PostgreSQL credentials** (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`).
   * **SMTP credentials** (`EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`).
   * Your **API key** for OpenRouter or OpenAI (`OPENROUTER_AI_KEY`).

---

## Database & Sample Data

### 1. Apply migrations:

```bash
cd CVProject
python manage.py migrate
```

### 2. Load the fixture data:

```bash
python manage.py loaddata cv-fixture.json
```

This will load a sample CV into the database for testing.

---

## Celery Worker

### Start the Celery worker:

```bash
poetry run celery -A CVProject worker --loglevel=info
```

## Django development server:

```bash
python manage.py runserver
```

---

## 🐳 Using Docker Compose

A **`docker-compose.yml`** is included, which runs:

* PostgreSQL
* Redis
* Django app (served via Gunicorn)
* Celery worker

To build and start everything:

```bash
docker compose up --build
```

---

## ✅ Running Tests

To run the test suite:

```bash
python manage.py test
```





## Requirements

- Follow **PEP 8** and other style guidelines.
- Use clear and concise **commit messages** and **docstrings** where needed.
- Structure your project for **readability and maintainability**.
- Optimize database access using **Django’s built-in methods**.
- Provide enough details in your **README.md**.

---

## Version Control System

1. Create a public GitHub repository, e.g., `DTEAM-django-practical-test`.
2. Put the text of this test (all instructions) into `README.md`.
3. For each task, create a separate branch (e.g., `tasks/task-1`, `tasks/task-2`, etc.).
4. When you finish each task, merge that branch back into `main` but **do not delete** the original task branch.

---

## Python Virtual Environment

1. Use **pyenv** to manage the Python version.
   - Create a file named `.python-version` in your repository.
2. Use **Poetry** to manage and store project dependencies.
   - This will create a `pyproject.toml` file.
3. Update your `README.md` with clear instructions on how to set up and use **pyenv** and **Poetry**.

---

## Tasks

### Task 1: Django Fundamentals

1. **Create a New Django Project**
   - Name it something like `CVProject`.
   - Use the Python version set up in this task and the latest stable Django release.
   - Use SQLite as your database for now.

2. **Create an App and Model**
   - Create a Django app (e.g., `main`).
   - Define a `CV` model with fields like `firstname`, `lastname`, `skills`, `projects`, `bio`, and `contacts`.
   - Organize the data efficiently and logically.

3. **Load Initial Data with Fixtures**
   - Create a fixture containing at least one sample CV instance.
   - Include instructions in `README.md` on how to load the fixture.

4. **List Page View and Template**
   - Implement a view for the main page (`/`) to display a list of CV entries.
   - Use any CSS library to style them nicely.
   - Ensure efficient data retrieval from the database.

5. **Detail Page View**
   - Implement a detail view (`/cv/<id>/`) to show all data for a single CV.
   - Style it nicely and ensure efficient data retrieval.

6. **Tests**
   - Add basic tests for the list and detail views.
   - Update `README.md` with instructions on how to run these tests.

---

### Task 2: PDF Generation Basics

1. Choose and install an HTML-to-PDF generation library or tool.
2. Add a "Download PDF" button on the CV detail page that allows users to download the CV as a PDF.

---

### Task 3: REST API Fundamentals

1. Install **Django REST Framework** (DRF).
2. Create CRUD endpoints for the `CV` model (Create, Retrieve, Update, Delete).
3. Add tests to verify that each CRUD action works correctly.

---

### Task 4: Middleware & Request Logging

1. **Create a `RequestLog` Model**
   - Include fields such as `timestamp`, `HTTP method`, `path`, and optionally query string, remote IP, or user.
   - You may put this in an existing app or a new app (e.g., `audit`).

2. **Implement Logging Middleware**
   - Write a custom Django middleware class that logs each incoming request.
   - Create a `RequestLog` record in the database.

3. **Recent Requests Page**
   - Create a view (`/logs/`) showing the 10 most recent requests, sorted by descending timestamp.
   - Include a template that displays the `timestamp`, `method`, and `path`.

4. **Test Logging**
   - Ensure your tests verify the logging functionality.

---

### Task 5: Template Context Processors

1. **Create `settings_context`**
   - A context processor that injects your Django `settings` into all templates.

2. **Settings Page**
   - Create a view (`/settings/`) that displays values such as `DEBUG` and others using the context processor.

---

### Task 6: Docker Basics

1. Use **Docker Compose** to containerize your project.
2. Switch the database from SQLite to **PostgreSQL** in Docker Compose.
3. Store environment variables (e.g., DB credentials) in a `.env` file.

---

### Task 7: Celery Basics

1. Install and configure **Celery**, using Redis or RabbitMQ as the broker.
2. Add a Celery worker to your Docker Compose setup.
3. On the CV detail page:
   - Add an email input field.
   - Add a "Send PDF to Email" button.
   - Trigger a Celery task to email the PDF.

---

### Task 8: OpenAI Basics

1. On the CV detail page, add a "Translate" button and a language selector.
2. Supported languages:
   - Cornish, Manx, Breton, Inuktitut, Kalaallisut, Romani, Occitan, Ladino, Northern Sami, Upper Sorbian, Kashubian, Zazaki, Chuvash, Livonian, Tsakonian, Saramaccan, Bislama
3. Use OpenAI's API or any translation mechanism to translate the CV content into the selected language.

---

### Task 9: Deployment

Deploy the project to **DigitalOcean** or another VPS.

If you don’t have a DigitalOcean account, you can use this referral link to create one with a $200 credit:  
[https://m.do.co/c/967939ea1e74](https://m.do.co/c/967939ea1e74)

---

## Final Notes

- Complete each task thoroughly.
- Follow the **branch-and-merge** structure.
- Ensure your `README.md` clearly explains:
  - How to install the project
  - How to run it
  - How to test it

Thank you, and we look forward to reviewing your submission!
