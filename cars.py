import math

class Car(object):
    """A generic car.
    
    """

    g = 9.81 # m/s^2
    air_density = 1.225 # kg/m^3

    def __init__(self, mass=1000, crr=0.01, vel=0, **kwargs):
        """Instantiates a car object.
        
        Args:
            mass (Real): The mass of the car in kg.
            crr (Real): The coefficient of rolling resistance of the car.
            vel (Real): The velocity of the car in m/s.
            **CdA (Real): The drag area of the car in m^2.
            **Cd (Real): The drag coefficient of the car.
            **A (Real): The reference area of the car in m^2. If not
                provided and the mass of the vehicle is between 800kg
                and 2000kg, the value 1.6 + 0.00056*(m - 765) will be
                used (Rajamani, Vehicle Dynamics and Control, 2e)

        Raises:
            TypeError: If any of the parameters are not real numbers.
            ValueError: If any of the parameters are negative.
        
        """
        
        # Ensure things are some form of number.
        try:
            self.mass = mass >= 0 and mass
            self.crr = crr >= 0 and crr
            self.vel = vel < math.inf and vel
        except TypeError:
            raise TypeError('Invalid mass, coefficient of rolling'
                            'resistance, or velocity type.')

        # If CdA is already given...
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
                    self.area = 1.6 + 0.00056*(self.mass - 765)
                else:
                    raise TypeError('Invalid frontal area type.')
        
        # Ensure all are nonnegative.
        if not all([self.mass, self.crr, self.vel,
                self.cda or (self.cd and self.area)]):
            raise ValueError('Something is negative...')
        self.cda = self.cda or self.cd * self.area

    def aero_drag(self, terrain=None, weather=None):
        """Determines the aerodynamic drag on the vehicle."""
        if terrain is None or weather is None:
            return 0.5*air_density*self.cda*self.vel**2
        else:
            raise NotImplementedError('Aero drag accounting for terrain
                and weather has not been developed yet')

    def kinetic_energy(self):
        """Determines the kinetic energy of the vehicle."""
        return 0.5*self.mass*self.vel**2

class GasCar(Car):

class HybridCar(Car):

class ElectricCar(Car):

class SolarCar(ElectricCar):

