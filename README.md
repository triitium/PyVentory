# Pyventory

Pyventory is a lightweight Python-based inventory management application designed to track laboratory samples, their descriptions, compounds, volumes, expiration dates, and related metadata. The application provides a user-friendly GUI for inserting, searching, and managing sample data efficiently.

---

## Features

- **Insert Data**: Add new samples with all relevant information including Sample ID, Description, Compound, Volume, Expiration Date, Validity, Comments, and Series information.
- **Search**: Query existing samples by multiple categories such as Sample ID, Description, Compound, Expiration Date, Validity, Series Name, Date, and Comment.
- **Series Management**: Group samples into series for easier batch management.
- **Database Integration**: Uses SQLAlchemy ORM for interaction with a PostgreSQL database.
- **GUI**: Built with PySide6 for a modern, responsive interface.
- **Configuration**: Easily manage database connection settings using a `.env` file.

---

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL database
- Required Python packages (listed in `requirements.txt`):

```bash
pip install -r requirements.txt
```

---

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/pyventory.git
cd pyventory
```

2. **Create a `.env` file** in the root directory with your database connection details:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=username
DB_PASSWORD=password
DB_NAME=pyventory
```

3. **Initialize the database tables:**

```python
from modules.sql import SQL
sql = SQL(host, port, user, password, database)
sql.create_table()
```

---

## Usage

Run the main application:

```bash
python main.py
```

### GUI Overview

- **Insert Data**: Opens a dialog to input sample information.
- **Search**: Open the search dialog to filter samples by various criteria.
- **Refresh**: Reload the data table to display updated entries.

---

## Project Structure

```
pyventory/
│
├── main.py                 # Main application entry point
├── sql.py                  # Database connection and setup
├── modules/                # Database models and helper classes
│   ├── __init__.py
│   └── ...
├── ui/                     # Auto-generated PySide6 UI files
│   ├── mainwindow.ui
│   ├── insertdialog.ui
│   ├── searchdialog.ui
│   └── ...
├── .env                    # Environment variables for database
├── README.md
└── requirements.txt
```

---

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

---

## License

MIT License © [Your Name]

---

## Acknowledgments

- Built using [PySide6](https://pypi.org/project/PySide6/) for GUI.
- Database ORM via [SQLAlchemy](https://www.sqlalchemy.org/).

