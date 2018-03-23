from pygal.maps.world import World

wm = World()
wm.title = 'North, Central, and South America'
wm.add('North America', {'ca': 34126000, 'mx': 113423000, 'us': 309349000})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('na_populations.svg')
