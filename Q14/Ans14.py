# ワールドカップ出場国を配列にセット
country = ["Brazil", "Croatia", "Mexico", "Cameroon",
           "Spain", "Netherlands", "Chile", "Australia",
           "Colombia", "Greece", "Cote d'Ivoire", "Japan",
           "Uruguay", "Costa Rica", "England", "Italy",
           "Switzerland", "Ecuador", "France", "Honduras",
           "Argentina", "Bosnia and Herzegovina", "Iran",
           "Nigeria", "Germany", "Portugal", "Ghana",
           "USA", "Belgium", "Algeria", "Russia",
           "Korea Republic"]

max_depth = 0


def searchNextCountry(parent_country, country, depth):
    global max_depth

    next_country = [c for c in country if c[0] == parent_country[-1].upper()]
    if len(next_country) > 0:
        for nc in next_country:
            searchNextCountry(nc,
                              [c for c in country if c != nc],
                              depth + 1)
    else:
        max_depth = max(max_depth, depth)


for first_country in country:
    searchNextCountry(first_country,
                      [c for c in country if c != first_country],
                      1)

print(max_depth)
