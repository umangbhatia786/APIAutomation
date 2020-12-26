#Created by Umang Bhatia

Feature: Verify that Books can be added and deleted using the Library API
  @regression
  Scenario Outline: Verify AddBook API Functionality
    Given The book details with <book_name>, <isbn> and author as <author>
    When We execute the AddBook API method
    Then Book is added successfully
    Examples:
      | book_name      | isbn  | author      |
      | Casual Vacancy | OIUOW | J.K Rowling |
      | Art of War     | WEWEQ | Mao Zedong  |
