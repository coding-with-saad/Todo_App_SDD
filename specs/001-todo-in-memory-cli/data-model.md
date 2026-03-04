# Data Model: Todo In-Memory Python CLI

## Entity: Task
Represent a single todo item.

| Field | Type | Description |
|-------|------|-------------|
| id | int | Unique auto-generated identifier |
| title | str | Name of the task (must be non-empty) |
| status | str | Status: "Pending" or "Complete" |

## State Transitions
- **Add**: Creates task in "Pending" status.
- **Mark Complete**: Changes status from "Pending" to "Complete".
- **Update**: Modifies the title attribute.
- **Delete**: Removes task from the collection.
