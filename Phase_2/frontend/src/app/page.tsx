'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { Button } from '@/components/ui/Button';
import { CheckCircle2, ListTodo, ShieldCheck, Zap, ArrowRight, Github } from 'lucide-react';

export default function LandingPage() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem('auth_token');
        setIsLoggedIn(!!token);
    }, []);

    return (
        <div className="min-h-screen bg-white text-gray-900 font-sans">
            {/* Navigation */}
            <nav className="flex items-center justify-between px-6 py-6 max-w-7xl mx-auto border-b border-gray-50">
                <div className="flex items-center gap-2">
                    <div className="bg-blue-600 p-1.5 rounded-lg text-white">
                        <CheckCircle2 size={24} />
                    </div>
                    <span className="text-xl font-bold tracking-tight text-blue-600">TodoMaster</span>
                </div>
                <div className="flex items-center gap-6">
                    {isLoggedIn ? (
                        <Link href="/dashboard">
                            <Button className="rounded-full px-6">Go to Dashboard</Button>
                        </Link>
                    ) : (
                        <>
                            <Link href="/login" className="text-sm font-semibold hover:text-blue-600 transition-colors">
                                Sign in
                            </Link>
                            <Link href="/signup">
                                <Button className="rounded-full px-6 shadow-lg shadow-blue-200">Get Started</Button>
                            </Link>
                        </>
                    )}
                </div>
            </nav>

            {/* Hero Section */}
            <section className="relative pt-20 pb-32 overflow-hidden">
                <div className="max-w-7xl mx-auto px-6 text-center">
                    <div className="inline-flex items-center gap-2 bg-blue-50 text-blue-700 px-4 py-2 rounded-full text-sm font-medium mb-8 animate-fade-in">
                        <Zap size={16} />
                        <span>Phase II is now live with persistent storage</span>
                    </div>
                    <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-8 leading-tight">
                        Organize your work <br />
                        <span className="text-blue-600">without the chaos.</span>
                    </h1>
                    <p className="text-xl text-gray-500 max-w-2xl mx-auto mb-12 leading-relaxed">
                        TodoMaster helps you capture and organize your tasks the moment they come to mind. 
                        Safe, secure, and available on all your devices.
                    </p>
                    <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
                        <Link href={isLoggedIn ? "/dashboard" : "/signup"}>
                            <Button className="w-full sm:w-auto text-lg px-10 py-7 rounded-2xl shadow-xl shadow-blue-200 flex items-center gap-2">
                                Start for free <ArrowRight size={20} />
                            </Button>
                        </Link>
                        <a href="https://github.com" target="_blank" rel="noopener noreferrer">
                            <Button variant="secondary" className="w-full sm:w-auto text-lg px-10 py-7 rounded-2xl border border-gray-200 bg-white hover:bg-gray-50 flex items-center gap-2">
                                <Github size={20} /> View on GitHub
                            </Button>
                        </a>
                    </div>
                </div>

                {/* Background Decoration */}
                <div className="absolute top-0 left-1/2 -translate-x-1/2 -z-10 w-full max-w-4xl h-[500px] bg-linear-to-b from-blue-100/50 to-transparent blur-3xl opacity-50 rounded-full" />
            </section>

            {/* Features Grid */}
            <section className="bg-gray-50 py-24">
                <div className="max-w-7xl mx-auto px-6">
                    <div className="text-center mb-16">
                        <h2 className="text-3xl font-bold mb-4">Why choose TodoMaster?</h2>
                        <p className="text-gray-500">Everything you need to stay productive, every day.</p>
                    </div>
                    
                    <div className="grid md:grid-cols-3 gap-8">
                        <FeatureCard 
                            icon={<ListTodo className="text-blue-600" size={32} />}
                            title="Task Management"
                            description="Create, update, and delete tasks with ease. Our intuitive interface keeps you focused on what matters."
                        />
                        <FeatureCard 
                            icon={<ShieldCheck className="text-indigo-600" size={32} />}
                            title="Safe & Secure"
                            description="Your data is protected with JWT-based authentication and hosted on Neon Serverless PostgreSQL."
                        />
                        <FeatureCard 
                            icon={<Zap className="text-orange-500" size={32} />}
                            title="Blazing Fast"
                            description="Built with FastAPI and Next.js for a lightning-fast experience. No more waiting for spinners."
                        />
                    </div>
                </div>
            </section>

            {/* Footer */}
            <footer className="py-12 border-t border-gray-100">
                <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-6">
                    <div className="flex items-center gap-2 grayscale opacity-70">
                        <CheckCircle2 size={20} />
                        <span className="font-bold">TodoMaster</span>
                    </div>
                    <p className="text-sm text-gray-400">
                        &copy; 2026 TodoMaster Application. All rights reserved.
                    </p>
                    <div className="flex gap-6 text-sm text-gray-500 font-medium">
                        <Link href="/login" className="hover:text-blue-600">Login</Link>
                        <Link href="/signup" className="hover:text-blue-600">Signup</Link>
                        <a href="#" className="hover:text-blue-600">Privacy</a>
                    </div>
                </div>
            </footer>
        </div>
    );
}

function FeatureCard({ icon, title, description }: { icon: React.ReactNode, title: string, description: string }) {
    return (
        <div className="bg-white p-10 rounded-3xl border border-gray-100 shadow-sm hover:shadow-xl transition-all hover:-translate-y-1">
            <div className="mb-6">{icon}</div>
            <h3 className="text-xl font-bold mb-4">{title}</h3>
            <p className="text-gray-500 leading-relaxed">{description}</p>
        </div>
    );
}
