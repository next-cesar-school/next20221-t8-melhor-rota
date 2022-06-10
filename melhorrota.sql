DROP TABLE IF EXISTS caminhoes;

CREATE TABLE caminhoes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT NOT NULL,
	localizacao TEXT NOT NULL,
	status BOOLEAN NOT NULL
);

select * from caminhoes;