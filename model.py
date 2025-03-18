import sqlite3

DB_FILE = "database.db"

def get_leads():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, company, status, score FROM leads")
    leads = [{"name": row[0], "company": row[1], "status": row[2], "score": row[3]} for row in cursor.fetchall()]
    conn.close()
    return leads

def add_lead(lead):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leads (name, company, status, score) VALUES (?, ?, ?, ?)",
                   (lead["name"], lead["company"], lead["status"], lead["score"]))
    conn.commit()
    conn.close()
