LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/moxious/fakestream/master/cypher/reference-data/worldcities-basic.csv' as line
CREATE (c:City {
   name: coalesce(line.city, ''),
   name_ascii: coalesce(line.city_ascii, ''),
   location: point({ latitude: toFloat(line.lat), 
       longitude: toFloat(line.lng) }),
   population: coalesce(line.pop, -1)   
})
MERGE (country:Country {
   name: coalesce(line.country, ''),
   iso2: coalesce(line.iso2, ''),
   iso3: coalesce(line.iso3, '')
})
MERGE (province:Province {
   name: coalesce(line.province, '')
})
CREATE (c)-[:IN]->(province)
CREATE (c)-[:IN]->(country)
MERGE (province)-[:IN]->(country)
return count(c);
