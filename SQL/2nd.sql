SELECT * FROM mydbms.`messlife`;

CREATE TABLE `mydbms`.`mess life` (
   `friend_name` VARCHAR(20) NOT NULL,
   `room_no` INT NOT NULL,
   `age` INT NOT NULL,
   `collage_name` VARCHAR(45) NOT NULL,
   `speciality` VARCHAR(45) NOT NULL,
   PRIMARY KEY (`friend_name`));

 ALTER TABLE `mydbms`.`mess life` 
 RENAME TO  `mydbms`.`messlife` ;

UPDATE `mydbms`.`messlife` SET `room_no` = '1', `speciality` = 'Handel in mess' WHERE (`friend_name` = 'Malay');
UPDATE `mydbms`.`messlife` SET `speciality` = 'W on Rockster in mess' WHERE (`friend_name` = 'Bibhakar');

INSERT INTO `mydbms`.`messlife` (`friend_name`, `room_no`, `age`, `collage_name`, `speciality`) VALUES ('Bibhakar', '1', '20', 'SGP', 'Rockster on w mess');
INSERT INTO `mydbms`.`messlife` (`friend_name`, `room_no`, `age`, `collage_name`, `speciality`) VALUES ( 'Malay', '1', '21', 'SGP', 'firstyear in ramukaka in mess');