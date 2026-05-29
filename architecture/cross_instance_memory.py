import os
import sqlite3
import json
from datetime import datetime

MEMORY_DIR = "/mnt/agents/output/persistent_memory_system"
DB_PATH = os.path.join(MEMORY_DIR, "memory_matrix.db")
os.makedirs(MEMORY_DIR, exist_ok=True)

class CrossInstanceMemory:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS system_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT, instance_id TEXT,
                memory_key TEXT UNIQUE, memory_payload TEXT
            )
        """)
    
    def write(self, instance_id: str, key: str, payload: dict) -> bool:
        ts = datetime.utcnow().isoformat()
        try:
            self.conn.execute("""
                INSERT INTO system_memory (timestamp, instance_id, memory_key, memory_payload)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(memory_key) DO UPDATE SET
                    timestamp=excluded.timestamp,
                    instance_id=excluded.instance_id,
                    memory_payload=excluded.memory_payload
            """, (ts, instance_id, key, json.dumps(payload)))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Write failed: {e}")
            return False
    
    def read(self, key: str) -> dict | None:
        row = self.conn.execute(
            "SELECT memory_payload FROM system_memory WHERE memory_key = ?", (key,)
        ).fetchone()
        return json.loads(row[0]) if row else None
    
    def ledger(self):
        return self.conn.execute(
            "SELECT timestamp, instance_id, memory_key FROM system_memory ORDER BY timestamp DESC"
        ).fetchall()

# Usage
if __name__ == "__main__":
    mem = CrossInstanceMemory()
    mem.write("demo_instance", "test_key", {"status": "operational"})
    print(mem.read("test_key"))
