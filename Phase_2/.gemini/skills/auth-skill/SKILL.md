---
name: auth-system
description: Implement authentication systems including signup, signin, password hashing, JWT tokens, and Better Auth integration. Use when building secure user authentication flows.
---

# Auth Skill – Signup, Signin, Password Hashing, JWT Tokens

## Instructions

1. **User Signup**
   - Accept email and password
   - Validate input
   - Hash password before storing
   - Save user record in database

2. **User Signin**
   - Verify email exists
   - Compare password with hashed value
   - Generate authentication token on success

3. **Password Hashing**
   - Use secure hashing algorithm (bcrypt or argon2)
   - Never store plain text passwords
   - Apply proper salt and hashing rounds

4. **JWT Authentication**
   - Generate JWT token after successful signin
   - Include user ID and expiration time
   - Verify token for protected routes

5. **Better Auth Integration**
   - Use Better Auth library for authentication flows
   - Configure providers and session handling
   - Ensure secure token and session management

## Best Practices

- Always hash passwords before storing
- Use short-lived JWT tokens
- Store secrets in environment variables
- Validate all authentication inputs
- Protect sensitive routes with token verification