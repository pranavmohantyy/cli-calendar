# CLI Calendar

A simple terminal calendar for managing events and reminders.

## Features
- Create and manage events
- Set reminders
- Weekly planning view

## Installation
Clone the repository and run:

```bash
python calendar.py
```

## Usage
### Adding an Event
Add an event by providing the date, time, title, and description:

```python
new_event = Event(date="2023-10-15", time="14:00", title="Meeting", description="Discuss project updates", reminder_minutes=30)
```

### Loading Events
Load events from the local JSON file:

```python
events = load_events()
```

### Saving Events
Save events to the local JSON file:

```python
save_events()
```

## License
MIT License