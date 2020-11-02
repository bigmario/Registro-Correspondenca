SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `fundamusicalBolivar` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci ;
USE `fundamusicalBolivar` ;

-- -----------------------------------------------------
-- Table `fundamusicalBolivar`.`Institucion`
-- -----------------------------------------------------
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
CREATE  TABLE IF NOT EXISTS `fundamusicalBolivar`.`Usuario` (
  `usu_id` INT NOT NULL AUTO_INCREMENT ,
  `usu_login` VARCHAR(45) NOT NULL ,
  `usu_pwd` VARCHAR(45) NOT NULL ,
  `usu_nombre` VARCHAR(45) NOT NULL ,
  `usu_apellido` VARCHAR(45) NOT NULL ,
  `usu_cargo` VARCHAR(45) NOT NULL ,
  `usu_rol` INT NOT NULL ,
  `usu_preguntaSeg` VARCHAR(200) NOT NULL ,
  `usu_respuestaSeg` VARCHAR(200) NOT NULL ,
  PRIMARY KEY (`usu_id`) ,
  UNIQUE INDEX `usu_login_UNIQUE` (`usu_login` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;


-- -----------------------------------------------------
-- Table `fundamusicalBolivar`.`Documento`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `fundamusicalBolivar`.`Documento` (
  `doc_id` INT NOT NULL AUTO_INCREMENT ,
  `doc_fechaRegistro` DATE NOT NULL ,
  `doc_fechaDocRecep` DATE NOT NULL ,
  `doc_numOficio` VARCHAR(45) NOT NULL ,
  `doc_Tipo` VARCHAR(45) NOT NULL ,
  `doc_Titulo` VARCHAR(100) NOT NULL ,
  `doc_Remitente` VARCHAR(100) NOT NULL ,
  `doc_Observaciones` TEXT NULL DEFAULT NULL ,
  `Institucion_inst_id` INT NOT NULL ,
  `Usuario_usu_id` INT NOT NULL ,
  PRIMARY KEY (`doc_id`, `Institucion_inst_id`, `Usuario_usu_id`) ,
  INDEX `fk_Documento_Institucion` (`Institucion_inst_id` ASC) ,
  INDEX `fk_Documento_Usuario1` (`Usuario_usu_id` ASC) ,
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


-- -----------------------------------------------------
-- Table `fundamusicalBolivar`.`Pauta`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `fundamusicalBolivar`.`Pauta` (
  `pau_id` INT NOT NULL AUTO_INCREMENT ,
  `pau_recibe` VARCHAR(45) NOT NULL ,
  `Documento_doc_id` INT NOT NULL ,
  `Documento_Institucion_inst_id` INT NOT NULL ,
  `Documento_Usuario_usu_id` INT NOT NULL ,
  PRIMARY KEY (`pau_id`, `Documento_doc_id`, `Documento_Institucion_inst_id`, `Documento_Usuario_usu_id`) ,
  INDEX `fk_Pauta_Documento1` (`Documento_doc_id` ASC, `Documento_Institucion_inst_id` ASC, `Documento_Usuario_usu_id` ASC) ,
  CONSTRAINT `fk_Pauta_Documento1`
    FOREIGN KEY (`Documento_doc_id` , `Documento_Institucion_inst_id` , `Documento_Usuario_usu_id` )
    REFERENCES `fundamusicalBolivar`.`Documento` (`doc_id` , `Institucion_inst_id` , `Usuario_usu_id` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
