CREATE TABLE leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    company TEXT NOT NULL,
    status TEXT NOT NULL,
    score REAL DEFAULT 0
);
