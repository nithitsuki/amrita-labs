# Database Management Systems (DBMS) Course Syllabus

## Unit 1: Introduction, Relational Data Model, and Database Design

### 1.1 Introduction: Overview of DBMS Fundamentals

#### 1.1.1 Overview and Purpose of DBMS
A Database Management System (DBMS) is a **collection of inter-related data** and a set of programs designed to store and access that data efficiently. The purpose of a database system is primarily to **manage data**. Key applications include Airlines, Telecom, Universities, Banking, Sales, and Online Shopping.

#### 1.1.2 DBMS vs. File Processing Systems (FPS)
The world transitioned from FPS to DBMS due to several drawbacks in FPS:
*   **Data Redundancy and Inconsistency:** FPS suffered from data duplication, which increased storage costs and led to inconsistency if updates were partial. DBMS removes redundancy through normalization, ensuring data consistency and integrity.
*   **Atomicity Issues:** In FPS, ensuring that all parts of a transaction execute (or none do) was difficult; DBMS upholds Atomicity.
*   **Data Isolation and Security:** Data scattered in different formats in FPS made retrieval difficult. DBMS makes it easier to apply security constraints and provide limited access, ensuring data privacy.
*   **Flexibility and Recovery:** DBMS provides easier access, faster response times, and easy recovery by keeping data backups.

#### 1.1.3 Levels of Data Abstraction (The Three-Schema Architecture)
Data abstraction refers to the presentation of data to users without revealing complex underlying details.
*   **Physical Level:** The lowest level, describing *how* data is actually stored in disk blocks and physical storage structures. The schema here is the data structure.
*   **Logical Level:** Describes *what* data is stored in the database (the table structure and interrelationships of attributes/columns). Programmers and database administrators typically work at this level.
*   **View Level:** The highest level, describing the end user interaction with the database system. It is often a subset of the logical schema, constrained by access privileges.

#### 1.1.4 Database Schema and Instance
*   **Schema (Design):** The design or structural view of a database. A schema changes **less frequently** than an instance. Types include Physical, Logical, and View schema.
*   **Instance (Data):** The data stored in the database at a **particular moment of time**; this changes frequently as data is added or deleted.

#### 1.1.5 Data Independence
This is the property of a DBMS allowing changes to the database schema at one level without requiring changes at the next higher level.
*   **Physical Data Independence:** The ability to change the physical data storage (e.g., upgrading storage systems) without impacting the logical schema.
*   **Logical Data Independence:** The ability to change the logical schema (e.g., modifying table formats or constraints) without impacting the view level schema.

#### 1.1.6 Overview of SQL (Query Languages)
SQL (Structured Query Language) commands are grouped by function:
*   **Data Definition Language (DDL):** Used for specifying and defining the database schema structure. Commands include `CREATE`, `ALTER`, `DROP`, and `TRUNCATE`.
*   **Data Manipulation Language (DML):** Used for accessing and manipulating data instances. Commands include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
*   **Data Control Language (DCL):** Used for granting and revoking user access. Commands are `GRANT` and `REVOKE`.
*   **Transaction Control Language (TCL):** Used to persist or rollback changes made by DML commands. Commands are `COMMIT` and `ROLLBACK`.

#### 1.1.7 DBMS Architecture and Components
The DBMS architecture includes Database Users, Query Processor, Storage Manager, and Disk Storage.
*   **Database Users:** Categories include Naive/Parametric End Users (interact via UI), Application Programmers (write DML queries embedded in programs), Sophisticated Users (interact directly via query language like SQL), Specialized Users (write specialized DB applications), and the Database Administrator (DBA).
    *   **DBA Functions:** Schema definition/modification, granting access, routine maintenance, periodical backing up, ensuring free disk space, and monitoring jobs.
*   **Query Processor:** Processes user queries.
    *   *DDL Interpreter:* Interprets DDL and records definitions in the data dictionary (metadata).
    *   *DML Compiler:* Translates DML into an evaluation plan, performs **query optimization** (picking the lowest cost plan), and finds the best relational algebra statement.
    *   *Query Evaluation Engine:* Executes the low-level instructions from the evaluation plan.
