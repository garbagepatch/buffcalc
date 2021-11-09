BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Buffer" (
	"id"	INTEGER NOT NULL UNIQUE,
	"Type"	TEXT NOT NULL UNIQUE,
	"pKa"	NUMERIC,
	"HAid"	INTEGER,
	"Aid"	INTEGER,
	FOREIGN KEY("Aid") REFERENCES "Chemical"("id"),
	FOREIGN KEY("HAid") REFERENCES "Chemical"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Chemical" (
	"Name"	TEXT NOT NULL UNIQUE,
	"MW"	NUMERIC NOT NULL,
	"id"	INTEGER,
	"Molarity"	INTEGER,
	"Comp"	INTEGER,
	"BufferId"	INTEGER,
	FOREIGN KEY("BufferId") REFERENCES "Buffer"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Buffer" VALUES (1,'Acetates',4.76,NULL,NULL);
INSERT INTO "Buffer" VALUES (2,'Sodium Phosphates',7.24,NULL,NULL);
INSERT INTO "Buffer" VALUES (3,'Tris',8.06,NULL,NULL);
INSERT INTO "Buffer" VALUES (4,'MOPS',7.2,NULL,NULL);
INSERT INTO "Buffer" VALUES (5,'MES',6.21,NULL,NULL);
INSERT INTO "Buffer" VALUES (6,'HEPES',7.66,1,NULL);
INSERT INTO "Buffer" VALUES (7,'',NULL,NULL,NULL);
INSERT INTO "Chemical" VALUES ('Sodium Acetate Anhydrous',82.03,1,NULL,1,1);
INSERT INTO "Chemical" VALUES ('Glacial Acetic Acid','',2,17.4,0,1);
INSERT INTO "Chemical" VALUES ('Sodium Acetate Trihydrate',136.08,3,NULL,1,1);
INSERT INTO "Chemical" VALUES ('Sodium Phosphate Monobasic Monohydrate',137.99,4,NULL,0,2);
INSERT INTO "Chemical" VALUES ('Sodium Phosphate Monobasic Dihydrate',156.01,5,NULL,0,2);
INSERT INTO "Chemical" VALUES ('Sodium Phosphate Monobasic Anhydrous',119.98,6,NULL,0,2);
INSERT INTO "Chemical" VALUES ('Sodium Phosphate Dibasic Anhydrous',141.96,7,NULL,1,2);
INSERT INTO "Chemical" VALUES ('Sodium Phosphate Dibasic Dihydrate',177.99,8,NULL,1,2);
INSERT INTO "Chemical" VALUES ('Sodium Phosphate Dibasic Heptahydrate',268.07,9,NULL,1,2);
INSERT INTO "Chemical" VALUES ('Tris',121.14,10,NULL,1,3);
INSERT INTO "Chemical" VALUES ('Tris HCl',157.6,11,NULL,0,3);
INSERT INTO "Chemical" VALUES ('MOPS',209.26,12,NULL,0,4);
INSERT INTO "Chemical" VALUES ('MOPS Sodium',231.25,13,NULL,1,4);
INSERT INTO "Chemical" VALUES ('MES',195.24,14,NULL,0,5);
INSERT INTO "Chemical" VALUES ('MES Sodium',217.22,15,NULL,1,5);
INSERT INTO "Chemical" VALUES ('HEPES',238.61,16,NULL,0,6);
INSERT INTO "Chemical" VALUES ('HEPES Sodium',260.28,17,NULL,1,6);
COMMIT;
