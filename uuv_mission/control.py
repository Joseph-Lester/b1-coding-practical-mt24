# Module for calling the controller 

class Controller:
    """Class for controlling the submarine in the cave.

    The purpose is to take the reference depth and the actual submarine depth as inputs,
    and output the action (force by the controller in the y-direction).
    """
    
    def __init__(self, kp: float = 0.15, kd: float = 0.6, ki: float = 0.0):
        # Controller constants
        self._kp = kp
        self._kd = kd
        self._ki = ki  # Not used for this controller but could consider implementing in the future
        self._last_error = 0.0

    def get_error(self, reference: float, depth: float) -> float:
        """Calculate the error between the reference depth and the actual depth."""
        return float(reference - depth)

    def get_action(self, reference: float, depth: float) -> float:
        """Calculate the current controller action (force in y-direction).

        Parameters:
            reference (float): Reference depth given by the CSV file.
            depth (float): Current y-position of the submarine.

        Returns:
            action (float): Control action to be applied.
        """
        error = self.get_error(reference, depth)
        action = self._kp * error + self._kd * (error - self._last_error)
        
        # Update last error for the next time step
        self._last_error = error
        return action

    def reset(self):
        """Reset the controller's state."""
        self._last_error = 0.0

 