*   **Storage Manager:** Provides the interface between low-level data storage and applications/queries. It enforces integrity constraints, checks authorization, manages disk space allocation, and handles data caching (Buffer Manager).
*   **Disk Storage:** Holds actual physical files, data dictionary (metadata), indices (for faster access), and statistical data.

### 1.2 Overview of Relational Databases and Keys

#### 1.2.1 Structure of Relational Databases
A relation is synonymous with a table in the DBMS context.

#### 1.2.2 Keys
Keys are fundamental to the structure of relational databases and include Primary Key, Secondary Key, Super Key, Foreign Key, and Candidate Key.

### 1.3 Formal Relational Query Languages

#### 1.3.1 Overview of Relational Algebra
Relational algebra is a **procedural query language** that takes instances of relations (tables) as input and yields instances of relations as output, using specific operators.

#### 1.3.2 Relational Operations (Operators)
Operators are classified as Unary (requiring one operand) or Binary (requiring two operands).

##### Unary Operators
*   **Select ($\sigma$):** Performs **row filtering** (tuple selection) based on a given predicate or condition (e.g., using $\land$ (AND), $\lor$ (OR), $\sim$ (NOT)). It corresponds to the `WHERE` clause in SQL.
*   **Project ($\Pi$):** Performs **column filtering**; specifies the columns to be included in the output. Duplicate rows are automatically eliminated. It corresponds to the `SELECT` clause in SQL.

##### Binary Set Operators (Requiring Union Compatibility)
For these operations to be valid, relations must be **union compatible**, meaning they must have the same number of attributes (arity) and the corresponding attribute domains must be the same.
*   **Union ($\cup$):** Returns all tuples present in either relation $r$ or $s$; duplicates are eliminated.
*   **Intersect ($\cap$):** Returns tuples common to both relations $r$ and $s$.
*   **Set Difference (-):** Returns tuples present in the first relation ($r$) but not in the second ($s$).

##### Binary Cartesian and Join Operators
*   **Cartesian Product ($\times$):** Combines every row from the first relation with every row from the second relation. This operation often results in **spurious tuples** (wrong records) when performed alone.
*   **Join ($\bowtie$):** Essentially a Cartesian product followed by a selection criterion.

| Join Type | Description |
| :--- | :--- |
| **Inner Join** | Returns only rows with matching values in both tables. |
| $\quad$ Theta Join ($\bowtie_{\theta}$) | General join using any comparison operator (e.g., $=, >, <$) in the join condition. |
| $\quad$ EQUI Join | A specialized Theta join using *only* the equality operator $(=)$. |
| $\quad$ Natural Join ($\bowtie$) | Automatically matches columns with the same name and data type, eliminating duplicate columns in the result. |
| **Outer Join** | Returns matching rows plus unmatched rows from one or both tables, filling missing values with NULLs. |
| $\quad$ Left Outer Join ($\leftouterjoin$) | Returns all rows from the left relation, and matched rows from the right. |
| $\quad$ Right Outer Join ($\rightouterjoin$) | Returns all rows from the right relation, and matched rows from the left. |
| $\quad$ Full Outer Join ($\fullouterjoin$) | Returns all rows from both relations, matching where possible and using NULLs where unmatched. |
*   **Division ($\div$):** $A \div B$ returns tuples from relation $A$ that are associated with *every* tuple in relation $B$. The attributes of $B$ must be a proper subset of the attributes of $A$.

### 1.4 Database Design: The E-R Models and Diagrams

#### 1.4.1 Overview of the Design Process (E-R Model)
The ER diagram serves as the logical blueprint of the database structure, showing the relationships among entities and relationships. The design process often involves identifying entities, attributes, relationships, refining with cardinality, and applying constraints.

#### 1.4.2 Basic E-R Concepts
*   **Entity:** A real-world object (thing, person, place, concept) with well-defined properties, mapping conceptually to a table.
*   **Entity Set:** A collection of similar entities.
*   **Attribute:** A property or characteristic of an entity.
*   **Relationship:** An association between two or more entities/tables.

