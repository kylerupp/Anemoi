CREATE DATABASE IF NOT EXISTS amenoi_db;

USE amenoi_db;

CREATE TABLE `amenoi_db`.`id` (
    `mac` VARCHAR(17) NOT NULL,
    `time` DATETIME NOT NULL,
    `last_online` DATETIME NOT NULL,
    PRIMARY KEY (`mac`)
);

CREATE TABLE `amenoi_db`.`firmware` (
    `mac` VARCHAR(17) NOT NULL,
    `firmware` VARCHAR(16) NOT NULL,
    PRIMARY KEY (`mac`)
);

CREATE TABLE `amenoi_db`.`location` (
    `mac` VARCHAR(17) NOT NULL,
    `location` VARCHAR(32),
    PRIMARY KEY (`mac`)
);

CREATE TABLE `amenoi_db`.`data` (
    `mac` VARCHAR(17) NOT NULL,
    `temp` INT NOT NULL,
    `time` DATETIME NOT NULL,
    PRIMARY KEY (`mac`,`time`)
);
