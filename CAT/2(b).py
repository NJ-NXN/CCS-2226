class VacuumAgent:
    def __init__(self):
        # The environment consists of two locations, 'A' and 'B'.
        # Both start in a 'Dirty' state.
        self.environment = {'A': 'Dirty', 'B': 'Dirty'}
        # The agent starts in location 'A'
        self.location = 'A'

    def sense(self):
        # Sensor: Detects the current location and its status
        return self.location, self.environment[self.location]

    def act(self):
        # Actuator: Determines the action based on the percept (Reflex Agent)
        location, status = self.sense()
        print(f"Agent is at Location {location}. Status: {status}")

        if status == 'Dirty':
            print(f"Action: SUCK dirt at Location {location}.")
            self.environment[location] = 'Clean'
        else:
            print(f"Location {location} is already Clean.")

        # Move to the other location
        if location == 'A':
            print("Action: Move RIGHT to Location B.\n")
            self.location = 'B'
        elif location == 'B':
            print("Action: Move LEFT to Location A.\n")
            self.location = 'A'

    def clean_environment(self):
        # Goal: Run the agent until both locations are clean
        print("--- Starting Vacuum Agent ---")
        # Run for a set number of steps to ensure both sides are checked
        for step in range(3):
            self.act()
            
        print("--- Environment is fully Cleaned ---")
        print("Final State:", self.environment)

# Initialize and run the agent
agent = VacuumAgent()
agent.clean_environment()