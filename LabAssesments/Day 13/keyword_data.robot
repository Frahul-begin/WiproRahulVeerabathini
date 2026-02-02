*** Settings ***
Library         DataDriver    login_data.csv
Test Template   Login Keyword

*** Test Cases ***
Login With Data
    # DO NOT put arguments here when using DataDriver

*** Keywords ***
Login Keyword
    [Arguments]    ${username}    ${password}
    Log To Console    Username=${username} | Password=${password}
