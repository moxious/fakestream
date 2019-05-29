FOREACH (id IN range(0,1000000) | CREATE (:Account {id:id}));
