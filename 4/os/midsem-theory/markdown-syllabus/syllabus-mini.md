# EXAM REVIEW: OPERATING SYSTEMS

## Chapter 1: Introduction

### 1. Operating System Fundamentals
*   **Definition:** An operating system (OS) is a program that acts as an intermediary between a computer user and the computer hardware. 
*   **Role:** The OS is generally considered the kernel, which is the one program running at all times on the computer. 
*   **Middleware:** Modern OSes for general-purpose and mobile computing include middleware, which are software frameworks providing additional services to developers like databases, multimedia, and graphics.

### 2. Computer-System Organization and Architecture
*   **Organization:** One or more CPUs and device controllers connect through a common bus providing access to shared memory.
*   **Architecture Models:** 
    *   **Von Neumann architecture:** Dictates how modern computers work, illustrating instruction execution and data movement between the CPU, cache, and memory.
    *   **Direct Memory Access (DMA):** Used for high-speed I/O devices to transmit information at close to memory speeds without burdening the CPU.
    *   **Symmetric Multiprocessing (SMP):** Each processor performs all tasks, sharing main memory.
    *   **Asymmetric Multiprocessing:** Each processor is assigned a specific task.
    *   **Dual-Core / Multicore:** Multiple processing cores on a single chip, sharing L2 cache but having individual L1 caches and registers.
    *   **Non-Uniform Memory Access (NUMA):** CPUs have local memory but can access memory of other CPUs via an interconnect.
    *   **Clustered Systems:** Multiple independent systems working together, usually sharing storage via a storage-area network (SAN) to provide high-availability.

### 3. Storage Hierarchy
*   **Measurement:** Storage is based on bits (0s and 1s) and bytes (8 bits). Larger metrics include KB, MB, GB, TB, and PB. A "word" is the native unit of data for a given architecture.
*   **Main Memory:** The only large storage media the CPU can access directly. It provides random access and is typically volatile (DRAM).
*   **Secondary Storage:** An extension of main memory that provides large, nonvolatile storage capacity (e.g., Hard Disk Drives/HDDs and Non-volatile memory/NVM devices).
*   **Hierarchy Design:** Storage systems are organized in a hierarchy based on speed, cost, and volatility. From fastest to slowest: Registers, Cache, Main Memory, Solid-state disk, Magnetic disk, Optical disk, Magnetic tapes.
*   **Caching:** Information in use is temporarily copied from slower storage to faster storage (cache). The faster storage is checked first; if the data is there, it is used directly. Managing cache size and replacement policies is critical. Multiprocessor systems require cache coherency so all CPUs have the most recent data.

### 4. Operating System Operations
*   **Multiprogramming (Batch system):** Organizes jobs (code and data) so the CPU always has one to execute, preventing idle time. If a job has to wait (e.g., for I/O), the OS switches to another job.
*   **Process Management:** A process is an active entity (a program in execution), whereas a program is a passive entity. Processes need resources (CPU, memory, files) and have a program counter specifying the next instruction. Single-threaded processes have one program counter, while multi-threaded processes have one per thread.
*   **Memory Management:** Determines what is in memory and when to optimize CPU utilization. The OS keeps track of used memory, decides what to move in/out, and allocates/deallocates space.
*   **File-System Management:** The OS provides a uniform, logical view of information storage by abstracting physical properties into logical units called files. Files are organized into directories with access controls.
*   **Mass-Storage Management:** Proper management (mounting, free-space management, disk scheduling, partitioning) is central to computer speed.

### 5. Security, Protection, and Environments
*   **Protection vs. Security:** Protection controls access to resources, while security defends the system against external and internal attacks (e.g., viruses, denial-of-service). Systems distinguish users via User IDs and Group IDs to determine access control.
*   **Virtualization:** Virtual Machine Managers (VMMs) can run natively on hardware (like VMware ESX) or be hosted to run guest OSes.
*   **Distributed Systems:** A collection of separate networked systems (LAN, WAN, MAN, PAN) that communicate via protocols like TCP/IP.
    *   **Peer-to-Peer (P2P):** Does not distinguish clients and servers; all nodes act as peers (e.g., Skype, Napster).
    *   **Cloud Computing:** Delivers computing, storage, and apps as a service (SaaS, PaaS, IaaS) across a network, using traditional OSes, VMMs, firewalls, and load balancers.
*   **Free and Open-Source OS:** FSF's "copyleft" GNU Public License (GPL) counters DRM. Examples include Linux and BSD UNIX.

### 6. Kernel Data Structures
*   **Lists:** Singly linked lists, doubly linked lists, and circular linked lists.
*   **Trees:** Binary search trees (left <= right) offer O(n) search, while balanced binary search trees offer O(lg n).
*   **Other Structures:** Hash functions mapping to hash maps, and Bitmaps (strings of n binary digits representing the status of n items).

---

## Chapter 2: Operating-System Services

