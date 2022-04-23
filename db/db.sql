CREATE DATABASE IF NOT EXISTS amenoi_db;

USE amenoi_db;

CREATE TABLE `amenoi_db`.`id` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `mac` VARCHAR(16) NOT NULL,
    `time` DATETIME NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `amenoi_db`.`location` (
    `mac` INT NOT NULL,
    `location` VARCHAR(32),
    PRIMARY KEY (`mac`)
);

CREATE TABLE `amenoi_db`.`temp` (
    `mac` INT NOT NULL,
    `temp` INT NOT NULL,
    `time` DATETIME NOT NULL,
    PRIMARY KEY (`mac`,`time`)
);
