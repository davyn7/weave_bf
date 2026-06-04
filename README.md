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

## BUANA TO-DO LIST

* Refactor Routers

* **CREATE** *[PUT]* `update_spouse(customer_id: int, spouse: SpouseBase)`

* **CREATE** *[PUT]* `update_guarantor(customer_id: int, guarantor: GuarantorBase)`

* **CREATE** *[PUT]* `approve_user(user_id: int)`
    * Once a `USER` registers, it will be added to the `USERS` table.
    * Call `generate_unique_code` for the new `USER`.
    * Update the following columns in `USER`: `IS_ACTIVE = True` & `UNIQUE_CODE` to the generated code.

* **CREATE** *[GET]* `get_new_users`
    * Retrieve all `USER` in `USERS` where `IS_ACTIVE = False`.

## USER TO-DO LIST

* **EDIT** *[POST]* `add_user(user: UserBase)`
    * Add `dealer_code` as parameter. 
    * Search for `DEALER` based on `dealer_code`. 
    * Add the `DEALER_ID` to `UserBase`.

## DEALER TO-DO LIST

* **CREATE** *[PUT]* `assign_dealer_pic(user_id: int)`

## Questions to Ask

* Does a Dealer need to be connected to a Province?
* When does CMO get assigned?
* When do the financial numbers get calculated?
* Does Asset need to be deleted once it's been assigned to an Application?