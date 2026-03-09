'use client';

import React, { useState } from 'react';
import { Trash2, CheckCircle, XCircle, Edit3, Save, X } from 'lucide-react';
import { Button } from './ui/Button';
import { Input } from './ui/Input';

interface Task {
    id: number;
    title: string;
    description?: string;
    completed: boolean;
}

interface TaskItemProps {
    task: Task;
    onToggle: (id: number, completed: boolean) => void;
    onDelete: (id: number) => void;
    onUpdate: (id: number, title: string, description: string) => void;
}

export const TaskItem: React.FC<TaskItemProps> = ({ task, onToggle, onDelete, onUpdate }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [editTitle, setEditTitle] = useState(task.title);
    const [editDesc, setEditDesc] = useState(task.description || '');

    const handleSave = () => {
        onUpdate(task.id, editTitle, editDesc);
        setIsEditing(false);
    };

    return (
        <div className={`p-6 bg-white border rounded-2xl mb-4 transition-all shadow-sm hover:shadow-md ${task.completed ? 'bg-gray-50/50' : ''}`}>
            {isEditing ? (
                <div className="flex flex-col gap-3">
                    <Input 
                        value={editTitle} 
                        onChange={(e) => setEditTitle(e.target.value)}
                        className="font-bold text-lg"
                    />
                    <textarea 
                        value={editDesc} 
                        onChange={(e) => setEditDesc(e.target.value)}
                        className="w-full border border-gray-200 rounded-xl px-3 py-2 outline-none min-h-[60px] resize-none text-gray-600"
                    />
                    <div className="flex gap-2 justify-end mt-2">
                        <Button variant="secondary" onClick={() => setIsEditing(false)} className="flex items-center gap-1">
                            <X size={16} /> Cancel
                        </Button>
                        <Button onClick={handleSave} className="flex items-center gap-1 bg-green-600 hover:bg-green-700">
                            <Save size={16} /> Save Changes
                        </Button>
                    </div>
                </div>
            ) : (
                <>
                    <div className="mb-4">
                        <h3 className={`text-xl font-bold mb-1 ${task.completed ? 'line-through text-gray-400' : 'text-gray-800'}`}>
                            {task.title}
                        </h3>
                        {task.description && (
                            <p className={`text-gray-500 leading-relaxed ${task.completed ? 'line-through opacity-50' : ''}`}>
                                {task.description}
                            </p>
                        )}
                    </div>

                    <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-4 border-t border-gray-50">
                        {task.completed ? (
                            <Button 
                                variant="secondary" 
                                onClick={() => onToggle(task.id, false)}
                                className="flex items-center justify-center gap-2 text-xs font-bold"
                            >
                                <XCircle size={16} /> Not Done
                            </Button>
                        ) : (
                            <Button 
                                onClick={() => onToggle(task.id, true)}
                                className="flex items-center justify-center gap-2 text-xs font-bold bg-green-600 hover:bg-green-700"
                            >
                                <CheckCircle size={16} /> Done
                            </Button>
                        )}

                        <Button 
                            variant="secondary" 
                            onClick={() => setIsEditing(true)}
                            className="flex items-center justify-center gap-2 text-xs font-bold"
                        >
                            <Edit3 size={16} /> Edit
                        </Button>

                        <Button 
                            variant="danger" 
                            onClick={() => onDelete(task.id)}
                            className="flex items-center justify-center gap-2 text-xs font-bold col-span-2 sm:col-span-1"
                        >
                            <Trash2 size={16} /> Delete
                        </Button>
                    </div>
                </>
            )}
        </div>
    );
};
