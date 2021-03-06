EURail = [
    (("Faro", "Lisbon"), 3.50),
    (("Lisbon", "Porto"), 2.45),
    (("Lisbon", "Madrid"), 10.10),
    
    (("Madrid", "Santiago"), 7.05),
    (("Madrid", "Santander"), 4.30),
    (("Madrid", "Pamplona"), 3.00),
    (("Madrid", "Barcelona"), 2.50),
    (("Madrid", "Valencia"), 3.30),
    (("Madrid", "Malaga"), 2.45),
    (("Madrid", "Seville"), 2.35),
    (("Seville", "Barcelona"), 5.40),
    (("Valencia", "Barcelona"), 2.55),
    
    (("Madrid", "Bordeaux"), 11.00),
    (("Bordeaux", "Paris"), 3.00),
    (("Paris", "Rennes"), 2.00),
    (("Bordeaux", "Lyon"), 6.15),
    (("Lyon", "Paris"), 1.55),
    (("Barcelona", "Montpellier"), 4.40),
    (("Montpellier", "Marseille"), 2.20),
    (("Marseille", "Lyon"), 1.40),
    (("Marseille", "Nice"), 2.35),
    
    #(("Paris", "London"), 2.30),
    #(("London", "Holyhead"), 3.50),
    #(("Holyhead", "Dublin"), 0.00),
    #(("Dublin", "Cork"), 2.45),
    
    #(("London", "Brussels"), 2.20),
    (("Paris", "Brussels"), 1.25),
    (("Brussels", "Amsterdam"), 1.53),
    (("Brussels", "Cologne"), 1.47),
    (("Brussels", "Frankfurt"), 3.10),
    (("Paris", "Frankfurt"), 3.55),
    (("Cologne", "Amsterdam"), 4.00),
    (("Cologne", "Frankfurt"), 3.40),
    (("Frankfurt", "Bern"), 3.55),
    (("Bern", "Lyon"), 3.50),

    (("Nice", "Milan"), 4.45),
    (("Bern", "Milan"), 4.00),
    (("Milan", "Venice"), 3.05),
    (("Milan", "Bologna"), 1.00),
    (("Bologna", "Florence"), 0.55),
    (("Venice", "Florence"), 2.40),
    (("Florence", "Rome"), 1.35),
    (("Rome", "Bari"), 4.00),
    (("Rome", "Napoli"), 1.20),
    (("Napoli", "Catania"), 8.30),
    
    (("Frankfurt", "Munich"), 3.10),
    (("Frankfurt", "Hamburg"), 3.40),
    (("Amsterdam", "Copenhagen"), 11.15),
    (("Hamburg", "Copenhagen"), 4.40),
    (("Amsterdam", "Berlin"), 6.10),
    (("Hamburg", "Berlin"), 1.35),
    (("Munich", "Berlin"), 5.45),
    
    #(("Copenhagen", "Stockholm"), 5.15),
    #(("Copenhagen", "Oslo"), 8.40),
    #(("Oslo", "Stockholm"), 6.20),
    #(("Oslo", "Bergen"), 6.45),
    #(("Stockholm", "Ostersund"), 7.00),
    #(("Ostersund", "Trondheim"), 3.50),
    #(("Stockholm", "Kiruna"), 16.00),
    
    (("Munich", "Prague"), 6.05),
    (("Munich", "Vienna"), 4.10),
    (("Munich", "Venice"), 7.05),
    #(("Berlin", "Warsaw"), 6.05),
    (("Berlin", "Prague"), 4.35),
    #(("Prague", "Warsaw"), 8.40),
    (("Prague", "Vienna"), 4.05),
    #(("Vienna", "Warsaw"), 9.40),
    (("Vienna", "Budapest"), 2.55),
    #(("Buda", "Warsaw"), 13.00),
    
    (("Venice", "Vienna"), 7.00),
    (("Venice", "Ljubljana"), 9.00),
    (("Ljubljana", "Zagreb"), 2.20),
    (("Ljubljana", "Budapest"), 9.00),
    #(("Zagreb", "Belgrade"), 6.05),
    #(("Zagreb", "Sarajevo"), 9.10),
    #(("Sarajevo", "Belgrade"), 9.00),
    #(("Belgrade", "Bar"), 9.32),
    (("Budapest", "Bucharest"), 13.50),
    #(("Belgrade", "Bucharest"), 12.10),
    #(("Belgrade", "Sofia"), 8.05),
    #(("Bucharest", "Sofia"), 9.00),
    #(("Belgrade", "Skopje"), 8.45),
    #(("Skopje", "Sofia"), 9.00),
    #(("Skopje", "Thessaloniki"), 4.00),
    #(("Sofia", "Thessaloniki"), 6.40),
    #(("Thessaloniki", "Athens"), 4.25),
    #(("Athens", "Patras"), 3.35)
]

Coords = {'Faro':(37.03,-7.94), 'Lisbon':(38.72,-9.14), 
'Porto':(41.15,-8.62), 'Madrid':(40.42,-3.71), 
'Santiago':(39.72,-6.88), 'Santander':(43.47,-3.8), 
'Pamplona':(42.82,-1.65), 'Barcelona':(41.4,2.17), 
'Valencia':(39.48,-0.39), 'Malaga':(36.72,-4.42), 
'Seville':(37.4,-5.98), 'Bordeaux':(44.84,-0.58), 
'Paris':(48.86,2.34), 'Rennes':(48.11,-1.68), 'Lyon':(45.76,4.83), 
'Montpellier':(43.61,3.87), 'Marseille':(43.31,5.37), 
'Nice':(43.7,7.27), 'Brussels':(50.83,4.33), 
'Amsterdam':(52.37,4.89), 'Cologne':(50.95,6.97), 
'Frankfurt':(50.12,8.68), 'Bern':(46.95,7.44), 'Milan':(45.48,9.19), 
'Venice':(45.43,12.33), 'Bologna':(44.5,11.34), 
'Florence':(43.78,11.24), 'Rome':(41.89,12.5), 'Bari':(41.12,16.87), 
'Napoli':(40.85,14.27), 'Catania':(37.5,15.08), 
'Munich':(48.14,11.58), 'Hamburg':(53.55,10.), 
'Copenhagen':(55.68,12.57), 'Berlin':(52.52,13.38), 
'Stockholm':(59.33,18.07), 'Oslo':(59.91,10.75), 
'Bergen':(60.38,5.34), 'Ostersund':(63.18,14.65), 
'Trondheim':(63.44,10.4), 'Kiruna':(67.86,20.22), 
'Prague':(50.08,14.43), 'Vienna':(48.22,16.37), 
'Budapest':(47.51,19.08), 'Ljubljana':(46.06,14.51), 
'Zagreb':(45.8,15.97), 'Bucharest':(44.44,26.1)}