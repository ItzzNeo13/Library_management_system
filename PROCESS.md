## LIBRARY MANAGEMENT SYSTEM.
### How it started -

6th March 2023, the day I tried out MYSQL for the first time and it was really a great learning experience.
Earlier I used to think that it is easier to manage databases, it only involves use of reserved keywords and unlink Web Development you do not have to put in much effort to complete any project depending on Database. But I was very wrong.
SQL needs a lot of effort put in to make the process of managing and retriving the data. 

After searching online for a while, I decided to go with a library management system. And the learning experience begun...

-----

### Resources used:
-  For data I used RandomPersonGenerator for generate details of members and staff. Website link [here.](https://www.fakepersongenerator.com)

-  For mapping out the Database I used DrawSQL website. Link [here.](https://drawsql.app/)

-  Tuorial/Reference used was Fireship's video on Youtube. Video link [here.](https://www.youtube.com/watch?v=Cz3WcZLRaWc)

-----

### Errors encountered till now:

1. `ER_NOT_SUPPORTED_AUTH_MODE: Client does not support authentication protocol requested by server; consider upgrading MySQL client.`

    **Caused by:** When I tried to log in for establishing connection through SQLTools extension in VS Code.
    
    **Fixed by:** Creating a second user and logging in through that account.
    
    - - - - 
 
2. `mysql : The term 'mysql' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.`

    **Caused by:** When I tried to log in though my system command line for the first time.
    
    **Fixed by:** Adding SQL Path to Environment Variables (The same way you add python path).
    
    - - - - 
3.  `error 2003 can't connect to mysql`

     **Caused by:** Trying to log in to non-root user (but with all privileges). Probably server was not running.
     
     **Fixed by:** Reconfiguring the server or it started on itself when I was reconfiguring.
     
     - - - -

4. `Module not found error for pymysql even when the module was installed`

   **Caused by:** Probably device issue or idk.
   
   **Fixed by:** Writing the entire code for GUI in Replit IDE.
   
   **ALSO tried fixing by:** Uninstalling the module and reinstalling it in the Scripts directory for Python on my device.
 
- - - -

### Things I learnt so far:
- [x] Configuring a MySQL server.
- [x] Logging into it remotely and with help of tools.
- [x] Basic Troubleshooting.
- [x] Adding data to DB.
- [x] Retriving data from DB.
- [x] Managing the DB via command line.
- [x] Using .env tokens to log into DB

# 
