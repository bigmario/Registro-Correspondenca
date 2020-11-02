SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS `fundamusicalBolivar` ;
CREATE SCHEMA IF NOT EXISTS `fundamusicalBolivar` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci ;
USE `fundamusicalBolivar` ;

-- -----------------------------------------------------
-- Table `fundamusicalBolivar`.`Institucion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `fundamusicalBolivar`.`Institucion` ;

CREATE  TABLE IF NOT EXISTS `fundamusicalBolivar`.`Institucion` (
  `inst_id` INT NOT NULL AUTO_INCREMENT ,
  `inst_Nombre` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`inst_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;


-- -----------------------------------------------------
-- Table `fundamusicalBolivar`.`Usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `fundamusicalBolivar`.`Usuario` ;

CREATE  TABLE IF NOT EXISTS `fundamusicalBolivar`.`Usuario` (
  `usu_id` INT NOT NULL AUTO_INCREMENT ,
  `usu_login` VARCHAR(45) NOT NULL ,
  `usu_pwd` VARCHAR(45) NOT NULL ,
  `usu_nombre` VARCHAR(45) NOT NULL ,
  `usu_apellido` VARCHAR(45) NOT NULL ,
  `usu_cargo` VARCHAR(45) NOT NULL ,
  `usu_rol` INT NOT NULL ,
  PRIMARY KEY (`usu_id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;

CREATE UNIQUE INDEX `usu_login_UNIQUE` ON `fundamusicalBolivar`.`Usuario` (`usu_login` ASC) ;


-- -----------------------------------------------------
-- Table `fundamusicalBolivar`.`Documento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `fundamusicalBolivar`.`Documento` ;

CREATE  TABLE IF NOT EXISTS `fundamusicalBolivar`.`Documento` (
  `doc_id` INT NOT NULL AUTO_INCREMENT ,
  `doc_fechaRegistro` DATE NOT NULL ,
  `doc_fechaDocRecep` DATE NOT NULL ,
  `doc_numOficio` VARCHAR(45) NOT NULL ,
  `doc_Tipo` VARCHAR(45) NOT NULL ,
  `doc_Titulo` VARCHAR(100) NOT NULL ,
  `doc_Remitente` VARCHAR(100) NOT NULL ,
  `doc_Observaciones` TEXT NULL ,
  `Institucion_inst_id` INT NOT NULL ,
  `Usuario_usu_id` INT NOT NULL ,
  PRIMARY KEY (`doc_id`, `Institucion_inst_id`, `Usuario_usu_id`) ,
  CONSTRAINT `fk_Documento_Institucion`
    FOREIGN KEY (`Institucion_inst_id` )
    REFERENCES `fundamusicalBolivar`.`Institucion` (`inst_id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Documento_Usuario1`
    FOREIGN KEY (`Usuario_usu_id` )
    REFERENCES `fundamusicalBolivar`.`Usuario` (`usu_id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;

CREATE INDEX `fk_Documento_Institucion` ON `fundamusicalBolivar`.`Documento` (`Institucion_inst_id` ASC) ;

CREATE INDEX `fk_Documento_Usuario1` ON `fundamusicalBolivar`.`Documento` (`Usuario_usu_id` ASC) ;


-- -----------------------------------------------------
-- Table `fundamusicalBolivar`.`Pauta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `fundamusicalBolivar`.`Pauta` ;

CREATE  TABLE IF NOT EXISTS `fundamusicalBolivar`.`Pauta` (
  `pau_id` INT NOT NULL AUTO_INCREMENT ,
  `pau_recibe` VARCHAR(45) NOT NULL ,
  `Documento_doc_id` INT NOT NULL ,
  `Documento_Institucion_inst_id` INT NOT NULL ,
  `Documento_Usuario_usu_id` INT NOT NULL ,
  PRIMARY KEY (`pau_id`, `Documento_doc_id`, `Documento_Institucion_inst_id`, `Documento_Usuario_usu_id`) ,
  CONSTRAINT `fk_Pauta_Documento1`
    FOREIGN KEY (`Documento_doc_id` , `Documento_Institucion_inst_id` , `Documento_Usuario_usu_id` )
    REFERENCES `fundamusicalBolivar`.`Documento` (`doc_id` , `Institucion_inst_id` , `Usuario_usu_id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;

CREATE INDEX `fk_Pauta_Documento1` ON `fundamusicalBolivar`.`Pauta` (`Documento_doc_id` ASC, `Documento_Institucion_inst_id` ASC, `Documento_Usuario_usu_id` ASC) ;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `fundamusicalBolivar`.`Usuario`
-- -----------------------------------------------------
START TRANSACTION;
USE `fundamusicalBolivar`;
INSERT INTO `fundamusicalBolivar`.`Usuario` (`usu_id`, `usu_login`, `usu_pwd`, `usu_nombre`, `usu_apellido`, `usu_cargo`, `usu_rol`) VALUES (NULL, 'admin', '21232f297a57a5a743894a0e4a801fc3', 'Administrador', 'Administrador', 'Admin', 1);

COMMIT;
