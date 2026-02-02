*** Settings ***
Library    BuiltIn
Library    Process
Library    SeleniumLibrary

*** Test Cases ***
Verify Environment Setup
    Log To Console    Checking Python installation...
    ${py}=    Run Process    python    --version
    Run Keyword If    ${py.rc} != 0    Fail    Python is not installed or not in PATH
    Log To Console    Python Version: ${py.stdout}

    Log To Console    Checking Robot Framework installation...
    ${rf_ver}=    Evaluate    __import__('robot').__version__
    Run Keyword If    '${rf_ver}' == ''    Fail    Robot Framework is not installed
    Log To Console    Robot Framework Version: ${rf_ver}

    Log To Console    Checking SeleniumLibrary import...
    Run Keyword And Continue On Failure    Import Library    SeleniumLibrary
    Log To Console    SeleniumLibrary imported successfully
