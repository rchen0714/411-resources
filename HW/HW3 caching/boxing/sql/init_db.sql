DROP TABLE IF EXISTS boxers;

CREATE TABLE boxers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    weight REAL NOT NULL,
    height REAL NOT NULL,
    reach REAL NOT NULL,
    age INTEGER NOT NULL,
    fights INTEGER NOT NULL DEFAULT 0,
    wins INTEGER NOT NULL DEFAULT 0,
    weight_class TEXT
);

CREATE INDEX idx_boxers_name ON boxers(name);
CREATE INDEX idx_boxers_weight_class ON boxers(weight_class);
CREATE INDEX idx_boxers_wins ON boxers(wins);
CREATE INDEX idx_boxers_age ON boxers(age);