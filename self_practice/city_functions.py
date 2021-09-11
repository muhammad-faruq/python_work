def get_city_country(city, country, population = 0):
	if population == 0:
		city_country_string = city.title() + ', ' + country.title()
		return city_country_string
	else:
		city_country_population_string = city.title() + ', ' + country.title() + ' - population ' + str(population)
		return city_country_string
