---
name: database-design
description: Design databases, create tables, manage schema structure, and handle migrations. Use when building or evolving application data models.
---

# Database Skill – Tables, Schema Design, Migrations

## Instructions

1. **Schema Design**
   - Identify core entities and relationships
   - Define primary keys for each table
   - Use clear, consistent naming for tables and columns
   - Normalize data to avoid redundancy

2. **Create Tables**
   - Define columns with correct data types
   - Apply constraints (PRIMARY KEY, UNIQUE, NOT NULL)
   - Add foreign keys to maintain relationships
   - Use indexes for frequently queried fields

3. **Migrations**
   - Track schema changes using migration files
   - Create migrations for table creation, updates, or deletions
   - Apply migrations sequentially
   - Ensure backward compatibility when modifying schemas

4. **Schema Evolution**
   - Avoid destructive changes without migrations
   - Add new columns safely with defaults
   - Maintain data integrity during updates

## Best Practices

- Use consistent naming conventions
- Always define primary keys
- Add indexes for performance-critical queries
- Keep migration files small and atomic
- Review schema changes before applying in production