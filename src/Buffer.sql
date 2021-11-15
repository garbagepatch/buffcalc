BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Buffer" (
	"id"	INTEGER NOT NULL UNIQUE,
	"Type"	TEXT NOT NULL UNIQUE,
	"HA"	TEXT,
	"A"	TEXT,
	"HAAlt1"	TEXT,
	"AAlt1"	TEXT,
	"HAAlt2"	TEXT,
	"AAlt2"	TEXT,
	"mwHA"	NUMERIC,
	"mwA"	NUMERIC,
	"mwHAAlt1"	NUMERIC,
	"mwAAlt1"	NUMERIC,
	"mwHAAlt2"	NUMERIC,
	"mwAAlt2"	NUMERIC,
	"pKa"	NUMERIC,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Buffer" VALUES (1,'Acetates','Glacial Acetic Acid','Sodium Acetate Anhydrous','','Sodium Acetate Trihydrate','','',17.4,82.03,'',136.08,'','',4.76);
INSERT INTO "Buffer" VALUES (2,'Sodium Phosphates','Sodium Phosphate Monobasic Monohydrate','Sodium Phosphate Dibasic Anhydrous','Sodium Phosphate Monobasic Dihydrate','Sodium Phosphate Dibasic Dihydrate','Sodium Phosphate Monobasic Anhydrous','Sodium Phosphate Dibasic Heptahydrate',137.99,141.96,156.01,177.99,119.98,268.07,7.24);
INSERT INTO "Buffer" VALUES (3,'Tris','Tris HCl','Tris','','','','',157.6,121.14,'','','','',8.06);
INSERT INTO "Buffer" VALUES (4,'MOPS','MOPS','MOPS Sodium','',NULL,NULL,NULL,209.26,231.25,NULL,NULL,NULL,NULL,7.2);
INSERT INTO "Buffer" VALUES (5,'MES','MES','MES Sodium','','','','',195.24,217.22,'','','','',6.21);
INSERT INTO "Buffer" VALUES (6,'HEPES','HEPES','HEPES Sodium','','','','',238.61,260.28,'','','','',7.66);
INSERT INTO "Buffer" VALUES (7,'','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
COMMIT;
