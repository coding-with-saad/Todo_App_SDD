---
name: backend-api
description: Generate backend API routes, process requests and responses, and connect application logic with the database.
---

# Backend Skill – Routes, Requests, Responses, DB Integration

## Instructions

1. **Route Creation**
   - Define clear API routes for each feature
   - Use REST-style endpoints (GET, POST, PUT, DELETE)
   - Group related routes under a common prefix

2. **Request Handling**
   - Validate incoming data using schemas
   - Extract parameters from body, query, or path
   - Pass validated data to service or repository layer

3. **Response Handling**
   - Return structured JSON responses
   - Include status codes for success and errors
   - Provide clear error messages for invalid requests

4. **Database Integration**
   - Use a repository or data access layer
   - Avoid writing database queries inside route handlers
   - Handle connection errors gracefully

## Best Practices

- Keep route handlers small and focused
- Separate business logic from route definitions
- Validate all incoming data
- Return consistent response formats
- Use environment variables for configuration