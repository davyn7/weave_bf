# Weave Backend for Buana Finance

## Introduction

## Infrastructure

Backend: Python FastAPI  
Database: Supabase  
Deployment: Railway    
Frontend: Retool

## Run Test

`uvicorn main:app --reload`

## Views and Functionalities

* Buana Dashboard for `BUANA`
    * `BUANA` creates `DEALER` account.
    * Approve new `USER` account by assigning a password.
    * Assign a `USER` as `DEALER_PIC`.
    * View `APPLICATIONS`.
    * Update `APPLICATION_STATUS` of `APPLICATION`.
    * Assign `CMO` based on `BRANCH`.
* Dealer Dashboard for `DEALER_PIC`
    * View `APPLICATIONS`.
    * Update data of `APPLICATION`, but not `APPLICATION_STATUS`.
    * Assign a `USER` as `DEALER_PIC`.
    * Add `ASSET` to `ASSETS`.
* User Mobile App for `USER`
    * Request to create an account.
    * Log in using OTP.
    * Create & submit new `APPLICATION` to `APPLICATIONS`.

## Flow

* 

## To-do List

*