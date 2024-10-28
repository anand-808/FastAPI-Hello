*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     http://localhost:8000

*** Test Cases ***
Verify Hello World is Displayed
    Open Browser    ${URL}    chrome
    Page Should Contain    Hello World
    Close Browser
