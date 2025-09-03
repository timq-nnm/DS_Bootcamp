def dict_sorter():
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
    for country in list_of_tuples:
        dict_with_country[country[0]] = int(country[1])

    sorted_dict = sorted(dict_with_country.items(), key=lambda item: item[1], reverse=True)
    
    print(*[_[0] for _ in sorted_dict], sep='\n')
    



if __name__ == '__main__':
    dict_sorter()