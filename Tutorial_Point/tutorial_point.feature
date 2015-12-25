Feature: Tutorials on tutorialspoint.com
  In order to check the functionality of tutorialpoint.com
  As a user of tutorialpoint.com
  I want it to display the course searched

  Scenario Outline: Search "<content>" on tutorialspoint.com
    Given I launch tutorialspoint.com
    When I view all courses
    And I select "<content>" under "<parent_course>"
    Then it shows "<course_header>" page

    Examples: Tutorials
        |     parent_course       |       content     |       course_header     |
        |     JAVA TECHNOLOGIES   |   Learn Eclipse   |   Eclipse Tutorial      |
        |     PROGRAMMING         |   Learn Awk Programming    |   Awk Tutorial       |
        |     WEB DEVELOPMENT     |   Learn Ajax      |   AJAX Tutorial    |
        |     WEB DEVELOPMENT     |   Learn CSS       |   CSS Tutorial       |