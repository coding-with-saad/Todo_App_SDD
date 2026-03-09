'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Card } from '@/components/ui/Card';
import { Input } from '@/components/ui/Input';
import { Button } from '@/components/ui/Button';
import Link from 'next/link';
import { Mail, Lock, LogIn, CheckCircle2 } from 'lucide-react';
import { api } from '@/lib/api-client';

export default function LoginPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const data = await api.login({ email, password });
            
            // Store the real JWT from the backend
            if (data.access_token) {
                localStorage.setItem('auth_token', data.access_token);
                console.log('Token stored successfully');
                router.push('/dashboard');
            }
 else {
                throw new Error('No access token received');
            }
        } catch (err: unknown) {
            const message = err instanceof Error ? err.message : 'Login failed';
            setError(message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-linear-to-br from-blue-50 to-indigo-100 p-4">
            <div className="w-full max-w-md">
                <div className="text-center mb-8">
                    <div className="inline-flex items-center justify-center w-16 h-16 bg-blue-600 rounded-2xl shadow-lg mb-4 text-white">
                        <CheckCircle2 size={32} />
                    </div>
                    <h1 className="text-3xl font-extrabold text-gray-900 tracking-tight">TodoMaster</h1>
                    <p className="text-gray-500 mt-2">Welcome back! Please enter your details.</p>
                </div>

                <Card className="shadow-xl border-0 ring-1 ring-black/5">
                    <h2 className="text-xl font-bold text-gray-800 mb-6 flex items-center gap-2">
                        <LogIn size={20} className="text-blue-600" />
                        Log In
                    </h2>
                    
                    <form onSubmit={handleSubmit} className="flex flex-col gap-5">
                        <div className="relative">
                            <Mail className="absolute left-3 top-9 text-gray-400" size={18} />
                            <Input 
                                label="Email Address"
                                type="email"
                                placeholder="you@example.com"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                className="pl-10"
                                required
                            />
                        </div>
                        
                        <div className="relative">
                            <Lock className="absolute left-3 top-9 text-gray-400" size={18} />
                            <Input 
                                label="Password"
                                type="password"
                                placeholder="••••••••"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                className="pl-10"
                                required
                            />
                        </div>

                        {error && (
                            <div className="bg-red-50 text-red-600 text-sm p-3 rounded-md border border-red-100">
                                {error}
                            </div>
                        )}

                        <Button 
                            type="submit" 
                            disabled={loading}
                            className="w-full py-3 shadow-md hover:shadow-lg transition-all"
                        >
                            {loading ? (
                                <span className="flex items-center justify-center gap-2">
                                    <div className="animate-spin h-4 w-4 border-2 border-white border-t-transparent rounded-full" />
                                    Logging in...
                                </span>
                            ) : 'Log In'}
                        </Button>
                    </form>

                    <div className="mt-8 pt-6 border-t border-gray-100 text-center">
                        <p className="text-sm text-gray-600">
                            Don&apos;t have an account?{' '}
                            <Link href="/signup" className="font-semibold text-blue-600 hover:text-blue-700 transition-colors">
                                Sign Up
                            </Link>
                        </p>
                    </div>
                </Card>
                
                <p className="text-center mt-8 text-xs text-gray-400 uppercase tracking-widest">
                    &copy; 2026 TodoMaster Inc.
                </p>
            </div>
        </div>
    );
}
