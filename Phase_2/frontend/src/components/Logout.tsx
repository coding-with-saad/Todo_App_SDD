import { useRouter } from "next/router";

export const Logout = () => {
    const router = useRouter();

    const handleLogout = () => {
        // Clear token from simulation storage
        localStorage.removeItem("auth_token");
        // In real app, call Better Auth signOut()
        router.push("/login");
    };

    return (
        <button 
            onClick={handleLogout}
            className="bg-red-500 text-white px-4 py-2 rounded"
        >
            Logout
        </button>
    );
};
