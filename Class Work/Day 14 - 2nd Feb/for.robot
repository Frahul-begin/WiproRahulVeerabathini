*** Test Cases ***
Print Names using for loop
    FOR     ${name}     IN  Ram Ravi Taj
        log to console      ${name}
    END

Print Names using while loop
    ${count}=    Set Variable     1
    WHILE       ${count}<=5
        log to console      ${count}
        ${count}=       Evaluate      ${count}+1
    END