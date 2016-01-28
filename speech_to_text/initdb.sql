DROP TABLE IF EXISTS textlogs;
CREATE TABLE textlogs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  filename TEXT,
  text TEXT,
  created_at INTEGER
);
