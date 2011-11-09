import csv, urllib

def load_csv(url):
  d = {}
  fp = urllib.urlopen(url)
  for row in csv.DictReader(fp):
     key = row['date']
     value = row['fish']

     x = d.get(key, [])
     x.append(value)
     d[key] = x

  return d

def make_dates_dict(fish_d):
    dates_d = {}
    for key in fish_d:
        for fish in fish_d[key]:
            dates_d[fish] = []
    for fish in dates_d:
        for key in fish_d:
            for fishname in fish_d[key]:
                if fishname == fish:
                    dates_d[fish].append(key)
    dates_d[fish] = set(dates_d[fish])
    return dates_d

def get_fishes_by_date(fish_d, date):
  fishlist = fish_d.get(date)
  return fishlist

def get_dates_by_fish(dates_d, fish):
    dateslist = dates_d.get(fish)
    return dateslist

def get_fishes_by_datelist(fish_d, datelist):
    fish_on_datelist = []
    for date in datelist:
        for key in fish_d:
            if key == date:
                for fish in fish_d[key]:
                    fish_on_datelist.append(fish)
    return fish_on_datelist
    

def get_dates_by_fishlist(dates_d, fishlist):
    dates_on_fishlist = []
    for fish in fishlist:
        for key in fish_d:
            for fishy in fish_d[key]:
                if fish == fishy:
                    dates_on_fishlist.append(key)
    dates_on_fishlist_set = set(dates_on_fishlist)
    return dates_on_fishlist_set

fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
dates_d = make_dates_dict(fish_d)


datelist = ['11/3', '11/4']
fishlist = ['cod', 'sole']
henry = get_fishes_by_datelist(fish_d, datelist)
frank = get_dates_by_fishlist(dates_d, fishlist)

# test 1
x = get_fishes_by_date(fish_d, '1/1')
assert 'salmon' in x

###

# test 2
x = get_dates_by_fish(dates_d, 'salmon')
assert '1/1' in x
assert '1/2' in x

###

# test 3
x = get_fishes_by_datelist(fish_d, ['1/1'])
assert 'salmon' in x, x

###

# test 4
x = get_dates_by_fishlist(dates_d, ['salmon'])
assert '1/1' in x



#    
