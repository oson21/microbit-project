
--
-- Setup av användare och databas
--

-- Skapa databas
-- CREATE DATABASE skolan;
CREATE DATABASE IF NOT EXISTS microB;

-- Skapa en användare user med lösenorder pass och ge tillgång oavsett
-- hostnamn. 
CREATE USER IF NOT EXISTS 'user'@'%'
IDENTIFIED BY 'pass'
;

-- Ge användaren alla rättigheter på en specifk databas.
GRANT ALL PRIVILEGES
    ON microB.*
    TO 'user'@'%'
;

--
-- Setup tables
--

SET NAMES 'utf8';
USE microB;

DROP TABLE IF EXISTS myapp_microbit;
DROP TABLE IF EXISTS myapp_microbitsummary;

CREATE TABLE IF NOT EXISTS myapp_microbit
(
`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`lastTemperatureReading` integer NOT NULL,
`lastLightReading` integer NOT NULL
);

CREATE TABLE IF NOT EXISTS myapp_microbitsummary
(
`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`temperatureMean` integer NOT NULL,
`lightMean` integer NOT NULL
);

BEGIN;
--
-- Alter field lastLightReading on microbit
--
ALTER TABLE `myapp_microbit` MODIFY `lastLightReading` varchar(6) NOT NULL;
--
-- Alter field lastTemperatureReading on microbit
--
ALTER TABLE `myapp_microbit` MODIFY `lastTemperatureReading` varchar(6) NOT NULL;
--
-- Alter field lightMean on microbitsummary
--
ALTER TABLE `myapp_microbitsummary` MODIFY `lightMean` varchar(6) NOT NULL;
--
-- Alter field temperatureMean on microbitsummary
--
ALTER TABLE `myapp_microbitsummary` MODIFY `temperatureMean` varchar(6) NOT NULL;
--
-- Alter field lightMean on microbitsummary
--
ALTER TABLE `myapp_microbit` MODIFY `timeOfReading` datetime NOT NULL DEFAULT current_timestamp;
--
-- Alter field lightMean on microbitsummary 
--
ALTER TABLE `myapp_microbitsummary` MODIFY `timeOfReading` datetime NOT NULL DEFAULT current_timestamp;
COMMIT;