#### 1.4.3 Types of Attributes
Attributes are visually represented by ellipses.
*   **Key Attribute (Primary Key):** Uniquely identifies an entity; represented by an **underlined ellipse**.
*   **Composite Attribute:** An attribute composed of several simple attributes (e.g., Address composed of State and Pin code).
*   **Multivalued Attribute:** Can hold multiple values (e.g., multiple phone numbers); represented by a **double ellipse**.
*   **Derived Attribute:** Value is calculated dynamically from another attribute (e.g., Age derived from Date of Birth); represented by a **dashed ellipse**.

#### 1.4.4 Constraints: Cardinality and Participation

*   **Mapping Cardinalities (Cardinality Ratio):** Specifies the number of instances of one entity related to instances of another. Types are 1:1, 1:M, M:1, and M:N.
*   **Participation Constraints:** Specifies whether all or only some instances of an entity participate in a relationship.
    *   **Total Participation:** Every instance in the entity set *must* participate in the relationship (e.g., every Passport must belong to a Person). Represented by a **double line**.
    *   **Partial Participation:** Only a few or none of the instances participate (e.g., every Person may not have a Passport). Represented by a single line.

#### 1.4.5 Extended E-R Features

*   **Specialization and Generalization:** Concepts for establishing superclass-subclass relationships.
    *   **Specialization (Top-down):** Dividing a higher-level entity into lower-level entities, each having specific attributes.
    *   **Generalization (Bottom-up):** Combining multiple lower-level entities into a single higher-level entity based on common attributes.
    *   **Overlapping vs. Disjoint:** Disjoint entities have no instance overlap (e.g., an employee is either Part Time or Full Time). Overlapping entities may have overlapping instances (e.g., a Teacher who is also a Student).
    *   **Condition-based vs. User Defined:** Subsets defined by a rule/condition versus no well-defined criteria.

*   **Weak Entity Sets:** Entity sets that lack sufficient attributes to form a primary key on their own.
    *   **Strong Entity (Owner Entity):** The entity the weak entity depends upon.
    *   **Discriminator (Partial Key):** The set of attributes that helps distinguish tuples within the weak entity set.
    *   **Identifying Relationship:** The relationship linking the weak entity to its strong entity; the weak entity has **total participation** (existence dependency) in this relationship.
*   **Aggregation:** Treating a relationship and its corresponding entities as a single, higher-level entity.

### 1.5 Reduction to Relational Schemas

Mapping the E-R model to a relational schema involves translating conceptual design elements into tables and columns.

| E-R Feature | Mapping Rule |
| :--- | :--- |
| **Strong Entity** | Becomes a table; attributes become columns; Primary Key (PK) remains PK. |
| **Composite Attribute** | Each component of the composite attribute becomes a separate column. |
| **Multivalued Attribute** | Create a separate table. This table includes the multivalued attribute as a column and the PK of the original entity as a Foreign Key (FK). |
| **1:1 Relationship** | Add the PK of one entity as a FK into the table of the other entity. |
| **1:M Relationship** | Add the PK of the "one" side entity as a FK into the table of the "many" side entity. |
| **M:N Relationship** | Create a *new table* for the relationship. This table contains FKs to the PKs of both entities. The PK is typically a composite key of these FKs. Descriptive attributes, if any, also become columns. |
| **Weak Entity** | Create a table including all attributes, plus a FK referencing the strong entity's PK. The new table's PK is a composite of the FK and the weak entity's discriminator. |
| **Derived Attribute** | Not mapped directly to a column; they are computed upon retrieval. |
| **Generalization/Specialization** | Strategies include Single Table (Table per Hierarchy), Class Table (Table per Entity), or Concrete Table (Table per Concrete Class). |

### 1.6 Overview of Unified Modelling Language (UML)

UML is a standardized **visual modeling language** used in software engineering to visualize the design and structure of a system. It is managed by the Object Management Group (OMG).

#### 1.6.1 UML Diagrams
UML diagrams are classified as structural or behavioral.
*   **Structural Diagrams:** Depict the static structure of the system (e.g., Class Diagram, Object Diagram, Component Diagram, Deployment Diagram).
*   **Behavioral Diagrams:** Describe the dynamic behavior of the system (e.g., State Machine Diagrams, Activity Diagrams, Use Case Diagrams, Sequence Diagram).

