def to_dictionary():
    dict_with_country = dict()
    list_of_tuples = [
  ('Russia', '25'),
  ('France', '132'),
  ('Germany', '132'),
  ('Spain', '178'),
  ('Italy', '162'),
  ('Portugal', '17'),
  ('Finland', '3'),
  ('Hungary', '2'),
  ('The Netherlands', '28'),
  ('The USA', '610'),
  ('The United Kingdom', '95'),
  ('China', '83'),
  ('Iran', '76'),
  ('Turkey', '65'),
  ('Belgium', '34'),
  ('Canada', '28'),
  ('Switzerland', '26'),
  ('Brazil', '25'),
  ('Austria', '14'),
  ('Israel', '12')
  ]
    for country, number in list_of_tuples:
        if (number in dict_with_country):
            dict_with_country[number] = [dict_with_country[number]]   
            dict_with_country[number].append(country)
        else: 
            dict_with_country[number] = country

    for number, countries in dict_with_country.items():
        if isinstance(countries, list):
            for country in countries:
                print(f"{number} : {country}")
        else:
            print(f"{number} : {countries}")

if __name__ == '__main__':
    to_dictionary()