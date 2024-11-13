*** Settings ***
Library    RequestsLibrary
Library    BuiltIn

*** Variables ***
${BASE_URL}    http://localhost:8000

*** Test Cases ***

Validate Root endpoint GET /
    Create Session    mysession    ${BASE_URL}
    ${response}=    GET On Session    mysession    /
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['message']}    Hello World

Test Read Item Endpoint
    Create Session    mysession    ${BASE_URL}
    ${response}=    GET On Session    mysession    /items/1
    Run Keyword If    '${response.status_code}' != '200'    Fail    "Item not found or error occurred"
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['item_id']}    1

Test Create Item Endpoint
    ${payload}=    BuiltIn.Create Dictionary    name=Test Item    price=20.5
    ${response}=    POST On Session    mysession    /items    json=${payload}
    Run Keyword If    '${response.status_code}' != '200'    Fail    "Error occurred while creating item"
    Log    ${response.json()}  # Log the full response to debug
    Should Be Equal As Strings    ${response.status_code}    200

Test Update Item Endpoint
    ${payload}=    BuiltIn.Create Dictionary    name=Updated Item    price=25.5
    ${response}=    PUT On Session    mysession    /items/1    json=${payload}
    Run Keyword If    '${response.status_code}' != '200'    Fail    "Error occurred while updating item"
    Log    ${response.json()}  # Log the full response to debug
    Should Be Equal As Strings    ${response.status_code}    200

Test Read Items with Cookies
    Create Session    mysession    ${BASE_URL}
    ${cookies}=    Create Dictionary    session_id=session123    fatebook_tracker=fatebook_value    googall_tracker=googall_value
    ${response}=    GET On Session    mysession    /items/    cookies=${cookies}
    Run Keyword If    '${response.status_code}' != '200'    Fail    "Error occurred while reading items"
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['session_id']}    session123
    Should Be Equal As Strings    ${response.json()['fatebook_tracker']}    fatebook_value
    Should Be Equal As Strings    ${response.json()['googall_tracker']}    googall_value

Test Login Endpoint
    # Send POST request to /login/ with form data
    ${payload}=    Create Dictionary    username=testuser    password=testpassword
    ${response}=    POST On Session    mysession    ${BASE_URL}/login/    data=${payload}
    Run Keyword If    '${response.status_code}' != '200'    Fail    "Error occurred during login"
    Log    ${response.json()}  # Log the full response to debug
    Should Be Equal As Strings    ${response.status_code}    200

Test Create File Endpoint
    # Create a small dummy file content
    ${payload}=    Create Dictionary    file=@path/to/your/file.txt
    ${response}=    POST On Session    mysession    ${BASE_URL}/files/    files=${payload}
    Run Keyword If    '${response.status_code}' != '200'    Fail    "Error occurred while creating file"
    Should Be Equal As Strings    ${response.status_code}    200

Test Upload File Endpoint
    # Upload a file
    ${payload}=    Create Dictionary    file=@path/to/your/file.txt
    ${response}=    POST On Session    mysession    ${BASE_URL}/uploadfile/    files=${payload}
    Run Keyword If    '${response.status_code}' != '200'    Fail    "Error occurred while uploading file"
    Should Be Equal As Strings    ${response.status_code}    200

Test Files With Token Endpoint
    # Create a dictionary with file paths and token as part of the form data
    ${payload}=    Create Dictionary    file=@path/to/your/file.txt    fileb=@path/to/another/file.txt
    ${form_data}=    Create Dictionary    token=mytoken
    ${response}=    POST On Session    mysession    ${BASE_URL}/files/    files=${payload}    data=${form_data}
    Run Keyword If    '${response.status_code}' != '200'    Fail    "Error occurred while uploading files with token"
    Should Be Equal As Strings    ${response.status_code}    200
