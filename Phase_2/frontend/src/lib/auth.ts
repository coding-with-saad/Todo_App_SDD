import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
    secret: process.env.JWT_SECRET || "fallback-secret-for-dev-only",
    database: {
        // Since we are using independent JWT verification on backend,
        // Better Auth still needs its own store for users/sessions
        // In a real app, this would be the Neon DB
        provider: "sqlite",
        url: ":memory:", 
    },
    plugins: [
        jwt()
    ],
    emailAndPassword: {
        enabled: true,
    }
});
