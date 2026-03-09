'use client';

import React, { useState } from 'react';
import { Input } from './ui/Input';
import { Button } from './ui/Button';
import { Plus, AlignLeft } from 'lucide-react';

interface TaskFormProps {
    onTaskCreated: (title: string, description: string) => void;
    loading?: boolean;
}

export const TaskForm: React.FC<TaskFormProps> = ({ onTaskCreated, loading }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (title.trim()) {
            onTaskCreated(title, description);
            setTitle('');
            setDescription('');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 mb-8 transition-all hover:shadow-md">
            <div className="flex flex-col gap-4">
                <div className="flex flex-col gap-1">
                    <label className="text-sm font-semibold text-gray-700 ml-1">Task Title</label>
                    <Input 
                        placeholder="What needs to be done?"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        className="text-lg font-medium py-3 border-gray-200 focus:border-blue-500"
                        required
                    />
                </div>
                
                <div className="flex flex-col gap-1">
                    <label className="text-sm font-semibold text-gray-700 ml-1 flex items-center gap-1">
                        <AlignLeft size={14} /> Description
                    </label>
                    <textarea 
                        placeholder="Add some more details..."
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        className="w-full border border-gray-200 rounded-xl px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none min-h-[80px] resize-none text-gray-600"
                    />
                </div>

                <Button type="submit" disabled={loading} className="w-full sm:w-auto self-end flex items-center justify-center gap-2 px-8 py-3 rounded-xl shadow-lg shadow-blue-100">
                    <Plus size={20} />
                    <span>Add Task</span>
                </Button>
            </div>
        </form>
    );
};
