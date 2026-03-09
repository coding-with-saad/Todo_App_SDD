# Quickstart: Todo Backend API + Database

## 1. Database Setup
1. Log in to [Neon.tech](https://neon.tech/).
2. Create a new project or select an existing one.
3. Copy the **PostgreSQL Connection String** from the dashboard.
4. Add it to your `.env` file:
   ```env
   DATABASE_URL="postgresql://user:password@your-neon-url.com/neondb?sslmode=require"
   ```

## 2. Backend Initialization
1. Ensure the virtual environment is active:
   ```powershell
   cd backend
   .\.venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   uv pip install -r requirements.txt
   ```

## 3. Database Migrations
1. Initialize Alembic (if not already done):
   ```powershell
   alembic init alembic
   ```
2. Generate and run migrations:
   ```powershell
   alembic revision --autogenerate -m "create todo table"
   alembic upgrade head
   ```

## 4. Run the API
1. Start the FastAPI server:
   ```powershell
   uvicorn src.main:app --reload
   ```
2. Verify connection via Swagger UI: `http://localhost:8000/docs`.

## 5. Integration Verification
1. Use a tool like Postman or `curl` to send a `POST` request to `/todos`.
2. Provide a valid JWT in the `Authorization` header.
3. Check the Neon SQL Editor to confirm the record was created.
