import fileinput, scipy

g = { ( x, y ): c
      for y, r in enumerate( fileinput.input() )
      for x, c in enumerate( r.strip( '\n' ) ) }

d = scipy.cluster.hierarchy.DisjointSet( g )
for ( x, y ), v in g.items():
    for n in ( ( x - 1, y ), ( x + 1, y ),
               ( x, y - 1 ), ( x, y + 1 ) ):
        if g.get( n, None ) == v:
            d.merge( ( x, y ), n )

t1, t2 = 0, 0
for r in d.subsets():
    r = set( r )
    a = len( r )
    p = 0
    s = 0
    for x, y in r:
        # Perimeter
        p += ( x - 1, y ) not in r
        p += ( x + 1, y ) not in r
        p += ( x, y - 1 ) not in r
        p += ( x, y + 1 ) not in r
        # Outer corners
        s += ( x - 1, y ) not in r and ( x, y - 1 ) not in r
        s += ( x + 1, y ) not in r and ( x, y - 1 ) not in r
        s += ( x - 1, y ) not in r and ( x, y + 1 ) not in r
        s += ( x + 1, y ) not in r and ( x, y + 1 ) not in r
        # Inner corners
        s += ( x - 1, y ) in r and ( x, y - 1 ) in r and ( x - 1, y - 1 ) not in r
        s += ( x + 1, y ) in r and ( x, y - 1 ) in r and ( x + 1, y - 1 ) not in r
        s += ( x - 1, y ) in r and ( x, y + 1 ) in r and ( x - 1, y + 1 ) not in r
        s += ( x + 1, y ) in r and ( x, y + 1 ) in r and ( x + 1, y + 1 ) not in r
    t1 += a * p
    t2 += a * s
print( t1, t2 )