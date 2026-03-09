'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Card } from '@/components/ui/Card';
import { Input } from '@/components/ui/Input';
import { Button } from '@/components/ui/Button';
import Link from 'next/link';
import { User, Mail, Lock, UserPlus, CheckCircle2 } from 'lucide-react';
import { api } from '@/lib/api-client';

export default function SignupPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            await api.register({ email, password, name });
            alert('Signup successful! Please log in.');
            router.push('/login');
        } catch (err: unknown) {
            const message = err instanceof Error ? err.message : 'Signup failed';
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
                    <h1 className="text-3xl font-extrabold text-gray-900 tracking-tight">Join TodoMaster</h1>
                    <p className="text-gray-500 mt-2">Start organizing your life today.</p>
                </div>

                <Card className="shadow-xl border-0 ring-1 ring-black/5">
                    <h2 className="text-xl font-bold text-gray-800 mb-6 flex items-center gap-2">
                        <UserPlus size={20} className="text-blue-600" />
                        Create Account
                    </h2>
                    
                    <form onSubmit={handleSubmit} className="flex flex-col gap-5">
                        <div className="relative">
                            <User className="absolute left-3 top-9 text-gray-400" size={18} />
                            <Input 
                                label="Full Name"
                                placeholder="John Doe"
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                className="pl-10"
                                required
                            />
                        </div>

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
                                minLength={8}
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
                            className="w-full py-3 shadow-md hover:shadow-lg transition-all bg-blue-600 hover:bg-blue-700"
                        >
                            {loading ? (
                                <span className="flex items-center justify-center gap-2">
                                    <div className="animate-spin h-4 w-4 border-2 border-white border-t-transparent rounded-full" />
                                    Creating Account...
                                </span>
                            ) : 'Sign Up'}
                        </Button>
                    </form>

                    <div className="mt-8 pt-6 border-t border-gray-100 text-center">
                        <p className="text-sm text-gray-600">
                            Already have an account?{' '}
                            <Link href="/login" className="font-semibold text-blue-600 hover:text-blue-700 transition-colors">
                                Log In
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
