% Facts
issue(car1, dead_battery).
issue(car2, blown_head_gasket).
issue(car3, radiator_leak).
issue(car4, no_fuel).

% Rules
fault(Car, engine_wont_start) :- issue(Car, dead_battery).
fault(Car, overheating) :- issue(Car, blown_head_gasket).
fault(Car, coolant_low) :- issue(Car, blown_head_gasket).
fault(Car, white_smoke) :- issue(Car, blown_head_gasket).

fault(Car, overheating) :- issue(Car, radiator_leak).
fault(Car, coolant_low) :- issue(Car, radiator_leak).

fault(Car, engine_wont_start) :- issue(Car, no_fuel).
fault(Car, fuel_gauge_empty) :- issue(Car, no_fuel).
