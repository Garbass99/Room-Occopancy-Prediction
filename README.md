The Room Occupancy prediction model Project is build to detect if a room is occupied using the features that can predict if a room is empty or occupied.
these feature includes:
1. date: The date the date that other features changes
   
2. Temperature: the Tempreture of the room at that very moment or day Units: Degrees Celsius (°C) or Fahrenheit (°F).
Tools: Thermometers, IoT sensors.
Why it matters: Affects occupant comfort and HVAC system efficiency.

3. Humidity: What it measures: Moisture level in the air.
Measurement:
Units: Percentage (% Relative Humidity, RH).
Tools: Hygrometers.
Why it matters: High humidity reduces comfort; low humidity causes dryness.


4. Light: What it measures: Illuminance (brightness).
Measurement:
Units: Lux (lx) or lumens (lm).
Tools: Light sensors (photodiodes).
Why it matters: Indicates natural/artificial light usage and energy efficiency.

5. CO2 (Caborn Oxider): What it measures: Concentration of CO₂ in the air.
Measurement:
Units: Parts per million (ppm).
Tools: NDIR (Non-Dispersive Infrared) sensors.
Why it matters: High CO₂ (>1,000 ppm) indicates poor ventilation and reduces cognitive performance

6. Humidity Ratio
What it measures: Absolute moisture content in air (mass of water vapor per mass of dry air).
Measurement:
Units: Grams of water per kilogram of dry air (g/kg).
Formula: Derived from temperature and relative humidity.
Why it matters: Critical for HVAC design and comfort analysis.

7. The out come variable What it measures: Presence/absence of people in a space.
Measurement:
Binary: 0 (unoccupied) or 1 (occupied).
We use the collected data to build a model that will dectect either a room is occupied or not occupied in this project
