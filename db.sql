--CREATE DATABASE CalculatorApp

USE [CalculatorApp]
GO

CREATE TABLE [UserLogs] (
    [ID] INT IDENTITY(1,1),
    [Action] VARCHAR(255),
    [Result] VARCHAR(255)
);

CREATE TABLE [History] (
    [ID] INT IDENTITY(1,1),
    [Expression] VARCHAR(255),
    [Result] VARCHAR(255),
    [TimeOfAction] DATETIME
);

--SELECT * FROM UserLogs
--SELECT * FROM History