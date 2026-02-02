***Settings***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Create New User
    Create Session    postingSession    ${BASE_URL}
    ${data}=    Create Dictionary    name=varsha
    ${response}=    POST On Session    postingSession    /users    json=${data}
    Status Should Be    201    ${response}
    ${user_json}=    Evaluate    ${response.json()}
    Log To Console    ${user_json}

Update User
    Create Session    postingSession    ${BASE_URL}
    ${data}=    Create Dictionary    name=Pooja
    ${response}=    PUT On Session    postingSession    /users/1    json=${data}
    Status Should Be    200    ${response}
    ${user_json}=    Evaluate    ${response.json()}
    Log To Console    ${user_json}

Patch User
    Create Session    postingSession    ${BASE_URL}
    ${data}=    Create Dictionary    name=Pooja patched
    ${response}=    PATCH On Session    postingSession    /users/1    json=${data}
    Status Should Be    200    ${response}
    ${user_json}=    Evaluate    ${response.json()}
    Log To Console    ${user_json}

Verify Get All Users
    Create Session    mySession    ${BASE_URL}
    ${response}=    GET On Session    mySession    /users
    Status Should Be    200    ${response}
    ${res_json}=    To Json    ${response.content}
    Log To Console    ${res_json}

Verify Get Single User
    Create Session    mySession    ${BASE_URL}
    ${response}=    GET On Session    mySession    /users/3
    Status Should Be    200    ${response}
    ${res_json}=    To Json    ${response.content}
    Log To Console    ${res_json}

Verify Get Single User Not Found
    Create Session    mySession    ${BASE_URL}
    ${response}=    GET On Session    mySession    /users/99999
    Status Should Be    404    ${response}
    ${res_json}=    To Json    ${response.content}
    Log To Console    ${res_json}

Verify Delete User By User ID
    Create Session    mySession    ${BASE_URL}
    ${response}=    DELETE On Session    mySession    /users/1
    Status Should Be    200    ${response}
    ${res_json}=    To Json    ${response.content}
    Log To Console    ${res_json}
