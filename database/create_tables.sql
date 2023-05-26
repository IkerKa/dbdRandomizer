

--Partiremos de la imagen del modelo entidad-relación que se encuentra en la carpeta "Image"

--Tabla de Survivors
--Tabla de Killers
--Tabla de Items
--Tabla de Perks
--Tabla de Offerings
--Tabla de Item-Addons
--Tabla de Power-Addons

CREATE TABLE Perks 
(
    perkName VARCHAR(50) NOT NULL,
    icon TEXT NOT NULL,
    perkDescription TEXT NOT NULL,
    --fromKiller and fromSurvivor will be integers
    fromSurvivor INT NOT NULL,
    fromKiller INT NOT NULL,


    PRIMARY KEY(perkName)
);

--Tabla de Survivors
CREATE TABLE Survivors
(
    survName VARCHAR(50) NOT NULL,

    perk_1s VARCHAR(50) NOT NULL,
    perk_2s VARCHAR(50) NOT NULL,
    perk_3s VARCHAR(50) NOT NULL,

    biography TEXT NOT NULL,

    image_s TEXT NOT NULL,

    PRIMARY KEY (survName),
    
    --las perks serán una clave ajena de la tabla Perks (porque son las que, pertenezcan al survivor en cuestion)
    FOREIGN KEY (perk_1s) REFERENCES Perks(perkName),
    FOREIGN KEY (perk_2s) REFERENCES Perks(perkName),
    FOREIGN KEY (perk_3s) REFERENCES Perks(perkName)
);

--Tabla de Killers
CREATE TABLE Killers
(
    killerName VARCHAR(50) NOT NULL,

    perk_1k VARCHAR(50) NOT NULL,
    perk_2k VARCHAR(50) NOT NULL,
    perk_3k VARCHAR(50) NOT NULL,

    mainHability VARCHAR(100) NOT NULL,

    image_k TEXT NOT NULL,

    PRIMARY KEY (killerName),
    
    --las perks serán una clave ajena de la tabla Perks (porque son las que, pertenezcan al killer en cuestion)
    FOREIGN KEY (perk_1k) REFERENCES Perks(perkName),
    FOREIGN KEY (perk_2k) REFERENCES Perks(perkName),
    FOREIGN KEY (perk_3k) REFERENCES Perks(perkName)
    
);

--modificar mainHability para que sea TEXT
--alter table Killers modify mainHability TEXT;
--en postgresql
--alter table Killers alter column mainHability type TEXT;

--Tabla de Items
CREATE TABLE Items
(

    itemName VARCHAR(50) NOT NULL,
    itemDescription TEXT NOT NULL,
    itemIcon TEXT NOT NULL,     --Url de la imagen del item

    PRIMARY KEY (itemName)
);

--Tabla de Item_Addons
CREATE TABLE Item_Addons
(
    addonName VARCHAR(50) NOT NULL,
    itemName VARCHAR(50) NOT NULL,

    addonDescription TEXT NOT NULL,
    addonIcon TEXT NOT NULL,    --Url de la imagen del addon

    PRIMARY KEY (itemName, addonName),

    --itemName será una clave ajena de la tabla Items (porque son los items a los que pertenezcan los addons)
    FOREIGN KEY (itemName) REFERENCES Items(itemName)
);

--Tabla de Offerings

CREATE TABLE Offerings
(

    offerName VARCHAR(50) NOT NULL,
    descripcion VARCHAR(50) NOT NULL,
    icon TEXT NOT NULL,
    
    fromSurvivor INT NOT NULL,
    
    fromKiller INT NOT NULL,

    PRIMARY KEY (offerName)
);

--alter table Offerings alter column descripcion type TEXT;

--POSTGRESQL, cambiar boolean a entero
--alter table Offerings alter column fromSurvivor type INT;
--alter table Offerings alter column fromKiller type INT;

--SQL Error [42804]: ERROR: column "fromkiller" cannot be cast automatically to type integer
  --Hint: You might need to specify "USING fromkiller::integer".

--   alter table Offerings alter column fromKiller type INT USING fromKiller::integer;
--   alter table Offerings alter column fromSurvivor type INT USING fromSurvivor::integer;

--Tabla de Power_Addons
CREATE TABLE Power_Addons
(
    powerAddName VARCHAR(50) NOT NULL,
    killerName VARCHAR(50) NOT NULL,

    powerAddDescription TEXT NOT NULL,
    powerAddIcon TEXT NOT NULL,    --Url de la imagen del addon

    PRIMARY KEY (killerName, powerAddName),     --entidad debil
    
    --killerName será una clave ajena de la tabla Killers (porque son los killers a los que pertenezcan los addons)
    FOREIGN KEY (killerName) REFERENCES Killers(killerName)
);