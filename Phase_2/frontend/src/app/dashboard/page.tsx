'use client';

import React, { useState, useEffect } from 'react';
import { TaskForm } from '@/components/TaskForm';
import { TaskList } from '@/components/TaskList';
import { api } from '@/lib/api-client';

interface Task {
    id: number;
    title: string;
    description?: string;
    completed: boolean;
}

export default function DashboardPage() {
    const [tasks, setTasks] = useState<Task[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    const fetchTasks = async () => {
        try {
            setLoading(true);
            const data = await api.getTodos();
            setTasks(data);
        } catch (err: unknown) {
            setError('Failed to load tasks');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    const handleCreateTask = async (title: string, description: string) => {
        try {
            const newTask = await api.createTodo({ title, description });
            setTasks([newTask, ...tasks]);
        } catch (err: unknown) {
            const message = err instanceof Error ? err.message : 'Failed to create task';
            alert(message);
        }
    };

    const handleToggleTask = async (id: number, completed: boolean) => {
        const originalTasks = [...tasks];
        setTasks(tasks.map(t => t.id === id ? { ...t, completed } : t));

        try {
            await api.updateTodo(id, { completed });
        } catch {
            setTasks(originalTasks);
            alert('Failed to update task status');
        }
    };

    const handleUpdateTask = async (id: number, title: string, description: string) => {
        const originalTasks = [...tasks];
        setTasks(tasks.map(t => t.id === id ? { ...t, title, description } : t));

        try {
            await api.updateTodo(id, { title, description });
        } catch {
            setTasks(originalTasks);
            alert('Failed to save task updates');
        }
    };

    const handleDeleteTask = async (id: number) => {
        if (!confirm('Are you sure you want to delete this task?')) return;

        const originalTasks = [...tasks];
        setTasks(tasks.filter(t => t.id !== id));

        try {
            await api.deleteTodo(id);
        } catch {
            setTasks(originalTasks);
            alert('Failed to delete task');
        }
    };

    return (
        <div className="max-w-2xl mx-auto py-8">
            <header className="mb-10 text-center sm:text-left">
                <h2 className="text-4xl font-black text-gray-900 mb-2 tracking-tight">Your Dashboard</h2>
                <p className="text-gray-500 text-lg">Organize your thoughts, one task at a time.</p>
            </header>

            <TaskForm onTaskCreated={handleCreateTask} />

            <div className="mt-12">
                <div className="flex items-center justify-between mb-6">
                    <h3 className="text-xl font-bold text-gray-800">Your Tasks</h3>
                    <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm font-bold">
                        {tasks.length} Total
                    </span>
                </div>

                {error && (
                    <div className="bg-red-50 text-red-600 p-4 rounded-xl mb-6 border border-red-100 flex items-center justify-between">
                        <span>{error}</span>
                        <button onClick={fetchTasks} className="underline font-bold">Retry</button>
                    </div>
                )}

                <TaskList 
                    tasks={tasks} 
                    onToggle={handleToggleTask} 
                    onDelete={handleDeleteTask} 
                    onUpdate={handleUpdateTask}
                    loading={loading}
                />
            </div>
        </div>
    );
}
