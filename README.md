This project provides a natural language interface for ConcourseDB. Because of the time constraint on this project, it is a very simple implementation and does not support complicated queries. Instead, there is a 1-to-1 mapping between queries and Concourse API function calls.

In the future, support for more complicated queries will be added. For example, questions of the type, who, what, when, where, why will be added. Because of the nature of these questions, the calls required tend to be much more complicated. For example (Using the database located under \examples) a question such as "What country is the employee Dwight from?" Would require the Concourse API call "get("country", find("name", Operator.EQUAL, Dwight))" As you can see this is a difficult NLP problem since there is no 1-to-1 mapping between query and Concourse API call. The way to solve this problem is through the use of an abstraction to represent the natural language query that can then be mapped to the appropriate Concourse API calls. This implementation employees an abstract query graph for just such a purpose. Note that the simple function calls implemented in this basic interface to not require the query graph because of the 1-to-1 mapping. However, the query graph is employed regardless for future use in complicated quries.

The implementation of NLICDB consists of three stages

+ Preprocessing
+ Abstract Query Graph
+ Concourse Query Generation

######Preprocessing
During this stage, given a natural language query, processing steps such as word segmentation, lower casing and stop-word removal are performed on the query.

######Abstract Query Graph
During this stage, we are given the preprocessed query, and from this we need to generate some form of  abstract intermediate expression that can then be mapped to the Concourse API query calls. We note that a database query can be thought as a graph where each node is a variable and every edge a relation. As such, this class implements such a graph to represent a database query in abstract form.

######Concourse Query Generation
Once we have our abstract query graph, we simply build the appropriate Concourse API query from the graph by traversing the graph appropriately.

Supported Concourse API Calls and Examples
-------

+ Set
  + Example query: Set the age to 18 of the user whose id is 1
  + Example query: Set the name to Dwight of the user whose id is 3
+ Get
  + Example query: Get the salary of the user whose id is 2
  + Example query: Get the country of the user whose id is 2
+ Remove
  + Example query: Remove the age of 18 of the user whose id is 1
  + Example query: Remove the name John from the user whose id is 3
+ Find
  + Example query: Find employees whose age is greater than 25
  + Example query: Find employees whose country is equal to USA

Setup
-------
#### Requirements
+ python3.3+
+ python libraries:
  + nltk
+ ConcourseDB


#### Setup Concourse server and Python drivers
To setup the dev version of ConcourseDB follow these steps:
1. sudo git clone https://github.com/cinchapi/concourse.git
2. cd concourse
3. sudo ./gradlew clean installer
4. sudo sh concourse-server/build/distributions/*.bin 
5. cd concourse-driver-python
6. sudo ./pyinvoke build


#### Install NLTK

1. Run the command "$ sudo pip install -U nltk"
2. Download the nltk data by launching the python interpreter and running the following commands:
  + >>> import nltk
  + >>> nltk.download()

Testing
------
Tests are performed using nosetests

To install nose tests execute "$ sudo pip install nose"

Then, navigate to the tests directory and execute "$ nosetests" to execute tests.

Examples
-------
A simple example is included under /examples to observe the NLICDB in action.

To run, ensure concourse server is running and then execute "$ python main.py"