### 1. OS Services and Interfaces
*   **User-Centric Services:**
    *   **User Interface (UI):** Includes Command-Line (CLI), Graphical User Interface (GUI), Touchscreen, and Batch. Mac OS X uses the "Aqua" GUI. Mobile interfaces rely on gestures and voice commands rather than a mouse.
    *   **Program Execution:** Loading programs into memory, running them, and handling termination.
    *   **I/O Operations:** Managing running programs that require files or I/O devices.
    *   **File-system manipulation:** Reading, writing, creating, and deleting files.
*   **System-Centric Services:** Logging usage and providing protection and security (authentication and preventing concurrent processes from interfering with each other).

### 2. System Calls
*   **Definition:** The programming interface to the services provided by the OS, typically accessed via high-level Application Programming Interfaces (APIs) like Win32 (Windows), POSIX (UNIX/Linux/macOS), or Java API.
*   **Implementation:** A number is associated with each system call, indexed in a table. Parameters are passed to the OS via registers, stored in a memory block/table, or pushed onto the stack.
*   **Types of System Calls:**
    *   **Process control:** fork(), exit(), wait().
    *   **File management:** open(), read(), write(), close().
    *   **Device management:** request/release device, attach/detach.
    *   **Information maintenance:** get/set time, date, and system data.
    *   **Communications:** create/delete connections, send/receive messages, map shared memory.
    *   **Protection:** get/set permissions.
*   **Standard C Library:** Acts as an intermediary; e.g., calling `printf()` in C invokes the `write()` system call in the OS.

### 3. Application Execution and Compilation
*   **Linkers and Loaders:** Source code is compiled into object files. The Linker combines object files into an executable file. The Loader places the executable into memory. Modern systems use Dynamically Linked Libraries (DLLs) to share library code across multiple apps.
*   **Why Apps are OS Specific:** Applications compiled on one OS cannot run on another because each OS has unique system calls and file formats. Cross-platform execution requires interpreted languages (Python), Virtual Machines (Java), or adherence to an Application Binary Interface (ABI).

### 4. OS Structure and Design
*   **Policy vs. Mechanism:** A critical design principle. Policy determines *what* needs to be done (e.g., interrupt every 100 seconds). Mechanism determines *how* to do it (e.g., using a timer). Separating them allows maximum flexibility.
*   **Structural Models:**
    *   **Monolithic:** Original UNIX; combines the file system, CPU scheduling, memory management, and drivers into one large kernel level.
    *   **Layered:** The OS is divided into layers where Layer 0 is hardware and Layer N is the user interface; higher layers only use services of lower layers.
    *   **Microkernels:** Moves as much as possible from the kernel to user space (e.g., Mach). Communication uses message passing. It is easier to extend and more secure, but suffers performance overhead from user-to-kernel communication.
    *   **Modules:** Uses Loadable Kernel Modules (LKMs). Core components are separate but loadable as needed, providing object-oriented flexibility (e.g., Linux).
    *   **Hybrid Systems:** Combines models. Linux is monolithic plus modular. macOS/iOS (Darwin) is layered with a Mach microkernel and BSD UNIX components. Android uses a modified Linux kernel, a Hardware Abstraction Layer (HAL), Bionic, and the ART/Dalvik virtual machine.

### 5. Building, Booting, and Debugging
*   **Building Linux:** Download source -> `make menuconfig` (configure) -> `make` (compile kernel `vmlinuz`) -> `make modules` -> `make install`.
*   **System Boot:** A bootstrap loader or BIOS (or UEFI on modern systems) in ROM locates the kernel, loads it into memory, and starts it. GRUB is a common bootloader allowing kernel selection.
*   **Debugging:** Involves finding/fixing errors and performance tuning. Errors generate log files, core dumps (app failure), or crash dumps (OS failure). Tools like BCC/BPF (e.g., `disksnoop.py`) trace system activity.

---

## Chapter 3: Processes

### 1. Process Concept
*   **Definition:** A process is a program in execution (an active entity), whereas an executable file on disk is a passive entity. Multiple processes can be spawned from the exact same program.
*   **Process Components in Memory:**
    *   **Text section:** Program code.
    *   **Stack:** Temporary data (function parameters, return addresses, local variables).
    *   **Data section:** Global variables.
    *   **Heap:** Memory dynamically allocated during run time.
*   **Process States:** New (being created), Running (executing instructions), Waiting (waiting for an event/IO), Ready (waiting to be assigned to a processor), Terminated (finished).
*   **Process Representation:** Linux represents processes using the `task_struct` C structure (contains pid, state, parent, children, open files, and memory space).
*   **Multiprocess Architecture:** Modern browsers like Google Chrome use multiple processes to prevent full crashes. Chrome uses a Browser process (UI/Disk IO), Renderer process (HTML/JS, runs in a restricted sandbox), and Plug-in processes.

