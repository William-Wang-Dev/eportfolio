# COCOMO II parameters
# referncing https://www.surendranathcollege.ac.in/new/upload/ROHAN_MUKHERJEECOCOMO%20and%20COCOMO-II%20cost%20estimation%20models%20for%20effort%20and%20schedule%20estimation2020-04-03COCOMO.pdf
parameters = {
    "organic": {"ai": 3.2, "bi": 1.05, "ci": 2.5, "ab": 0.38},
    "semi-detached": {"ai": 3.0, "bi": 1.12, "ci": 2.5, "ab": 0.35},
    "embedded": {"ai": 2.8, "bi": 1.20, "ci": 2.5, "ab": 0.32},
}

class CostDriver:
    """
    A class to represent a cost driver.

    Args:
        name: The name of the cost driver.
        very_low: The cost of the cost driver at the very low level.
        low: The cost of the cost driver at the low level.
        normal: The cost of the cost driver at the normal level.
        high: The cost of the cost driver at the high level.
        very_high: The cost of the cost driver at the very high level.
        extra_high: The cost of the cost driver at the extra high level.

    Raises:
        KeyError: If an invalid level name is accessed.
    """

    def __init__(self, name, very_low, low, normal, high, very_high, extra_high):
        """
        Initialize a cost driver object.

        Args:
            name: The name of the cost driver.
            very_low: The cost of the cost driver at the very low level.
            low: The cost of the cost driver at the low level.
            normal: The cost of the cost driver at the normal level.
            high: The cost of the cost driver at the high level.
            very_high: The cost of the cost driver at the very high level.
            extra_high: The cost of the cost driver at the extra high level.
        """

        self._name = name
        self._levels = {
            "very_low": very_low,
            "low": low,
            "normal": normal,
            "high": high,
            "very_high": very_high,
            "extra_high": extra_high,
        }

    @property
    def name(self):
        """
        Get the name of the cost driver.

        Returns:
            The name of the cost driver.
        """

        return self._name

    def __repr__(self):
        """
        Get a string representation of the cost driver object.

        Returns:
            A string representation of the cost driver object.
        """

        return f"CostDriver(name={self.name}, levels={self.levels})"

    def __getattr__(self, key):
        """
        Get the value of the cost driver at the specified level.

        Args:
            key: The name of the level.

        Returns:
            The value of the cost driver at the specified level.

        Raises:
            KeyError: If the specified level is not valid.
        """

        if key in self._levels:
            return self._levels[key]
        else:
            raise KeyError(f"Invalid level name: {key}")


# Placeholder values
project_type = "embedded"  # Replace with "organic", "semi-detached", or "embedded"
KLOC = 100  # Replace with your estimated KLOC


# Calculate EAF (adjustment factor)
# you can get them from COCOMO II manual
EAF = 1 # EAF initial value is 1
EAF *= CostDriver("software reliability", 0.82, 0.92, 1.00, 1.10, 1.26, 1.26).very_low
EAF *= CostDriver("database size", 0.90, 0.90, 1.00, 1.17, 1.34, 1.74).very_low
EAF *= CostDriver("complexity of the product", 0.73, 0.87, 1.00, 1.17, 1.34, 1.74).very_low
EAF *= CostDriver("Execution Time Constraint", 1.00, 1.00, 1.00, 1.11, 1.29, 1.63).very_low
EAF *= CostDriver("Memory Constraint ", 1.00, 1.00, 1.00, 1.05, 1.17, 1.46).very_low
EAF *= CostDriver("Platform Volatility", 0.87, 0.87, 1.00, 1.15, 1.30, 1.30).very_low
EAF *= CostDriver("Required turnabout time ", 0.87, 0.87, 1.00, 1.07, 1.15, 1.15).very_low
EAF *= CostDriver("Analyst Capability", 1.42, 1.19, 1.00, 0.85, 0.71, 0.71).very_low
EAF *= CostDriver("Applications Experience", 1.34, 1.15, 1.00, 0.88, 0.81, 0.81).very_low
EAF *= CostDriver("Platform Experience", 1.19, 1.09, 1.00, 0.91, 0.85, 0.85).very_low
EAF *= CostDriver("Personnel continuity", 1.29, 1.12, 1.00, 0.91, 0.85, 0.85).very_low
EAF *= CostDriver("Documentation match to life-cycle needs", 0.81, 0.91, 1.00, 1.11, 1.23, 1.23).very_low
EAF *= CostDriver("Multisite development", 1.22, 1.09, 1.00, 0.93, 0.86, 0.80).very_low
EAF *= CostDriver("Required Development Schedule", 1.43, 1.14, 1.00, 1.00, 1.00, 1.00).very_low
EAF *= CostDriver("Required Development Schedule", 1.43, 1.14, 1.00, 1.00, 1.00, 1.00).very_low
EAF *= CostDriver("Required reusability", 0.95, 0.95, 1.00, 1.07, 1.15, 1.24).very_low


# Calculate effort and development time
ai = parameters[project_type]["ai"]
bi = parameters[project_type]["bi"]
ci = parameters[project_type]["ci"]
ab = parameters[project_type]["ab"]

effort = ai * (KLOC ** bi) * EAF  # work loading
dev_time = ci * (effort ** ab)    # dev time

print(f"Estimated effort (total work loading): {effort} person-months")
print(f"Estimated development time (consider Brooks's law): {dev_time} months")
