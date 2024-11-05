*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary

*** Variables ***
${URL}     http://localhost:8000

*** Test Cases ***
Verify FastAPI Cassandra API is Displayed
    Open Browser    ${URL}    chrome
    Page Should Contain    FastAPI Cassandra API
    Close Browser

Verify Users Endpoint is Accessible
    ${response}=    Get Request    ${URL}/users/
    Log    Response status: ${response.status_code}
    Log    Response content: ${response.content}
    Should Be Equal As Numbers    ${response.status_code}    200