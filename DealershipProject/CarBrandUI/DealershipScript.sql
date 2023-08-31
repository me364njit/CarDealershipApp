-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema Dealership
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Dealership
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Dealership` ;
USE `Dealership` ;

-- -----------------------------------------------------
-- Table `Dealership`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dealership`.`Cars` (
  `idCar` INT NOT NULL,
  `Color` VARCHAR(45) NULL,
  `Make` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` INT NULL,
  `CarCondition` VARCHAR(45) NULL,
  `Date_On_Lot` VARCHAR(45) NULL,
  `Miles` INT NULL,
  `Number_of_past_buyers` INT NULL,
  `Number_of_accidents` INT NULL,
  `Price` INT NULL,
  PRIMARY KEY (`idCar`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dealership`.`Supplier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dealership`.`Supplier` (
  `idSupplier` INT NULL,
  `Supplier_FirstName` VARCHAR(45) NULL,
  `Supplier_LastName` VARCHAR(45) NULL,
  `Supplier_Address` VARCHAR(100) NULL,
  `CompanyName` VARCHAR(45) NULL,
  `idCar` INT NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dealership`.`Buyer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dealership`.`Buyer` (
  `idBuyer` INT NOT NULL,
  `idCar` INT NULL,
  `Buyer_Name` VARCHAR(45) NULL,
  `Buyer_Address` VARCHAR(45) NULL,
  `Payment_Date` VARCHAR(45) NULL,
  `Finance_or_Lease` VARCHAR(45) NULL,
  `Price_Paid` INT NULL,
  PRIMARY KEY (`idBuyer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dealership`.`Dealer_Services`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dealership`.`Dealer_Services` (
  `idCar` INT NOT NULL,
  `idBuyer` INT NULL,
  `Number_of_Oil_Changes` INT NULL,
  `Last_Brake_Replacement_Miles` INT NULL,
  `Last_Oil_Change_Miles` INT NULL,
  `Last_Tire_Change_Miles` INT NULL,
  `Break_fluid_replacement_miles` INT NULL,
  `Filter_Replacement_Miles` INT NULL,
  `Cars_idCar` INT NULL,
  `Buyer_idBuyer` INT NOT NULL,
  PRIMARY KEY (`idCar`),
  INDEX `fk_Dealer_Services_Cars1_idx` (`Cars_idCar` ASC) VISIBLE,
  INDEX `fk_Dealer_Services_Buyer1_idx` (`Buyer_idBuyer` ASC) VISIBLE,
  CONSTRAINT `fk_Dealer_Services_Cars1`
    FOREIGN KEY (`Cars_idCar`)
    REFERENCES `Dealership`.`Cars` (`idCar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Dealer_Services_Buyer1`
    FOREIGN KEY (`Buyer_idBuyer`)
    REFERENCES `Dealership`.`Buyer` (`idBuyer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
