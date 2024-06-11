# ALX Backend - Queuing System in JavaScript

This repository contains exercises and projects related to building a queuing system in JavaScript, focusing on backend development. The projects are part of the ALX Backend curriculum.


### Learning Objectives

- Set up a Redis server on your machine
- Perform basic operations with the Redis client
- Utilize a Redis client with Node.js for basic operations
- Store hash values in Redis
- Manage async operations with Redis
- Implement Kue as a queue system
- Build a basic Express app interacting with a Redis server
- Build a basic Express app interacting with a Redis server and queue

### Requirements

- Environment: Ubuntu 18.04, Node 12.x, Redis 5.0.7
- All files should end with a new line
- Use `.js` extension for code files
- Create a `README.md` file at the root of each project folder

## Projects Overview

1. **Install a redis instance**
   - Download, extract, and compile Redis
   - Start Redis server and perform basic operations
   - Requirements: Ubuntu, Node.js, Redis

2. **Node Redis Client**
   - Connect to Redis server using node_redis library
   - Handle connection errors and logging
   - Use Babel and ES6
   - Requirements: Node.js, Babel

3. **Node Redis client and basic operations**
   - Implement set and get operations with Redis
   - Handle callbacks for operations
   - Requirements: Node.js, Redis

4. **Node Redis client and async operations**
   - Modify operations to use promisify and async/await
   - Requirements: Node.js, Redis

5. **Node Redis client publisher and subscriber**
   - Create publisher and subscriber for Redis
   - Handle message subscription and publishing
   - Requirements: Node.js, Redis

6. **Create the Job creator**
   - Create a queue with Kue
   - Create and process job objects
   - Requirements: Node.js, Kue, Redis

7. **Create the Job processor**
   - Create a queue with Kue
   - Process job objects with blacklisted phone numbers
   - Requirements: Node.js, Kue, Redis

8. **Track progress and errors with Kue: Create the Job creator**
   - Create jobs with progress tracking and error handling
   - Requirements: Node.js, Kue, Redis

9. **Track progress and errors with Kue: Create the Job processor**
   - Process jobs with progress tracking and error handling
   - Requirements: Node.js, Kue, Redis

10. **Writing the job creation function**
    - Write a function to create and manage jobs
    - Requirements: Node.js, Kue, Redis

11. **Writing the test for job creation**
    - Write tests for job creation function
    - Requirements: Mocha, Chai, Node.js, Kue, Redis

12. **In stock?**
    - Create a system to manage product stock using Redis
    - Implement API routes for product listing and details
    - Requirements: Express.js, Node.js, Redis
