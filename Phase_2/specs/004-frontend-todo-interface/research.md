# Research: Frontend Todo Web Interface

## Decision: Next.js 16+ App Router with Better Auth Client

### Rationale
- **Next.js App Router** is the modern standard for React applications, providing excellent support for layouts, loading states, and server components.
- **Better Auth** offers a seamless client-side library (`createAuthClient`) that simplifies session management and JWT handling in Next.js.
- A **Centralized API Client** ensures that the `Authorization: Bearer <token>` header is consistently applied to all requests and that 401 errors are handled globally (e.g., redirecting to login).

### Implementation Patterns

#### 1. Better Auth Integration
- Use `createAuthClient` from `better-auth/react`.
- Configure the client with the `jwt` plugin to match the backend's expectations.
- Utilize `useSession()` hook for reactive UI updates based on auth state.

#### 2. Centralized API Client (Axios/Fetch)
- Create a `lib/api-client.ts` file.
- Implement an interceptor (or wrapper) that retrieves the current JWT from Better Auth and adds it to the `Authorization` header.
- Add global error handling for `401 Unauthorized` to trigger a logout/redirect flow.

#### 3. Component-Based UI
- **TaskList**: Renders a collection of `TaskItem` components.
- **TaskForm**: Handles both creation and editing (if applicable).
- **ProtectedRoute**: A layout wrapper or higher-order component to prevent unauthenticated access to the dashboard.

### Alternatives Considered
- **Axios**: Provides powerful interceptors but adds bundle size.
- **Native Fetch**: Lightweight but requires more boilerplate for interceptors. *Decision: Use a simple fetch wrapper for minimal overhead.*
- **State Management (Redux/Zustand)**: Likely overkill for this feature since Better Auth and React Context/Hooks can handle the session and task state effectively.

### Risk Mitigation
- **JWT Persistence**: Better Auth handles token storage (usually in cookies or local storage). We will ensure the API client correctly retrieves it for the backend.
- **Responsive Layout**: Use **Tailwind CSS** with a mobile-first approach to meet the responsiveness requirements.
