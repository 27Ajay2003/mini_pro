# Similar Questions

Provides 40 similar questions for a given list of question ids.

**URL** : `/api/technical/question/similar/`

**Method** : `POST`

**Auth required** : ADMIN

**Data constraints**

```json
{
    "ids": "[comma separated list of ids]"
}
```

**Data example**

```json
{
    "ids":[234,256,288,290,312,344,167,199,399]
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "OS": [
        {
            "question_id": 13,
            "topic": "Introduction to Operating Systems",
            "question": "What is the kernel of an operating system?",
            "option_a": "The central component that provides basic services for all other parts of the OS",
            "option_b": "A graphical interface that allows users to interact with the OS",
            "option_c": "A utility program that manages hardware and software resources",
            "option_d": "An application program that runs on the OS",
            "correct_answer": "a",
            "difficulty": "hard",
            "cognitive_level": "applying",
            "subject": "OS"
        },
        {
            "question_id": 81,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is not a key characteristic of a distributed system?",
            "option_a": "Transparency",
            "option_b": "Concurrency",
            "option_c": "Scalability",
            "option_d": "Reliability",
            "correct_answer": "d",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "OS"
        },
        {
            "question_id": 83,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is a type of distributed system where the components work together to achieve a common goal and share a global state?",
            "option_a": "Loosely-coupled system",
            "option_b": "Tightly-coupled system",
            "option_c": "Clustered system",
            "option_d": "All of the above",
            "correct_answer": "b",
            "difficulty": "medium",
            "cognitive_level": "applying",
            "subject": "OS"
        },
        {
            "question_id": 84,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is a technique used in distributed systems to ensure consistency of data across different nodes?",
            "option_a": "Replication",
            "option_b": "Partitioning",
            "option_c": "Load balancing",
            "option_d": "All of the above",
            "correct_answer": "a",
            "difficulty": "hard",
            "cognitive_level": "analyzing",
            "subject": "OS"
        },
        {
            "question_id": 85,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is a key advantage of using cloud computing?",
            "option_a": "Reduced infrastructure costs",
            "option_b": "Increased security risks",
            "option_c": "Decreased scalability",
            "option_d": "All of the above",
            "correct_answer": "a",
            "difficulty": "medium",
            "cognitive_level": "applying",
            "subject": "OS"
        },
        {
            "question_id": 86,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is a cloud service model where the consumer uses the provider's applications over a network?",
            "option_a": "Infrastructure as a Service (IaaS)",
            "option_b": "Platform as a Service (PaaS)",
            "option_c": "Software as a Service (SaaS)",
            "option_d": "All of the above",
            "correct_answer": "c",
            "difficulty": "easy",
            "cognitive_level": "understanding",
            "subject": "OS"
        },
        {
            "question_id": 87,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is a cloud deployment model where the cloud infrastructure is only available to a single organization?",
            "option_a": "Public cloud",
            "option_b": "Private cloud",
            "option_c": "Hybrid cloud",
            "option_d": "All of the above",
            "correct_answer": "b",
            "difficulty": "medium",
            "cognitive_level": "applying",
            "subject": "OS"
        },
        {
            "question_id": 88,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is a cloud deployment model where the cloud infrastructure is shared by multiple organizations but with different access levels and security measures?",
            "option_a": "Public cloud",
            "option_b": "Private cloud",
            "option_c": "Hybrid cloud",
            "option_d": "Community cloud",
            "correct_answer": "d",
            "difficulty": "hard",
            "cognitive_level": "analyzing",
            "subject": "OS"
        },
        {
            "question_id": 89,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is a technology used in distributed systems to handle the failure of nodes in the system?",
            "option_a": "Replication",
            "option_b": "Load balancing",
            "option_c": "Fault tolerance",
            "option_d": "All of the above",
            "correct_answer": "c",
            "difficulty": "medium",
            "cognitive_level": "analyzing",
            "subject": "OS"
        },
        {
            "question_id": 90,
            "topic": "Distributed Systems and Cloud Computing",
            "question": "Which of the following is a type of distributed system that provides a way to share computing resources data and applications across different organizations or sites?",
            "option_a": "Clustered system",
            "option_b": "P2P system",
            "option_c": "Grid system",
            "option_d": "All of the above",
            "correct_answer": "c",
            "difficulty": "hard",
            "cognitive_level": "analyzing",
            "subject": "OS"
        }
    ],
    "CN": [
        {
            "question_id": 161,
            "topic": "Application layer and network services",
            "question": "Which of the following protocols is used for remote access to a network?",
            "option_a": "SMTP",
            "option_b": "RDP",
            "option_c": "SSH",
            "option_d": "FTP",
            "correct_answer": "b",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "CN"
        },
        {
            "question_id": 163,
            "topic": "Application layer and network services",
            "question": "Which protocol is used to transfer files between systems on the internet?",
            "option_a": "FTP",
            "option_b": "SFTP",
            "option_c": "SCP",
            "option_d": "TELNET",
            "correct_answer": "a",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "CN"
        },
        {
            "question_id": 165,
            "topic": "Application layer and network services",
            "question": "Which of the following protocols is used to access web pages on the internet?",
            "option_a": "HTTP",
            "option_b": "FTP",
            "option_c": "SMTP",
            "option_d": "TCP",
            "correct_answer": "a",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "CN"
        },
        {
            "question_id": 168,
            "topic": "Application layer and network services",
            "question": "Which of the following protocols is used for remote terminal emulation?",
            "option_a": "SSH",
            "option_b": "FTP",
            "option_c": "SMTP",
            "option_d": "TCP",
            "correct_answer": "a",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "CN"
        },
        {
            "question_id": 169,
            "topic": "Application layer and network services",
            "question": "Which of the following protocols is used for directory services?",
            "option_a": "DNS",
            "option_b": "LDAP",
            "option_c": "FTP",
            "option_d": "TFTP",
            "correct_answer": "b",
            "difficulty": "hard",
            "cognitive_level": "applying",
            "subject": "CN"
        },
        {
            "question_id": 170,
            "topic": "Application layer and network services",
            "question": "Which of the following protocols is used for network printing?",
            "option_a": "TCP/IP",
            "option_b": "LPR/LPD",
            "option_c": "FTP",
            "option_d": "SNMP",
            "correct_answer": "b",
            "difficulty": "hard",
            "cognitive_level": "applying",
            "subject": "CN"
        },
        {
            "question_id": 106,
            "topic": "Introduction to Computer Networks",
            "question": "Which of the following protocol is used to transfer files over the internet?",
            "option_a": "HTTP",
            "option_b": "FTP",
            "option_c": "SMTP",
            "option_d": "TCP",
            "correct_answer": "b",
            "difficulty": "easy",
            "cognitive_level": "understanding",
            "subject": "CN"
        },
        {
            "question_id": 110,
            "topic": "Introduction to Computer Networks",
            "question": "Which of the following protocol is used for secure communication over the internet?",
            "option_a": "HTTP",
            "option_b": "FTP",
            "option_c": "SMTP",
            "option_d": "HTTPS",
            "correct_answer": "d",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "CN"
        },
        {
            "question_id": 122,
            "topic": "Network Protocols and Standards",
            "question": "Which protocol is used for securely transferring files between a client and server?",
            "option_a": "SFTP",
            "option_b": "FTP",
            "option_c": "TFTP",
            "option_d": "HTTP",
            "correct_answer": "a",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "CN"
        },
        {
            "question_id": 126,
            "topic": "Network Protocols and Standards",
            "question": "Which protocol is used for transferring files over the internet?",
            "option_a": "FTP",
            "option_b": "SFTP",
            "option_c": "TFTP",
            "option_d": "HTTP",
            "correct_answer": "a",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "CN"
        }
    ],
    "DBMS": [
        {
            "question_id": 231,
            "topic": "Data Manipulation Language (DML) and Query Optimization",
            "question": "Which of the following is not a type of SQL statement?",
            "option_a": "Data Definition Language (DDL)",
            "option_b": "Data Manipulation Language (DML)",
            "option_c": "Data Query Language (DQL)",
            "option_d": "Data Control Language (DCL)",
            "correct_answer": "c",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "DBMS"
        },
        {
            "question_id": 296,
            "topic": "Distributed Databases and Replication",
            "question": "What is the CAP theorem?",
            "option_a": "A principle in distributed computing",
            "option_b": " A method of data encryption",
            "option_c": " A database management system",
            "option_d": " A network protocol",
            "correct_answer": "a",
            "difficulty": "hard",
            "cognitive_level": "analyzing",
            "subject": "DBMS"
        },
        {
            "question_id": 233,
            "topic": "Data Manipulation Language (DML) and Query Optimization",
            "question": "Which of the following SQL statement is used to retrieve data from a database?",
            "option_a": "SELECT",
            "option_b": "INSERT",
            "option_c": "UPDATE",
            "option_d": "DELETE",
            "correct_answer": "a",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "DBMS"
        },
        {
            "question_id": 235,
            "topic": "Data Manipulation Language (DML) and Query Optimization",
            "question": "Which of the following SQL statement is used to change the data in a database?",
            "option_a": "SELECT",
            "option_b": "UPDATE",
            "option_c": "DELETE",
            "option_d": "INSERT",
            "correct_answer": "b",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "DBMS"
        },
        {
            "question_id": 237,
            "topic": "Data Manipulation Language (DML) and Query Optimization",
            "question": "Which of the following SQL operator is used to retrieve specific data from a table based on a certain criteria?",
            "option_a": "ORDER BY",
            "option_b": "GROUP BY",
            "option_c": "FILTER BY",
            "option_d": "WHERE",
            "correct_answer": "d",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "DBMS"
        },
        {
            "question_id": 208,
            "topic": "Introduction to DBMS",
            "question": "What is SQL?",
            "option_a": "A language used to manage relational databases",
            "option_b": "An operating system for managing databases",
            "option_c": "An application used to create databases",
            "option_d": "An algorithm used to store data",
            "correct_answer": "a",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "DBMS"
        },
        {
            "question_id": 240,
            "topic": "Data Manipulation Language (DML) and Query Optimization",
            "question": "Which of the following is not a SQL Aggregate function?",
            "option_a": "MAX()",
            "option_b": "MIN()",
            "option_c": "AVG()",
            "option_d": "UPSERT()",
            "correct_answer": "d",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "DBMS"
        },
        {
            "question_id": 243,
            "topic": "Indexing and Query Execution Plans",
            "question": "Which of the following is not a type of join used in SQL?",
            "option_a": "Inner join",
            "option_b": "Outer join",
            "option_c": "Full join",
            "option_d": "Split join",
            "correct_answer": "d",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "DBMS"
        },
        {
            "question_id": 216,
            "topic": "Relational Model and Normalization",
            "question": "Which of the following is not a type of join in SQL?",
            "option_a": "Inner join",
            "option_b": "Outer join",
            "option_c": "Left join",
            "option_d": "Top join",
            "correct_answer": "d",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "DBMS"
        },
        {
            "question_id": 287,
            "topic": "NoSQL Databases and Big Data Management",
            "question": "What is MapReduce?",
            "option_a": "A programming model used for processing large amounts of data in a distributed system",
            "option_b": "A query language used in NoSQL databases",
            "option_c": "A schema used for organizing data in a NoSQL database",
            "option_d": "A data processing tool",
            "correct_answer": "a",
            "difficulty": "hard",
            "cognitive_level": "applying",
            "subject": "DBMS"
        }
    ],
    "OOPS": [
        {
            "question_id": 391,
            "topic": "OOP in Practice",
            "question": "What is the main benefit of using object-oriented programming in practice?",
            "option_a": "Code reusability",
            "option_b": "Code maintainability",
            "option_c": "Code readability",
            "option_d": "Code efficiency",
            "correct_answer": "a",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "OOPS"
        },
        {
            "question_id": 330,
            "topic": "Inheritance and Polymorphism",
            "question": "What is the purpose of using abstract classes and interfaces in object-oriented programming?",
            "option_a": "To provide a common interface for a group of related classes",
            "option_b": "To create objects",
            "option_c": "To provide a blueprint for a class",
            "option_d": "To store data",
            "correct_answer": "a",
            "difficulty": "hard",
            "cognitive_level": "analyzing",
            "subject": "OOPS"
        },
        {
            "question_id": 331,
            "topic": "Interfaces and Abstract Classes",
            "question": "What is an abstract class?",
            "option_a": "A class that can be instantiated directly",
            "option_b": "An interface with no method",
            "option_c": " A class with at least one abstract method",
            "option_d": " A class with only private methods",
            "correct_answer": "c",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "OOPS"
        },
        {
            "question_id": 363,
            "topic": "Design Patterns",
            "question": "Which of the following pattern is used to manage a group of related objects?",
            "option_a": "Factory Method",
            "option_b": "Iterator",
            "option_c": "Composite",
            "option_d": "Singleton",
            "correct_answer": "c",
            "difficulty": "medium",
            "cognitive_level": "applying",
            "subject": "OOPS"
        },
        {
            "question_id": 311,
            "topic": "Encapsulation and Abstraction",
            "question": "Which of the following concepts focuses on hiding the complexity of an object and showing only essential features to the user?",
            "option_a": "Encapsulation",
            "option_b": "Abstraction",
            "option_c": "Inheritance",
            "option_d": "Polymorphism",
            "correct_answer": "b",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "OOPS"
        },
        {
            "question_id": 313,
            "topic": "Encapsulation and Abstraction",
            "question": "Which of the following is not true about encapsulation?",
            "option_a": "It provides improved security",
            "option_b": "It reduces the complexity of code",
            "option_c": "It helps in achieving abstraction",
            "option_d": "It allows direct access to object's internal state",
            "correct_answer": "d",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "OOPS"
        },
        {
            "question_id": 315,
            "topic": "Encapsulation and Abstraction",
            "question": "Which of the following refers to the process of bundling data and methods into a single unit?",
            "option_a": "Encapsulation",
            "option_b": "Abstraction",
            "option_c": "Inheritance",
            "option_d": "Polymorphism",
            "correct_answer": "a",
            "difficulty": "easy",
            "cognitive_level": "remembering",
            "subject": "OOPS"
        },
        {
            "question_id": 317,
            "topic": "Encapsulation and Abstraction",
            "question": "Which of the following is not an example of encapsulation in Java?",
            "option_a": "Getters and Setters",
            "option_b": "Constructors",
            "option_c": "Instance variables",
            "option_d": "Inheritance",
            "correct_answer": "d",
            "difficulty": "medium",
            "cognitive_level": "understanding",
            "subject": "OOPS"
        },
        {
            "question_id": 318,
            "topic": "Encapsulation and Abstraction",
            "question": "Which of the following keywords is used to implement abstraction in Java?",
            "option_a": "this",
            "option_b": "super",
            "option_c": "abstract",
            "option_d": "interface",
            "correct_answer": "c",
            "difficulty": "medium",
            "cognitive_level": "applying",
            "subject": "OOPS"
        },
        {
            "question_id": 319,
            "topic": "Encapsulation and Abstraction",
            "question": "Which of the following keywords is used to implement encapsulation in Java?",
            "option_a": "this",
            "option_b": "super",
            "option_c": "private",
            "option_d": "protected",
            "correct_answer": "c",
            "difficulty": "easy",
            "cognitive_level": "understanding",
            "subject": "OOPS"
        }
    ]
}
```
