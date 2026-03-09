'use client';

import React from 'react';
import { TaskItem } from './TaskItem';

interface Task {
    id: number;
    title: string;
    description?: string;
    completed: boolean;
}

interface TaskListProps {
    tasks: Task[];
    onToggle: (id: number, completed: boolean) => void;
    onDelete: (id: number) => void;
    onUpdate: (id: number, title: string, description: string) => void;
    loading?: boolean;
}

export const TaskList: React.FC<TaskListProps> = ({ tasks, onToggle, onDelete, onUpdate, loading }) => {
    if (loading) {
        return (
            <div className="flex flex-col gap-3 animate-pulse">
                {[1, 2, 3].map(i => (
                    <div key={i} className="h-24 bg-gray-200 rounded-2xl"></div>
                ))}
            </div>
        );
    }

    if (tasks.length === 0) {
        return (
            <div className="text-center py-16 bg-white border-2 border-dashed border-gray-100 rounded-3xl">
                <p className="text-gray-500 mb-2 font-semibold text-lg">Your task list is empty</p>
                <p className="text-gray-400">Add your first task above to start your journey!</p>
            </div>
        );
    }

    return (
        <div className="space-y-4">
            {tasks.map(task => (
                <TaskItem 
                    key={task.id} 
                    task={task} 
                    onToggle={onToggle} 
                    onDelete={onDelete} 
                    onUpdate={onUpdate}
                />
            ))}
        </div>
    );
};