#### 1.6.2 Object-Oriented Concepts in UML
UML is closely linked to O-O principles, including Class (blueprint of an object), Objects (instances of classes), Inheritance, Abstraction, Encapsulation, and Polymorphism.

## Unit 2: Relational Database Design and SQL

### 2.1 Relational Database Design

#### 2.1.1 Features of Good Relational Designs
A good relational design minimizes redundancy and ensures data integrity by preventing anomalies (insertion, deletion, and update anomalies).

*   **Anomalies:**
    *   **Insertion Anomaly:** Inability to add new data due to the absence of other related data, often resulting in null values or inconsistencies.
    *   **Deletion Anomaly:** Unintended loss of data (about one entity) when deleting a record concerning another related entity, due to conflating unrelated information.
    *   **Update Anomaly:** Data inconsistency resulting from redundancy and a partial update (e.g., updating a location in one record but missing others).

#### 2.1.2 Atomic Domains and 1NF
**Normalization** is the process of minimizing redundancy from relations by splitting them into well-structured relations, allowing efficient insertion, deletion, and updating of tuples.

*   **First Normal Form (1NF):** A relation is in 1NF if all its attributes are **atomic** (single-valued) in nature. Multivalued attributes must be eliminated, often by decomposition.

### 2.2 Decomposition using Functional Dependencies

#### 2.2.1 Functional Dependency Theory
A Functional Dependency (FD), represented as $A \rightarrow B$, signifies that the value of attribute set A uniquely determines the value of attribute set B.

*   **Armstrong Axioms (Inference Rules):** Rules used to derive additional FDs from a given set ($F$):
    *   **Reflexivity:** If $Y \subseteq X$, then $X \rightarrow Y$.
    *   **Augmentation:** If $X \rightarrow Y$, then $XA \rightarrow YA$.
    *   **Transitivity:** If $X \rightarrow Y$ and $Y \rightarrow Z$, then $X \rightarrow Z$.
    *   **Union:** If $X \rightarrow Y$ and $X \rightarrow Z$, then $X \rightarrow YZ$.
    *   **Decomposition:** If $X \rightarrow YZ$, then $X \rightarrow Y$ and $X \rightarrow Z$.
*   **Closure of a Functional Dependency ($F^+$):** The complete set of all possible FDs that can be derived from the initial set $F$ using Armstrong’s Rules.

#### 2.2.2 Normal Forms (2NF, 3NF, BCNF)
Normal forms are applied sequentially to eliminate dependencies that cause anomalies.

*   **Second Normal Form (2NF):** A relation must be in 1NF and must not contain any **partial dependency**. A partial dependency occurs when a non-key attribute is functionally dependent on only a proper subset of the primary key.
*   **Third Normal Form (3NF):** A relation must be in 2NF and must not contain any **transitive dependency**. A transitive dependency exists when a non-key attribute is determined by another non-key attribute via a chain of FDs ($A \rightarrow B$ and $B \rightarrow C$).
    *   *Alternative Definition for 3NF:* For all FDs $X \rightarrow Y$, one of the following must be true: i. $X \rightarrow Y$ is trivial; ii. $X$ is a super key; or iii. $Y$ is a prime attribute (part of some candidate key).
*   **Boyce-Codd Normal Form (BCNF) (3.5 NF):** A higher form of 3NF. For all non-trivial FDs $X \rightarrow Y$, $X$ must be a **super key**.

#### 2.2.3 Algorithm for Decomposition
Decomposition is required if a relation violates a normal form. The decomposition should ideally be **lossless** (the original table can be reconstructed via natural joins of the decomposed tables) and preserve dependencies.

### 2.3 Decomposition using Multi-Valued Dependency

*   **Fourth Normal Form (4NF):** A relation must satisfy 3NF (or BCNF) and must not contain multiple **multi-valued dependencies**.

### 2.4 SQL: Review, Intermediate, and Advanced SQL
SQL is categorized into DDL, DML, DCL, and TCL commands. The sources review the functionality of basic commands:
*   **DML/DQL:** `SELECT` (retrieve data), `INSERT` (add records), `UPDATE` (modify data), `DELETE` (remove records).
*   **DDL:** `CREATE` (create instance/table), `ALTER` (change structure), `DROP` (remove structure), `TRUNCATE` (delete table contents).