### 2. Interprocess Communication (IPC)
*   **Overview:** Processes can be independent or cooperating. Cooperating processes need IPC for information sharing, computation speedup, modularity, and convenience.
*   **IPC Models:**
    *   **Shared Memory:** Processes map a shared memory region. In POSIX, this involves `shm_open()`, setting size with `ftruncate()`, and mapping with `mmap()`.
    *   **Message Passing:** Processes communicate without sharing address spaces via `send()` and `receive()` primitives using mailboxes (ports). 
        *   *Buffering:* Message queues can have zero capacity (sender must wait for rendezvous), bounded capacity (sender waits if full), or unbounded capacity (sender never waits).
        *   *Mach Example:* Uses `mach_msg()` for system calls and IPC, requiring a Kernel port and Notify port.
        *   *Windows Example:* Uses Local Procedure Call (LPC) facilities to pass messages.

### 3. Client-Server Communication
*   **Remote Procedure Calls (RPC):** Abstracts procedure calls across a network.
*   **Stubs:** The client-side stub locates the server and marshals the parameters. The server-side stub unpacks the message and performs the procedure.
*   **Data Representation:** Handled via External Data Representation (XDL) to account for differences in architectures (like big-endian vs. little-endian).
*   **Execution:** The OS typically provides a matchmaker/rendezvous service to connect the client and server.

---

## Chapter 4: Threads & Concurrency

### 1. Threads vs. Processes
*   **Definition:** A thread is a basic unit of CPU utilization consisting of a program counter, stack, and set of registers. 
*   **Shared vs. Unshared:** A thread shares its code section, data section, and open files with other threads belonging to the same process, but maintains its own stack and registers.
*   **Motivation:** Thread creation is light-weight compared to the heavy-weight process creation. Multi-threading allows an application to perform multiple tasks (update display, fetch data, spell check) concurrently, simplifying code and increasing efficiency.

### 2. Concurrency and Parallelism
*   **Concurrency:** Supports more than one task making progress. On a single-core system, concurrency is achieved by the scheduler rapidly switching between threads.
*   **Parallelism:** Implies a system can perform multiple tasks simultaneously across a multi-core processor.
    *   *Data parallelism:* Distributes subsets of the same data across multiple cores.

### 3. Thread Libraries
*   **Pthreads:** A POSIX standard (IEEE 1003.1c) API for thread creation and synchronization. It is a *specification, not an implementation*, heavily used in UNIX/Linux/macOS. Key functions include `pthread_create()`, `pthread_join()`, and `pthread_exit()`.

### 4. Implicit Threading
*   **Overview:** Shifting the burden of thread creation and management from developers to compilers and run-time libraries.
*   **OpenMP:** Uses compiler directives like `#pragma omp parallel` in C/C++ to identify parallel regions and automatically spawn threads matching the number of cores.
*   **Intel Threading Building Blocks (TBB):** A C++ template library utilizing structures like `parallel_for` for parallel loop execution.
*   **Grand Central Dispatch (GCD):** Apple technology for macOS/iOS that manages thread pools using Dispatch Queues. Tasks are defined as blocks or closures (in Swift). Queues can be *serial* (FIFO main queue) or *concurrent* (assigned based on Quality of Service classes like user interactive, user initiated, utility, or background).

### 5. Threading Issues
*   **Fork and Exec Semantics:** `fork()` can either duplicate just the calling thread or all threads. `exec()` replaces the entire running process including all threads.
*   **Signal Handling:** Signals (synchronous or asynchronous) notify a process of an event and are processed by signal handlers.
*   **Thread Cancellation:** Terminating a thread before completion can be done asynchronously or deferred.
*   **Other features:** Thread-local storage and Scheduler Activations.

---

## Chapter 5: CPU Scheduling

### 1. Multi-Processor and Multicore Scheduling
*   **Overview:** CPU scheduling becomes highly complex when multiple CPUs are available. 
*   **Chip-multithreading (CMT):** Also known as hyperthreading by Intel. Assigns each physical core multiple hardware threads. If one hardware thread stalls (e.g., waiting for memory), the core rapidly switches to execute another hardware thread.
*   **Two-Level Scheduling:** 
    1. The operating system decides which software thread to assign to a logical CPU.
    2. The hardware decides which logical processor (hardware thread) actually executes on the physical processing core.

### 2. Scheduling Algorithms 
*(Note: Excerpts specifically detail the following queue structures)*
*   **Multilevel Queue:** Partitions the ready queue into multiple separate queues based on process type (e.g., real-time processes, system processes, interactive processes, batch processes). Each queue can have its own priority (e.g., real-time is highest priority), and the scheduler will always execute processes in the highest-priority queue first.
*   **Multilevel Feedback Queue:** A dynamic version of the multilevel queue where a process can move between the various queues. It is defined by parameters such as the number of queues, the scheduling algorithm for each queue, and the methods used to determine when to upgrade or demote a process based on behavior.