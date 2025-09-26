*** Settings ***
Library    RFStackSpotAILibrary.py
Test Setup    Setup StackSpot AI

*** Keywords ***
Setup StackSpot AI
    Set Credentials

*** Test Cases ***
Simple Test
    Set Instructions    You are a Senior Quality Engineering with experience integrating AI with Automated Software Testing.
    ${response}    Send Message    Draft a learning path for another Quality Engineer trying to achieve the same level of expertise.
    Log    ${response}