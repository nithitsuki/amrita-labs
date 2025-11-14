

# Introduction


## DBMS vs FPS

-   There is a need for structure while modelling the real world. We use **entities**, a physical or abstract concept that we can use to orient our data around.
-   A database is a store of information about a group of certain entities.

A DBMS is a software which is used to manage databases, which allows you to add, remove, update and read data.

Prior to DBMS, there was such a thing known as a File Processing System.

An **instance** is an entry in the database.


### Why Did The World Switch From FPS to DBMS

1.  Redundancy

    Redundancy is the duplication of data to ensure that the data remains safe in case one of the copies fail. A File Processing System used copies, an RDBMS on the other hand has only one table, this meant that there&rsquo;s no data wastage.

2.  Consistency

    An issue with having multiple files instead of a table is sometimes the data does not match between copies or files.

3.  Atomicity

    If any operation on the DB crashes then the DB must be brought back to the previous state before the failure.

4.  Security

    Based on the user, a DB can assign permissions to the user on what parts of the entire DB that they can read. There is no ambiguity involved when making a query, and it&rsquo;s easier to make changes to the overall structure of the table than it is to make changes to a file.

5.  Data Independence

    1.  **Physical Data Independence** - Modifications at the physical schema should make no change to the [Logical Level](#org05ae553).
    2.  **Logical Data Independence** - Modifications to the logical schema should make no change to the [View Level](#orgb784b46)


## Schema

A schema is a definition of the structure.

A relation, in the DBMS context, is a table. A relationship is an association between relations.

**NOTE**: A schema changes <span class="underline">less</span> frequently than an instance.


## Levels Of Abstraction

There are three levels:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">View Level      -&gt; Subset Of Logical Schema</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Logical Level   -&gt; What data is stored and it&rsquo;s relationship</td>
</tr>
</tbody>
<tbody>
<tr>
<td class="org-left">Physical Level  -&gt; How data is stored at disk level</td>
</tr>
</tbody>
</table>


### View Level

The schema here is that the structure 
re but constrained by access privileges. In other words, it&rsquo;s a subset of the logical schema.


### Logical Level

How data is organized, with the entity model and the relationship between different tables. The schema at the logical level is the table structure.


### Physical Level

This concerns itself with the way data is stored, using data structures to optimize for querying. The schema at the physical level is the data structure.


## SQL Types

1.  DDL - Data Definition Language. Defines the structure of the database. Example - `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
2.  DCL - Data Control Language. Controls access permissions Example - `GRANT`, `REVOKE`
3.  DML - Data Manipulation Language. Modifies the instances of the database. Example - `INSERT`, `UPDATE`
4.  DQL - Data Query Language. Retrieves data from the database. Example - `SELECT`
5.  TCL - Transmission Control Language. Controls the state of the database management system. Example -  `COMMIT`, `ROLLBACK`


## DB Architecture

1.  Database Users
2.  Query Processor
3.  Storage Manager
4.  Data File


## Syntax


### Creating a Table

    CREATE TABLE Stud(RegNo char(10) PRIMARY KEY, name varchar(15));


### Inserting Data

    INSERT INTO tablename(col1,col2...) VALUES('value1','value2')
    INSERT INTO tablename VALUES('value1','value2')


## Database Architecture


### DB Users

1.  Naive Users

    The end users interacting with the database using the UI

2.  Application Programmer

    The programmers writing the backend and frontend and writing queries.

3.  Sophisticated Users

    Writes specific queries that require larger levels of control over the DB

4.  Specialized Users

    Perform analyses and AI to write richer queries.

5.  Database Administrator

    Most important role in a DB application, is responsible for overall management or overall wellbeing of the application.
    The DBA should:
    
    1.  make provisions for frequent backups.
    2.  have enough free disk space.
    3.  change the logical schema if necessary
    4.  manage data access privileges


### Query Processor

-   DDL Interpreter - It performs the parsing of the command. If a DDL command is passed, its data is stored to data dictionary with metadata(data about data). The metadata includes the constraints about the data.
-   DML Compiler
    1.  Translation - Translate the query into a language that the Query Evaluation Engine understands.
    2.  Optimization - Searches the best among the possible relational algebra statements to represent the mathematical model to query the data, so that the resources aren&rsquo;t wasted.
-   Query Evaluation Engine - Executes the solution sent by the DML Compiler.


### Storage Manager

-   Buffer Manager - Helps in the data transportation between the buffer and secondary storage with the help of a log writer.
-   File Manager - Helps maintain the data in the secondary storage
-   Authorization & **Integrity Manager** - Accepts the DCL commands, and checks whether a user is authorized to access the data. It also prevents the constraints of the logical schema from being broken.
-   Transaction Manager - Upholds [Atomicity](#orgde739fb).


### Disk File

-   Data Dictionary
-   Data File
-   Indices


## Keys

1.  Primary Key
2.  Secondary Key
3.  Super Key
4.  Foreign Key
5.  Candidate Key


# E-R Diagram

This corresponds to the design phase of making a software project. The blueprint of our software.

1.  An entity can be mapped to a table.
2.  A relationship is an association between tables.


## Why Have Relationships In The First Place

1.  This prevents data repetition.
2.  If there were no relationships, data can&rsquo;t be connected together as is necessary to solve problems.


## Notation


## Types Of Attributes

1.  Single valued &  Multivalued attribute
2.  Stored And Derived attribute
    SvelteKit - `$state` vs `$derived`
3.  Simple and composite attribute


## Mapping Cardinalities

Also known as cardinality ratios, they denote how many instances map to another instances in a relationship


### One To One

$Person \Leftrightarrow Passport, 1:1$


### One To Many

$Department \Leftrightarrow Employees, 1:m$


### Many To One

$Employees \Leftrightarrow Department, 1:1$


### Many To Many

$Student \Leftrightarrow Course, 1:n, m:1 \rightarrow m:n$


## Participation Constraints

Taking the example of students mapped to courses.


### Total

Students **must** register for at least one course


### Partial

Not necessary that all courses have one student.

1.  University Management System


## Case Study 1

<p class="verse">
A university has multiple departments each of which employs multiple staffs, the department offers courses taught by the staff. Students register for multiple courses. One staff heads the department. Draw the E-R diagram for the same.<br />
</p>

To begin solving this, we need to go about a `Noun-Phrase` Approach. We must identify all the nouns in the scenario.

The approach is:

1.  Identify the entities
2.  Identify the attributes
3.  Identify the primary key
4.  Identify the relationship
5.  Refine your model with the mapping cardinalities
6.  Refine it with the participation constraints.


### Solution

The nouns here become the *entities*:

1.  University
2.  Departments
3.  Staff
4.  Courses
5.  Students

Though a university qualifies as an entity, it&rsquo;s a singular entity. Thus, we cannot identify it as an entity in the E-R diagram.


## Extended ER Features


### Generalization/Specialization

The `IS A` block is used to denote inheritance

A generalization is a top-down, while a specialization is bottom-up.

1.  Disjoint/Overlapping

    A disjoint specialization/generalization are those which have zero overlap with each other.
    An overlapping set is now self explanatory.

2.  Condition Based & User Defined

    A generalization/specialization is condition based if the entity is defined terms of a set rule or condition.
    If the rule is arbitrary, it&rsquo;s a user defined generalization/specialization.


### Weak Entity

Every weak entity has an identifying relationship with a strong entity.

An attribute that **helps** in uniquely identifying the entities while not being unique is called a discriminator.


### CASE STUDY 2

> In a university, there are multiple libraries. Each of which has many books, every book is uniquely identified within the library using `Book Number`. Each library has multiple members. A person can be a member of multiple libraries, one library can take interlibrary loan. Draw the ER diagram.


### Mapping ER To Relational Model

1.  Multivalued attribute

    When we have multivalued attribute, we must split the entity into two tables. For example, a student can have **multiple** phone numbers, the way to represent this in a relational model is as so:
    
    The main table Student() will be like so.
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left"><span class="underline">Registration Number</span></th>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Branch</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td class="org-left">R1</td>
    <td class="org-left">A</td>
    <td class="org-left">AID</td>
    </tr>
    
    <tr>
    <td class="org-left">R2</td>
    <td class="org-left">B</td>
    <td class="org-left">CSE</td>
    </tr>
    
    <tr>
    <td class="org-left">R3</td>
    <td class="org-left">B</td>
    <td class="org-left">ECE</td>
    </tr>
    </tbody>
    </table>
    
    And, the registration number and phone number together are (PRIMARY KEY). There&rsquo;s a secondary table `Stud_PhoneNo()` made like so.
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-right" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Registration Number</th>
    <th scope="col" class="org-right">Phone Number</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td class="org-left">R1</td>
    <td class="org-right">100</td>
    </tr>
    
    <tr>
    <td class="org-left">R2</td>
    <td class="org-right">101</td>
    </tr>
    
    <tr>
    <td class="org-left">R2</td>
    <td class="org-right">102</td>
    </tr>
    
    <tr>
    <td class="org-left">R2</td>
    <td class="org-right">103</td>
    </tr>
    
    <tr>
    <td class="org-left">R3</td>
    <td class="org-right">104</td>
    </tr>
    
    <tr>
    <td class="org-left">R3</td>
    <td class="org-right">105</td>
    </tr>
    </tbody>
    </table>

2.  Strong Entity/Entity

    Represent the table with attributes as is

3.  Composite Attribute

    A composite attribute&rsquo;s components are represented as columns directly. An entity with a1, a2 and a3 where a2 can be divided into a21 and a22.
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">E</td>
    <td class="org-left">a1</td>
    <td class="org-left">a21</td>
    <td class="org-left">a22</td>
    </tr>
    </tbody>
    </table>

4.  Derived Attribute

    They&rsquo;re not mapped at all into a table. They&rsquo;re computed.

5.  Mapping Relationships

    1.  1:1 relationship
        The total participation is usually the one with the foreign key, otherwise it can go either way.
    2.  1:m/m:1 relationship
        The one with the $m$ entities contains the foreign key.
    3.  m:n relationship
        There will be at minimum 3 tables, the two entity tables and one tablewith the foreign keys of both entities

6.  Descriptive Attribute

    They only arrive for m:n relationships, they exist in the third table formed to represent the relation in m:n.

7.  Weak Entity

    The mapping cardinality and participation constraints don&rsquo;t matter. The strong entity table is created, the weak entity table is created with the strong entity&rsquo;s primary key as a foreign key, and the primary key of this table is the strong entity&rsquo;s primary key along with the discriminator.

8.  Generalization/Specialization

    We don&rsquo;t map the generalization, we make separate tables for each new sub-entity

9.  Mapping To Relational Model

    For Case Study 1,
    
    1.  Dept
        
        <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
        
        
        <colgroup>
        <col  class="org-left" />
        
        <col  class="org-left" />
        
        <col  class="org-left" />
        </colgroup>
        <tbody>
        <tr>
        <td class="org-left"><span class="underline">dname</span></td>
        <td class="org-left">dloc</td>
        <td class="org-left">staffhead(staff.sid)</td>
        </tr>
        </tbody>
        </table>
    2.  Staff
        
        <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
        
        
        <colgroup>
        <col  class="org-left" />
        
        <col  class="org-left" />
        
        <col  class="org-left" />
        </colgroup>
        <tbody>
        <tr>
        <td class="org-left"><span class="underline">sid</span></td>
        <td class="org-left">sname</td>
        <td class="org-left">dept.dname</td>
        </tr>
        </tbody>
        </table>
    3.  Course
        
        <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
        
        
        <colgroup>
        <col  class="org-left" />
        
        <col  class="org-left" />
        
        <col  class="org-left" />
        </colgroup>
        <tbody>
        <tr>
        <td class="org-left"><span class="underline">ccode</span></td>
        <td class="org-left">cname</td>
        <td class="org-left">staff.sid</td>
        </tr>
        </tbody>
        </table>
    4.  Stud
        
        <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
        
        
        <colgroup>
        <col  class="org-left" />
        
        <col  class="org-left" />
        
        <col  class="org-left" />
        </colgroup>
        <tbody>
        <tr>
        <td class="org-left"><span class="underline">RegNo</span></td>
        <td class="org-left">fname</td>
        <td class="org-left">lname</td>
        </tr>
        </tbody>
        </table>
    5.  Stud<sub>Ph</sub>
        
        <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
        
        
        <colgroup>
        <col  class="org-left" />
        
        <col  class="org-left" />
        </colgroup>
        <tbody>
        <tr>
        <td class="org-left"><span class="underline">RegNo</span></td>
        <td class="org-left"><span class="underline">PhNo</span></td>
        </tr>
        </tbody>
        </table>
    6.  Stud<sub>Course</sub>
        
        <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
        
        
        <colgroup>
        <col  class="org-left" />
        
        <col  class="org-left" />
        
        <col  class="org-left" />
        </colgroup>
        <tbody>
        <tr>
        <td class="org-left"><span class="underline">RegNo</span></td>
        <td class="org-left">CCode</td>
        <td class="org-left">grade</td>
        </tr>
        </tbody>
        </table>


# Relational Algebra

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Unary</th>
<th scope="col" class="org-left">Binary</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Project(&pi;)</td>
<td class="org-left">Cross product (X)</td>
</tr>

<tr>
<td class="org-left">Select(&sigma;)</td>
<td class="org-left">Join</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Set diff</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Union</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Intersection</td>
</tr>
</tbody>
</table>

    SELECT ename from Emp where sal > 50000

We write this as,

$$\pi_{ename}(\sigma_{\text{sal>50000}}(Emp))$$


## Unary Operators

1.  Select
    $$\sigma_{condition}(Relation)$$
2.  Project
    $$\Pi_{col_1,col_2,\cdots}(Relation)$$


## Binary Operators


### Logical Operators

1.  &and; - AND
2.  &or; - OR
3.  <> or ! or ~ - NOT


### The Union Compatibility Rule

1.  The <span class="underline">arity</span> of both the relation should be the same
2.  The <span class="underline">domain of ith attribute</span> of both the relations should be the <span class="underline">same</span>.


## Cartesian Product/Cross Product

When a cartesian product is applied, we&rsquo;d have **spurious tuples** which are the <span class="underline">wrong</span> instances of data.


## PROBLEMS

> Given:
> 
> 1.  Emp(eno, name, city, sal, gender, dno)
> 2.  Dept(dno, dname)
> 3.  Pjt(pno, pname, loc, dno)
> 4.  Dependent(`dep_name`, gener, eno)
> 
> 5.  List the details of all the employees
> 6.  Names of employees
> 7.  Details of employees who belong to bangalore
> 8.  Details of employees whose salary is between 50000 and 1 lakh
> 9.  Employees who work in HR department and make over 50000 or work in accounts department and make over 70000
> 10. Names that are shared between the employees and the dependents

1.  Emp
2.  $\Pi_{name}(Emp)$
3.  $\sigma_{city = Bangalore}(Emp)$
4.  $\sigma_{salary > 50000 \land salary< 100000}(Emp)$
5.  $\sigma_{(dname = HR \land salary > 50000) \lor (dname = account \land salary > 70000)}$
6.  $\Pi_{name}(Dependent \cap Emp)$

> 1.  Details of the project
> 2.  Details of the department controlling that project
> 3.  Details of the project controlled by or handled by CSE
> 4.  Names of employees along with their dep name
> 5.  Names of female dependents of employee named Sai Preran
> 6.  Names of male dependents of employees who work for ECE department
> 7.  Names of employees who have dependents
> 8.  Names of employees who don&rsquo;t have dependents

1.  Proj
2.  Project $\bowtie$ Dep
3.  $\sigma_{depname = \text{CSE}}(Project \bowtie Dep)$
4.  $\Pi_{ename,depname}(Emp \bowtie Dep)$
5.  $\sigma_{ename = \text{Sai Preran} \land gender = \text{F}}(Dependent \bowtie Emp)$
6.  $\Pi_{dependent.depname}(\sigma_{gender = \text{M} \land dep.dno = \text{ECE}}(Emp \bowtie Dep))$
7.  $\Pi_{ename}(Emp \bowtie Dep)$
8.  $\Pi_{ename}(Emp \times (\Pi_{eno}(Emp) - \Pi_{eno}(Dep))$)

> Sailor(sid, sname, age)
> Boat((bid, bname, colour)
> Resv(sid, bid)
> 
> 1.  Names of the sailors who have reserved a boat with bid B01
> 2.  Names of sailors who have reserved a red coloured boat
> 3.  Colours of the boat reserved by the sailor named ABC
> 4.  Names of sailors who have reserved at least one boat.
> 5.  Find sname who have reserved a red OR a green  boat.
> 6.  Find sname who have reserved a red AND a green  boat.
> 7.  Retrieve sid of sailors with age > 20 who have not reserved a red boat.

1.  $\Pi_{sname}(\sigma_{Sailor.sid = Resv.sid \land Boat.bid = Resv.bid \land Boat.bid = 'B01'}(Sailor \times Boat \times Resv))$


## Functional Dependency And Normalization


### Functional Dependency

When we write $A \rightarrow B$, it means that we can definitely get B from what we know of A.

For example in a DB with a table Emp(Eno, Ename, city, state),

$Eno \rightarrow City$

These are **based on the instances of a table.**


### Armstrong Axioms or Inference Rules

1.  Augmentation Rule

    If $X \rightarrow Y$ then $AX \rightarrow AY$

2.  Union Rule

    If $X \rightarrow Y$ and $X \rightarrow Z$ then $X \rightarrow YZ$

3.  Decomposition Rule

    If $X \rightarrow YZ$ then $X \rightarrow Y$ and $X \rightarrow Z$

4.  Transitive Rule

    If $X \rightarrow Y$ and $Y \rightarrow Z$ then $X \rightarrow Z$

5.  Pseudotransitivity Rule

    If $X \rightarrow Y$ and $WY \rightarrow Z$ then $XW \rightarrow Z$

6.  Reflexivity Rule[[

    If $X \subseteq Y$ then $Y \rightarrow X$


### PROBLEM

1.  Closure of F

    > Given R(ABCDE),
    > FDs are $A \rightarrow BC, A \rightarrow C, C \rightarrow D, CD \rightarrow E$ find $F^+$
    > 
    > Find $F^+$ = Closure of F
    
    > R(PQSTU)
    > 
    > F = {Q &rarr; ST, T &rarr; U, Q &rarr; P, U &rarr; S, PT &rarr; Q}
    > 
    > Find $F^+$
    
    1.  T &rarr; U and U &rarr; S, we get T &rarr; S (Transitive)
    2.  Q &rarr; P and Q &rarr; ST, we get Q &rarr; PST(Union Rule)
    3.  Q &rarr; ST, we get Q &rarr; S and Q &rarr; T

2.  Closure of an attribute

    > Given R(ABC), F = {AB &rarr; C, C &rarr; B}, find C^+
    
    Say, $\alpha = C, C^+ = C$
    
    > Given R(ABCDEH),
    > F = {A &rarr; B,  AB &rarr; E, BH &rarr; C, CD &rarr; D, D &rarr; A}


### Normalization

A set of rules we enforce on data design.


### 1NF - Atomic Attribute

1.  Guidelines

    -   All the attributes of the table should be atomic in nature ( Single valued attiribute )
    
    Example - E is an entity with attributes a1, a2,a3;; a3 is a mva. Here E is not in 1NF as a3 is not atomic, therefore decompose `E` to `E and E_mva`
    
    `E(a1,a2), E_mva(a1,a3)`


### 2NF - Partial Dependency

-   There should not be any partial dependency between a key and a non key attribute.
    When R(<span class="underline">A,B</span>,C,D), B -> C is a partial dependency. So it does not follow the 2nd normal form. The resultant table formed from the natural joins of the tables decomposed for holding 2NF.
    
    The decomposition should be lossless and the dependencies are preserved(optional).

> Given Relation R with set of functional dependencies F. R<sub>1</sub> and R<sub>2</sub> are the decomposed tables of R with their corresponding tables of R with their corresponding FD sets F1 & F2. The dependency preservation is achieved.

> R(ABCDE)
> R1(ABC), R2(CDE)
> F = {AB -> E, A->B, C -> D, CD-> E}

> Consider a customer of a bank, whose information like cno, cname, city and phone number are recorded. A customer may have more than one phone number. Is the customer table in 1NF.

> No, due to ph being an mva to remedy this, we must decompose the table. C(cno, cname, city) and C<sub>ph</sub>(Cno, phno)

> R(eno, dno, ename, dname, pjt)

> R1(eno, dno, pjt), R2(dno, dname), R3(eno,ename)

> R(ABCD), given AB -> C, C -> A, C -> D
> D = {AB, ACD}

> Solution
> R1 = AB, R2 = ACD
> 
> R1 intersection R2 = A
> A^+ = A
> 
> A is not a superkey of R1 or R2
> Hence decomposition is lossy

> R(ABCDEF)
> D = {BE, ACDEF}
> 
> F = {A -> B, C -> DE, AC -> F}

> Solution
> R1 int R2
> E
> 
> E^+ = E
> 
> Thus E is not a superkey of R1 or R2
> Hence decomp is lossy.

> R(ABCDE)
> R1(ABC), R2(ACDE)
> F = {A -> BC, CD -> E, B -> D, E ->A }

> R(ABCDEG)
> F = {AB -> C, AC -> B, AD -> E, B -> D, BC -> A, E -> G}
> 
> D = {ABC, ACDE, ADG}

> (<span class="underline">A,B</span>)
> 
> AB -> C
> AB -> D
> AB -> E
> D -> C
> D -> E
> B -> C
> 
> R1 = ABD
> R2 = DE
> R3 = DCE
> 
> R1 has
> AB -> D
> 
> R2 has
> D -> E
> 
> R3 has
> D -> C
> D -> E


### Canonical Cover

> A **canonical cover is -** Given R(Relation) & F (Set of functional dependencies) to find F<sub>c</sub>, remove extraneous attributes.

> **Extraneous attributes** - Assume &alpha; is extraneous in LHS. Then find (LHS - &alpha;^+) under F and check if it covers given RHS, then assumption that &alpha; is extraneous is true.

> R(ABCDE),
> F = {A -> D, AD -> C, D -> AC, D -> E }
> 
> Since we can derive everything from D alone, and remove A.
> 
> Thus A is an extraneous attribute.

> F = { A -> BC, B -> C, A ->B, AB -> C}
> 
> Assume,
> A+ under F&rsquo;, A+ = (ACB)
> 
> F = {A -> C, B -> C, A -> B, AB -> C}
> 
> Consider AB -> C, assuming extraneous attribute = B
> 
> B &isin; C
> 
> A \subseteq A+
> 
> F = {A -> C, B -> C, A -> B, A -> C}
> 
> F<sub>c</sub> = B-> C, A -> B

> LHS -> RHS, &alpha;
> Extraneous in LHS
> 
> (LHS - &alpha;)^+ under F cover original RHS
> 
> extraneous in RHS
> F&rsquo; = F - assumed extraneous attribute
> 
> (LHS)^+ under F
> Cover assumed extraneous attribute

> F = {AB -> CD, A -> E, E -> C}


### 3NF

1.  Should satisfy 2nd normal form.
2.  There should not be any transitive dependency between a key and a non key.

LHS - Determinant,
RHS - Dependent.

> R(A,B,C,D,E,F)
> AB is primary key
> B -> C, C -> D, D-> E, AB -> F
> 
> This violates 1st Normal Form,
> To fix we decompose F into F<sub>1</sub>, F<sub>2</sub> and so on.
> 
> R1(A,B,C,D,E)
> R2<sub>mva</sub>(A,B,F)
> 
> To 2nd normal form,
> R1(<span class="underline">A,B</span>,D,E)
> R2(B, C)
> R3(<span class="underline">A,B</span>,F)
> 
> For 3rd normal form,
> R1(<span class="underline">A,B</span>,D)
> R2(<span class="underline">A,B,</span>,E)
> R3(B, C)
> R4(<span class="underline">A,B</span>,F)


### 2nd Definition

\#+begin<sub>quote</sub>
All the given FDs should satisfy any one of the following:

1.  &alpha; -> &beta; should be trivial
2.  &alpha; should be a super key (FOR &alpha; to be a super key, (&alpha;)^+ should be R)
3.  &beta; - &alpha; should be contained in the key (candidate key).

Note on BCNF(Boyce Codd), All FDs should satisfy either rule 1 or rule 2.


### 4NF

1.  Satisfy 3NF
2.  Relation cannot have multiple multivalued dependencies


## Concurrency Control


### Deadlock detection using wait for graph

1.  Draw a vertex for each transaction in the schedule.

2.  An edge is added to the graph if and only if Ti is waiting for Tj

3.  If the graph at any point of time has cycle, it implies deadlock.


# SQL Syntax


### UPDATE

    UPDATE tablename SET columnname = 'value' WHERE condition;


### DELETE

    DELETE FROM tablename WHERE condition;


### DROP

    DROP TABLE tablename;


### ALTER

    ALTER TABLE tablename ADD columnName datatype(size)
    ALTER TABLE tablename DROP COLUMN columnName;
    # Change just the datatype.
    ALTER TABLE tablename MODIFY COLUMN columnName datatype(newSize);