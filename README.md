# Spy Cat Agency Management App

This is a RESTful CRUD application developed for the Spy Cat Agency (SCA) to manage spy cats, their missions, and assigned targets. It simplifies the spying work processes by enabling seamless management of cats, missions, and their collected data.

## Features Implemented

### Spy Cats
1. **Create Spy Cats**: Add a new spy cat to the system with the following attributes:
   - Name
   - Years of Experience
   - Breed (validated using [TheCatAPI](https://api.thecatapi.com/v1/breeds))
   - Salary
2. **Update Spy Cats**: Modify the salary of an existing spy cat.
3. **Delete Spy Cats**: Remove a spy cat from the system.
4. **List Spy Cats**: View all spy cats.
5. **Get a Spy Cat**: Retrieve details of a specific spy cat.

### Missions and Targets
1. **Create Missions**: Create a new mission along with its targets in one request. Each mission includes:
   - Assigned Cat (if any)
   - Targets (1–3 targets per mission), described by:
     - Name
     - Country
     - Notes
     - Completion State
   - Mission Completion State
2. **Assign Missions**: Assign a mission to an available spy cat.
3. **Update Targets**:
   - Update target notes (disabled if the target or mission is completed).
   - Mark a target as completed.
4. **Delete Missions**:
   - Missions cannot be deleted if they are assigned to a spy cat.
5. **List Missions**: View all missions.
6. **Get a Mission**: Retrieve details of a specific mission.


## How to Run the Application

### Prerequisites
- Install Docker and Docker Compose.
- Obtain a valid API key from [TheCatAPI](https://thecatapi.com/) for breed validation.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spy-cat-agency.git
   cd spy-cat-agency
2. Then fill the `docker-compose.env` file (if you want it to run via Docker Compose).
3. Finally, run `docker-compose up --build` and wait for it to start.
