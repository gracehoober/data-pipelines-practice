# Data and Pipelines Practice
This repo contains 3 practice questions focused on assessing and working on my skills for data ingestion, handling gaps in data, and handling data "events" of interest.

## Question 1:
Question 1: Flight Data Ingestion
Scenario: Flight drones send JSON packets every second during flight containing basic telemetry. You need to design a Python service that receives this data and stores it.

## Question 2:
Data Quality Monitoring
Scenario: The data labeling team reports that some flight videos have "gaps" where telemetry data is missing for several seconds. This causes problems for training AI models. You need to build a data quality checker.

## Question 3:
Scenario: Human labelers need to review flight footage and mark "events of interest" (birds, other aircraft, obstacles). Currently this is manual and untracked. Design a system to manage this workflow.

## Question 4:
Scenario: You are an engineer for a lock company. You need to create a function that unlocks the lock if the correct knock pattern has occurred. The open method and knock listener method  has already been created for you.
- open() : opens the door attached to the lock.
- knock_listener(): returns a timestamp of when a knock occurred.
