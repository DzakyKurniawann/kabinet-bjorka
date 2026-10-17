CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nim TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    prodi TEXT DEFAULT 'Informatika',
    angkatan TEXT DEFAULT '2026',
    photo_url TEXT,
    role TEXT DEFAULT 'mahasiswa' CHECK(role IN ('mahasiswa', 'admin')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL CHECK(category IN ('event', 'recruit', 'assign', 'pay')),
    title TEXT NOT NULL,
    start_day INTEGER NOT NULL,
    end_day INTEGER NOT NULL,
    location TEXT,
    description TEXT,
    amount TEXT DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    division TEXT DEFAULT NULL,
    motivation TEXT DEFAULT NULL,
    proof_file TEXT DEFAULT NULL,
    status TEXT DEFAULT 'Menunggu' CHECK(status IN ('Menunggu', 'Terverifikasi', 'Ditolak')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);
