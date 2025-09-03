#!/bin/bash

curl "https://api.hh.ru/vacancies?text=Data+science&page=1&per_page=20" | jq > hh.json
