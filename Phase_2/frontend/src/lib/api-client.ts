export class ApiClient {
    private baseUrl: string;

    constructor() {
        this.baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";
    }

    private async request(path: string, options: RequestInit = {}) {
        const token = typeof window !== 'undefined' ? localStorage.getItem('auth_token') : null;

        const headers: HeadersInit = {
            "Content-Type": "application/json",
            ...(token ? { "Authorization": `Bearer ${token}` } : {}),
            ...options.headers,
        };

        try {
            const response = await fetch(`${this.baseUrl}${path}`, {
                ...options,
                headers,
            });

            if (!response.ok) {
                if (response.status === 401 && !path.includes('/auth/')) {
                    console.error("Unauthorized request, redirecting to login...");
                    if (typeof window !== 'undefined') {
                        localStorage.removeItem("auth_token");
                        window.location.href = "/login";
                    }
                }
                const errorData = await response.json().catch(() => ({ detail: response.statusText }));
                throw new Error(errorData.detail || `API Error: ${response.status} ${response.statusText}`);
            }

            if (response.status === 204) return null;
            return response.json();
        } catch (error: any) {
            console.error(`Fetch error for ${path}:`, error);
            if (error.message === 'Failed to fetch') {
                throw new Error(`Cannot connect to backend at ${this.baseUrl}. Please ensure the backend server is running.`);
            }
            throw error;
        }
    }

    async register(data: any) {
        return this.request("/auth/register", {
            method: "POST",
            body: JSON.stringify(data),
        });
    }

    async login(data: any) {
        return this.request("/auth/login", {
            method: "POST",
            body: JSON.stringify(data),
        });
    }

    async getTodos() {
        return this.request("/todos");
    }

    async createTodo(data: { title: string; description?: string }) {
        return this.request("/todos", {
            method: "POST",
            body: JSON.stringify(data),
        });
    }

    async updateTodo(id: number, data: { title?: string; completed?: boolean; description?: string }) {
        return this.request(`/todos/${id}`, {
            method: "PATCH",
            body: JSON.stringify(data),
        });
    }

    async deleteTodo(id: number) {
        return this.request(`/todos/${id}`, {
            method: "DELETE",
        });
    }
}

export const api = new ApiClient();
