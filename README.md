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
    * Create `DEALER` account.
    * Approve new `USER` account by assigning a password.
    * Assign a `USER` as `DEALER_PIC`.
    * View `APPLICATIONS`.
    * Update `APPLICATION_STATUS` of `APPLICATION`.
    * Create `BRANCH` into `BRANCHES`.
    * Create `CMO` account.
    * Assign `CMO` into a `BRANCH`.
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

## Questions to Ask

* Does a Dealer need to be connected to a Province?
* When does CMO get assigned?
* When do the financial numbers get calculated?
* Does Asset need to be deleted once it's been assigned to an Application?