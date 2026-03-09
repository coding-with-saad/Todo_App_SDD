'use client';

import React, { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Button } from '@/components/ui/Button';

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
    const router = useRouter();

    useEffect(() => {
        // Simple auth check
        const token = localStorage.getItem('auth_token');
        if (!token) {
            router.push('/login');
        }
    }, [router]);

    const handleLogout = () => {
        localStorage.removeItem('auth_token');
        router.push('/login');
    };

    return (
        <div className="min-h-screen bg-gray-50 flex flex-col">
            <header className="bg-white border-b px-6 py-4 flex items-center justify-between shadow-sm">
                <h1 className="text-xl font-bold text-blue-600 tracking-tight">TodoMaster</h1>
                <div className="flex items-center gap-4">
                    <Button variant="secondary" onClick={handleLogout} className="text-sm">
                        Logout
                    </Button>
                </div>
            </header>
            <main className="flex-1 max-w-4xl w-full mx-auto p-6">
                {children}
            </main>
        </div>
    );
}