## Unit 3: Transactions and Concurrency Control

### 3.1 Transactions

#### 3.1.1 Transaction Concept
A transaction is a **logical unit of database processing** that involves one or more read/write operations. It is a unit of program execution that accesses and possibly updates various data items.

#### 3.1.2 A Simple Transaction Model
The database is modeled as a collection of named data items. Basic operations are:
*   **Read ($\text{read\_item(X)}$):** Reads a database item $X$ into a program variable. Steps involve finding the disk block, copying the block to the main memory buffer, and copying $X$ from the buffer to the program variable.
*   **Write ($\text{write\_item(X)}$):** Writes the value of program variable $X$ to the database item. Steps involve finding the disk block, copying the block to the buffer, copying the program variable value into the buffer, and storing the updated block back to disk.
*   **Transaction States:** Active, Partially Committed, Committed, Failed, and Terminated.
*   **Recovery Operations:** $\text{begin\_transaction}$, $\text{end\_transaction}$, $\text{commit\_transaction}$ (signals success, changes are permanent), $\text{rollback}$/$\text{abort}$ (signals failure, changes must be undone), $\text{undo}$ (single operation rollback), $\text{redo}$ (reapply committed operations).

#### 3.1.3 Storage Structure
The storage structure dictates how data is physically arranged and accessed.

*   **File Organization:** The physical storage method for records. Types include **Sequential** (sorted by key), **Heap/Unordered** (stored randomly, fast insertion but slow search), and **Clustered** (related records grouped in the same block).
*   **Indexing:** Data structure for improving retrieval speed (like a book index).
    *   **B+ Tree Index:** A self-balancing tree structure optimized for disk-based storage. All data records reside **only in leaf nodes**, which are linked sequentially for efficient range queries. Searching is logarithmic time, $O(\log n)$.
*   **Hashing:** Used for very fast equality search ($O(1)$ average time). Types include **Static Hashing** (fixed buckets) and **Dynamic Hashing** (buckets grow/shrink, e.g., Extendible Hashing). Hashing is generally *not suitable* for range queries.

#### 3.1.4 Transaction Atomicity and Durability (ACID Properties)
The ACID properties ensure data integrity.
*   **Atomicity:** A transaction is an atomic unit; it is either **performed in its entirety or not at all**. The log is used to undo transactions if failure occurs before commit.
*   **Durability:** Once a transaction is **committed**, its changes are permanent and must never be lost due to subsequent failures.

#### 3.1.5 Transaction Isolation and Serializability

##### Transaction Isolation
The property of isolation requires that a transaction should not make its updates visible to other transactions until it is committed; transactions should work **independently**. Concurrent execution is necessary for **better throughput** and reduced response time.

*   **Problems due to lack of Isolation (Concurrent Execution Issues):**
    *   **Lost Update Problem (W-W Conflict):** One transaction's write operation is overwritten and lost by a concurrent transaction.
    *   **Dirty Read Problem (W-R Conflict):** One transaction reads data updated by another uncommitted transaction, resulting in invalid data if the first transaction later rolls back.
    *   **Blind Write Problem:** A transaction writes a value without reading it first.
    *   **Unrepeatable Read Problem (W-R Conflict):** A transaction reads two different values for the same data item within its execution because another transaction updated it in between.

##### Serializability
A concept identifying which non-serial schedules are correct because their effect is equivalent to executing the transactions sequentially (serially).

*   **Schedule:** The chronological ordering of operations from concurrent transactions.
*   **Conflict Serializability:** A schedule is conflict serializable if it can be transformed into a serial schedule by swapping only non-conflicting operations.
    *   **Conflicting Operations:** Occur when two different transactions access the same data item, and at least one operation is a write (RW, WR, or WW conflicts).
    *   **Precedence Graph (Serialization Graph):** Used to test conflict serializability. Draw an edge $T_i \rightarrow T_j$ if $T_i$ precedes a conflicting operation in $T_j$. The schedule is serializable if the graph contains **no cycles**.
*   **View Serializability:** A schedule is view serializable if it is **view equivalent** to its serial schedule.
    *   **View Equivalence Conditions:** 1. Initial read operations must be the same. 2. Write-Read sequence (update read) must be the same. 3. Final write operation must be the same.

