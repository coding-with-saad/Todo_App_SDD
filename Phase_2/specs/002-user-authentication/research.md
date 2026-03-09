# Research: Authentication System (Better Auth + FastAPI JWT)

## Decision: Better Auth JWT Plugin with FastAPI Middleware

### Rationale
- **Better Auth** provides a high-level, secure authentication solution for Next.js with minimal configuration.
- The **JWT Plugin** in Better Auth allows the frontend to generate a stateless token that can be consumed by other services.
- **FastAPI** can independently verify these tokens if they share the same secret or public key, fulfilling the "decoupled backend" requirement.
- This approach satisfies the **III. JWT-Based Authentication (NON-NEGOTIABLE)** principle of the project constitution.

### Implementation Patterns

#### 1. Better Auth (Frontend)
- Enable the `jwt` plugin in `auth.ts`.
- The frontend will receive a JWT which should be stored securely (e.g., in a cookie or memory) and sent in the `Authorization` header.

#### 2. FastAPI Middleware (Backend)
- Use `PyJWT` or `python-jose` to decode and verify the token.
- Verification must check:
  - Signature (using `JWT_SECRET`).
  - Expiration (`exp`).
  - Issuer/Audience (if configured).
- Extract `user_id` (usually stored in the `sub` claim) and attach it to `request.state.user`.

#### 3. Database Isolation
- Ensure `user_id` is a column in relevant tables (e.g., `Todo`).
- Repositories must always filter by this `user_id`.

### Alternatives Considered
- **Session-based Auth (Better Auth default)**: Rejected because it requires shared session storage (Redis/DB) between Next.js and FastAPI, which complicates the architecture.
- **Custom Auth System**: Rejected per **Technology Constraints** and the "No manual coding" mandate—using established libraries is safer and faster.

### Risk Mitigation
- **Secret Management**: Use a strong, random string for `JWT_SECRET` and ensure it is identical in `.env` for both frontend and backend.
- **Token Expiry**: Keep JWT lifespan short and use Better Auth's refresh token mechanism if needed.
