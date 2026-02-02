*** Settings ***
Library    BuiltIn

*** Variables ***
${NAME}        Rahul
${ROLE}        Python Developer
@{SKILLS}      C    Python  C++   Selenieum    RTOS

*** Test Cases ***
Log Scalar Variables
    Log    User Name is ${NAME}
    Log To Console    Role: ${ROLE}

Log List Variables
    Log    User skills are ${SKILLS}
    Log To Console    First skill is ${SKILLS}[0]
