LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/moxious/fakestream/master/cypher/reference-data/states.csv' as line
MATCH (p:Province { name: line.name })
SET p:State, p.code=line.code
RETURN count(p);
