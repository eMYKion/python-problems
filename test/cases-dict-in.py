dicts = [
    ({"Alice":3, "Bob":4, "Sam":155},"Alice"),
    ({"Abram":5, "Nyomi":6, "Sophia":133},"Sergio"),
    ({"Azrael":6, "Nasir":11, "Juniper":44},"Azrael"),
    ({"Anaya":1, "Wade":41, "Alayah":12},"Brock"),
]



cases = {
    i:(p,p[1] in p[0]) for i,p in enumerate(dicts)
}
