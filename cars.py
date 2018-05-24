import math

class Car(object):
    """A generic car object.
    
    
    
    """

    g = 9.81 # Acceleration due to gravity (m/s^2).
    air_density = 1.225 # Mass density of air in standard conditions (kg/m^3).

    def __init__(self, mass=1200, crr=0.015, vel=0, **kwargs):
        """Instantiates a car object.
        
        Args:
            mass (float): The mass of the car (kg).
            crr (float): The coefficient of rolling resistance of the car.
            vel (float): The velocity of the car (m/s).
            **CdA (float): The drag area of the car (m^2).
            **Cd (float): The drag coefficient of the car.
            **A (float): The reference area of the car (m^2). If not
                provided and the mass of the vehicle is between 800kg
                and 2000kg, the value 1.6 + 0.00056 * (m - 765) will
                be used (Rajamani, Vehicle Dynamics and Control, 2e).

        Raises:
            TypeError: If any of the parameters are not numbers.
            ValueError: If any of the parameters are negative.
        
        """
        
        # Ensure things are valid numbers.
        try:
            self.mass = mass >= 0 and mass
            self.crr = crr >= 0 and crr
            self.vel = vel < math.inf and vel
        except TypeError:
            raise TypeError('Invalid mass, coefficient of rolling'
                            'resistance, or velocity type.')
        # If CdA is already given, use it...
        try:
            self.cda = kwargs.get('CdA')
            self.cda = self.cda >= 0 and self.cda
        except TypeError:
            pass
        # ...otherwise compute it.
        if not self.cda:
            try:
                self.cd = kwargs.get('Cd')
                self.cd = self.cd >= 0 and self.cd
            except TypeError:
                raise TypeError('Invalid drag coefficient type.')
            
            try:
                self.area = kwargs.get('A')
                self.area = self.area >= 0 and self.area
            except TypeError:
                if self.mass >= 800 and self.mass <= 2000:
                    self.area = 1.6 + 0.00056 * (self.mass - 765)
                else:
                    raise TypeError('Invalid frontal area type.')
        # Ensure all are nonnegative.
        if not all([self.mass, self.crr, self.vel,
                self.cda or (self.cd and self.area)]):
            raise ValueError('Something is negative.')
        # Calculate CdA if not already done.
        self.cda = self.cda or self.cd * self.area
    
    def aero_drag(self, terrain=None, weather=None):
        """Determines the aerodynamic drag on the vehicle."""
        if terrain is None or weather is None:
            return 0.5 * air_density * self.cda * self.vel ** 2
        else:
            raise NotImplementedError('Aero drag accounting for terrain
                and weather has not been developed yet')
    
    def rolling_resistance(self, terrain=None)
        """Determines the rolling resistance of the vehicle."""
        # Assumes terrain.grade is a percentage.
        return self.crr * self.mass * g * (1 if terrain is None
            else math.cos(math.atan(terrain.grade / 100)))
    
    @property
    def kinetic_energy(self):
        """Determines the kinetic energy of the vehicle."""
        return 0.5*self.mass*self.vel**2
    
    def power(self, terrain=None, weather=None):
        """Determines the instantaneous power required at a given state."""
        force = aero_drag(terrain, weather) + rolling_resistance(terrain)
            + (0 if terrain is None else math.sin(math.atan(terrain.grade / 100))
            * self.vel) * self.mass * g
        return force * self.vel
    
    def energy(self, terrain1, terrain2, weather=None, vel1, vel2=None):
        """Determines the energy needed to go from terrain1 to terrain2.
        
        Assumes a straight line trajectory and constant acceleration.
        
        Args:
            terrain1 (
            terrain2 (
            weather (
            vel1 (float): Initial velocity (m/s).
            vel2 (float): Final velocity (m/s). Assumed to be equal to
                the initial velocity if not provided.
        
        Returns:
            float: Energy needed to go from terrain1 to terrain2
                starting at vel1 and ending at vel2.
        
        """
        
        if vel2 is None:
            vel2 = vel1
        raise NotImplementedError

class GasCar(Car):

class ElectricCar(Car):

class HybridCar(GasCar, ElectricCar):

class SolarCar(ElectricCar):

