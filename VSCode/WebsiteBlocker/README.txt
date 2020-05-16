Use of this code is to block some websites to avoid distraction during working hours and unblocking them when working hour is over.

This code will block the websites specified by the user in the website_list during specified hours of the day as working hours.

Program requires administrative rights to run and access the hosts file located in C:\Windows\System32\drivers\etc\hosts. Therefore open command line as administrator.

We can schedule the program in the task scheduler by :
    Create Task 
        configure for - your windows version
        Tick Run with highest privilege for administrative rights
    Triggers
        New
        Select Begin the task - At startup    
    Actions
        New
        Action: Start a program
        Point to your program
    Conditions 
        uncheck start the task only if the computer is on AC power    

Run using cmd as administrator.

Task Manager can be used to track the program is running or not.

