#Created by Umang Bhatia

Feature: Verify that Books can be added and deleted using the Library API

  Scenario: Verify AddBook API Functionality
    Given The book details which need to be added to the library
    When We execute the AddBook API method
    Then Book is added successfully