#### 3.1.6 Recoverable Schedules and Cascadeless Schedules

*   **Irrecoverable Schedule:** A schedule where one transaction performs a dirty read from an uncommitted transaction and then commits *before* the uncommitted transaction commits/aborts.
*   **Recoverable Schedule:** A schedule where, if a dirty read occurs, the commit operation of the transaction that performed the dirty read is **delayed** until the writing transaction either commits or rolls back. (All conflict serializable schedules are recoverable).
*   **Cascading Schedule (Cascading Rollback):** Failure of one transaction causes several other dependent transactions (those that read uncommitted data) to also roll back, wasting CPU time.
*   **Cascadeless Schedule:** A schedule where a transaction is **not allowed to read** a data item until the last transaction that wrote it is committed or aborted. This avoids cascading rollbacks.
*   **Strict Schedule:** Implements the strongest restriction: a transaction is **neither allowed to read nor write** a data item until the writing transaction is committed or aborted.

### 3.2 Concurrency Control: Lock-based Protocols

Concurrency control protocols ensure the serializability of schedules. Locking is the most popular technique.

#### 3.2.1 Locks and Granting of Locks
A lock is a variable assigned to a data item to track its status and ensure isolation.
*   **Binary Locks:** Can only be `locked` (1) or `unlocked` (0). They have the drawback of applying a lock even when read-read operations occur, which are not conflicts.
*   **Shared (S) Lock (Read Lock):** Permits multiple transactions to read concurrently but prevents any update operations. A shared lock is granted if no exclusive lock is held on the object.
*   **Exclusive (X) Lock (Write Lock):** Allows a transaction to both read and write; this lock cannot be held concurrently. An exclusive lock is granted only if no other transaction holds any lock on the data item.
*   **Lock Compatibility Matrix:** Shows which lock modes can be held concurrently.

#### 3.2.2 The Two-Phase Locking (2PL) Protocol
2PL is a concurrency control method that guarantees serializability by dividing a transaction's execution into two phases.

1.  **Expanding (Growing) Phase:** The transaction can acquire new locks, but cannot release any. Lock conversion upgrades must be performed during this phase.
2.  **Shrinking Phase:** The transaction can release existing locks, but cannot acquire any new locks. Downgrades must be done during this phase.

**Important Note:** 2PL ensures serializability but **does not ensure that deadlocks do not happen**.

*   **Strict 2PL:** A variation where a transaction does not release **exclusive (X) locks** until after it commits or aborts. Strict 2PL ensures **conflict serializability and recoverability**.
*   **Conservative (Static) 2PL:** Requires a transaction to lock *all* items it needs access to before the transaction begins, making it a **deadlock-free protocol**.

### 3.3 Deadlock Handling

#### 3.3.1 Deadlock Definition
A deadlock is a condition where two or more transactions are waiting indefinitely for one another to release locks, causing activity to halt.

#### 3.3.2 Deadlock Detection and Recovery
Deadlock detection involves the DBMS detecting whether a waiting transaction is part of a deadlock.
*   **Wait for Graph:** A suitable method for detection. Draw a vertex for each transaction. An edge $T_i \rightarrow T_j$ is added if $T_i$ is waiting for $T_j$. If the graph forms a **cycle**, it implies a deadlock.

#### 3.3.3 Deadlock Prevention
Deadlock prevention allocates resources in a way that deadlocks never occur. Timestamp-based protocols can be used:

| Scheme | Mechanism | Rule |
| :--- | :--- | :--- |
| **Wait-Die (Non Pre-emptive)** | Older transaction ($T_i$) has higher priority. | If $T_i$ requests item held by $T_j$: If $T_i$ is **older** than $T_j$, $T_i$ waits. Otherwise, $T_i$ (younger) is rolled back (dies). |
| **Wound-Wait (Pre-emptive)** | Older transaction ($T_i$) has higher priority. | If $T_i$ requests item held by $T_j$: If $T_i$ is **older** than $T_j$, $T_i$ forces $T_j$ to roll back (wounds $T_j$). Otherwise, $T_i$ (younger) waits. |

**Timestamp Ordering Protocol** itself ensures serializability and **freedom from deadlock** since no transaction ever waits.