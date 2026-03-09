# Quickstart: Todo App Authentication System

## Prerequisites
- **Python 3.13+**
- **Node.js (LTS)**
- **Shared Secret**: Ensure `JWT_SECRET` in `.env` is identical for both frontend and backend.

## Environment Setup
1. Create a `.env` file in the project root with the following:
   ```env
   JWT_SECRET="edd2ZeaieYwF9JX6HKW8oX1pZskqQcdhmi51UPeJJ08="
   DATABASE_URL="postgresql://user:password@localhost:5432/todo"
   BETTER_AUTH_SECRET="fS2v6/L5Dk4O0e/F/9S6X+6X4X+6X4X+6X4X+6X4X="
   BETTER_AUTH_URL="http://localhost:3000"
   ```

## Running the Backend (FastAPI)
1. Navigate to the `backend/` directory.
2. Activate the virtual environment:
   - Windows: `.\.venv\Scripts\activate`
   - Unix/macOS: `source .venv/bin/activate`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Run the application:
   - `uvicorn src.main:app --reload`
5. Access the API documentation at: `http://localhost:8000/docs`

## Running the Frontend (Next.js)
1. Navigate to the `frontend/` directory.
2. Install dependencies:
   - `npm install`
3. Run the development server:
   - `npm run dev`
4. Access the application at: `http://localhost:3000`

## Implementation Verification
1. **Signup**: Visit `http://localhost:3000/signup`.
2. **Login**: Visit `http://localhost:3000/login`.
3. **Protected API**: Attempt to access `http://localhost:8000/todos` without a JWT in the `Authorization` header and verify it returns a **401 Unauthorized** error.
